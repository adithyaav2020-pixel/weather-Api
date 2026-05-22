import json
import urllib.request
import boto3
from datetime import datetime


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather_data')

def lambda_handler(event, context):
    
    cities = ["Thiruvananthapuram", "Shimla", "Delhi","Gujarat","Meghalaya"]
    api_key = "6ad440315d5ddaad1d53569e6d064864" 
    
    results = []
    
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())
                
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description']
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                
                table.put_item(
                    Item={
                        'city': city,
                        'timestamp': timestamp,
                        'temperature': str(temp),
                        'humidity': str(humidity),
                        'condition': description 
                    }
                )
                results.append(f"Success: {city}")
                
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")
            results.append(f"Failed: {city}")

    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }