# Step 4: SBOM and Vulnerability/License Scanning with Trivy

## Installation
- Trivy CLI installed via apt repository
- `trivy --version`: [Version: 0.71.2
Vulnerability DB:
  Version: 2]

## SBOM Generation
- `trivy image --format cyclonedx --output screenshots/nginx-sbom.json nginx:1.25`
- Output: screenshots/nginx-sbom.json (CycloneDX format)

## Vulnerability Scanning
- `trivy image nginx:1.25`
- Output: [nginx:1.25 (debian 12.5)
========================
Total: 921 (UNKNOWN: 64, LOW: 265, MEDIUM: 334, HIGH: 237, CRITICAL: 21)]

## License Scanning
- `trivy image --scanners license nginx:1.25`
- Output: [OS Packages (license)
=====================
Total: 828 (UNKNOWN: 243, LOW: 205, MEDIUM: 2, HIGH: 378, CRITICAL: 0)]

