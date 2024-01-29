#!/usr/bin/env python3
"""Simple pagination"""

import csv
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """main class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.

        Args:
        - page (int): Page number (1-indexed).
        - page_size (int): Number of items per page.

        Returns:
        - List[List]: A list containing rows of data for the specified page.
        """
        assert isinstance(page, int)\
        and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int)\
        and page_size > 0, "Page size must be a positive integer."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
