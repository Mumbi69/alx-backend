#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.

    Args:
    - page (int): Page number (1-indexed).
    - page_size (int): Number of items per page.

    Returns:
    - tuple: A tuple containing start and end indexes.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size must be positive integers.")

    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index
