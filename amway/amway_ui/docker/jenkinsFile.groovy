pipeline {
    agent {
        label 'slave_01'
    }
    environment{
        docker_image_name='amway'
        docker_container_name='amway'
    }
    stages {
        stage('同步源码') {
            steps {
                git url:'git@github.com:Ellie2020-ellie/Hogwarts_works.git'
            }
        }
        stage('输入内容') {
            steps {
                sh '''
                    . ~/.bash_profile
                    echo '${docker_image_name}  +>>>>test>>>+   $docker_container_name'
                    echo ${chrome}
                    echo ${pwd}
                '''
            }
        }
    }
    post {
        always{
            echo 'hello ,ellie'
        }
    }
}