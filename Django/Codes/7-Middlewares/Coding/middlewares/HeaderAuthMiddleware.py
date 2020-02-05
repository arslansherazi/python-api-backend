from Coding.constants.constants import HEADER_AUTHORIZED_KEY


class HeaderAuthMiddleware:
    get_response = ''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        header_authorized_key = request.headers['Header-Authorized-Key']
        if header_authorized_key != HEADER_AUTHORIZED_KEY:
            response.content = str.encode('Unauthorized access')
            response.status_code = 401
        return response
