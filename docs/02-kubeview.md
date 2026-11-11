# Step 2: KubeView Installation

## Installation
- Helm chart: kubeview/kubeview
- Namespace: kubeview
- Service: NodePort 30001 (patched from LoadBalancer)
- Values: manifests/kubeview/values.yaml

## Verification
- `kubectl get pods -n kubeview`: Running
- `kubectl get svc -n kubeview`: NodePort 8000:30001/TCP
- Screenshot: screenshots/kubeview-dashboard.png

## Purpose
Visual exploration of Kubernetes resources and their relationships.
Shows Kubescape components (operator, node-agent, storage, kubevuln) and demo workload.
