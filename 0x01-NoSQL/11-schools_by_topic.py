#!/usr/bin/env python3
"""
Task 11's module
"""


def schools_by_topic(mongo_collection, topic):
    """
    specific topic
    """
    return mongo_collection.find({"topics": topic})
