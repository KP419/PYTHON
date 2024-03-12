from flask import Flask , request

import json
from config import db

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

def fix_id(obj):
    obj["_id"]=str(obj["_id"])
    return obj

@app.post("/api/products")
def save_products():
    product = request.get_json()
    
    print(product)

    #product.append(product)
    db.products.insert_one(product)
    
    return json.dumps(fix_id(product))

app.run(debug=True)
