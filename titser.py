from titser import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'your_page_access_token'

# Handle incoming messages
@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.json
    if data['object'] == 'page':
        for entry in data['entry']:
            messaging = entry['messaging'][0]
            if 'message' in messaging:
                sender_id = messaging['sender']['id']
                message_text = messaging['message']['text']

                # Call OpenAI or any other function to handle the conversation
                response_message = handle_conversation(message_text)

                # Send response back to Messenger
                send_message(sender_id, response_message)
    return "OK", 200

# Function to send message back via Messenger API
def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v11.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    headers = {"Content-Type": "application/json"}
    data = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

# OpenAI function to handle the conversation
def handle_conversation(user_message):
    # Example OpenAI API call
    prompt = f"Reply to this message in Tagalog: {user_message}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(port=5000)