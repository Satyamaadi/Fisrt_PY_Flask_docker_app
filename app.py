from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World from Python in Docker</h1>"

if __name__ == "main":
    app.run(debug=True)