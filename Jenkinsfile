pipeline {
    agent {
        docker {
            image 'chinodesuuu/ci-amethyst'
        }
    }
    environment { 
        WEBHOOK_URL = credentials('WEBHOOK_URL') 
    }
    stages {
        stage('Test') {
            steps {
                sh 'cloc .'
                sh 'flake8 --show-source --max-line-length 120 .'
                sh 'python3 -m compileall .'
            }
        }
    }
    post {
        success {
        sh 'python3.5 jenkins.py successful'
        }
        failure {
        sh 'python3.5 jenkins.py failure'
        }
        unstable {
        sh 'python3.5 jenkins.py unstable'
        }
    }
}