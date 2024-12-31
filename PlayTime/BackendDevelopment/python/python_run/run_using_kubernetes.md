### example of `k8s-deployments.yaml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: module1-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: module1
  template:
    metadata:
      labels:
        app: module1
    spec:
      containers:
        - name: module1-container
          image: your-registry/python-app:latest # Replace with your Docker image
          env:
            - name: PYTHON_MODULE
              value: "src/module1.py"
          ports:
            - containerPort: 8000 # Optional if the module exposes a web service

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: module2-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: module2
  template:
    metadata:
      labels:
        app: module2
    spec:
      containers:
        - name: module2-container
          image: your-registry/python-app:latest # Replace with your Docker image
          env:
            - name: PYTHON_MODULE
              value: "src/module2.py"
          ports:
            - containerPort: 8000 # Optional if the module exposes a web service

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: module3-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: module3
  template:
    metadata:
      labels:
        app: module3
    spec:
      containers:
        - name: module3-container
          image: your-registry/python-app:latest # Replace with your Docker image
          env:
            - name: PYTHON_MODULE
              value: "src/module3.py"
          ports:
            - containerPort: 8000 # Optional if the module exposes a web service
```

### example of `k8s-services.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: module1-service
spec:
  selector:
    app: module1
  ports:
    - protocol: TCP
      port: 80 # Expose port 80
      targetPort: 8000 # Route to container's port 8000
  type: ClusterIP

---
apiVersion: v1
kind: Service
metadata:
  name: module2-service
spec:
  selector:
    app: module2
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: ClusterIP

---
apiVersion: v1
kind: Service
metadata:
  name: module3-service
spec:
  selector:
    app: module3
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: ClusterIP
```

### commands to apply and check the deployments

```shell
kubectl apply -f k8s-deployments.yaml

kubectl apply -f k8s-services.yaml

kubectl get deployments

kubectl get services
```
