#!/usr/bin/env python3
"""
task 10 documntation
"""


def update_topics(mongo_collection, name, topics):
    """
    change all topics
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
