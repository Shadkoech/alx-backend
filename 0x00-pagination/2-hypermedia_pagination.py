#!/usr/bin/env python3
"""
Python module that orchestrates the use of pagination"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function calculating start and end indexes for pagination
    Args:
        page: int representing the current page number (1-indexed).
        page_size: int representing number of items per page.

    Returns:
        Tuple of size 2 containing start and end index for current page """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a specific page from the dataset based on pagination parameters.
        Args:
            page: int representing the current page number (1-indexed).
            page_size: int representing number of items per page.

        Returns:
            list of dict rep rows of data for the specified page.
            If input args are out of range for dataset, return empty list"""

        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieves some detailed information about a given page"""

        data_page = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }

        return page_info
