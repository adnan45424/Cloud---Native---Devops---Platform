# Architecture

## Components
- API: FastAPI (Docker)
- CI: GitHub Actions (tests + build)
- CD: GitHub Actions deploy (kubectl apply -k)
- K8s: Kustomize (base + overlays)
- GitOps: Argo CD (optional)
- Observability: Prometheus/Grafana + logging (planned)
- Security: NetworkPolicy, LimitRange, ResourceQuota + Trivy scan

## Flow
1) Commit -> CI test/build
2) Push to main -> CD deploy dev overlay
3) (optional) ArgoCD sync from repo path (GitOps)