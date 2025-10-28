# Automated CI/CD Pipeline for a Python Research Project

Repo: https://github.com/JustHushh/research_project_ASDP
Docker Hub: justhushh/research_project_ASDP

## Overview
This project demonstrates how to automate testing, building, and deploying a small Python research project using **Jenkins** and **Docker**.

## Project structure
```
research_project_ASDP/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── processor.py
├── tests/
│   └── test_processor.py
├── data.csv
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## Quick local run (Windows / Linux)
1. Install Python 3.10+ and pip.
2. From the project root:
   ```
   pip install -r requirements.txt
   pytest
   python app/main.py
   ```

Expected output:
```
Column means: {'a': 2.0, 'b': 5.0}
```

## Docker build & run
Build:
```
docker build -t justhushh/research_project_ASDP:latest .
```
Run:
```
docker run --rm justhushh/research_project_ASDP:latest
```

## Jenkins setup (minimal)
1. Run Jenkins with Docker (example):
   ```
   docker run -d --name jenkins ^
     -p 8080:8080 -p 50000:50000 ^
     -v jenkins_home:/var/jenkins_home ^
     -v //var/run/docker.sock:/var/run/docker.sock ^
     jenkins/jenkins:lts
   ```
2. In Jenkins: Manage Jenkins -> Plugins -> install: Git, Pipeline, Docker Pipeline, Credentials Binding.
3. Add Docker Hub token: Manage Jenkins -> Credentials -> Global -> Add Credentials (Secret text) ID: dockerhub_token
4. Create a new Pipeline:
   - Pipeline from SCM -> Git -> Repository: https://github.com/JustHushh/research_project_ASDP.git
   - Branch: */main
   - Script Path: Jenkinsfile

## What Jenkins will do
- Checkout code from GitHub
- Install dependencies
- Run pytest
- Build Docker image justhushh/research_project_ASDP:latest
- Push image to Docker Hub (if running on branch main/master and dockerhub_token provided)

## Troubleshooting
- If `docker: error during connect` -> start Docker Desktop and ensure WSL integration enabled.
- If Jenkins can't run docker -> grant access to docker socket when running Jenkins container.
- If `denied: access denied` on push -> recreate Docker Hub access token and update Jenkins credential.

## License
MIT
