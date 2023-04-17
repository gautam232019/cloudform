pipeline {
    agent any
    stages{
        stage('Deploy CloudFormation Stack') {
            steps {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "gautamawscreds"]]) {
                        sh '''
                            python3 script.py
                        '''
                }
            }
        }
    }
}