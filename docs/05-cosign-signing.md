# Step 5: SBOM Signing with Cosign

## Installation
- Cosign v3.x installed via GitHub releases
- `cosign version`: [version]

## Key Generation
- `cosign generate-key-pair` in `cosign-keys/`
- Private key: `cosign-keys/cosign.key` (gitignored)
- Public key: `cosign-keys/cosign.pub`

## Signing (bundle format)
- `cosign sign-blob --key cosign-keys/cosign.key --bundle screenshots/nginx-sbom.sigstore.json screenshots/nginx-sbom.json`
- Bundle: `screenshots/nginx-sbom.sigstore.json`

## Verification
- `cosign verify-blob --key cosign-keys/cosign.pub --bundle screenshots/nginx-sbom.sigstore.json screenshots/nginx-sbom.json`
- Result: **Verified OK**
