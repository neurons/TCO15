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

# Get access token
access_token = get_fb_token(APP_ID, APP_SECRET)
graph = facebook.GraphAPI(access_token=access_token)

# Try to access https://www.facebook.com/events/789305557821642/
post = graph.get_object('789305557821642')
print "Name:", post['name']
print "Start time:", post['start_time']
print "End time:", post['end_time']
