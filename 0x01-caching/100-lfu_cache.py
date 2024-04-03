#!/usr/bin/env python3
"""
Module that orchestrates LFU caching strategy"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Caching system that inherits from BaseCaching
    It applies the Least Frequently Used (LFU) algorithm """

    def __init__(self):
        """Initialize the LFUCache instance."""
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0
        self.used_order = []

    def put(self, key, item):
        """Method adding an item to cache dictionary using LFU replacement
        Args:
            key: The key to add the item with.
            item: The item to add to the cache.
        Note:
            If key or item is None, this method does nothing.
            If the number of items exceeds BaseCaching.MAX_ITEMS, the least
            frequently used item (LFU) will be discarded.
            If multiple items have the same least frequency, the least
            recently used item (LRU) among them will be discarded.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # LFU eviction: Remove the least frequency used item
                k_v = self.frequency.items()
                min_freq_keys = \
                    [key for key, freq in k_v  if freq == self.min_frequency]
                lru_key = \
                    min(min_freq_keys, key=lambda k: self.used_order.index(k))
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.min_frequency = min(self.frequency.values())
            self.used_order.append(key)

    def get(self, key):
        """Method retrieving an item from cache dictionary
        Args:
            key: The key of the item to retrieve.
        Returns:
            The value associated with the provided key, or None if the key
            doesn't exist or is None.
        """
        if key in self.cache_data:
            # Update the frequency of the accessed key
            self.frequency[key] += 1
            # Update the min_frequency
            self.min_frequency = min(self.frequency.values())
            # Update the used_order
            self.used_order.remove(key)
            self.used_order.append(key)
            return self.cache_data[key]
        return None
