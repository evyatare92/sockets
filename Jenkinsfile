pipeline
{
    agent {
		label 'master'
	}
    stages
    {
        stage("build") {
            steps{
                //sh script: "docker build ./src -t sockets"
				sh script: 'echo testing dev1'
            }
        }
        stage("deploy local docker"){
            steps{
				//sh script: "docker stop mysocket 2> /dev/null"
				//sh script: "docker rm mysocket 2> /dev/null"
                //sh script: "docker run -d --name mysocket -p 1234:1234 -e SOCKET_PORT=1234 -e SOCKET_QUEUE_LENGTH=5 sockets"
				sh script: 'echo running container dev1'
            }
        }
		stage("test container"){
            steps{
				//sh script: "python3.6 test/Client.py localhost 1234"
				sh script: 'testing container dev1'
            }
        }
        stage("deploy to azure AKS"){
            steps{
                //sh script: "helm install sockets ./helm/sockets --kubeconfig /home/jenkins/.kube/config"
				sh script: 'deploying to kubernetes dev1'
            }
        }
    }
}
