pipeline {
    agent {
        docker {
            image 'docker:latest' // Use the Docker image
            args '-v /var/run/docker.sock:/var/run/docker.sock' // Mount Docker socket for Docker commands
        }
    }

    environment {
        AWS_REGION = 'us-east-1'
        ECR_URI = '123456789012.dkr.ecr.us-east-1.amazonaws.com/my-repo'
        IMAGE_NAME = 'my-image'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/yourrepo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_URI}
                    docker tag ${IMAGE_NAME}:latest ${ECR_URI}:latest
                    docker push ${ECR_URI}:latest
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "kubectl set image deployment/my-deployment my-container=${ECR_URI}:latest --record"
                }
            }
        }
    }
}
