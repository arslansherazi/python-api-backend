from flask import jsonify, current_app
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse
from flask_restful.representations import json

from app import db, app, limiter
from models import Company
from schemas import CompanySchema


@jwt_required
def rate_limit_from_config():
    username = get_jwt_identity()
    company = Company.query.get(username)
    subscription = 0
    if company:
        subscription = company.subscription
    if subscription == 1:
        return current_app.config.get("CUSTOM_LIMIT", "5/minute;20/day")
    else:
        return current_app.config.get("CUSTOM_LIMIT", "10/minute;40/day")


@jwt_required
def limiter_identifier():
    username = get_jwt_identity()
    company = Company.query.get(username)
    return company


# register new company
@app.route('/register_company', methods=['POST'])
def register_company():
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True)  # gets argument from POST body
    args1 = parser.parse_args()
    try:
        company = Company.query.get(args1['username'])
    except Exception as e:
        return {'Exception': str(e)}
    if company:
        return 'Company exists already'
    else:
        parser.add_argument('password', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('subscription', required=False)
        parser.add_argument('is_active', required=False)
        args2 = parser.parse_args()
        student = Company(
            args2['username'],
            args2['password'],
            args2['email'],
            args2['name'],
            args2['subscription'],
            args2['is_active']
        )
        try:
            db.session.add(student)
            db.session.commit()
            jwt_access_token = create_access_token(
                identity=args2['username'],
                expires_delta=False  # expires_delta = False will disable expiration time of token
            )
            data = {
                "message": "Company is added successfully",
                "jwt_access_token": jwt_access_token,
            }
            response = app.response_class(
                response=json.dumps(data),
                status=200,
                mimetype='application/json'
            )
            return response
        except Exception as e:
            return {'exception': str(e)}


class CompanyApis(Resource):
    decorators = [limiter.limit(rate_limit_from_config, key_func=limiter_identifier)]

    # get company details
    @jwt_required
    def get(self):
        username = get_jwt_identity()  # get username from jwt token
        try:
            company = Company.query.get(username)
        except Exception as e:
            return {'Exception': str(e)}
        if company:
            company_schema = CompanySchema()
            company_response = company_schema.dump(company).data
            company_response_json = jsonify(company_response)
            return company_response_json
        else:
            return 'Company does not exist'

    # update company
    @jwt_required
    def put(self):
        username = get_jwt_identity()  # get username from jwt token
        try:
            company = Company.query.get(username)
        except Exception as e:
            return {'Exception': str(e)}
        if not company:
            return "Company does not exist"
        else:
            parser = reqparse.RequestParser()
            parser.add_argument('password', required=True)
            parser.add_argument('email', required=True)
            parser.add_argument('name', required=True)
            parser.add_argument('subscription', required=False)
            parser.add_argument('is_active', required=False)
            args = parser.parse_args()

            company.password = args['password']
            company.email = args['email']
            company.name = args['name']
            if args['subscription']:
                company.subscription = args['subscription']
            if args['is_active']:
                company.is_active = int(args['is_active'])
            try:
                db.session.commit()
                return "Company is updated successfully"
            except Exception as e:
                return {'Exception': str(e)}

    # delete company
    @jwt_required
    def delete(self):
        username = get_jwt_identity()  # get username from jwt token
        try:
            company = Company.query.get(username)
        except Exception as e:
            return {'Exception': str(e)}
        if not company:
            return "Company does not exist"
        else:
            try:
                db.session.delete(company)
                db.session.commit()
                return "Company is deleted successfully"
            except Exception as e:
                return {'Exception': str(e)}
