import openai, os

openai.api_key = os.environ.get("OPENAI_KEY")
messages = [ {"role": "system", "content":
            "You are a intelligent assistant."} ]

def ai_response(message):
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply
