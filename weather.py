import requests

from datetime import datetime

def get_weather_data(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
       data = response.json()
       city = data['name']
       temp = data['main']['temp']
       humidity = data['main']['humidity']   
       desc = data['weather'][0]['description'] 
       time = data['dt']
       print(f"City: {city}")
       print(f"Temperature: {temp}°C")
       print(f"Humidity: {humidity}%")
       print(f"Description: {desc}")
       print(f"timestamp = {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    else:
       print(f"Error: {response.status_code}")
       return None

#for testing
MY_API_KEY = "API_KEY"
cities = ["Thiruvananthapuram", "Shimla", "Delhi","Gujarat","Meghalaya"]

for city in cities:
    get_weather_data(city, MY_API_KEY)
