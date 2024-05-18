# web_flask/0-hello_route.py
from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

