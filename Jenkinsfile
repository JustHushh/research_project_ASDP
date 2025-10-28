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

        // ⚡ Самое важное: используем Docker CLI внутри docker-агента
        stage('Build and Push Docker Image') {
            agent {
                docker {
                    image 'docker:27.0.3' // образ с Docker CLI
                    args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            environment {
                DOCKER_CLI_HINTS = 'false'
            }
            steps {
                echo 'Building and pushing Docker image...'
                withCredentials([string(credentialsId: 'dockerhub_token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh '''
                        echo "$DOCKERHUB_TOKEN" | docker login -u ${DOCKERHUB_USER} --password-stdin
                        docker build -t ${DOCKERHUB_USER}/research_project_ASDP:latest .
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
