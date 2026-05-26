variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment (demo, staging, production)"
  type        = string
}

variable "image_uri" {
  description = "ECR image URI for the Lambda function"
  type        = string
}

variable "django_secret_key" {
  description = "Django SECRET_KEY — use a long, random string in production"
  type        = string
  sensitive   = true
}

variable "about_message" {
  description = "Message returned by the root endpoint"
  type        = string
  default     = ""
}

variable "log_retention_in_days" {
  description = "Number of days to retain CloudWatch logs"
  type        = number
  default     = 30
}
