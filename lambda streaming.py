import json
import boto3
import datetime

s3 = boto3.client('s3')
BUCKET_NAME = 'weather-storage123'

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] in ['INSERT', 'MODIFY']:
            new_image = record['dynamodb'].get('NewImage', {})
            
            # City extraction
            city = new_image.get('city', {}).get('S', 'Unknown')
            
            # Temperature extraction
            temp_field = new_image.get('temperature') or new_image.get('Temperature')
            if temp_field:
                temp = temp_field.get('N') or temp_field.get('S') or "0"
            else:
                temp = "0"

            # Humidity and Condition extraction
            humidity = new_image.get('humidity', {}).get('S', '0')
            condition = new_image.get('condition', {}).get('S', 'N/A')

            # Proper indentation for the dictionary
            weather_data = {
                'city': city,
                'temperature': temp,
                'humidity': humidity,
                'condition': condition,
                'timestamp': str(datetime.datetime.now())
            }
            
            file_name = f"weather_{city}_{datetime.datetime.now().strftime('%H%M%S')}.json"
            
            # Upload to S3
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=file_name,
                Body=json.dumps(weather_data)
            )
            print(f"Success! Saved data for {city}")

    return {'statusCode': 200, 'body': 'Processed'}