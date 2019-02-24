from slackclient import SlackClient
import os
 
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
 
api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        print user.get('name')
else:
    print ("error")