pipeline {
    agent {
        label 'slave_01'
    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }
    post {
        always{
            echo 'hello ,ellie'
        }
    }
}