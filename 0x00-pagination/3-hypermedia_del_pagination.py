#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """main class"""
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
        """
        Retrieve hypermedia information for a page of data
        from the indexed dataset.

        Args:
        - index (int): Start index of the requested page.
        - page_size (int): Number of items per page.

        Returns:
        - dict: A dictionary containing hypermedia information
        for the specified index and page size.
        """
        assert index is None or (isinstance(index, int) and index >= 0), \
            "Index must be a non-negative integer."
        assert isinstance(page_size, int)\
            and page_size > 0, "Page size must be a positive integer."

        indexed_dataset = self.indexed_dataset()

        if index is not None:
            assert index < len(indexed_dataset), "Index out of range."

        start_index = index if index is not None else 0
        end_index = start_index + page_size

        data = [indexed_dataset[i] for i in range(start_index, min(end_index, len(indexed_dataset)))]

        next_index = end_index if end_index < len(indexed_dataset) else None

        hyper_data = {
            "index": start_index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }

        return hyper_data
