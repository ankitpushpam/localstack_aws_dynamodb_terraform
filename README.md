# Local DynamoDB Setup and Data Interaction Guide

This guide provides step-by-step instructions for setting up a local DynamoDB instance using LocalStack and interacting with it using Terraform and a Python script. This setup allows you to develop and test DynamoDB-related functionalities without the need for an AWS account.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your development machine:

- Docker: To run LocalStack in a Docker container.
- Terraform: For provisioning infrastructure.
- Python: To run the provided Python script.
- AWS CLI (Optional): For additional DynamoDB operations using the AWS CLI.

## Project Structure

This project consists of the following components:

- Docker Compose File: `docker-compose.yaml`
  - Defines the LocalStack service, which simulates AWS services locally.
- Terraform Configuration: `main.tf`
  - Defines the Terraform resources for DynamoDB tables using the LocalStack-specific provider.
- Python Script: `local_dynamodb_interaction.py`
  - Demonstrates how to interact with the local DynamoDB tables using Python and the `boto3` library.
- Makefile: `Makefile`
  - Provides convenient commands for starting, stopping, and testing the setup.

## Step 1: Start LocalStack and DynamoDB

1. Open your terminal and navigate to the project directory.

2. Run the following command to start LocalStack and DynamoDB in a Docker container:

   ```shell
   make run-docker
   ```

   This command uses the `docker-compose.yaml` file to launch LocalStack with DynamoDB on port 4566.

## Step 2: Initialize Terraform

1. With LocalStack running, open a new terminal window.

2. Navigate to the project directory.

3. Run the following commands to initialize Terraform:

   ```shell
   make init-terraform
   ```

   This command initializes the Terraform configuration.

## Step 3: Create DynamoDB Tables

1. After initializing Terraform, run the following command to create DynamoDB tables:

   ```shell
   make apply-terraform
   ```

   Terraform will create two DynamoDB tables, `order_table` and `user_table`, using the LocalStack-specific provider. These tables simulate AWS DynamoDB tables locally.

## Step 4: Interact with Local DynamoDB

1. Run the Python script to interact with the local DynamoDB tables:

   ```shell
   python local_dynamodb_interaction.py
   ```

   This script does the following:

   - Initializes a `boto3` DynamoDB resource with the LocalStack endpoint.
   - Uploads sample records to the `order_table` and `user_table`.
   - Reads a single item from the `order_table`.
   - Reads batch items from the `user_table`.
   - Saves the results as JSON files (`order_item.json` and `user_items.json`).

2. Check the terminal output for the results of the operations.

## Additional Operations (Optional)

If you want to perform additional DynamoDB operations using the AWS CLI, you can use the LocalStack endpoint URL. For example:

```shell
aws dynamodb list-tables --endpoint-url http://localhost:4566
```

## Clean Up

To stop and remove the LocalStack Docker container and DynamoDB tables, run the following command:

```shell
make stop-docker
```

This command will stop the LocalStack container and remove the DynamoDB tables created by Terraform.

## Conclusion

You have successfully set up a local DynamoDB instance using LocalStack, provisioned DynamoDB tables using Terraform, and interacted with the tables using a Python script. This development environment allows you to test and develop DynamoDB-related functionality locally without the need for an AWS account.

[Medium Article: Setting Up LocalStack and DynamoDB Tables with Docker and Terraform](https://medium.com/@pushpam.ankit/setting-up-localstack-and-dynamodb-tables-with-docker-and-terraform-44e2811d554d)
