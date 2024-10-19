import requests
import json
from flask import current_app

def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v11.0/me/messages?access_token={current_app.config['PAGE_ACCESS_TOKEN']}"
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()
