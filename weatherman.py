import json
import requests

my_params = {
    "latitude": 57.7814,
    "longitude": 14.1562,
    "daily": "weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_sum"
}

result = requests.get("https://api.open-meteo.com/v1/forecast",
                      params=my_params)
result_json = result.json()

print(result_json)


temp_max = result_json["daily"]["temperature_2m_max"][1]
temp_min = result_json["daily"]["temperature_2m_min"][1]
uv_index = result_json["daily"]["uv_index_max"][1]
precipitation = result_json["daily"]["precipitation_sum"][1]

message = ("Maximitemperatur: " + str(temp_max)
           + result_json["daily_units"]["temperature_2m_max"]
           + ", Minimitemperatur: " + str(temp_min)
           + result_json["daily_units"]["temperature_2m_min"]
           + ", UV-index: " + str(uv_index)
           + result_json["daily_units"]["uv_index_max"]
           + ", Nederbörd: " + str(precipitation)
           + result_json["daily_units"]["precipitation_sum"])