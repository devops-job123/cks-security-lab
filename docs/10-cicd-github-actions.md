# Step 10: CI/CD Integration (GitHub Actions)

## Workflow
- File: `.github/workflows/security-scan.yml`
- Trigger: push/pull_request to `main`
- Status: **Completed successfully** (1m 4s)

## Steps
1. Checkout code
2. Set up Python 3.12
3. Install Syft and Grype
4. Install Python dependencies (embedded-app)
5. Generate SBOM (`syft dir:embedded-app -o cyclonedx-json`)
6. Scan SBOM with Grype (`grype sbom:...`)
7. Upload artifacts (SBOM + report)

## Verification
- GitHub Actions: "Security Scan" workflow run #1 completed successfully.
- Artifacts: `security-artifacts` (contains SBOM and Grype report).
