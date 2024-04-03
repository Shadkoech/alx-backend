#!/usr/bin/env python3
"""
Module that orchestrates LIFO caching strategy"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching system that inherits from BaseCaching
    It applies the Last-In, First-Out algorithm"""

    def __init__(self):
        """Initializing the LIFO instance"""
        super().__init__()

    def put(self, key, item):
        """Method adding an item to cache dictionary using LIFO replacement
        Args:
            Key: The key to add the item with
            item: The item to add to the cache
        Note:
            If key or item is None, the method will pass
            If items exceed BaseCaching.MAX_ITEMS, the last item
            added to the cache is discarded (LIFO)"""

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # LIFO eviction: Remove the last item added to the cache
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD: {}". format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """Method retrieving an item from cache dictionary
        Args:
            The key of the item to retrieve
        Returns:
            Value associated with provided key or
            None if the key doesn't exist or value is None
        """

        return self.cache_data.get(key)
