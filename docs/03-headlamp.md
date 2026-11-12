# Step 3: Headlamp Installation

## Installation
- Helm chart: headlamp/headlamp
- Namespace: headlamp
- Service: NodePort 30002
- Values: manifests/headlamp/values.yaml

## Verification
- `kubectl get pods -n headlamp`: Running
- `kubectl get svc -n headlamp`: NodePort 80:30002/TCP
- Screenshot: screenshots/headlamp-dashboard.png

## Purpose
Modern Kubernetes UI for cluster management and visualization.
Used to verify namespaces, workloads, and Kubescape CRDs (VulnerabilityManifestSummary).
