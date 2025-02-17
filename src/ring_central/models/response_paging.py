# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "per_page": "perPage",
        "total_pages": "totalPages",
        "total_elements": "totalElements",
    }
)
class ResponsePaging(BaseModel):
    """Paging information

    :param page: The current page number
    :type page: int
    :param per_page: How many items are displayed on the page
    :type per_page: int
    :param total_pages: The total number of pages
    :type total_pages: int
    :param total_elements: The total number of items in the dataset
    :type total_elements: int
    """

    def __init__(self, page: int, per_page: int, total_pages: int, total_elements: int):
        self.page = page
        self.per_page = per_page
        self.total_pages = total_pages
        self.total_elements = total_elements
