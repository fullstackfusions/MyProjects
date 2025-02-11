
Folder structure:

```
project-root/
│── backend/                # Go backend
│   ├── main.go             # Entry point
│   ├── go.mod              # Go module dependencies
│   ├── go.sum              # Checksums for dependencies
│   ├── Dockerfile          # Docker configuration
│   ├── .gitignore          # Ignore files
│   ├── README.md           # Backend documentation
│── frontend/               # React frontend
│   ├── public/             # Static assets
│   ├── src/                # Source code
│   │   ├── App.tsx         # Main React component
│   │   ├── index.tsx       # Entry point
│   │   ├── api.ts          # API call functions
│   │   ├── styles.css      # Custom styles (optional)
│   ├── package.json        # Frontend dependencies
│   ├── vite.config.ts      # Vite configuration
│   ├── tsconfig.json       # TypeScript config
│   ├── Dockerfile          # Docker configuration
│   ├── .gitignore          # Ignore files
│   ├── README.md           # Frontend documentation
│── deployment/             # Deployment-related files
│   ├── Caddyfile           # Caddy Load Balancer Config
│   ├── docker-compose.yml  # Local dev environment
│── .github/                # GitHub Actions CI/CD workflows
│   ├── workflows/
│   │   ├── backend.yml     # CI/CD for backend
│   │   ├── frontend.yml    # CI/CD for frontend
│── k8s/                    # Kubernetes manifests
│   ├── backend-deploy.yaml # Backend Deployment
│   ├── frontend-deploy.yaml # Frontend Deployment
│   ├── caddy-deploy.yaml   # Caddy Deployment
│── README.md               # Project documentation
```

# Running through docker compose:

## **✅ Steps to Test the Full Application**

### **1️⃣ Check Running Containers**
Run the following command to **verify if all containers are running**:
```sh
docker ps
```
✅ Expected Output (or similar):
```
CONTAINER ID   IMAGE                PORTS                  NAMES
xxxxxxxxxxxx   caddy:2              0.0.0.0:80->80/tcp     caddy-container
xxxxxxxxxxxx   your-frontend-image  0.0.0.0:3000->80/tcp   frontend-container
xxxxxxxxxxxx   your-backend-image   0.0.0.0:8080->8080/tcp backend-container
```
This confirms all services are up.

---

## **✅ Step 1: Basic Frontend UI Testing**
1. **Open your browser** and go to:
   ```
   http://localhost
   ```
   ✅ **Expected:** You should see the frontend UI.

2. **Enter a name in the input field**.
3. **Click the "Greet Me" button**.

---

## **✅ Step 2: Check Browser (Frontend)**
   - Open **Developer Tools (`F12`) → Network Tab**.
   - Click **"Greet Me"** in UI.
   - Look for **API request to `/greet?name=<yourname>`**.
   - ✅ **Expected Backend Log Entry:**
     ```
     Received request: GET /greet
     ```

---

## **✅ Step 3: Verify Backend Response via Browser**
1. **Open Developer Tools (`F12`) → Network Tab**.
2. **Click the "Greet Me" button again**.
3. Look for the **API request to `/greet?name=<yourname>`**.
   - **If it appears in Network Tab → Click on it → Check Response.**
   - ✅ **Expected Response:** `"Hello, <yourname>!"`.

4. **If no API request is triggered**, check the **Console Tab** for errors.

---

## **✅ Step 4: Test API Request (`http://localhost/greet?name=<yourname>`)**

Run:
```sh
curl "http://localhost/greet?name=<yourname>"
```
✅ **Expected Logs in Backend Container**
```
Received request: GET /greet
Response: Hello, <yourname>!
```

---

## **✅ Step 5: Directly Test Backend Through Caddy**
If the frontend **does not display the greeting**, test if Caddy **is correctly routing to the backend**.

Run:
```sh
curl "http://localhost/greet?name=<yourname>"
```
✅ **Expected Output:**
```
Hello, <yourname>!
```


# Running through Kubernetes:

Since you may be using **Minikube**, let's restart it and ensure `kubectl` is properly configured.

