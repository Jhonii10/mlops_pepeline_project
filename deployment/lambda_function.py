import boto3
import json

def lambda_handler(event, context):
    runtime = boto3.client('sagemaker-runtime')
    endpoint_name = "mlops-endpoint"

    # Recibir datos de entrada
    data = json.loads(event['body'])

    # Invocar endpoint
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=json.dumps(data)
    )

    result = json.loads(response['Body'].read().decode())
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
