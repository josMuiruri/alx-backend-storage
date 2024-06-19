#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all docs in a MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object

    Returns:
    list: A list of all docs in the collection. Returns an empty list if no docs are found.
    """
    if mongo_collection is None:
        return []

    docs = list(mongo_collection.find())

    return docs
