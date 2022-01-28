from django.shortcuts import render,HttpResponse
from .tasks import send_email_to_all
# Create your views here.
def test(request):
    send_email_to_all.delay()
    return HttpResponse("sent")