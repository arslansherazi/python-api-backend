from django.http import HttpResponse


def get_response(request):
    return HttpResponse('Request Authenticated')


