# Step 8: Embedded Security (Python App)

## Context
Simulates an embedded/edge Python application to demonstrate SBOM generation and vulnerability scanning outside Kubernetes.

## Application
- `embedded-app/app.py` imports `requests==2.28.0` and `PyYAML==6.0.1`.
- Dependencies installed in a virtualenv.
- `requests==2.28.0` pulls `urllib3==1.26.20` (known vulnerabilities).

## SBOM Generation
- `syft dir:embedded-app -o cyclonedx-json > screenshots/embedded-python-sbom.json`
- Format: CycloneDX JSON

## SBOM Scanning
- `grype sbom:screenshots/embedded-python-sbom.json`
- Output: screenshots/embedded-python-grype-report.txt

## Findings
- Total vulnerabilities: **21**
  - CRITICAL: 0
  - HIGH: 6
  - MEDIUM: 14
  - LOW: 1
  - NEGLIGIBLE: 0
- **By status**: 21 fixed, 0 not-fixed, 0 ignored
- **Notable CVEs** (all in `urllib3==1.26.20`):
  - GHSA-38jv-5279-wg99 (High, CVSS 2.3)
  - GHSA-2xpw-w6gg-jr37 (High, CVSS 0.6)
  - GHSA-gm62-xv2j-4w53 (High, CVSS 0.6)
  - GHSA-vxq7-64xx-v4gw (High, CVSS 0.3)
  - GHSA-qccp-gfcp-xxvc (High, CVSS 0.2)
  - GHSA-8988-9cw3-xx77 (High, CVSS 0.2)

## Mitigation
- Upgrade `requests` to a version that pulls `urllib3>=2.6.3` (which fixes all 6 High CVEs).
- Rebuild SBOM and re-scan.

## Next
Automate this scan in GitHub Actions (CI/CD).
