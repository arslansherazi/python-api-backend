from flask import request, Response, redirect

from app import app
from constants import HEADER_AUTHORIZED_KEY, CONTENT_TYPE


# pipe-line of middlewares

@app.before_request
def header_auth_middleware():
    header_authorized_key = request.headers.environ['HTTP_HEADER_AUTHORIZED_KEY']
    if header_authorized_key != HEADER_AUTHORIZED_KEY:
        response = Response()
        response.data = str.encode('Unauthorized Access')
        response._status = '401 OK'
        response._status_code = 401
        return response


@app.before_request
def content_type_middleware1():
    content_type = request.headers.environ['CONTENT_TYPE']
    if content_type != CONTENT_TYPE:
        response = Response()
        response.data = str.encode('Invalid Content-Type')
        response._status = '415 OK'
        response._status_code = 415
        return response


