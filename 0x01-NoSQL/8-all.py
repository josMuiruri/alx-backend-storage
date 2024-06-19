#!/usr/bin/env python3
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    """
    Lists all docs in a PyMongo collection.

    Args:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
    list: A list of all docs in the collection. Returns an empty list if no docs are found.
    """
db = myclient["mydb"]
dbs = db["mongo_collection"]

for doc in dbs.find():
    print(doc)

