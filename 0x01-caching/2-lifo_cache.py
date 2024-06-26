#!/usr/bin/python3
"""
LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        cache = self.cache_data
        if not key or not item:
            return
        if self.MAX_ITEMS == len(cache) and key not in cache:
            first_key = list(cache)[-1]
            print('DISCARD: {}'.format(first_key))
            cache.pop(first_key)
        cache[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if not key:
            return
        return self.cache_data.get(key, None)
