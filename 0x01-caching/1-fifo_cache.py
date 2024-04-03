#!/usr/bin/env python3
"""
Module that orchestrates FIFO caching strategy"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Caching system that inherits from BaseCaching
    It applies the First-In, First-Out algorith"""

    def __init__(self):
        """Initializing the FIFO instance"""
        super().__init__()

    def put(self, key, item):
        """Method adding an item to cache dictionary using FIFO replacement
        Args:
            Key: The key to add the item with
            item: The item to add to the cache
        Note:
            If key or item is None, the method will pass
            If items exceed BaseCaching.MAX_ITEMS, the first item
            added to the cache is discarded FIFO"""

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # FIFO eviction: Remove the first item added to cache
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

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
