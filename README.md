# Deployment of a Helicone proxy server on AWS Lambda using the Serverless Framework.

## Description

This repository demonstrates how to deploy helicone proxy server on AWS Lambda using the serverless framework.

**Reference**: `https://github.com/madgicaltechdom/python-lambda-db-extraction/blob/main/README.md`


## Prerequisite
  - AWS ACCOUNT 
  - SERVERLESS should be installed on your local machine
    ```
    brew install serverless   #For MacOS
    ```
    ```
    serverless --version
    ```
  - AWS CLI
  - [AWS should be configured on your local machine](https://medium.com/nerd-for-tech/configuration-and-credential-file-settings-in-aws-cli-61c7ff0a1cd6)

## Deployment

Step-by-step user guide

1. Run the below command to clone this repo:
```
git clone https://github.com/madgical-ai/deployment-error.git
```

2. Run the below command to install the dependency: 

```
pip3 install -t src/vendor -r aws_requirements.txt
```

4. You can test the Lambda function locally using the Serverless Framework:

```
serverless invoke local --function proxyserver
```
5. To deploy the function you can use below command.
```
serverless deploy
```
6. After deploying, you will receive an API link.
```
POST - https://kyuy826iz5.execute-api.ap-south-1.amazonaws.com/dev/request/{remaining_path+}
```
7. Test Case Example
```
import openai
from langchain.llms import AzureOpenAI
import os

openai.api_type  = "azure"
os.environ["OPENAI_API_KEY"]="9fb2f004510099a"
openai.api_version="2023-03-15-preview"
openai.api_base = "https://kyuy826iz5.execute-api.ap-south-1.amazonaws.com/dev/request/a"

# Create the completion request
output = AzureOpenAI(
    headers={
        "Helicone-Auth": "Bearer sk-helicone-kjll5bq-ywceloy-ujfo7ea-5jh7wwq",
        "Helicone-User-Id": "Abhishek Srivastava",  
    },
    engine="GPT4-8k",
    model_name="gpt-3.5-turbo",
    temperature= 0.5
    
)
print(output("Hii"))

```
Output : 
```
Hello! How can I help you today?
```
