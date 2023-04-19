pipeline {
    agent any
    stages{
        //manas
        stage('Deploy CloudFormation Stack in first aws account') {
            steps {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "gautamawscreds"]]) {
                        sh '''
                            python3 script2.py
                        '''
                }
            }
        },
        //gautam
        stage('Deploy CloudFormation Stack in second aws account') {
            steps {
                    withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: "gautamawscreds2"]]) {
                        sh '''
                            python3 script.py
                        '''
                }
            }
        }
    }
}