# Scilab on Cloud – Containerized Deployment on Minikube

This repository documents the steps I followed to containerize and run the [Scilab on Cloud](https://github.com/prashantsinalkar/scilab-on-cloud) project using Minikube and Podman.

---

## 🔧 Changes Made

I forked the original [scilab-on-cloud](https://github.com/prashantsinalkar/scilab-on-cloud) project and made changes to:

- Ensure compatibility with Python 3.9.21
- Make the application Docker-ready

You can see the changes here:  
👉 [Compare maxprocess...RaghavJit:maxprocess](https://github.com/prashantsinalkar/scilab-on-cloud/compare/maxprocess...RaghavJit:scilab-on-cloud:maxprocess)

---

## 🐳 Dockerization

I created a `Dockerfile` using `python:3.9.21-slim` as the base image.

### Build the Image

```bash
podman build -t scilab-app .
```

### Export the Image as a TAR

```bash
podman save -o scilab-app.tar scilab-app
```

---

## Minikube Setup (Using Podman)

> ⚠️ Podman support is still experimental. I recommend using Docker or a VM-based driver if you face issues.

### Set Minikube to Rootless Mode

```bash
minikube config set rootless true
```

### Start Minikube with Podman and containerd

```bash
minikube start --driver=podman --container-runtime=containerd
```

---

## Load Docker Image into Minikube

```bash
minikube image load scilab-app.tar
```

---

## Kubernetes Deployment

Apply your deployment configuration:

```bash
kubectl apply -f scilab-deploy.yaml
```

---

## Access the Web Interface

To view the application in your browser:

```bash
minikube dashboard
```

Or get the external URL:

```bash
minikube service scilab-app --url
```

---

## 🛑 `.dockerignore`

Make sure your `.dockerignore` includes the following to keep your image clean:

```
scilab-on-cloud/
scilab-app.tar
```

---

## ✅ Summary of Commands

```bash
podman build -t scilab-app .
podman save -o scilab-app.tar scilab-app
minikube config set rootless true
minikube start --driver=podman --container-runtime=containerd
minikube image load scilab-app.tar
kubectl apply -f scilab-deploy.yaml
minikube dashboard
```

---

Let me know if you want to include a sample `scilab-deploy.yaml` file or add screenshots.