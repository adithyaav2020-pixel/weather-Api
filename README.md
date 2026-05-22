 Serverless Weather Data Pipeline Analysis

Features
Fully serverless architecture
Automated scheduled data collection
Real-time stream processing
Cloud storage integration
Auto-ingestion into Snowflake
Scalable and cost-effective pipeline

Workflow

1. **OpenWeather API**
   - Fetches real-time weather data.

2. **Amazon EventBridge**
   - Triggers the pipeline on a schedule.

3. **AWS Lambda**
   - Calls the OpenWeather API.
   - Processes and transforms the response.

4. **Amazon DynamoDB**
   - Stores incoming weather records.

5. **DynamoDB Streams**
   - Captures changes in DynamoDB.

6. **AWS Lambda (Stream Processor)**
   - Reads stream events.
   - Pushes processed data into Amazon S3.

7. **Amazon S3**
   - Stores weather data files.

8. **S3 Event Notification / SQS**
   - Detects new files uploaded to S3.

9. **Snowpipe**
   - Automatically ingests files from S3.

10. **Snowflake**
    - Stores and analyzes weather data.

Technologies Used

- Python
- AWS Lambda
- Amazon EventBridge
- DynamoDB
- DynamoDB Streams
- Amazon S3
- Amazon SQS
- Snowflake
- Snowpipe
- OpenWeather API



Weather Data Pipeline Project
_______________________________

This project is a serverless weather data pipeline built using AWS services and Snowflake.

The pipeline collects real-time weather data from the OpenWeather API, processes it using AWS Lambda, stores it in DynamoDB and S3, and finally loads the data into Snowflake using Snowpipe for analytics and reporting.

Features
____________
1.Fully serverless architecture
2.Automated scheduled data collection
3.Real-time stream processing
4.Cloud storage integration
5.Auto-ingestion into Snowflake
6.Scalable and cost-effective pipeline

Workflow
_______________
1 OpenWeather API
    Fetches real-time weather data.

2 Amazon EventBridge
    Triggers the pipeline on a schedule.

3 AWS Lambda
    Calls the OpenWeather API.
    Processes and transforms the response.

4 Amazon DynamoDB
    Stores incoming weather records.

5 DynamoDB Streams
    Captures changes in DynamoDB.

6 AWS Lambda (Stream Processor)
    Reads stream events.
    Pushes processed data into Amazon S3.

7 Amazon S3
    Stores weather data files.

8 S3 Event Notification / SQS
    Detects new files uploaded to S3.

9 Snowpipe
    Automatically ingests files from S3.

10 Snowflake
     Stores and analyzes weather data.

Weather Data Pipeline Project
___________

This project is a serverless weather data pipeline built using AWS services and Snowflake.

The pipeline collects real-time weather data from the OpenWeather API, processes it using AWS Lambda, stores it in DynamoDB and S3, and finally loads the data into Snowflake using Snowpipe for analytics and reporting.

Features
____
1.Fully serverless architecture
2.Automated scheduled data collection
3.Real-time stream processing
4.Cloud storage integration
5.Auto-ingestion into Snowflake
6.Scalable and cost-effective pipeline

Workflow
_____
1 OpenWeather API
    Fetches real-time weather data.

2 Amazon EventBridge
    Triggers the pipeline on a schedule.

3 AWS Lambda
    Calls the OpenWeather API.
    Processes and trans…

Architecture Flow

OpenWeather API
        ↓
Lambda 1 (Fetch Weather Data)
        ↓
DynamoDB
        ↓
DynamoDB Stream Trigger
        ↓
Lambda 2
        ↓
Amazon S3
        ↓
Snowflake Stage + Pipe
        ↓
Snowflake Table

Deploy AWS Resources
Create Lambda Functions
Configure EventBridge Trigger
Create DynamoDB Table
Enable DynamoDB Streams
Create S3 Bucket
Configure SQS Queue
Setup Snowpipe in Snowflake

Output
The pipeline continuously collects weather data and loads it into Snowflake for:
Analytics
Reporting
Dashboard Creation
Real-time Monitoring

Author : ADITHYA A V

