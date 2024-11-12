Here’s a list of the most useful Kubernetes (`kubectl`) commands that are commonly used for managing Kubernetes clusters, deployments, services, pods, and more.

### **Basic Commands**

1. **Check Cluster Info**

```bash
kubectl cluster-info # Displays information about the Kubernetes cluster.
```

2. **Check Node Status**

```bash
kubectl get nodes # Lists all nodes in the cluster and shows their statuses.
```

3. **View Configurations**

```bash
kubectl config view # Displays the current context and configuration.
```

4. **Switch Context (Cluster)**

```bash
kubectl config use-context <context-name> # Switches between different cluster contexts.
```

---

### **Working with Pods**

1. **Get Pods**

```bash
kubectl get pods # Lists all pods in the default namespace.
```

2. **Get Pods in All Namespaces**

```bash
kubectl get pods --all-namespaces # Lists all pods in every namespace.
```

3. **Describe a Pod**

```bash
kubectl describe pod <pod-name> # Shows detailed information about a specific pod.
```

4. **Log Output from a Pod**

```bash
kubectl logs <pod-name> # Displays the logs of a specific pod.
```

5. **Tail Logs in Real-Time**

```bash
kubectl logs -f <pod-name> # Follows the logs of a specific pod in real-time.
```

6. **Execute a Command in a Running Pod**

```bash
kubectl exec -it <pod-name> -- /bin/sh # Opens an interactive shell session in the container (replace `/bin/sh` with the appropriate shell for your container).
```

---

### **Working with Deployments**

1. **Get Deployments**

```bash
kubectl get deployments # Lists all deployments in the current namespace.
```

2. **Describe a Deployment**

```bash
kubectl describe deployment <deployment-name> # Provides detailed information about a specific deployment.
```

3. **Create or Apply a Deployment**

```bash
kubectl apply -f <deployment-file.yaml> # Creates or updates resources in the deployment YAML file.
```

4. **Scale a Deployment**

```bash
kubectl scale deployment <deployment-name> --replicas=<number-of-replicas> # Scales the specified deployment to the desired number of replicas.
```

5. **Update Deployment (Rolling Update)**

```bash
kubectl rollout restart deployment <deployment-name> # Performs a rolling update by restarting the deployment.
```

6. **Check Rollout Status**

```bash
kubectl rollout status deployment <deployment-name> # Checks the status of a rollout.
```

7. **Undo a Deployment Rollout**

```bash
kubectl rollout undo deployment <deployment-name> # Rolls back to the previous version of the deployment.
```

---

### **Working with Services**

1. **Get Services**

```bash
kubectl get services # Lists all services in the current namespace.
```

2. **Describe a Service**

```bash
kubectl describe service <service-name> # Displays detailed information about a specific service.
```

3. **Expose a Deployment as a Service**

```bash
kubectl expose deployment <deployment-name> --type=LoadBalancer --port=80 --target-port=8080 # Exposes a deployment as a service. You can use `--type=NodePort`, `ClusterIP`, or `LoadBalancer`.
```

4. **Get Service Endpoints**

```bash
kubectl get endpoints # Lists all endpoints that are exposed by services.
```

---

### **Working with Namespaces**

1. **Get All Namespaces**

```bash
kubectl get namespaces # Lists all available namespaces in the cluster.
```

2. **Create a New Namespace**

```bash
kubectl create namespace <namespace-name> # Creates a new namespace.
```

3. **Switch Namespace for Commands**

```bash
kubectl config set-context --current --namespace=<namespace-name> # Switches the default namespace for all subsequent commands.
```

4. **Delete a Namespace**

```bash
kubectl delete namespace <namespace-name> # Deletes a specific namespace.
```

---

### **Working with ConfigMaps and Secrets**

1. **Create a ConfigMap**

```bash
kubectl create configmap <configmap-name> --from-literal=<key>=<value> # Creates a ConfigMap from literal key-value pairs.
```

2. **Get ConfigMaps**

```bash
kubectl get configmaps # Lists all ConfigMaps in the current namespace.
```

3. **Describe a ConfigMap**

```bash
kubectl describe configmap <configmap-name> # Shows detailed information about a specific ConfigMap.
```

4. **Create a Secret**

```bash
kubectl create secret generic <secret-name> --from-literal=<key>=<value> # Creates a secret with literal key-value pairs.
```

5. **Get Secrets**

```bash
kubectl get secrets # Lists all secrets in the current namespace.
```

---

### **Managing Resources**

1. **Delete a Resource**

```bash
kubectl delete <resource-type> <resource-name> # Deletes the specified resource, e.g., `kubectl delete pod my-pod`.
```

2. **Apply Changes from a YAML File**

```bash
kubectl apply -f <file.yaml> # Applies changes defined in the YAML file to the cluster.
```

3. **Delete Resources from a YAML File**

```bash
kubectl delete -f <file.yaml> # Deletes the resources defined in the YAML file.
```

4. **View Resource Usage (CPU/Memory)**

```bash
kubectl top pods # Shows resource usage for all running pods.
```

---

### **Additional Useful Commands**

1. **Get Cluster Events**

```bash
kubectl get events # Lists all recent cluster events.
```

2. **Dry Run (Test a Command without Applying Changes)**

```bash
kubectl apply -f <file.yaml> --dry-run=client # Runs the command in dry-run mode to see the result without applying it.
```

3. **Port Forward a Pod**

```bash
kubectl port-forward pod/<pod-name> <local-port>:<container-port> # Forwards a port from the local machine to a pod.
```

4. **Run a Pod (One-Off Command)**

```bash
kubectl run <pod-name> --image=<image-name> --command -- <command> # Runs a one-time pod that executes the specified command.
```

5. **Get All Resources in a Namespace**

```bash
kubectl get all -n <namespace-name> # Lists all resources (pods, services, deployments, etc.) in a specific namespace.
```

---

### **Troubleshooting Commands**

1. **Get Pod Events**

```bash
kubectl get events --field-selector involvedObject.name=<pod-name> # Shows events related to a specific pod for troubleshooting.
```

2. **Check Pod Health**

```bash
kubectl get pod <pod-name> -o json | jq '.status' # Displays detailed status information about a specific pod.
```

3. **Debug a Pod**

```bash
kubectl exec -it <pod-name> -- /bin/sh # Opens an interactive shell session inside the pod for debugging.
```
