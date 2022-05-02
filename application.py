import pymongo
from flask import Flask
from pymongo import database, MongoClient, collection

client: database.Database = MongoClient("localhost", 27017)["ShareNakov"]
test_collection: collection.Collection = client.test
products_collection: collection.Collection = client.products
test_collection.create_index([("loc", pymongo.GEOSPHERE)], name="user_location_index", unique=False)
products_collection.create_index([("loc", pymongo.GEOSPHERE)], name="product_location_index", unique=False)

app = Flask(__name__)
