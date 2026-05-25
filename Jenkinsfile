pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Run Prediction') {
            steps {
                sh 'python predict.py'
            }
        }
    }
}
