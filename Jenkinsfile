pipeline {
    agent any
    stages{
        //gautam
        stage('Deploy CloudFormation Stack in first aws account') {
            steps {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "gautamawscreds2"]]) {
                        sh '''
                            python3 script.py
                        '''
                }
            }
        }
        stage('Deploy CloudFormation Stack in second aws account') {
            steps {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "gautamawscreds"]]) {
                        sh '''
                            python3 script2.py
                        '''
                }
            }
        }
    }
}