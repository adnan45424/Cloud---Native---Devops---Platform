# Runbook

## Deploy (dev)
- kubectl apply -k security/policies
- kubectl apply -k k8s/overlays/dev

## Health check
- kubectl port-forward -n platform svc/platform-api 8000:80
- curl http://localhost:8000/health

## Troubleshooting
- kubectl get pods -n platform
- kubectl describe pod -n platform <pod>
- kubectl logs -n platform deploy/platform-api