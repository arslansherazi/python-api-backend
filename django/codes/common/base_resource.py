from requests import codes
from rest_framework.decorators import APIView
from rest_framework.response import Response

from django.codes.common.common_helpers import CommonHelpers
from django.codes.common.contants import INTERNAL_SERVER_ERROR_MESSAGE, SUCCESS_STATUS_CODES, ROUTING_PREFIX


class BaseResource(APIView):
    end_point = ''
    request_validator = None
    status_code = 200

    def request_flow(self):
        logger = None
        try:
            if self.request.query_params:
                self.request_args = self.request.query_params
            else:
                self.request_args = self.request.data
            self.is_send_response = False
            self.response = {}
            try:
                if self.request_validator:
                    self.request_args = self.request_validator.run_validation(data=self.request_args)
            except Exception as exception:
                self.request_path = None
                self.handle_bad_request_response(exception)
                return self.send_response()
            self.request_path = '{routing_prefix}/{api_endpoint}'.format(
                routing_prefix=ROUTING_PREFIX, api_endpoint=self.end_point
            )
            log_file_path = 'logs/apis/{end_point}'.format(end_point=self.end_point)
            log_file = '{end_point}.log'.format(end_point=self.end_point)
            logger = CommonHelpers.get_logger(log_file_path, log_file)
            self.process_request()
            return self.send_response()
        except Exception as e:
            if logger:
                logger.exception(str(e))
                self.handle_exception_response()
                return self.send_response()

    def process_request(self):
        pass

    def populate_request_arguments(self):
        pass

    def handle_bad_request_response(self, exception):
        param_name = list(exception.detail.keys())[0]
        response_message = exception.detail.get(param_name)[0]
        if param_name != 'non_field_errors':
            response_message = '{param_name}: {message}'.format(param_name=param_name, message=response_message)
        self.response = {
            'message': response_message
        }
        self.status_code = codes.BAD_REQUEST

    def send_response(self):
        final_response = self.response
        if self.request_path:
            final_response.update(cmd=self.request_path)
        final_response.update(status_code=self.status_code)
        if self.status_code in SUCCESS_STATUS_CODES:
            final_response.update(success=True)
        else:
            final_response.update(success=False)
        return Response(final_response, self.status_code)

    def handle_exception_response(self):
        self.response = {
            'message': INTERNAL_SERVER_ERROR_MESSAGE
        }
        self.status_code = codes.INTERNAL_SERVER_ERROR


class BaseGetResource(BaseResource):
    def get(self, request):
        self.request = request
        return self.request_flow()


class BasePostResource(BaseResource):
    def post(self, request):
        self.request = request
        return self.request_flow()


class BasePutResource(BaseResource):
    def put(self, request):
        self.request = request
        return self.request_flow()


class BaseDeleteResource(BaseResource):
    def delete(self, request):
        self.request = request
        return self.request_flow()
