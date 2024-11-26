from celery import Celery
from src.utils.mail import mail, create_message
from asgiref.sync import async_to_sync

c_app = Celery()

c_app.config_from_object('src.core.config')

@c_app.task()
def send_email(recipients: list[str], subject:str, body:str):
    message = create_message(recipients=recipients, subject=subject, body=body)
    
    async_to_sync(mail.send_message)(message)
    print("Sent email")