import json
import requests

year = input("Välj ett Eurovision-år som du vill ha information om (1956-2024): ")

esc_result = requests.get("https://eurovisionapi.runasp.net/api/contests/" + year)

esc_result_json = esc_result.json()

#print(esc_result_json)




final = esc_result_json["rounds"][0]

winner_id = -1

for i in range(len(final["performances"])):
    performance = final["performances"][i]

    if performance["place"] == 1:
        winner_id = performance["contestantId"]
        break


winner_info = esc_result_json["contestants"][winner_id]

host_country = requests.get("https://restcountries.com/v3.1/alpha/" + esc_result_json["country"])
host_country_json = host_country.json()

winner_country = requests.get("https://restcountries.com/v3.1/alpha/" + winner_info["country"])
winner_country_json = winner_country.json()

host_country_name = host_country_json[0]["translations"]["swe"]["common"]
winner_country_name = winner_country_json[0]["translations"]["swe"]["common"]

print("År " + str(esc_result_json["year"]) + " så hölls tävlingen i " + esc_result_json["city"] + ", " + host_country_name)
print(winner_info["artist"] + " från " + winner_country_name + " vann tävlingen med låten " + winner_info["song"])