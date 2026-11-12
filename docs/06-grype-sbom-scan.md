# Step 6: SBOM Scanning with Grype

## Installation
- Grype installed via snap (`sudo snap install grype --classic`)
- `grype version`:
  - Application: grype
  - Version: 0.121.3
  - Syft Version: v1.57.1
  - Supported DB Schema: 6

## SBOM Scan
- `grype sbom:screenshots/nginx-sbom.json`
- Output: screenshots/grype-sbom-report.txt
- **Total vulnerabilities: 177**
  - CRITICAL: 22
  - HIGH: 62
  - MEDIUM: 51
  - LOW: 12
  - NEGLIGIBLE: 25
  - UNKNOWN: 5
- **By status**: 90 fixed, 87 not-fixed, 0 ignored

## Comparison with Trivy
| Tool | Method | Total Vulnerabilities |
|------|--------|----------------------|
| Trivy | Image scan (`trivy image nginx:1.25`) | 921 |
| Grype | SBOM scan (`grype sbom:nginx-sbom.json`) | 177 |

**Why the difference?**
- **Trivy** scans the full image filesystem and reports all known CVEs, including those with no fix (won't fix) and negligible severity.
- **Grype** applies stricter default filtering (e.g., ignores "won't fix" by default in some configurations), and its DB matching logic differs.
- **This is expected and demonstrates tool comparison knowledge** — a key skill for supply chain security.

## Key Findings
- nginx:1.25 (Debian 12.5) has significant OS-level vulnerabilities (22 CRITICAL, 62 HIGH).
- 90 vulnerabilities have fixes available; 87 do not.
- SBOM scanning confirms the image is not production-ready without mitigation (e.g., distroless base, regular rebuilds).
