import json
import os
import requests

def lambda_handler(event, context):
    
    # 🔐 Get API key from environment variable (recommended)
    API_KEY = os.environ.get("API_KEY")
    
    if not API_KEY:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "API key not configured"})
        }
    
    # 🌍 Cities list
    CITIES = ["Thiruvananthapuram", "Himachal Pradesh", "Delhi","Gujarat","Meghalaya"]
    
    weather_results = []
    failed_cities = []

    print(f"Fetching weather for {len(CITIES)} cities...")

    for city in CITIES:
        try:
            url = "https://api.openweathermap.org/data/2.5/weather"
            
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                
                weather_results.append({
                    "city": data.get("name"),
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"],
                    "wind_speed": data["wind"]["speed"]
                })
                
                print(f"Success: {city}")
            
            else:
                failed_cities.append({
                    "city": city,
                    "status_code": response.status_code
                })
                print(f"Failed: {city} ({response.status_code})")

        except Exception as e:
            failed_cities.append({
                "city": city,
                "error": str(e)
            })
            print(f"Error fetching {city}: {str(e)}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Weather fetch completed",
            "success_count": len(weather_results),
            "failed_count": len(failed_cities),
            "data": weather_results,
            "errors": failed_cities
        })
    } 

    