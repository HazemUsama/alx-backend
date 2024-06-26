#!/usr/bin/python3
"""
BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = None

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if not key:
            return
        return self.cache_data.get(key, None)