## **✅ Step 1: Stop and Restart Minikube**
```sh
minikube stop   # If you have previously running
minikube delete
minikube start  # This will start new minikube cluster
```
🚨 **Why?**
- `minikube delete` **removes any corrupted clusters**.
- `minikube start` **creates a fresh cluster**.

---

## **✅ Step 2: Check If Kubernetes Is Running**
After Minikube starts, verify that Kubernetes is running:
```sh
kubectl cluster-info
```
✅ Expected Output:
```
Kubernetes control plane is running at https://127.0.0.1:XXXXX
```
If you see **"Unable to connect to the server"**, Minikube is still not running.

---

## **✅ Step 3: Set `kubectl` to Use Minikube's Context**
Run:
```sh
kubectl config use-context minikube
```
Then, check:
```sh
kubectl get nodes
```
✅ Expected Output:
```
NAME       STATUS   ROLES                  AGE     VERSION
minikube   Ready    control-plane,master   2m      v1.XX.XX
```
If you see **"No resources found"**, Kubernetes is not ready yet. Wait a few minutes and try again.

---

## **✅ Step 4: Apply Kubernetes Deployment Again**
Once the cluster is confirmed running, try deploying again:
```sh
kubectl apply -f k8s/backend-deploy.yaml
kubectl apply -f k8s/frontend-deploy.yaml
kubectl apply -f k8s/caddy-deploy.yaml
```
✅ **Expected Output**
```
deployment.apps/backend created
service/backend-service created
deployment.apps/frontend created
service/frontend-service created
deployment.apps/caddy created
service/caddy-service created
configmap/caddy-config created
```

---

## **✅ Step 5: Verify Deployments & Services**

### **1️⃣ Check if Pods Are Running**

```sh
kubectl get pods
```
✅ Expected Output:
```
NAME                           READY   STATUS    RESTARTS   AGE
backend-xxxx-xxxxx             1/1     Running   0         1m
backend-xxxx-xxxxx             1/1     Running   0         1m
frontend-xxxx-xxxxx            1/1     Running   0         1m
frontend-xxxx-xxxxx            1/1     Running   0         1m
caddy-xxxx-xxxxx               1/1     Running   0         1m
```
- If any **pod is in `CrashLoopBackOff` or `Pending`**, check logs:
  ```sh
  kubectl logs -l app=backend
  kubectl logs -l app=frontend
  kubectl logs -l app=caddy
  ```

---

### **2️⃣ Check Services**
```sh
kubectl get services
```
✅ Expected Output:
```
NAME               TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
backend-service   ClusterIP      10.96.0.1       <none>        8080/TCP       1m
frontend-service  ClusterIP      10.96.0.2       <none>        80/TCP         1m
caddy-service     LoadBalancer   10.96.0.3       <pending>     80:30000/TCP   1m
```
- If **Caddy’s `EXTERNAL-IP` is `<pending>`**, expose Minikube’s LoadBalancer:
  ```sh
  minikube service caddy-service --url
  ```
  ✅ Expected Output:
  ```
  http://192.168.49.2:30000
  ```
  - Open this **URL in your browser** → **You should see the frontend UI**.

---

## **✅ Step 6: Test API Calls**
### **1️⃣ Open Browser & Test Frontend**
1. Visit the **Minikube URL** (`http://192.168.49.2:30000`).
2. **Enter a name** in the input field.
3. **Click "Greet Me"**.
4. ✅ **Expected:** **Greeting response should appear.**

### **2️⃣ Test Backend via Caddy**
Run:
```sh
curl "http://192.168.49.2:30000/greet?name=<yourname>"
```
✅ Expected Output:
```
Hello, <yourname>!
```
- If this **fails**, check **Caddy logs**:
  ```sh
  kubectl logs -l app=caddy
  ```

---

To **delete all existing Kubernetes resources (deployments, pods, and services)** so you can recreate everything cleanly, follow these steps:

## **✅ Step 7: If Any trouble, Delete All Deployments, Pods, and Services**
it is in local so it will not cause any harm deleting the pods, services. Run the following command to remove all related resources:

