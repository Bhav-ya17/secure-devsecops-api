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


if __name__ == "__main__":
    app.run()