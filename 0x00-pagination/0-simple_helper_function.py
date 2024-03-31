#!/usr/bin/env python3
"""
Python module that orchestrates the use of pagination"""

from typing import Tuple


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
