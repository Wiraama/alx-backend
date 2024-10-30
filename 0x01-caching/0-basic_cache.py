#!/usr/bin/env python3
"""
eturn the value in self.cache_data linked to key.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ class to inherit fro, basecaching """

    def put(self, key, item):
        """ ... """
        if key == None or item == None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ ... """
        return self.cache_data.get(key, None)
