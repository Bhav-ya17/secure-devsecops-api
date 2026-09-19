# Secure DevSecOps Flask API

[![CI Security Pipeline](https://github.com/Bhav-ya17/secure-devsecops-api/actions/workflows/ci.yml/badge.svg)](https://github.com/Bhav-ya17/secure-devsecops-api/actions/workflows/ci.yml)

A containerized Flask REST API with an automated DevSecOps pipeline using GitHub Actions. The project integrates automated testing and multiple security checks into the software development lifecycle.

## Technologies

* Python / Flask
* pytest
* Git & GitHub
* GitHub Actions
* Semgrep (SAST)
* Gitleaks (secret scanning)
* pip-audit (dependency scanning)
* Docker
* Trivy (container security scanning)

## API Endpoints

| Endpoint      | Method | Description                |
| ------------- | ------ | -------------------------- |
| `/`           | GET    | Basic API response         |
| `/api/health` | GET    | Service health check       |
| `/api/status` | GET    | Service status information |

## DevSecOps Pipeline

Every push to `main` and pull request triggers GitHub Actions:

```text
Code Push
    ↓
Automated Tests
    ↓
Semgrep
    ↓
pip-audit
    ↓
Gitleaks
    ↓
Docker Build
    ↓
Trivy Scan
```

The pipeline uses automated security checks to identify vulnerabilities, insecure code patterns, exposed secrets, and container security issues.

## Run Locally

```bash
git clone https://github.com/Bhav-ya17/secure-devsecops-api.git
cd secure-devsecops-api

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

API:

```text
http://localhost:5000
```

Run tests:

```bash
python -m pytest
```

Run with Docker:

```bash
docker build -t secure-devsecops-api .
docker run -p 5000:5000 secure-devsecops-api
```
