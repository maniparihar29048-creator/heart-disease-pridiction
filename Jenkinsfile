pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/maniparihar29048-creator/heart-disease-pridiction.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 train_model.py'
            }
        }

        stage('Run Prediction') {
            steps {
                sh 'python3 predict.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t heart-disease-app .'
            }
        }
    }
}
