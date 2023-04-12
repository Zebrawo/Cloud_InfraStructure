# K8s deployment

This repository contains the kubernetes deployment file for a DNS applications that consists of three containers: **'webgui-dns'**, **'dns-rest-api'** and **'mongodb'**.

## Prerequisities

Before you begin, make sure you have:

- A K8s cluster with **'kubectl'** configured to communicate with the cluster.
- Docker images for each of the three containers:
  -**'webgui-dns'**
  -**'dns-rest-api'**
  -**'mongodb'**
  
# Deployment

Deploy the application to your kubernetes cluster:
```bash
kubectl apply -f <yaml file>
```

# Usage

Once the deployment is complete, you can access the DNS application through the webgui-dns container at "http://Pod_IP_address:5000"

# Cleaning up

To delete the deployment and all associated resources, run:
```bash
kubectl delete deployment <Deployment name>
```
If you don't know the deployment name, check your own deployment yaml file.

# Troubleshooting
If you experience any issues with the deployment, you can check the status of the pods and containers using the following commands:
```bash
kubectl get pods
kubectl logs <pod name> -c <container name>
```
Additionally, you can check the kubernetes event logs for the deployment using:
```bash
kubectl describe deployment <pod name>
```
