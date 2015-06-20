from twilio.rest import TwilioRestClient
import yaml

def send_sms(mes, recipient):
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    #Twilio details
    account_sid = cfg['twilio']['account_sid']
    auth_token =  cfg['twilio']['auth_token']
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=mes, to=recipient, from_=cfg['twilio']['from_num'])
    
