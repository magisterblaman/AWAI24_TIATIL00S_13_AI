import json

import requests

messages = []

while True:
    question = input("What do you wonder? ")

    messages.append({
        "role": "user",
        "content": question
    })

    my_headers = {
        "Authorization": "Bearer <key>" #klista in din OpenRouter-nyckel
    }

    my_body = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": messages
    }

    result = requests.post("https://openrouter.ai/api/v1/chat/completions",
                           headers=my_headers,
                           data=json.dumps(my_body))
    result_json = result.json()

    if "error" in result_json:
        print("Error!")
    else:
        answer = result_json["choices"][0]["message"]
        messages.append(answer)
        content = answer["content"]

        print(content)
