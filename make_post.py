import os
from pyChatGPT import ChatGPT
# read CHATGPT_TOKEN from os
CHATGPT_SESSION_TOKEN = os.getenv("CHATGPT_TOKEN")
session_token = CHATGPT_SESSION_TOKEN  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)  # auth with session token


resp = api.send_message('What is html?')
print(resp)
print(resp['message'])