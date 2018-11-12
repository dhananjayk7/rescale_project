# Rescale data engineering price pipeline project

This repository contains instruction about how to deploy this project. This project uses AWS as the cloud provider to run the pipeline.

This repository contains: 
    1. Terraform script for deploying lambda function.
    2. Terraform script for deploying aws glue crawler. 
    3. Source code for lambda fucntion.


Steps to deploy the pipeline: 

    1. To run the project with all the default values, run the build.sh script. This script initializes terraform and runs terraform.
    2. when you run the build.sh script you will be able to see what resources would be created in the AWS account whose credentials are       stored in the aws credential file. 
    3. This code will automatically deploy the lambda code to read the json files from s3://sample-spot-prices bucket and deploy convert       them to csv files and upload to another S3 bucket in your account.
    4. I have not added code to create new s3 bucket to store CSV files, for now I will be using the S3 bucket which I already created         manually.
    5. This lambda function will be invoked everyday at 00:10 UTC using AWS CloudWatch event.
    6. This code will also create AWS glue crawler which will be schedules to run everyday at 00:15 UTC. This crawler will crawl over the      S3 bucket containing the csv files and create AWs Athena database and table to store the data in it. 
    7. You can log on to AWS Athena console to query the data or can connect to the databse using database connectors.
    
Future Scope: 

    1. Deploy the S3 bucket to store the CSV files using Terraform.
    2. Exception handling and error handling in lambda code.
    3. Logging in lambda code. 
    4. Deploy all IAM roles (AWS glue role and Lambda execution role) using Terraform.
    5. Deploy all components under one VPC.



