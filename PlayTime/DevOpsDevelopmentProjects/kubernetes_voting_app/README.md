## Commands to use when you are on local

you don't need to use deployfiles

- cd into working directory
- ls to see all the files
- `kubectl get svc` to check if there's any services running
- `kubectl create -f voting-app-pod.yml` to create the pod for voting-app
- `kubectl create -f voting-app-service.yml` to create the service for voting app
- check the status of pod and servicr for voting app by `kubectl get pods, svc`
- check the url on which you can see the voting app can be accessed as end user: `minikube service voting-service --url`
- this command will give you ip address and port to access voting-app
- `kubectl create -f redis-pod.yml` to create the pod for redis
- `kubectl create -f redis-service.yml` to create the service for redis
- check the status of pod and service for redis by `kubectl get pods, svc`
- `kubectl create -f postgres-pod.yml` to create the pod for postgres
- `kubectl create -f postgres-service.yml` to create the service for postgres
- check the status of pod and service for postgres by `kubectl get pods, svc`
- `kubectl create -f worker-app-pod.yml` to create the pod for worker app
- `kubectl create -f worker-app-service.yml` to create the service for worker-app
- check the status of pod and service for worker-app by `kubectl get pods, svc`
- `kubectl create -f result-app-pod.yml` to create the pod for worker app
- `kubectl create -f result-app-service.yml` to create the service for worker-app
- check the status of pod and service for result-app by `kubectl get pods, svc`
- check the url on which you can see the voting app can be accessed as end user: `minikube service result-service --url`
- this command will give you ip address and port to access result-app

## Commands to use when you deploy the apps

- `kubectl create -f voting-app-deploy.yml` to create the pod for voting-app
- `kubectl create -f voting-app-service.yml` to create the service for voting app
- `kubectl create -f redis-deploy.yml` to create the pod for voting-app
- `kubectl create -f redis-service.yml` to create the service for voting app
- `kubectl create -f postgres-deploy.yml` to create the pod for voting-app
- `kubectl create -f postgres-service.yml` to create the service for voting app
- `kubectl create -f worker-app-deploy.yml` to create the pod for voting-app
- `kubectl create -f worker-app-service.yml` to create the service for voting app
- `kubectl create -f result-app-deploy.yml` to create the pod for voting-app
- `kubectl create -f result-app-service.yml` to create the service for voting app
- check the status of deployment by `kubectl get deployments`
- check the status of pod and service by `kubectl get pods, svc`
- check the pods by `kubectl get pods`
- check the url on which you can see the voting app can be accessed as end user: `minikube service voting-service --url`
  `minikube service result-service --url`
- this command will give you ip address and port to access result-app
