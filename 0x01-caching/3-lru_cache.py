#!/usr/bin/python3
"""
LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
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
        if self.MAX_ITEMS == len(cache):
            if key in cache:
                first_key = key
            else:
                first_key = list(cache)[0]
                print('DISCARD: {}'.format(first_key))
            cache.pop(first_key)
        cache[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.put(key, self.cache_data[key])
            return self.cache_data[key]
