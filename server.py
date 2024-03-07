from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # code for home route
    return "Hello, World!"

app.run(debug=True)
