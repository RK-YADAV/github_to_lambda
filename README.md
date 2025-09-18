# Github [Project Repo] to AWS Lambda

In an organization which is leveraging/ looking to leverage serverless compute for say API/Backend Calls routing, AWS lambda can be an ideal choice.
If you have a project and your main code reside's on a Github repo like this, and there are parts of which you want to deploy as an AWS lambda code, then 
you can leverage AWS CodeBuild for automated deployment from Github to AWS Lambda. 

Just FYI - 

**AWS Lambda** is a serverless compute service provided by Amazon Web Services (AWS) that allows users to run code without provisioning or managing servers. It operates on an event-driven model, executing code in response to various events and automatically managing the underlying compute resources.

**AWS CodeBuild** is a fully managed build service within the Amazon Web Services (AWS) cloud. It is designed to compile source code, run unit tests, and produce deployable artifacts, eliminating the need for users to provision, manage, and scale their own build servers.

In this demo, we are preparing - 
 - buildspec.yml - Required for the AWS CodeBuild to start automated deployment of our AWS Lambda Function, and tells -
      - Exactly which folder to use,
      - What dependencies to install,
      - Where to look for the lambda code,
      - Where the code is to be stored post deployment (S3 in our case).
      - Which AWS Lambda function to be used/created.
 - requirement.txt - Contains all the required packages and dependencies name required by the lambda function.
 - Lambda function - A python file, containing our main function, for serverless processing.
