from locale import format_string
from urllib import request
import requests

API_KEY = "4ce044c00053759875c9bc1b3ebe2f1e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273 , 2)

    temperature = 1.80 * (temperature) + 32

    print("Weather:", weather)
    print("Temperature:", temperature, "°F")
else:
    print("An error occurred.")
