pipeline {
    agent {
        label 'slave_01'
    }
    environment{
        docker_image_name='amway'
        docker_container_name='amway'
    }
    parameters{
	string(name:'branch',defaultValue:'master',description:'git branch')
    }
    stages {
        stage('同步源码') {
            steps {
                git url:'git@github.com:Ellie2020-ellie/Hogwarts_works.git', branch: '$branch'
            }
        }
        stage('输入内容') {
            steps {
                sh '''
                    . ~/.bash_profile
                    echo '$?????????>>>>>>>>>>'
                    echo '$docker_container_name'
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