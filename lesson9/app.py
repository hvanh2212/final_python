# import slack
# import schedule
# import requests
# import time

# """
# Write a Slack bot that: send a cat image every 5 minus
# """
# client = slack.WebClient(token = 'xoxb-3686149598261-3689084967026-7hX8Cx08yj1wJ8ss55AG9L6K')

# def send_message():
#     """
#     send a cat image
#     """
#     # get link of random cat image from 'https://some-random-api.ml/img/cat'
#     request = requests.get('https://some-random-api.ml/img/cat')
#     link_json = request.json()
#     link = list(link_json.values())[0]
#     # send the link to channel
#     client.chat_postMessage(channel = '#test', text = link)

# # send a cat image every 5'
# schedule.every(1).seconds.do(send_message)

# while True:
#     schedule.run_pending()
#     time.sleep(10)
username = "abc"
def user_name(name):
    global username
    username = "hiii"
