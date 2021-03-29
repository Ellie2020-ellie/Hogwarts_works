pipeline {
    environment{
        docker_image_name='amway'
        docker_container_name='amway'
        workspace='/data/Server/Node'
    }
    agent {
        node {
            label 'slave_01'
            customWorkspace "${workspace}"
        }
    }
    stages {
        stage('同步源码') {
            steps {
                git url:'git@github.com:Ellie2020-ellie/Hogwarts_works.git'
            }
        }
        stage('执行自动化脚本') {
            steps {
                sh '''
                    . ~/.bash_profile
                    cd "${workspace}/amway/amway_ui/test_case"
                    pytest -s test_grid.py
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