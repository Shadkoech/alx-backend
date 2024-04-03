#!/usr/bin/env python3
"""
Module that orchestrates LRU caching strategy"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Caching system that inherits from BaseCaching
    It applies the Least Recently Used (LRU) algorithm """

    def __init__(self):
        """Initializing the LRUCache instance"""
        super().__init__()
        self.used_order = []

    def put(self, key, item):
        """Method adding an item to cache dictionary using LRU replacement
        Args:
            Key: The key to add the item with
            item: The item to add to the cache
        Note:
            If key or item is None, the method will pass
            If items exceed BaseCaching.MAX_ITEMS, the least
            recently used item (LRU) will be discarded."""

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # LRU eviction: Remove the least recently used item
                least_used_key = self.used_order.pop(0)
                del self.cache_data[least_used_key]
                print("DISCARD: {}". format(least_used_key))
            self.cache_data[key] = item
            self.used_order.append(key)

    def get(self, key):
        """Method retrieving an item from cache dictionary
        Args:
            The key of the item to retrieve
        Returns:
            Value associated with provided key or
            None if the key doesn't exist or value is None
        """

        if key in self.cache_data:
            # Update the order of usage
            self.used_order.remove(key)
            # Appending the same removed key at the end of the list
            self.used_order.append(key)
            return self.cache_data[key]
        return None
