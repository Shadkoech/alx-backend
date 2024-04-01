#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia info based on given start index and page size.
        Args:
            index: current start index of the return page. Defaults to None.
            page_size: (int, optional): The page size. Defaults to 10.

        Returns:
            dictionary containing hypermedia information.
        """
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer."

        # If index is None, set it to 0
        if index is None:
            index = 0
        else:
            assert isinstance(index, int) and index >= 0, \
                "Index must be a non-negative integer."

        data = self.dataset()
        data_length = len(data)

        # Calculate the next index
        next_index = index + page_size

        # Adjust next_index if it exceeds the length of the dataset
        next_index = min(next_index, data_length)

        # Calculate the current page size
        current_page_size = min(page_size, data_length - index)

        # Get the actual page of the dataset
        page_data = data[index:next_index]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': current_page_size,
            'data': page_data
        }
