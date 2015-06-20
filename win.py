import facebook
import requests
import yaml
import twilio_caller
from datetime import datetime, timedelta

# This should not be committed to a public repo. But this
# is a hackathon so who gives a shit.
APP_ID = '1667264776818224'
APP_SECRET = '1be1d6fe492e70c79d2e397c16685152'
STRPTIME_FORMAT = '%Y-%m-%dT%H:%M:%S-0700'
SMS_FORMAT = '%s will run from %s to %s. Attending: %d'
RECEIVER_NUMBER = '+11111111111'

def get_fb_token(app_id, app_secret):           
  payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
  file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
  result = file.text.split("=")[1]
  print "\n\n\n"
  return result

def get_event_count(event_id):
  """ Event count given event id """
  event_obj = graph.get_object(event_id, fields='attending.summary(true).limit(1)')
  return event_obj['attending']['summary']['count']

# Get access token
access_token = get_fb_token(APP_ID, APP_SECRET)
graph = facebook.GraphAPI(access_token=access_token)

# Try to access https://www.facebook.com/events/1041695122513908/
event_id = '1041695122513908'
event = graph.get_object(event_id)
event_count = get_event_count(event_id)
event_name = event['name']
event_start = datetime.strptime(event['start_time'], STRPTIME_FORMAT) + timedelta(hours=7)
event_end = datetime.strptime(event['end_time'], STRPTIME_FORMAT) + timedelta(hours=7)

# Format it nicely
event_start_str = event_start.strftime("%B %d at %H:%M %p")
event_end_str = event_end.strftime("%H:%M %p")
sms_msg = SMS_FORMAT % (event_name, event_start_str, event_end_str, event_count)

twilio_caller.send_sms(sms_msg, RECEIVER_NUMBER)
