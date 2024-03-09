from flask import Flask , request

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

@app.get("/version")
def version():
    version = {"name": "mouse", "version": "2", "build": 123456}
    return json.dumps(version)

product = []

@app.get("/api/products")
def get_products():

    return json.dumps(product)

@app.post("/api/products")
def save_products():
    product = request.get_json()
    print(product)

    product.append(product)
    return json.dumps(product)




