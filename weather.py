import requests
from plyer import notification

API_KEY = " "  

CITY = " "


URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if data["cod"] == 200:
    weather = data["weather"][0]["description"].capitalize()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]


    message = f"Weather: {weather}\nTemperature: {temperature}°C\nHumidity: {humidity}%"

   
    notification.notify(
        title=f"Weather Update - {CITY}",
        message=message,
        timeout=10
    )
else:
    print(f"Error fetching weather data: {data}")
