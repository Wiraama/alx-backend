#!/usr/bin/env python3
"""
eturn the value in self.cache_data linked to key.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class to inherit fro, basecaching """


    def put(self, key, item):
        """ ... """
        if key is not None and item is not None:
            self.cache_data[key] = item


    def get(self, key):
        """ ... """
        return self.cache_data.get(key, None)
