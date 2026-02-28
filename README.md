# Cloud-Native DevOps Platform (DevOps Showcase)

Ovaj repo je portfolio projekat koji pokazuje kompletan DevOps/GitOps tok:
- aplikacija (FastAPI)
- Docker build
- CI (test + build + push)
- K8s deployment sa Kustomize (base + overlays dev/prod)
- CD/GitOps preko Argo CD
- Observability (Prometheus/Grafana + logging stack)
- Security (NetworkPolicy, LimitRange, ResourceQuota)

## Preduvjeti
- Docker
- Kubernetes cluster (k3d/kind/minikube ili cloud)
- kubectl
- kustomize (ili kubectl -k)
- (opcionalno) helm
- (opcionalno) Argo CD

## Brzi start (lokalno)
### 1) Pokreni app lokalno
```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000