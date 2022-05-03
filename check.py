import requests
import os

app_id = os.getenv('api')
r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=39.607773&lon=66.977065&appid={api_id}").json()
print(r["coord"]["lat"])
