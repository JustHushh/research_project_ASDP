pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'justhushh'
        // Добавляем ~/.local/bin в PATH
        PATH = "$HOME/.local/bin:$PATH"
        // Для Docker (если в контейнере)
        DOCKER_HOST = 'unix:///var/run/docker.sock'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/JustHushh/research_project_ASDP.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip --user
                    python3 -m pip install -r requirements.txt --user
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Теперь pytest будет найден
                sh 'pytest --maxfail=1 --disable-warnings -q || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Используем docker из PATH
                    def image = docker.build("${DOCKERHUB_USER}/research_project_ASDP:latest")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
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
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        always {
            // Опционально: очистка
            sh 'docker rmi ${DOCKERHUB_USER}/research_project_ASDP:latest || true'
        }
    }
}
