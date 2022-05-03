import requests

r=requests.get("https://api.openweathermap.org/data/2.5/weather?lat=39.607773&lon=66.977065&appid=711d46548dd90cf800df2d92430740b7").json()
print(r["coord"]["lat"])