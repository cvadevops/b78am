from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS CodePipeline Demo</h1>
    <h2>Application Successfully Deployed!</h2>
    <p>Welcome to AWS Elastic Beanstalk.</p>
    """

@app.route("/health")
def health():
    return "Healthy", 200

@app.route("/about")
def about():
    return {
        "Application": "AWS CI/CD Demo",
        "Version": "1.0",
        "Status": "Running"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)