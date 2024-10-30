#!/usr/bin/env python3
"""  class FIFOCache that inherits from BaseCaching and is a caching system """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ ... """

    def __init__(self):
        super().__init__()


    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_data = next(iter(self.cache_data))
            print(f"DISCARD: {discard_data}")
            del self.cache_data[discard_data]

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
