from flask import Flask

import json

app = Flask(__name__)

@app.get("/")
def home():
    # code for home route
    return "hello from flask"

@app.get("/testing")
def test():
    return "hello from another page"

@app.get("/about")
def about():
    me= {"name": "Kory Plotts"}
    return json.dumps(me)

app.run(debug=True)
