# Step 4: SBOM and Vulnerability/License Scanning with Trivy

## Installation
- Trivy CLI installed via apt repository
- `trivy --version`: Version: 0.71.2

## SBOM Generation
- `trivy image --format cyclonedx --output screenshots/nginx-sbom.json nginx:1.25`
- Output: screenshots/nginx-sbom.json (CycloneDX format)

## Vulnerability Scanning
- `trivy image --scanners vuln nginx:1.25`
- Target: `nginx:1.25 (debian 12.5)`
- Total: **921 vulnerabilities**
- Breakdown (from full report): 
  - CRITICAL: 21
  - HIGH: 237
  - MEDIUM: 334
  - LOW: 265
  - UNKNOWN: 64
- Note: These are OS-level package vulnerabilities (144 packages) from the Debian base image. The high count is expected for base images; mitigation involves using distroless or regularly rebuilt images.

## License Scanning
- `trivy image --scanners license nginx:1.25`
- Total: 828 license findings
- Breakdown: CRITICAL: 0, HIGH: 378, MEDIUM: 2, LOW: 205, UNKNOWN: 243
