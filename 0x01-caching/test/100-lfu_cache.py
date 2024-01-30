#!/usr/bin/env python3
""" LFUCache module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching"""
    def __init__(self):
        """ Initialize LFUCache"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]

                if len(least_frequent_keys) == 1:
                    discarded_key = least_frequent_keys[0]
                else:
                    lru_key = min(self.order, key=lambda k: self.order.index(k))
                    discarded_key = lru_key

                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print("DISCARD: {}".format(discarded_key))

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.order.append(key)

    def get(self, key):
        """ Get an item by key"""
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
