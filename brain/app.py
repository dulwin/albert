import logging
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is an endpoint"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
