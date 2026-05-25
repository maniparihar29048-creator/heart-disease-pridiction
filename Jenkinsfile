pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/maniparihar29048-creator/heart-disease-pridiction.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train_model.py'
            }
        }

        stage('Run Prediction') {
            steps {
                bat 'python predict.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t heart-disease-app .'
            }
        }
    }
}
