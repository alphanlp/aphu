from app.extensions import mail
# from app.extensions import celery, mail

# @celery.task()
def send_async_email(msg):
    mail.send(msg)
