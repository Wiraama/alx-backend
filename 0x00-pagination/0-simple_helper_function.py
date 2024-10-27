#!/usr/bin/env python3
"""
return a tuple of size two containing a start index and an
end index corresponding to the range of indexes
"""


def index_range(page: int, page_size: int) -> tuple:
    """return tuple of two sizes"""
    start_page = (page - 1) * page_size
    end_page = page * page_size

    return (start_page, end_page)
