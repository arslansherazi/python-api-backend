import json

from app import app, apm

DIVISION_TRANSACTION_TYPE = 'division'
DIVISION_TRANSACTION_NAME ='division_transaction'
TRANSACTION_STATUS = 'completed'


@app.route('/', methods=['GET'])
def division():
    try:
        apm.client.begin_transaction(DIVISION_TRANSACTION_TYPE)
        division = 100 / 0
        return json.dumps({'result': division})
    except Exception as e:
        app.logger.info(str(e), exc_info=True)
        app.logger.error(str(e), exc_info=True)
        return json.dumps({'message': str(e)})
    finally:
        apm.client.end_transaction(DIVISION_TRANSACTION_NAME, TRANSACTION_STATUS)
