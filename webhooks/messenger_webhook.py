from flask import Blueprint, request, jsonify
from app.messenger_api import send_message
from app.openai_integration import generate_response

# Create a blueprint for webhook routes
webhook_blueprint = Blueprint('webhook', __name__)

@webhook_blueprint.route("/webhook", methods=['POST'])
def webhook():
    data = request.json
    if data['object'] == 'page':
        for entry in data['entry']:
            messaging = entry['messaging'][0]
            if 'message' in messaging:
                sender_id = messaging['sender']['id']
                message_text = messaging['message']['text']

                # Generate response using OpenAI
                response_message = generate_response(message_text)

                # Send response back to Messenger
                send_message(sender_id, response_message)
    return "OK", 200
