# Student Academic Management Platform

A DevOps mini-project demonstrating a Python-based academic management application, automated testing, Docker containerization, and Kubernetes deployment.

## Project Overview

The application provides API endpoints for student records, courses, enrollments, and grades. It also calculates semester GPA based on recorded grades.

## Technologies Used

- Python and Flask
- Pytest for automated testing
- Flake8 for code quality
- Docker for containerization
- Kubernetes and Minikube for deployment
- Jenkins for CI/CD
- Git and GitHub for version control

## Features

- Application health-check endpoint
- Student record creation
- Course and enrollment management
- Enrollment credit-limit validation
- Duplicate-enrollment prevention
- Semester GPA calculation
- Automated unit testing
- Docker image creation
- Kubernetes deployment with three replicas
- Automatic pod replacement after a pod is deleted

## Project Structure

```text
student-academic-platform/
├── app/
│   ├── routes/
│   └── services/
├── database/
├── tests/
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── run.py
```

## Run Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run tests:

```bash
python -m pytest -v
```

Check code quality:

```bash
python -m flake8 app tests run.py
```

## Run with Docker

Build the image:

```bash
docker build -t student-academic-platform:v1.0.0 .
```

Run the container:

```bash
docker run -d --name student-academic-demo -p 5050:5000 student-academic-platform:v1.0.0
```

Test the health endpoint in PowerShell:

```powershell
Invoke-RestMethod http://localhost:5050/health
```

Stop the container:

```bash
docker stop student-academic-demo
```

## Kubernetes Deployment

Start Minikube and load the image:

```bash
minikube start
minikube image load student-academic-platform:v1.0.0
```

Apply the Kubernetes configuration:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Verify the deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

The deployment is configured for three replicas. Kubernetes was verified to replace a deleted pod and restore the desired replica count.

Stop Minikube after the practical:

```bash
minikube stop
```

## Jenkins CI/CD Pipeline

The Jenkins pipeline automates the main stages of the application workflow, including dependency installation, code quality checks, automated testing, and Docker image building. These stages help maintain code quality and support consistent application builds.

## Data Management

The application manages student records, courses, enrollments, and grades through its academic service layer. The project structure separates application routes, business logic, tests, and deployment configuration to support maintainability and future development.

## Testing Results

- Five automated unit tests passed.
- Flake8 completed without reported issues.
- Kubernetes deployment was verified with three running replicas.
- Pod replacement was successfully observed after deleting a pod.

## Future Improvements

- Integrate a persistent database.
- Add authentication and authorization.
- Expand automated test coverage.
- Improve deployment automation and monitoring.

## Repository

[DevOps-And-Cloud on GitHub](https://github.com/ashutoshnarawade/DevOps-And-Cloud)

**Project:** Student Academic Management Platform — DevOps Mini-Project
