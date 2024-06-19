#!/usr/bin/env python3
from pymongo.cursor import CursorType

def list_all(mongo_collection: pymongo.collection.Collection) -> list:
    """
    Lists all docs in a PyMongo collection.

    Args:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
    list: A list of all docs in the collection. Returns an empty list if no docs are found.
    """
    docs = []
    cursor = mongo_collection.find(filter=None, projection=None, cursor_type=CursorType.EXHAUST)
    for doc in cursor:
        docs.append(doc)
    return docs

