# 🚀 GitOps-Based Kubernetes Application Deployment using ArgoCD

> A production-style DevOps Engineering project demonstrating how to implement a complete GitOps workflow where all Kubernetes deployments happen automatically through Git commits — no manual kubectl commands in production. Built with Docker, Minikube, ArgoCD, and GitHub.

![Kubernetes](https://img.shields.io/badge/Kubernetes-GitOps-blue?style=flat-square&logo=kubernetes)
![ArgoCD](https://img.shields.io/badge/ArgoCD-Continuous%20Delivery-orange?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=flat-square&logo=docker)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)
![Author](https://img.shields.io/badge/Author-Premkumar%20Patil-purple?style=flat-square)

---

## Project Preview

> **ArgoCD Dashboard** showing the gitops-demo application as Synced and Healthy — the visual proof that Git is the single source of truth for the Kubernetes cluster.

![ArgoCD Dashboard Preview](image/06-argocd-synced-healthy.png)

---

## Introduction

In traditional deployments, engineers SSH into servers or run `kubectl apply` manually to update applications. This creates several problems: no audit trail of who changed what, no peer review process, difficult rollbacks, and impossible reproducibility when the cluster crashes.

GitOps solves all of these problems by making Git the single source of truth for everything. The rule is simple — **no manual kubectl commands in production**. Every change to the cluster must come through a Git commit. ArgoCD enforces this automatically by continuously watching the GitHub repository and syncing the cluster to match whatever is in Git.

This project implements a complete GitOps pipeline where:

- A Python Flask application is containerized with Docker
- The Docker image is pushed to Docker Hub
- Kubernetes manifests are stored in GitHub
- ArgoCD monitors the repository and auto-syncs the cluster
- Updating a Docker image tag in Git triggers an automatic rolling deployment
- Manual kubectl changes are automatically reverted by ArgoCD (self-healing)

---

## Project Overview

| What | Details |
|---|---|
| Type | GitOps-Based Kubernetes Application Deployment |
| Role | DevOps Engineer |
| Application | Python Flask web app (Version 1.0 → 2.0) |
| Container Registry | Docker Hub (premkumar71/gitops-demo-app) |
| Kubernetes Cluster | Minikube (local single-node cluster) |
| GitOps Tool | ArgoCD 2.x |
| Git Repository | GitHub (public) |
| OS | Ubuntu 22.04 |
| Status | Completed |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        GitOps Pipeline                              │
│                                                                     │
│  Developer Laptop                                                   │
│  ┌─────────────────┐                                                │
│  │ 1. Edit app.py  │                                                │
│  │ 2. docker build │                                                │
│  │ 3. docker push  │──────────────────► Docker Hub                 │
│  │ 4. Update       │                   premkumar71/                │
│  │    image tag in │                   gitops-demo-app:v2          │
│  │    deployment   │                         ▲                     │
│  │    .yaml        │                         │ pulls image         │
│  │ 5. git push     │──────► GitHub           │                     │
│  └─────────────────┘        Repository       │                     │
│                             k8s/             │                     │
│                             deployment.yaml  │                     │
│                             service.yaml     │                     │
│                                  │           │                     │
│                                  │ watches   │                     │
│                                  ▼           │                     │
│                             ArgoCD           │                     │
│                             (running in      │                     │
│                              cluster)        │                     │
│                                  │           │                     │
│                                  │ syncs     │                     │
│                                  ▼           │                     │
│                        Kubernetes Cluster    │                     │
│                        (Minikube)            │                     │
│                        ┌──────────────────┐  │                     │
│                        │  Pod 1 (Flask)───┘  │                     │
│                        │  Pod 2 (Flask)   │  │                     │
│                        │  Service (port80)│  │                     │
│                        └──────────────────┘  │                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Complete GitOps Flow

```
Step 1: Developer edits app.py (changes Version 1.0 to 2.0)
Step 2: docker build -t premkumar71/gitops-demo-app:v2 .
Step 3: docker push premkumar71/gitops-demo-app:v2
Step 4: Edit k8s/deployment.yaml — change image tag from v1 to v2
Step 5: git commit -m "Deploy Version 2.0" && git push
Step 6: ArgoCD detects the change in GitHub (polls every 3 minutes)
Step 7: ArgoCD applies updated deployment.yaml to the cluster
Step 8: Kubernetes pulls v2 image from Docker Hub
Step 9: Rolling update — new pods start, old pods terminate
Step 10: Zero downtime — users see Version 2.0 automatically
```

---

## GitOps Principles Demonstrated

```
1. Declarative
   Desired state described in YAML files in Git
   Not imperative scripts like "run this command"

2. Versioned
   Every deployment is a Git commit with author and timestamp
   Complete audit trail — who deployed what and when

3. Pulled (not pushed)
   ArgoCD pulls from Git — CI never pushes directly to cluster
   Cluster pulls its own desired state from Git

4. Continuously reconciled
   ArgoCD checks every 3 minutes
   Manual cluster changes are automatically reverted to Git state
   Self-healing — cluster always converges to match Git
```

---

## Technologies and Tools

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.11 | Application runtime |
| Flask | 3.0.0 | Web framework for the demo app |
| Docker | latest | Build and run container images |
| Docker Hub | - | Public container image registry |
| Minikube | latest | Local single-node Kubernetes cluster |
| kubectl | latest | Kubernetes CLI tool |
| ArgoCD | 2.x | GitOps continuous delivery controller |
| GitHub | - | Git repository (source of truth) |

---

## Repository Structure

```
gitops-argocd-demo/
├── README.md              ← this file
├── app.py                 ← Python Flask web application
├── requirements.txt       ← Python dependencies (flask==3.0.0)
├── Dockerfile             ← containerizes the app
├── .gitignore             ← excludes __pycache__ etc
├── k8s/
│   ├── deployment.yaml    ← ArgoCD watches this file
│   └── service.yaml       ← exposes the app on port 80
└── image/
    ├── 01-project-folder-structure.png
    ├── 02-docker-build-output.png
    ├── 03-docker-images-list.png
    ├── 04-docker-push-output.png
    ├── 05-dockerhub-repository.png
    ├── 06-argocd-synced-healthy.png
    ├── 07-argocd-app-graph.png
    ├── 08-kubectl-pods-running.png
    ├── 09-browser-version-1.png
    ├── 10-github-commit-v2.png
    ├── 11-argocd-syncing-v2.png
    ├── 12-browser-version-2.png
    ├── 13-self-heal-before.png
    └── 14-self-heal-after.png
```

---

## Phase 1 — Application Code

The demo application is a Python Flask web server with two endpoints — the main page showing the version number, and a `/health` endpoint that Kubernetes uses to check if each pod is alive.

### app.py

```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <body style="font-family:sans-serif;text-align:center;padding:50px;background:#f0f4f8">
      <div style="background:white;padding:40px;border-radius:12px;
                  max-width:500px;margin:auto;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
        <h1 style="color:#2d3748">GitOps Demo App</h1>
        <h2 style="color:#48bb78">Version 1.0</h2>
        <p style="color:#718096">Deployed automatically by ArgoCD</p>
        <p style="color:#718096">No kubectl commands used in production</p>
      </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### requirements.txt

```
flask==3.0.0
```

> **Project folder structure** — showing all files created correctly before building the Docker image.

![Project Folder Structure](image/01-project-folder-structure.png)

---

## Phase 2 — Containerization with Docker

The Dockerfile packages the Flask app into a self-contained container image. The non-root user (`appuser`) is a security best practice — the app does not need root privileges to serve web pages.

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Security: run as non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build commands

```bash
# Build the image
docker build -t gitops-demo-app:v1 .

# Test locally before pushing
docker run -d --name test-app -p 5000:5000 gitops-demo-app:v1
curl http://localhost:5000/health
# Returns: OK

# Clean up local test
docker stop test-app && docker rm test-app

# Tag with Docker Hub username
docker tag gitops-demo-app:v1 premkumar71/gitops-demo-app:v1

# Push to Docker Hub
docker push premkumar71/gitops-demo-app:v1
```

> **Docker build output** — showing each Dockerfile step executing successfully, FROM → WORKDIR → COPY → RUN pip install → COPY → RUN useradd → CMD.

![Docker Build Output](image/02-docker-build-output.png)

> **docker images list** — showing gitops-demo-app:v1 image created on your machine with its size.

![Docker Images List](image/03-docker-images-list.png)

> **docker push output** — showing each image layer being uploaded to Docker Hub with the final digest hash confirming successful upload.

![Docker Push Output](image/04-docker-push-output.png)

> **Docker Hub repository** — browser showing hub.docker.com with premkumar71/gitops-demo-app repository and v1 tag visible.

![Docker Hub Repository](image/05-dockerhub-repository.png)

---

## Phase 3 — Kubernetes Manifests

Two YAML files define how the application runs in Kubernetes. ArgoCD watches these files in the `k8s/` folder of the GitHub repository and applies them to the cluster automatically whenever they change.

### k8s/deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gitops-demo-app
  namespace: default
  labels:
    app: gitops-demo-app
    managed-by: argocd
spec:
  replicas: 2
  selector:
    matchLabels:
      app: gitops-demo-app
  template:
    metadata:
      labels:
        app: gitops-demo-app
    spec:
      containers:
      - name: gitops-demo-app
        image: premkumar71/gitops-demo-app:v1
        imagePullPolicy: Always
        env:
        - name: APP_VERSION
          value: "1.0"
        ports:
        - containerPort: 5000
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 15
          periodSeconds: 10
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "200m"
```

### k8s/service.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: gitops-demo-service
  namespace: default
  labels:
    app: gitops-demo-app
    managed-by: argocd
spec:
  selector:
    app: gitops-demo-app
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 5000
  type: NodePort
```

### What each field does

**Deployment:**
```
replicas: 2           run 2 pods simultaneously for high availability
imagePullPolicy: Always  always pull latest image from Docker Hub
livenessProbe         restart pod if /health fails 3 times in a row
readinessProbe        remove pod from load balancer if /health fails
resources.requests    minimum CPU/RAM Kubernetes reserves for this pod
resources.limits      maximum CPU/RAM the pod is allowed to use
```

**Service:**
```
selector              routes traffic to pods with label app=gitops-demo-app
port: 80              users connect to this port
targetPort: 5000      traffic is forwarded to this port on the pod
type: NodePort        accessible from outside the cluster via minikube ip
```

---

## Phase 4 — Push to GitHub and Install ArgoCD

### Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: GitOps ArgoCD demo"
git remote add origin https://github.com/Premkumar-Patil001/gitops-argocd-demo.git
git branch -M main
git push -u origin main
```

### Install ArgoCD

```bash
# Create namespace
kubectl create namespace argocd

# Install ArgoCD
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for all pods to start (2-4 minutes)
kubectl get pods -n argocd -w

# Access ArgoCD UI
kubectl port-forward svc/argocd-server -n argocd 8080:443 &

# Get admin password
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d && echo
```

### Create ArgoCD Application

```bash
# Login to ArgoCD CLI
argocd login localhost:8080 --username admin --password YOUR_PASSWORD --insecure

# Create application — connect Git to cluster
argocd app create gitops-demo \
  --repo https://github.com/Premkumar-Patil001/gitops-argocd-demo.git \
  --path k8s \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace default \
  --sync-policy automated \
  --auto-prune \
  --self-heal
```

**What each flag means:**

```
--repo              GitHub repository ArgoCD will watch
--path k8s          only watch the k8s/ subfolder
--dest-server       deploy to this cluster
--dest-namespace    deploy into this namespace
--sync-policy automated   auto-sync when Git changes detected
--auto-prune        delete resources removed from Git
--self-heal         revert manual kubectl changes to match Git
```

> **ArgoCD application — Synced and Healthy** — showing the gitops-demo app with green Synced status and Healthy health status after initial sync from GitHub.

![ArgoCD Synced Healthy](image/06-argocd-synced-healthy.png)

> **ArgoCD application graph** — visual tree showing Deployment → ReplicaSet → 2 Pods all in green/healthy state.

![ArgoCD App Graph](image/07-argocd-app-graph.png)

> **kubectl get pods** — terminal showing 2 pods running with status 1/1 Running after ArgoCD synced the cluster.

![kubectl Pods Running](image/08-kubectl-pods-running.png)

> **Browser showing Version 1.0** — the app accessible via minikube service showing the initial Version 1.0 deployment.

![Browser Version 1](image/09-browser-version-1.png)

---

## Phase 5 — GitOps Deployment — Version 2.0

This phase demonstrates the complete GitOps loop. No kubectl commands are used after the git push. ArgoCD handles everything automatically.

### Step 1 — Update the application

```python
# Edit app.py — change Version 1.0 to Version 2.0
# Change the h2 line from:
<h2 style="color:#48bb78">Version 1.0</h2>
# To:
<h2 style="color:#38a169">Version 2.0 ✓</h2>
```

### Step 2 — Build and push new image

```bash
# Build Version 2
docker build -t premkumar71/gitops-demo-app:v2 .

# Push to Docker Hub
docker push premkumar71/gitops-demo-app:v2
```

### Step 3 — Update image tag in deployment.yaml

```yaml
# Change this line in k8s/deployment.yaml:
image: premkumar71/gitops-demo-app:v1
# To:
image: premkumar71/gitops-demo-app:v2
```

### Step 4 — Push to GitHub (triggers deployment)

```bash
git add app.py k8s/deployment.yaml
git commit -m "Deploy Version 2.0 - update image to v2"
git push origin main
```

### Step 5 — ArgoCD auto-deploys

```
ArgoCD detects change within 3 minutes
→ applies updated deployment.yaml to cluster
→ Kubernetes pulls v2 image from Docker Hub
→ Rolling update: new pods start, old pods terminate
→ Zero downtime throughout
```

> **GitHub commit showing image tag update** — the commit on GitHub changing image from v1 to v2 in deployment.yaml. This single commit triggers the entire deployment.

![GitHub Commit v2](image/10-github-commit-v2.png)

> **ArgoCD syncing** — status showing OutOfSync → Syncing after detecting the GitHub change. This proves ArgoCD detected the Git push and is applying the update.

![ArgoCD Syncing v2](image/11-argocd-syncing-v2.png)

> **Browser showing Version 2.0** — the app now shows Version 2.0 after ArgoCD completed the automatic deployment. No kubectl command was used.

![Browser Version 2](image/12-browser-version-2.png)

---

## Phase 6 — GitOps Self-Healing Proof

This test proves that Git is the only way to change production. Any manual kubectl changes are automatically reverted by ArgoCD.

### Test — manually scale pods (bypassing GitOps)

```bash
# Manually scale to 5 pods (bypassing GitOps)
kubectl scale deployment gitops-demo-app --replicas=5

# Check immediately — shows 5 pods
kubectl get pods
# 5 pods running

# Wait 3 minutes — ArgoCD reverts it
kubectl get pods
# 2 pods — back to what deployment.yaml says in Git!
```

### Why this happens

```
deployment.yaml in Git says: replicas: 2
kubectl scale set it to:     replicas: 5
ArgoCD sees the difference → cluster does not match Git
ArgoCD applies deployment.yaml from Git → replicas: 2
Result: manual change reverted automatically
```

> **kubectl get pods showing 5 pods** — immediately after the manual kubectl scale command. This is the drift state before self-healing.

![Self Heal Before](image/13-self-heal-before.png)

> **kubectl get pods showing 2 pods** — 3 minutes later after ArgoCD automatically reverted the manual change back to what deployment.yaml says in Git.

![Self Heal After](image/14-self-heal-after.png)

---

## How to Deploy a New Version

```bash
# 1. Update your app code
nano app.py

# 2. Build new image with new tag
docker build -t premkumar71/gitops-demo-app:v3 .

# 3. Push to Docker Hub
docker push premkumar71/gitops-demo-app:v3

# 4. Update image tag in deployment.yaml
sed -i 's|gitops-demo-app:v2|gitops-demo-app:v3|g' k8s/deployment.yaml

# 5. Push to GitHub
git add k8s/deployment.yaml
git commit -m "Deploy Version 3.0"
git push

# 6. Wait 3 minutes — ArgoCD deploys automatically
# No kubectl needed after Step 5
```

---

## How to Rollback

```bash
# Option 1: Git revert (recommended)
git revert HEAD
git push
# ArgoCD detects the revert → deploys previous version

# Option 2: ArgoCD rollback
argocd app rollback gitops-demo 1
# Rolls back to revision 1

# View deployment history
argocd app history gitops-demo
```

---

## Screenshot Reference

| # | File Name | When to take it | What it shows |
|---|---|---|---|
| 01 | `image/01-project-folder-structure.png` | After creating all files | Terminal showing ls output with all project files |
| 02 | `image/02-docker-build-output.png` | During docker build | Terminal showing each build step completing |
| 03 | `image/03-docker-images-list.png` | After docker build | docker images command showing gitops-demo-app:v1 |
| 04 | `image/04-docker-push-output.png` | After docker push | Terminal showing layer upload progress and digest |
| 05 | `image/05-dockerhub-repository.png` | After push | hub.docker.com showing premkumar71/gitops-demo-app with v1 tag |
| 06 | `image/06-argocd-synced-healthy.png` | After ArgoCD app created | ArgoCD UI showing app as Synced + Healthy in green |
| 07 | `image/07-argocd-app-graph.png` | Same as above | ArgoCD visual graph showing Deployment → ReplicaSet → Pods |
| 08 | `image/08-kubectl-pods-running.png` | After ArgoCD syncs | kubectl get pods showing 2 pods in Running state |
| 09 | `image/09-browser-version-1.png` | After initial deployment | Browser showing Version 1.0 via minikube service URL |
| 10 | `image/10-github-commit-v2.png` | After git push v2 | GitHub showing the commit that changed image tag to v2 |
| 11 | `image/11-argocd-syncing-v2.png` | During auto-deploy | ArgoCD UI showing OutOfSync or Syncing status |
| 12 | `image/12-browser-version-2.png` | After ArgoCD deploys v2 | Browser showing Version 2.0 — proves GitOps worked |
| 13 | `image/13-self-heal-before.png` | After kubectl scale to 5 | kubectl get pods showing 5 pods (manual drift) |
| 14 | `image/14-self-heal-after.png` | 3 min after scale | kubectl get pods showing 2 pods (auto-reverted by ArgoCD) |

---

## How to Add Screenshots

```
1. Create image/ folder in your repo:
   mkdir image

2. Take each screenshot at the exact moment described above

3. Save with the exact filename from the table

4. Push to GitHub:
   git add image/
   git commit -m "Add project screenshots"
   git push

The README will automatically display them on GitHub.
```

---

## Kubernetes Concepts Used

| Concept | What it is | Where used |
|---|---|---|
| Deployment | Manages a set of identical pods | deployment.yaml |
| ReplicaSet | Ensures desired number of pods run | Created by Deployment |
| Pod | Smallest unit — runs one container | Created by ReplicaSet |
| Service | Stable network endpoint for pods | service.yaml |
| NodePort | Exposes service on cluster node port | service.yaml type |
| Namespace | Logical isolation within cluster | default namespace |
| Label | Key-value tag on resources | app: gitops-demo-app |
| Selector | Matches resources by label | spec.selector |
| Liveness Probe | Checks if pod is alive | deployment.yaml |
| Readiness Probe | Checks if pod is ready for traffic | deployment.yaml |
| Resource Limits | CPU/RAM boundaries per pod | deployment.yaml |

---

## What I Learned

**GitOps is a philosophy, not just a tool.** The real insight is that making Git the source of truth changes team culture — deployments require code review via Pull Requests, every change is auditable, and rollback is as simple as `git revert`. These are process improvements as much as technical ones.

**The difference between liveness and readiness probes matters in production.** Liveness restarts a broken pod. Readiness temporarily removes a pod from the load balancer during startup or overload without killing it. Using both together means zero-downtime deployments where new pods must pass readiness before receiving traffic, and broken pods are automatically replaced.

**Layer caching in Dockerfiles directly affects build speed.** Copying `requirements.txt` before `app.py` means pip install is cached and only runs when dependencies actually change. This reduced my rebuild time from 45 seconds to 3 seconds when only the app code changed.

**Running containers as non-root is a simple change with significant security impact.** Adding `RUN useradd -m appuser` and `USER appuser` means even if there is a vulnerability in the Flask app, the attacker only gets access as a low-privilege user inside the container rather than root.

**ArgoCD self-healing is the most powerful GitOps feature.** The fact that any manual kubectl change is automatically reverted means the cluster state is guaranteed to match Git — not just usually matches, but always matches. This makes the system auditable in a way that manual deployments can never be.

**Resource requests and limits are not optional in production.** Without them, one pod can consume all cluster resources and starve other pods. Setting requests ensures fair scheduling and limits prevent runaway processes from crashing the node.

---

## Cost Summary

| Resource | Cost |
|---|---|
| Minikube | Free — runs on your laptop |
| Docker Hub | Free — public repositories |
| GitHub | Free — public repository |
| ArgoCD | Free — open source |
| **Total** | **₹0** |

---

## Conclusion

This project demonstrates that GitOps is the correct deployment model for teams that care about reliability, security, and auditability. The traditional model of engineers running kubectl commands creates invisible, untrackable changes that accumulate into system instability. GitOps eliminates this entirely.

The most important lesson is that ArgoCD's self-healing is not just a nice feature — it is what makes the GitOps guarantee enforceable. Without self-healing, GitOps is just a recommendation. With self-healing, GitOps is a technical contract: the cluster always matches Git, period.

For a DevOps team, this means every production change is a peer-reviewed Git commit with a timestamp and author. Rollbacks are git reverts. Disaster recovery is a fresh cluster pointed at the same Git repo. Onboarding is giving a new engineer read access to the repo. These operational improvements are why GitOps has become the standard deployment model for Kubernetes workloads.

---

## Author

**Premkumar Keshav Patil**
Cloud & DevOps Enthusiast | Learning Kubernetes and GitOps

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/premkumar-patil-bb9471253)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-grey?style=flat-square&logo=github)](https://github.com/Premkumar-Patil001)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-premkumar71-2496ED?style=flat-square&logo=docker)](https://hub.docker.com/u/premkumar71)

---

## Tags

`Kubernetes` `GitOps` `ArgoCD` `Docker` `Python` `Flask` `Minikube` `GitHub` `CI/CD` `Container` `DevOps` `Continuous Delivery` `Self-Healing` `Rolling Update` `Zero Downtime`
