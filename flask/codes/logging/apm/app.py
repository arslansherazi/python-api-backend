from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler
import logging
import os

# app configurations
app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'division',
    'ELASTIC_APM_SERVER_URL': 'http://localhost:8200',
}
apm = ElasticAPM(app)


def set_logging_handlers():
    file_path = 'logs/division_logs.log'
    if not os.path.isdir('logs'):
        os.makedirs('logs')
    # app logging handlers
    apm_handler = LoggingHandler(client=apm.client)
    apm_handler.setLevel(logging.ERROR)
    file_handler = logging.FileHandler(filename=file_path)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.addHandler(apm_handler)
