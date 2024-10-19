import openai

def generate_response(user_message):
    prompt = f"Reply to this message in Tagalog: {user_message}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
