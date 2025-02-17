# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .messaging_navigation_info_uri import MessagingNavigationInfoUri


@JsonMap(
    {
        "first_page": "firstPage",
        "next_page": "nextPage",
        "previous_page": "previousPage",
        "last_page": "lastPage",
    }
)
class MessagingNavigationInfo(BaseModel):
    """Information on navigation

    :param first_page: Canonical URI for the corresponding page of the list, defaults to None
    :type first_page: MessagingNavigationInfoUri, optional
    :param next_page: Canonical URI for the corresponding page of the list, defaults to None
    :type next_page: MessagingNavigationInfoUri, optional
    :param previous_page: Canonical URI for the corresponding page of the list, defaults to None
    :type previous_page: MessagingNavigationInfoUri, optional
    :param last_page: Canonical URI for the corresponding page of the list, defaults to None
    :type last_page: MessagingNavigationInfoUri, optional
    """

    def __init__(
        self,
        first_page: MessagingNavigationInfoUri = None,
        next_page: MessagingNavigationInfoUri = None,
        previous_page: MessagingNavigationInfoUri = None,
        last_page: MessagingNavigationInfoUri = None,
    ):
        if first_page is not None:
            self.first_page = self._define_object(
                first_page, MessagingNavigationInfoUri
            )
        if next_page is not None:
            self.next_page = self._define_object(next_page, MessagingNavigationInfoUri)
        if previous_page is not None:
            self.previous_page = self._define_object(
                previous_page, MessagingNavigationInfoUri
            )
        if last_page is not None:
            self.last_page = self._define_object(last_page, MessagingNavigationInfoUri)
