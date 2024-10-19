import os

class Config:
    PAGE_ACCESS_TOKEN = os.getenv('PAGE_ACCESS_TOKEN', 'your_page_access_token')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key')

    # Add more configuration variables if needed
