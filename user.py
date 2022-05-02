from bson import ObjectId


def new_user(name, password, ):
    port = {"_id": ObjectId(), "name": name, "password": password}
    return port


def get_a_product(r, p, d, longtitude, latitude):
    port = {"_id": ObjectId(), "radius": r, "product": p, "description": d, "loc": {"type": "Point", "coordinates": [latitude, longtitude]}}
    return port