#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple


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

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        return a tuple of size two containing a start index and an end index
        """
        start = (page * page_size) - page_size
        end = start + page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get Page"""
        assert type(page_size) is int and type(page) is int
        assert page > 0 and page_size > 0
        self.dataset()
        start, end = self.index_range(page, page_size)
        return self.__dataset[start:end]
