# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "page_token": "pageToken",
        "per_page": "perPage",
        "first_page_token": "firstPageToken",
        "previous_page_token": "previousPageToken",
        "next_page_token": "nextPageToken",
    }
)
class PagingResource(BaseModel):
    """Pagination details

    :param page_token: Page token of the current response list, defaults to None
    :type page_token: str, optional
    :param per_page: Number of records per page, defaults to None
    :type per_page: int, optional
    :param first_page_token: First page token of the current filter criteria, defaults to None
    :type first_page_token: str, optional
    :param previous_page_token: Previous page token of the current filter criteria, defaults to None
    :type previous_page_token: str, optional
    :param next_page_token: Next page token of the current filter criteria, defaults to None
    :type next_page_token: str, optional
    """

    def __init__(
        self,
        page_token: str = None,
        per_page: int = None,
        first_page_token: str = None,
        previous_page_token: str = None,
        next_page_token: str = None,
    ):
        if page_token is not None:
            self.page_token = page_token
        if per_page is not None:
            self.per_page = per_page
        if first_page_token is not None:
            self.first_page_token = first_page_token
        if previous_page_token is not None:
            self.previous_page_token = previous_page_token
        if next_page_token is not None:
            self.next_page_token = next_page_token
