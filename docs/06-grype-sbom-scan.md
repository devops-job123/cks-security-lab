# Step 6: SBOM Scanning with Grype

## Installation
- Grype installed via snap (`sudo snap install grype --classic`)
- `grype version`: [Application:         grype
Version:             0.121.3
BuildDate:           2026-11-09T15:11:52Z
GitCommit:           cd1f23eb50dfb52647090158f453c7359172591f
GitDescription:      v0.121.3
Platform:            linux/amd64
GoVersion:           go1.27.3
Compiler:            gc
Syft Version:        v1.57.1
Supported DB Schema: 6]

## SBOM Scan
- `grype sbom:screenshots/nginx-sbom.json`
- Output: screenshots/grype-sbom-report.txt

## Comparison with Trivy
- Trivy scanned the image directly (`trivy image nginx:1.25`): 921 vulnerabilities
- Grype scanned the SBOM (`grype sbom:nginx-sbom.json`)
- Differences may arise from DB versions, matching logic, and severity assignment.
