from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Secure DevSecOps API is running!"


@app.route("/api/health")
def health():
    return {
        "status": "healthy",
        "service": "secure-devsecops-api"
    }


@app.route("/api/status")
def status():
    return {
        "service": "secure-devsecops-api",
        "status": "running",
        "environment": "production"
    }

if __name__ == "__main__":
    # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(host="0.0.0.0", port=5000)