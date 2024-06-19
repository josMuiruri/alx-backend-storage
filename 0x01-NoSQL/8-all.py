#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all docs in a PyMongo collection.

    Args:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
    list: A list of all docs in the collection. Returns an empty list if no docs are found.
    """
    db = client["mydb"]list_all

    dbs  = db["mongo_collection"]

    for doc in dbs.find()
    print(doc)

