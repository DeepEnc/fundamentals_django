pipeline {
    agent any

    environment {
        AWS_REGION = 'your-aws-region'
        ECR_URI = 'your-ecr-repo-uri'
        IMAGE_NAME = 'your-image-name'
        CLUSTER_NAME = 'your-eks-cluster-name'
        DEPLOYMENT_NAME = 'your-deployment-name'
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
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        stage('Login to ECR') {
            steps {
                script {
                    sh '''
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_URI}
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh '''
                    docker tag ${IMAGE_NAME}:latest ${ECR_URI}:${BUILD_NUMBER}
                    docker push ${ECR_URI}:${BUILD_NUMBER}
                    '''
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                script {
                    sh '''
                    kubectl set image deployment/${DEPLOYMENT_NAME} ${DEPLOYMENT_NAME}=${ECR_URI}:${BUILD_NUMBER} --record
                    kubectl rollout status deployment/${DEPLOYMENT_NAME}
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
