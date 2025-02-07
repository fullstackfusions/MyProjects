**For learning Kubernetes I am referring to the following Sources**:

YouTube Videos:
- [Kubernetes In One Shot by TrainWithShubham](https://youtu.be/W04brGNgxN4?si=QHS3GvB6dDPBbz29)

##

## Minikube vs. Prod
Minikube is a great tool for learning Kubernetes, but it’s not a production-scale Kubernetes cluster. The primary difference is that Minikube runs a single-node cluster, whereas production clusters are multi-node distributed systems.

## Distributed Systems Are Complex
Whenever you’re dealing with a system that involves multiple machines talking to each other over a network, you’re dealing with a distributed system. Distributed systems are inherently complex, and Kubernetes is no exception, but that complexity is generally abstracted away from you as a K8s user. That’s what makes Kubernetes so cool! It does a lot of the hard work for you.

**Resources and Nodes**
To zoom way out, Kubernetes’ job is to run software applications, and applications require resources. Resources are things like:

- CPU
- Memory
- Disk space

Kubernetes’ job is to manage those resources and allocate them to the applications that are running on it. Let’s look at an oversimplified example:

3 Nodes (Machines)
Node	RAM
Node 1	16GB
Node 2	8GB
Node 3	8GB

5 Pods (Applications)
App	Required RAM
App 1	12GB
App 2	2GB
App 3	5GB
App 4	4GB
App 5	4GB

Kubernetes looks at the resources required by each application and decides which node to run it on. In this case, it might do something like this:

Node	Apps	RAM Left Over
Node 1	App 1 (12GB), App 2 (2GB)	2GB
Node 2	App 4 (4GB), App 5 (4GB)	0GB
Node 3	App 3 (5GB)	3GB

What happens if we get a new application that requires 10GB of RAM? The cluster doesn’t have enough resources to run it! The solution? Easy. Just add another node to the cluster and let Kubernetes figure out where to run it.

This Won’t Work With Minikube
With Minikube, you only get one node! So once your machine runs out of resources, you’re out of luck. That’s why Minikube is great for learning, but not for production.

Kubernetes clusters are running in production that have thousands of nodes. That’s a lot of resources to manage! But that’s the beauty of Kubernetes.
