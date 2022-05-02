from flask import *
import user

from application import products_collection, app, test_collection
from helper import returns_json


@app.post('/login')
def login():
    name = request.form.get('name')
    password = request.form.get('password')
    print(name)
    print(password)
    m = list(products_collection.find({'name': name, 'password': password}))
    if len(m)>0:
        return True
    if len(m)<0:
        return False
    return m


@app.post('/signUp')
@returns_json
def signUp():
    name = request.form.get('name')
    password = request.form.get('password')
    print(name)
    print(password)
    post = user.new_user(name, password)
    print(post)
    post["_id"] = str(post['_id'])
    test_collection.insert_one(post)
    return post


@app.post('/product')
@returns_json
def add_product_to_db():
    radius = request.form.get('radius')
    product = request.form.get('product')
    description = request.form.get('description')
    latitude = request.form.get('latitude')
    longtitude = request.form.get('longtitude')
    print(radius)
    print(product)
    print(description)
    post = user.get_a_product(radius, product, description, float(latitude), float(longtitude))
    print(post)
    post["_id"] = str(post['_id'])
    products_collection.insert_one(post)
    return post


@app.get('/product')
@returns_json
def get_product_from_db():
    loc = [31.88, 34.88]
    radius = 150000
    m = list(products_collection.find({"loc": {
        "$nearSphere": {
            "$geometry": {
                "type": "point",
                "coordinates": loc
            },
            "$maxDistance": radius + 1000
        }

    }
    }))
    print(m)
    return m