```sh
kubectl delete deployment backend frontend caddy
kubectl delete service backend-service frontend-service caddy-service
kubectl delete pod --all
kubectl delete configmap caddy-config
```

🚨 **Why?**
- This **removes existing deployments** so they don’t try to pull broken images.
- **Deletes all running pods** (including those in `ImagePullBackOff` or `ErrImagePull`).
- **Removes `caddy-config` ConfigMap** to ensure fresh deployment.

---

## **✅ Step 8: Ensure No Leftover Resources**
Run:
```sh
kubectl get pods
kubectl get services
```
✅ Expected Output:
```
No resources found in default namespace.
```

If any resources **are still present**, delete them manually:
```sh
kubectl delete pod <POD_NAME>
kubectl delete deployment <DEPLOYMENT_NAME>
kubectl delete service <SERVICE_NAME>
```

---

## **✅ Step 9: Build & Push Fresh Images**
Since **Docker Compose works fine**, you need to **rebuild and push images** for Kubernetes.

### **1️⃣ Use Minikube's Local Docker (Alternative)**
If you want Minikube to **use locally built images**, run:
```sh
eval $(minikube docker-env)
```
Then **rebuild the images inside Minikube**:
```sh
docker build -t your-backend-image:latest backend/
docker build -t your-frontend-image:latest frontend/
```
Kubernetes will now **use these local images** instead of pulling from a registry.

### **2️⃣ Push Images to a Registry (You must login into docker desktop)**
If Kubernetes needs to pull images from a registry, push them:
```sh
docker tag your-backend-image:latest your-dockerhub-username/backend:latest
docker tag your-frontend-image:latest your-dockerhub-username/frontend:latest

docker push your-dockerhub-username/backend:latest
docker push your-dockerhub-username/frontend:latest
```
Then, **update `k8s/backend-deploy.yaml` & `frontend-deploy.yaml`** with:
```yaml
image: your-dockerhub-username/backend:latest
```
```yaml
image: your-dockerhub-username/frontend:latest
```

---

## **✅ Step 10: Reapply Kubernetes Manifests**
```sh
kubectl apply -f k8s/backend-deploy.yaml
kubectl apply -f k8s/frontend-deploy.yaml
kubectl apply -f k8s/caddy-deploy.yaml
```

Then check:
```sh
kubectl get pods
kubectl get services
```
🚀 **Everything should now be clean and working!** Let me know if any issues remain! 🚀

---

## **✅ Step 11: Debugging If Something Fails**
### **1️⃣ Check Caddy Can Reach Backend**
Enter the **Caddy pod** and test connectivity:
```sh
kubectl exec -it $(kubectl get pods -l app=caddy -o jsonpath="{.items[0].metadata.name}") -- sh
curl -I http://backend-service:8080/greet?name=<yourname>
curl -I http://frontend-service:80
exit
```
✅ Expected:
```
HTTP/1.1 200 OK
Content-Type: text/plain
```
- If `curl` **hangs or fails**, backend **might not be reachable from Caddy**.

### **2️⃣ Check Backend Logs**
```sh
kubectl logs -l app=backend
```
Look for errors like:
```
404 Not Found: /
Received request: GET /greet
Response: Hello, <yourname>!
```
- If you **see no logs**, then **Caddy is not sending requests correctly**.

### **3️⃣ Describe Services**
```sh
kubectl describe service caddy-service
kubectl describe service backend-service
kubectl describe service frontend-service
```
- Look for **incorrect ports, missing endpoints, or errors**.

---

## **🎯 Summary**
✅ **Checked if pods and services are running (`kubectl get pods && kubectl get services`).**
✅ **Exposed Minikube’s LoadBalancer (`minikube service caddy-service --url`).**
✅ **Opened browser (`http://192.168.49.2:30000`) and tested frontend.**
✅ **Tested backend via Caddy (`curl http://192.168.49.2:30000/greet?name=<yourname>`).**
✅ **Debugged using logs (`kubectl logs -l app=backend && kubectl logs -l app=caddy`).**
