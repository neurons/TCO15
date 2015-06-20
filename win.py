import facebook
import requests

# This should not be committed to a public repo. But this
# is a hackathon so who gives a shit.
APP_ID = '1667264776818224'
APP_SECRET = '1be1d6fe492e70c79d2e397c16685152'

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

# Try to access https://www.facebook.com/events/789305557821642/
event_id = '789305557821642'
event = graph.get_object(event_id)
event_count = get_event_count(event_id)
print "Name:", event['name']
print "Start time:", event['start_time']
print "End time:", event['end_time']
print "Attending:", event_count

