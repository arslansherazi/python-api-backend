from flask import Flask, request
from celery import Celery
from flask_mail import Mail, Message

# app configurations
app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# celery configurations
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'arslan.python.dev@gmail.com'
app.config['MAIL_PASSWORD'] = 'glennmaxwell2018'
app.config['MAIL_DEFAULT_SENDER'] = 'arslan.python.dev@gmail.com'
mail = Mail(app)


@app.route('/send_email', methods=['POST'])
def send_email():
    recipient_email = request.form['recipient_mail']
    email_data = {
        'subject': 'Hello from flask',
        'recipient_email': recipient_email,
        'body': 'This is a test email sent from a background Celery task.'
    }
    celery_task.apply_async(args=[email_data], countdown=10)
    return "Email is sent successfully"


@celery.task
def celery_task(email_data):
    email_configurations = Message(
        email_data['subject'],
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[email_data['recipient_email']]
    )
    email_configurations.body = email_data['body']
    with app.app_context():
        mail.send(email_configurations)


if __name__ == '__main__':
    app.run()

