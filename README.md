# Deploying a Flask API

This is the starter repo for the tutorial @ [Deploy A Simple Flask API To Kubernetes Using EKS](medium.com): for CI/CD with testing.

In this tutorial you will containerize and deploy a Flask API to a Kubernetes cluster using Docker, AWS EKS, CodePipeline, and CodeBuild.

This Flask api consists of an API with two endpoints:

- `GET '/'` 
- `POST '/data'`

The built-in Flask server is adequate for local development, but not production, so you will be using the production-ready [Gunicorn](https://gunicorn.org/) server when deploying the app.

## Dependencies

- Docker Engine
    - Installation instructions for all OSes can be found [here](https://docs.docker.com/install/).
    - For Mac users, if you have no previous Docker Toolbox installation, you can install Docker Desktop for Mac. If you already have a Docker Toolbox installation, please read [this](https://docs.docker.com/docker-for-mac/docker-toolbox/) before installing.
- AWS Account
     - You can create an AWS account by signing up [here](https://aws.amazon.com/#).
     
## Deployment Steps

Deploying the app involves several steps:

1. Write a Dockerfile for the flask-api
2. Build and test the container locally
3. Create an EKS cluster
4. Store a secret using AWS Parameter Store
5. Create a CodePipeline pipeline triggered by GitHub checkins
6. Create a CodeBuild stage which will build, test, and deploy your code.
