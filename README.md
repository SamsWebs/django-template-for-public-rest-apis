# Django Template for Public REST APIs

This is a template for creating a public REST API using Django, Django Ninja, and AWS Lambda with API Gateway. It is intended to be used as a starting point for new projects.

[![Tests](https://github.com/SamsWebs/django-template-for-public-rest-apis/actions/workflows/pr-validate.yml/badge.svg)](https://github.com/SamsWebs/django-template-for-public-rest-apis/actions/workflows/pr-validate.yml)

## Overview

This template is written in Python 3.12 and uses the [Django Ninja](https://django-ninja.dev/) framework for handling HTTP requests/responses.  Our API is stateless, has no database, and is intended to run ephemerally on serverless environments (currently AWS Lambda via API Gateway v2).  We achieve this by wrapping our ASGI application with [Mangum](https://mangum.fastapiexpert.com/), an ASGI adapter for AWS Lambda.  You can still develop locally by running Django's built-in development server.

## Setup

1. Create a new repository from this template and clone it!
2. Create and activate a virtual environment: `python -m venv .venv && source .venv/bin/activate`
3. Install dependencies with `pip install -r requirements-dev.txt`.
4. Create `.envrc` via `cp .envrc.example .envrc` and fill in the necessary environment variables.  This file type assumes you are using `direnv` to manage your environment variables.  If you are not, export the variables in your shell or use a different method.
5. Start your local server with `python -m django runserver --settings=app.settings`.
6. Start developing!

## Development

Enable git hooks by running `pre-commit install --hook-type pre-commit --hook-type pre-push` in the root of your project.

**On every commit:**
- `ruff format` — formats code (Black-compatible)
- `ruff check --fix` — lints and auto-fixes imports, style, annotations, and more

**On every push:**
- `pytest` — runs the full test suite and blocks the push if any tests fail

You can also run these manually at any time:

```bash
ruff format app/ specs/   # format
ruff check app/ specs/    # lint
pytest                    # test
pytest --cov=app --cov-report term  # test with coverage
```

**Important things to note:**

- This template uses API Gateway v2 (HTTP API), making it publicly accessible over the internet.
- There is no database. The API is stateless by design.
- Django Ninja generates automatic interactive API documentation at `/api/docs`.

## Testing

Run the test suite with:

```bash
pytest
```

## Linting

Run the linter with:

```bash
ruff check .
```

## Deployment

This template is intended to be deployed to AWS Lambda via API Gateway v2. You can deploy your code by running the [push-images-and-update-lambda.yml](.github/workflows/push-images-and-update-lambda.yml) GitHub Action. A pre-requisite is the necessary infrastructure to be set up in AWS via the Terraform code in the `.infrastructure` directory.  This will create the necessary resources for your Lambda function to run.  Please see the [README](.infrastructure/README.md) in the `.infrastructure` directory for more information.

For the GitHub Action to work, you will need to set up the necessary secrets in your repository:

- `AWS_ACCOUNT_ID` - Your AWS account ID
- `AWS_ACCESS_KEY_ID` - Your AWS access key ID
- `AWS_SECRET_ACCESS_KEY` - Your AWS secret access key
