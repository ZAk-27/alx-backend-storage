#!/usr/bin/env python3
"""
 documntation task8
"""


def list_all(mongo_collection):
    """
    list all documents
    """
    return list(mongo_collection.find())
