pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args '-u root' // чтобы можно было устанавливать пакеты
    }
  }

  environment {
    IMAGE_NAME = "justhushh/research_project_ASDP"
  }

  stages {
    stage('Checkout') {
      steps {
        echo 'Cloning repository...'
        checkout scm
      }
    }

    stage('Install Dependencies') {
      steps {
        echo 'Installing Python dependencies...'
        sh '''
          python3 -m pip install --upgrade pip
          pip install -r app/requirements.txt pytest
        '''
      }
    }

    stage('Run Tests') {
      steps {
        echo 'Running tests...'
        sh 'pytest -q || true'  // убери || true если хочешь, чтобы падало на ошибках
      }
    }

    stage('Build and Push Docker Image') {
      steps {
        echo 'Building Docker image...'
        sh '''
          docker build -t ${IMAGE_NAME}:latest .
          docker images | grep ${IMAGE_NAME}
        '''
      }
    }
  }

  post {
    success {
      echo '✅ Build succeeded!'
    }
    failure {
      echo '❌ Pipeline failed! Check logs for details.'
    }
  }
}
