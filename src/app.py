from flask import Flask

# Flask app initialization
app = Flask(__name__)

# Flask app logic
@app.route("/")
def hello_world():
    return "Hello, World!"