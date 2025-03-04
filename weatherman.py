import json
import requests

weather_params = {
    "latitude": 57.7814,
    "longitude": 14.1562,
    "daily": "weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_sum"
}

weather_result = requests.get("https://api.open-meteo.com/v1/forecast",
                              params=weather_params)
weather_result_json = weather_result.json()

#print(weather_result_json)


temp_max = weather_result_json["daily"]["temperature_2m_max"][1]
temp_min = weather_result_json["daily"]["temperature_2m_min"][1]
uv_index = weather_result_json["daily"]["uv_index_max"][1]
precipitation = weather_result_json["daily"]["precipitation_sum"][1]

message = ("Maximitemperatur: " + str(temp_max)
           + weather_result_json["daily_units"]["temperature_2m_max"]
           + ", Minimitemperatur: " + str(temp_min)
           + weather_result_json["daily_units"]["temperature_2m_min"]
           + ", UV-index: " + str(uv_index)
           + weather_result_json["daily_units"]["uv_index_max"]
           + ", Nederbörd: " + str(precipitation)
           + weather_result_json["daily_units"]["precipitation_sum"])

ai_headers = {
    "Authorization": "Bearer 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"
}

ai_body = {
    "model": "mistralai/mistral-7b-instruct:free",
    "messages": [
        {
            "role": "user",
            "content": "Kan du skapa en kort text som beskriver"
                       "vad man behöver ha på sig för kläder imorgon"
                       "utifrån denna information: " + message
        }
    ]
}

ai_result = requests.post("https://openrouter.ai/api/v1/chat/completions",
                          headers=ai_headers,
                          data=json.dumps(ai_body))

ai_result_json = ai_result.json()

if "error" in ai_result_json:
    print("Error!")
else:
    answer = ai_result_json["choices"][0]["message"]["content"]

    print(answer)