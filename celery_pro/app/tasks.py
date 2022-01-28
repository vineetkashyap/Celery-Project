from celery import shared_task
from django.contrib.auth import get_user_model

from django.core.mail import send_mail
from celery_pro import settings

@shared_task(bind=True)
def send_email_to_all(self):
    
    
        mail_subject = "Hi! User Celery Testing"
        message = "Good Morning Bro. I hope you are doing well. This email for testing celery purspose."
        to_email = 'shilpikashyap2007@gmail.com'
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
        return "Done Ho gya"
    
