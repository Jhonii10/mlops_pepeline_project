import boto3

def create_latency_alarm(endpoint_name, threshold=1000):
    cloudwatch = boto3.client('cloudwatch')
    cloudwatch.put_metric_alarm(
        AlarmName=f"{endpoint_name}-LatencyAlarm",
        MetricName="Latency",
        Namespace="AWS/SageMaker",
        Dimensions=[{"Name": "EndpointName", "Value": endpoint_name}],
        Statistic="Average",
        Period=60,
        EvaluationPeriods=1,
        Threshold=threshold,
        ComparisonOperator="GreaterThanThreshold",
        ActionsEnabled=False
    )
    print("Alarma de latencia configurada para el endpoint:", endpoint_name)

create_latency_alarm("mlops-endpoint")
