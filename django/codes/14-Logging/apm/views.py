from rest_framework.decorators import api_view
from rest_framework.response import Response
from elasticapm.contrib.django.client import client as apm_client
import logging
import os

DIVISION_TRANSACTION_TYPE = 'division'
DIVISION_TRANSACTION_NAME ='division_transaction'
TRANSACTION_STATUS = 'completed'


@api_view(['GET'])
def division(request):
    file_path = 'logs/division_logs.log'
    if not os.path.isdir('logs'):
        os.makedirs('logs')
    file_logger = logging.FileHandler(file_path)
    apm_logger = logging.getLogger('apm_logger')
    try:
        apm_client.begin_transaction(DIVISION_TRANSACTION_TYPE)
        division = 100 / 0
        return Response({'result': division})
    except Exception as e:
        apm_logger.error(str(e), exc_info=True)
        file_logger.info(str(e), exc_info=True)
        return Response({'result': str(e)})
    finally:
        apm_client.end_transaction(DIVISION_TRANSACTION_NAME, TRANSACTION_STATUS)
