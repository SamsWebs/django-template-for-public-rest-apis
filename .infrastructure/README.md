# Deploying Infrastructure with Terraform

This directory contains the Terraform configuration files to deploy the infrastructure for this Lambda function to AWS.

## Prerequisites

- Install Terraform [link](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- Install AWS CLI [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- Configure AWS CLI [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

## Deploying Environments

Currently, the Terraform code is set up to deploy the **demo**, **staging**, and **production** environments.  To deploy an environment, run the following commands:

```bash
cd .infrastructure
terraform init  # Initialize the Terraform configuration
terraform plan -var-file "environments/demo.tfvars"  # Plan the deployment
terraform apply -var-file "environments/demo.tfvars"  # Deploy the infrastructure
```

Terraform allows for reproducible infrastructure deployments by using the same configuration files to deploy the same infrastructure in different environments.  The `terraform apply -var-file "environments/<env name>.tfvars"` command will prompt you to confirm the deployment before proceeding.  So, any changes to the infrastructure can be reviewed before applying them.

Note: Additional environments can be added by creating a new `.tfvars` file in the `.infrastructure/environments` directory.

Each environment sets up the following AWS infrastructure:

- IAM Roles and Policies
- Lambda Function (container image)
- API Gateway v2 (HTTP API) — publicly accessible endpoint
- CloudWatch Log Group

## First-Time Setup

Before running Terraform, you must create an ECR repository to store your Docker images:

```bash
aws ecr create-repository --repository-name django-serverless-template --region us-east-1
```

Copy the repository URI and set it as `image_uri` in your `.tfvars` files (append a tag, e.g., `:latest`).

## Sensitive Variables

The `django_secret_key` variable is marked `sensitive` in Terraform. For production environments, consider storing it in AWS Secrets Manager and referencing it via a Lambda environment variable rather than passing it directly through Terraform.

If you make changes to the Terraform configuration, run `terraform validate` to check for syntax errors.  Before applying the changes, you can run `terraform plan` to see the changes that will be applied before running `terraform apply`.

## Cost Estimates

AWS Lambda, API Gateway v2, and CloudWatch Logs costs are based on usage. At low to moderate traffic, these services typically fall within the AWS free tier. Use the [AWS Pricing Calculator](https://calculator.aws) to estimate costs for your expected workload.
