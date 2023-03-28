from django.contrib.auth.models import User
import requests
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from Coding.models import Company
from Coding.serializers import CompanySerializer
from Coding.throttles.subscription1 import BurstRateThrottleSub1, SustainedRateThrottleSub1
from Coding.throttles.subscription2 import BurstRateThrottleSub2, SustainedRateThrottleSub2


# register new company
@api_view(['POST'])
def register_company(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        try:
            company = serializer.save()  # Deserialization
            # create authentication user (it will be saved in auth_user table)
            User.objects.create_user(username=company.username, password=company.password, email=company.email)
            params = {"username": company.username, "password": company.password}  # auth user
            response = requests.post('http://127.0.0.1:8000/Company/api/token', data=params)
            tokens = response.text.split(',')
            # jwt_refresh_token = tokens[0].split(':')[1]
            # jwt_refresh_token = jwt_refresh_token[1:len(jwt_refresh_token) - 1]
            jwt_access_token = tokens[1].split(':')[1]
            jwt_access_token = jwt_access_token[1:len(jwt_access_token) - 2]
            company.save()  # insert company into database
            '''return Response({
                "message": "Company is added successfully",
                "jwt_access_token": jwt_access_token,
                "jwt_refresh_token": jwt_refresh_token
            })'''
            return Response({
                "message": "Company is added successfully",
                "jwt_access_token": jwt_access_token,
            })
        except Exception as e:
            return Response({"message": str(e)})
    else:
        return Response({"message": "Company already exist"})


class CompanyApis(APIView):
    permission_classes = (IsAuthenticated, )

    # get company details
    def get(self, request):
        username = request.user.username  # get username from jwt token
        try:
            company = Company.objects.get(username=username)
        except Exception as e:
            return Response({"message": str(e)})
        else:
            if company:
                serialized_company = CompanySerializer(company)
                return Response({"data": serialized_company.data})
            else:
                return Response({"message": "Company does not exist"})

    # update company
    def put(self, request):
        username = request.user.username  # get username from jwt token
        try:
            company = Company.objects.get(username=username)
        except Exception as e:
            return Response({"message": str(e)})
        else:
            if company:
                serializer = CompanySerializer(company, data=request.data)
                if serializer.is_valid():
                    updated_company = serializer.save()
                    try:
                        updated_company.save()  # update company in database
                        return Response({"message": "Company is updated successfully"})
                    except Exception as e:
                        return Response({"message": str(e)})
                else:
                    return Response({"message": "Company does not exist"})

    # delete company
    def delete(self, request):
        username = request.user.username  # get username from jwt token
        try:
            company = Company.objects.get(username=username)
        except Exception as e:
            return Response({"message": str(e)})
        else:
            if company:
                try:
                    company.delete()  # delete company from database
                    return Response({"message": "Company is deleted successfully"})
                except Exception as e:
                    return Response({"message": str(e)})
            else:
                return Response({"message": "Company does not exist"})


class CompanyApisSubscription1(CompanyApis):
    throttle_classes = (BurstRateThrottleSub1, SustainedRateThrottleSub1,)


class CompanyApisSubscription2(CompanyApis):
    throttle_classes = (BurstRateThrottleSub2, SustainedRateThrottleSub2,)
