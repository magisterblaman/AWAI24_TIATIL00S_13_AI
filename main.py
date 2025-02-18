import json

import requests

question = input("What do you wonder? ")

my_headers = {
    "Authorization": "Bearer <key>" #klista in din OpenRouter-nyckel
}

my_body = {
    "model": "google/gemini-flash-1.5-8b-exp",
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
}

result = requests.post("https://openrouter.ai/api/v1/chat/completions",
                       headers=my_headers,
                       data=json.dumps(my_body))
result_json = result.json()

if "error" in result_json:
    print("Error!")
else:
    content = result_json["choices"][0]["message"]["content"]

    print(content)