#!/usr/bin/python3
"""
LFUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.freq = {}
        self.usage_order = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order[key] = self.usage_order[key] + 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                lfu_keys = [k for k, v in self.freq.items() if v == min_freq]

                if len(lfu_keys) > 1:
                    lru_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                else:
                    lru_key = lfu_keys[0]

                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.freq[lru_key]
                del self.usage_order[lru_key]

            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order[key] = len(self.usage_order) + 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.usage_order[key] = self.usage_order[key] + 1
        return self.cache_data[key]
