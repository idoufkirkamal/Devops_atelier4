# Jenkins CI/CD Setup with Flask Application

This repository contains a simple Flask application with Jenkins CI/CD pipeline configuration.

## Prerequisites

- Docker Desktop installed
- Git installed

## Setup Instructions

### 1. Running Jenkins and Flask App with Docker Compose

```bash
# Start Jenkins and Flask application
docker-compose up -d
```

### 2. Accessing Jenkins

- Open a browser and navigate to `http://localhost:8080`
- The initial admin password can be found by running:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### 3. Setting up Jenkins

1. Install suggested plugins when prompted
2. Create your admin user
3. Configure Jenkins URL (default is fine)

### 4. Configure Jenkins Pipeline

1. Click on "New Item"
2. Enter a name for your project (e.g., "flask-app-pipeline") and select "Pipeline"
3. Click "OK"
4. In the configuration page, scroll down to the "Pipeline" section
5. Select "Pipeline script from SCM" from the Definition dropdown
6. Select "Git" from the SCM dropdown
7. Enter your repository URL
8. Make sure the "Script Path" is set to "Jenkinsfile"
9. Click "Save"

### 5. Running the Pipeline

1. Click on your pipeline project
2. Click "Build Now" to start the build process
3. Monitor the build progress in the "Build History" section

## Testing the Application

- Flask app will be available at `http://localhost:5000`
- API endpoints:
  - Homepage: `http://localhost:5000/`
  - Hello DevOps: `http://localhost:5000/hello`

## Running Tests Manually

```bash
python -m unittest test_app.py
```

## Project Structure

- `app.py`: Flask application
- `Dockerfile`: Docker configuration for Flask app
- `Jenkinsfile`: Jenkins pipeline definition
- `docker-compose.yml`: Docker Compose configuration
- `test_app.py`: Unit tests for Flask app
