// Windows-compatible Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                bat 'docker build -t flask-app:%BUILD_NUMBER% .'
            }
        }
        
        stage('Test') {
            steps {
                bat 'echo "Running tests..."'
                // Add actual test commands here
                // bat 'python -m pytest test_app.py -v'
            }
        }
        
        stage('Deploy') {
            steps {
                bat 'docker stop flask-app || true'
                bat 'docker rm flask-app || true'
                bat 'docker run -d -p 5000:5000 --name flask-app flask-app:%BUILD_NUMBER%'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
