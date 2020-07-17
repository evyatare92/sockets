pipeline
{
    agent any
    stages
    {
        stage("build") {
            steps{
                sh script: "docker build ./src -t sockets"
            }
        }
        stage("deploy"){
            steps{
                sh script: "docker run -d --name mysocket -p 1234:1234 -e SOCKET_PORT=1234 -e SOCKET_QUEUE_LENGTH=5 sockets"
            }
        }
        
    }
}