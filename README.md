# Github [Project Repo] to AWS Lambda

If your organization wants to use serverless computing (for example, to handle API or backend requests), then AWS Lambda can be a great choice.

Suppose you already have a project where the main code is stored in a GitHub repository. If you want to take some parts of that code/scripts and run them as AWS Lambda functions, you don’t have to copy things manually.

Instead, you can use AWS CodeBuild. It helps you automatically take your code from GitHub, build it, and deploy it to AWS Lambda whenever you make updates. This way, deployment is automated, faster, and less error-prone.

# TL;DR

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

# **OVERVIEW OF STEPS INVOLVED:**

1> Prepare the code, for Codebuild on local IDE (for me, it was Visual Studio Code).
<img width="1252" height="302" alt="image" src="https://github.com/user-attachments/assets/0223c1a8-8f34-409c-a750-dbaacdbdad9d" />

2> Create a AWS CodeBuild Project 
  - Add your Github Repository Details
  - Configure AWS Code Buil Project:
     - Configure your Credentials so that AWS can check with Github for Events like PR Merge/Etc on specific branches.
       
       <img width="596" height="762" alt="image" src="https://github.com/user-attachments/assets/cd4d5f9b-b6f7-4997-87de-c6c538fe186f" />
     - Configure the environment on which CodeBuild will run.
       
       <img width="602" height="712" alt="image" src="https://github.com/user-attachments/assets/e942b65d-6bf1-4bfd-a11e-a002c27b55fa" />

     - If Reqd, add your custom BuildSpec yaml file.
       
       <img width="603" height="282" alt="image" src="https://github.com/user-attachments/assets/1754b5ed-39a4-4a87-9a1f-fa162b12020e" />
     - If your Codebuild, is using S3/Lambda/any other AWS resources, you will need to configure Lambda'a IAM/ Service Role policies accordingly.
       <img width="1297" height="551" alt="image" src="https://github.com/user-attachments/assets/fd18fd45-8509-4553-8c9e-f6229778a6cc" />
       <img width="1022" height="222" alt="image" src="https://github.com/user-attachments/assets/568a8d3c-322b-4c7f-af26-b21f200b70cd" />

3> Create a Pull request to simulate the PULL_REQUEST_MERGE event, for AWS CodeBuild to trigger.
4> Monitor the CodeBuild Build's run.
5> Post build run, view the targetted lambda fucntion.

**Lambda Function Post Deployment:**

<img width="742" height="162" alt="image" src="https://github.com/user-attachments/assets/cd644a53-ce08-4a74-b23d-7baec40717f6" />

**CodeBuild Project:**
<img width="917" height="226" alt="image" src="https://github.com/user-attachments/assets/af0431bc-8ce4-41fd-b085-07645556e830" />
<img width="913" height="536" alt="image" src="https://github.com/user-attachments/assets/0b2742e7-f057-4736-8dba-dfcf26121f12" />
<img width="890" height="416" alt="image" src="https://github.com/user-attachments/assets/f8dd2cf9-fe1e-4edd-a180-56ffc258a91e" />
