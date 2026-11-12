# CKS Security Lab 2026

Advanced Kubernetes security lab aligned with CKS, focused on **supply chain security**, **vulnerability management**, and **cluster security**.

## Features

### Supply Chain Security
- **SBOM Generation**: CycloneDX via Trivy
- **SBOM Signing**: Cosign (Sigstore bundle) — Verified OK
- **SBOM Scanning**: Grype (177 vulns) vs Trivy (921 vulns) — demonstrates tool comparison

### Vulnerability & License Scanning
- **Trivy**: 921 OS vulnerabilities (21 CRITICAL, 237 HIGH) + 828 license findings
- **Grype**: 177 vulnerabilities (22 CRITICAL, 62 HIGH) from SBOM

### Cluster Security
- **Kubescape Operator**: Config + vuln + runtime scanning
- **KubeView**: Visual cluster map
- **Headlamp**: Kubernetes UI with Kubescape CRDs

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

## Key Findings
- nginx:1.25 (Debian 12.5): 921 vulns (Trivy) / 177 vulns (Grype). 22 CRITICAL, 90 fixed.
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

## Next Steps
- Embedded systems security (binary SBOM, cross-compilation)
- Network Policies / Pod Security Standards
- CI/CD integration
