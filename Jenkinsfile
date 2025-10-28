pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "justhushh/research_project_ASDP"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/JustHushh/research_project_ASDP.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { return env.BRANCH_NAME == 'main' || env.BRANCH_NAME == 'master' }
            }
            steps {
                withCredentials([string(credentialsId: 'dockerhub_token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh '''
                    echo "$DOCKERHUB_TOKEN" | docker login -u justhushh --password-stdin
                    docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { return env.BRANCH_NAME == 'main' }
            }
            steps {
                echo 'Running container from the latest image...'
                sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE:latest || true'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
