# Step 11: Network Policies & Pod Security

## Network Policies (namespace: demo)
- `default-deny-all`: denies all ingress/egress by default.
- `allow-dns-and-web`: allows DNS (UDP/TCP 53) to kube-system and HTTP/HTTPS (TCP 80/443) to anywhere.
- Verified: DNS resolved, HTTP worked, unauthorized port blocked.

## Pod Security Standards (namespace: restricted-demo)
- Enforced `restricted` profile via namespace labels (enforce, warn, audit).
- Verified: insecure nginx pod rejected (violates runAsNonRoot, allowPrivilegeEscalation, seccomp, capabilities).
- Secure pod (nginx-unprivileged) accepted.

## Commands
- `kubectl apply -f manifests/network-policies/`
- `kubectl apply -f manifests/pod-security/restricted-ns.yaml`
