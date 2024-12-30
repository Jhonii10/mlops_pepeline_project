import boto3
from sagemaker import Session
from sagemaker.sklearn import SKLearn

ROLE = "arn:aws:iam::123456789012:role/SageMakerRole"

def deploy_model(s3_model_path, endpoint_name):
    sagemaker_session = Session()
    model = SKLearn(
        model_data=s3_model_path,
        role=ROLE,
        framework_version="1.0-1",
        sagemaker_session=sagemaker_session,
    )
    predictor = model.deploy(
        instance_type="ml.m5.large",
        initial_instance_count=1,
        endpoint_name=endpoint_name
    )
    print("Modelo desplegado en SageMaker con el endpoint:", endpoint_name)
    return predictor

deploy_model("s3://your-bucket/mlops_pipeline_project/model.joblib", "mlops-endpoint")
