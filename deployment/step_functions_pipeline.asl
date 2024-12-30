{
  "StartAt": "GenerateDataset",
  "States": {
    "GenerateDataset": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:generate-dataset",
      "Next": "PreprocessData"
    },
    "PreprocessData": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:preprocess-data",
      "Next": "TrainModel"
    },
    "TrainModel": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:train-model",
      "Next": "DeployModel"
    },
    "DeployModel": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:deploy-model",
      "End": true
    }
  }
}
