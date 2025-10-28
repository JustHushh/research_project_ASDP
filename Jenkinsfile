pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')  // ID твоего секрета
        IMAGE_NAME = "justhushh/research_project_asdp"
        TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📦 Cloning repository..."
                git branch: 'main', url: 'https://github.com/JustHushh/research_project_ASDP.git'
            }
        }

        stage('Set up Python environment') {
            steps {
                echo "🐍 Setting up Python virtual environment..."
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "🧪 Running tests..."
                sh '''
                    . venv/bin/activate
                    pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh '''
                    docker build -t $IMAGE_NAME:$TAG .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "🚀 Pushing Docker image to Docker Hub..."
                sh '''
                    echo "$DOCKERHUB_CREDENTIALS_PSW" | docker login -u "$DOCKERHUB_CREDENTIALS_USR" --password-stdin
                    docker push $IMAGE_NAME:$TAG
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed! Check logs for details."
        }
    }
}
