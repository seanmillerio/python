from slackclient import SlackClient
import time
import os
 
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
 
if slack_client.rtm_connect(with_team_state=False):
    print "Successfully connected, listening for events"
    while True:
        print slack_client.rtm_read()
         
        time.sleep(1)
else:
    print "Connection Failed"