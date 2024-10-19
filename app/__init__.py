from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints (for webhooks)
    from webhooks.messenger_webhook import webhook_blueprint
    app.register_blueprint(webhook_blueprint)

    return app