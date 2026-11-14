# CKS Security Lab 2026

Advanced Kubernetes security lab aligned with CKS, focused on **supply chain security**, **vulnerability management**, and **cluster security**.

## Features

### Supply Chain Security
- **SBOM Generation**: CycloneDX via Trivy and Syft
- **SBOM Signing**: Cosign (Sigstore bundle) — Verified OK
- **SBOM Scanning**: Grype (177 vulns for nginx, 21 vulns for Python app)

### Vulnerability & License Scanning
- **Trivy**: 921 OS vulnerabilities (21 CRITICAL, 237 HIGH) + 828 license findings
- **Grype**: Cross-verification of SBOM findings (image and embedded app)
- **Embedded Security**: Python app SBOM + scan (21 vulns, 6 HIGH)

### Cluster Security
- **Kubescape Operator**: Config + vuln + runtime scanning
- **KubeView**: Visual cluster map
- **Headlamp**: Kubernetes UI with Kubescape CRDs
- **Network Policies**: Default deny + allow DNS/HTTP
- **Pod Security Standards**: Restricted profile enforced

### CI/CD
- **GitHub Actions**: Automated SBOM generation and Grype scanning on push

## Environment
- Kubernetes v1.33.13 (self-managed, AWS EC2)
- 1 control-plane (2 vCPU / 7.6 GiB / 96 GB disk)
- Helm v3.22.1

## Components
| Component | Version | Purpose |
|-----------|---------|---------|
| Kubescape Operator | v1.42.0 | Config/vuln/runtime scanning |
| KubeView | v2.2.1 | Visual cluster map |
| Headlamp | v0.46.0 | Kubernetes UI |
| Trivy | v0.71.2 | SBOM + vuln + license scanning |
| Cosign | v3.x | SBOM signing |
| Grype | v0.121.3 | SBOM scanning |
| Syft | v1.56.0 | SBOM generation |

## Key Findings
- nginx:1.25 (Debian 12.5): 921 vulns (Trivy) / 177 vulns (Grype).
- Python embedded app (`requests==2.28.0`, `PyYAML==6.0.1`): 21 vulns (6 HIGH in urllib3).
- License scan: 828 findings (378 HIGH), mostly Debian base.
- SBOM signed & verified with Cosign.
- Difference between Trivy/Grype demonstrates understanding of tool scopes.

## Steps
1. [Environment Setup](docs/01-environment-setup.md)
2. [KubeView](docs/02-kubeview.md)
3. [Headlamp](docs/03-headlamp.md)
4. [SBOM & Trivy](docs/04-sbom-trivy.md)
5. [Cosign Signing](docs/05-cosign-signing.md)
6. [Grype SBOM Scan](docs/06-grype-sbom-scan.md)
7. [Embedded Security (Python)](docs/07-embedded-security.md)
8. [CI/CD Integration](docs/08-cicd-github-actions.md)
9. [Network Policies & Pod Security](docs/09-network-policies-and-pod-security.md)

## Next Steps
- Add screenshots for GitHub Actions success and NetworkPolicy tests.
- Extend to multi-node cluster with worker nodes.
