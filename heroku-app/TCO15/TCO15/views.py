from django.http import HttpResponse
from win import *

def homepage(request):
  send_sms_to('+14156322541')
  return HttpResponse("Message sent!")
