#!/usr/bin/env python3
"""
Caching system module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system class that inherits from BaseCaching
    This caching system has no limit."""

    def __init__(self):
        """Initialize inheritance"""
        super().__init__()

    def put(self, key, item):
        """Method that adds an item to cache dictionary
        Args:
            key: The key to add the item with
            item: The item to add to the cache
        Note:
            If key is None, the method does nothing
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Method that retrieves an item from the cache dictionary
        Args:
            The key of the item to retrieve
        Returns:
            Value associated with provided key or
            None if the key doesn't exist or value is None
        """

        return self.cache_data.get(key)
