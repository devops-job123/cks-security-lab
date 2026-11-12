# Step 1: Environment Setup (Baseline)

## Cluster Info
- Type: Self-managed Kubernetes on AWS EC2 (not kind)
- Kubernetes: v1.33.13 (client and server)
- Node: ip-172-31-26-113 (control-plane, single node)
- CNI: Calico
- Container runtime: containerd 2.2.2
- OS: Ubuntu 26.04.1 LTS

## Resource Baseline
- vCPU: 2 (1200m requests already allocated = 60%)
- RAM: 7.6 GiB (2142Mi used = 27%, ~6.3 GiB available)
- Disk: 96 GB total, 81 GB free (after EBS expansion 30→100 GB)

## Pre-flight Cleanup
- Helm releases removed: falco, headlamp, kubeview, my
- Namespaces deleted: falco, headlamp, kubeview, app-teame1, autoscale, echo-sound, mariadb-lab, production, secure-app, sp-calculator, web-migration, test, sidecar-lab, restricted, envoy-gateway-system
- RBAC removed: headlamp-admin-binding, sealed-secrets-controller SA/Role/RoleBinding
- StatefulSet removed: webbb (default)
- EBS volume deleted: vol-07d1570f0a9465e45 (2 GiB, Available)

## Constraints & Mitigation
- CPU requests at 60%: limit new components to essential only
- No Falco
- Use syft/trivy/grype
- Scale Headlamp to 0 when idle

## Tools Available
- Helm: v3.22.1
- kubectl: v1.33.13
- Cluster: self-managed Kubernetes v1.33.13 on AWS EC2
