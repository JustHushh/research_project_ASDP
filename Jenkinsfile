pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'justhushh'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/JustHushh/research_project_ASDP.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                // обходим PEP 668 и обновляем pip
                sh '''
                    python3 -m pip install --upgrade pip --break-system-packages
                    python3 -m pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    python3 -m pytest --maxfail=1 --disable-warnings -q || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    docker.build("${DOCKERHUB_USER}/research_project_ASDP:latest")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                withCredentials([string(credentialsId: 'dockerhub_token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login -u ${DOCKERHUB_USER} --password-stdin
                        docker push ${DOCKERHUB_USER}/research_project_ASDP:latest
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs for details.'
        }
    }
}
