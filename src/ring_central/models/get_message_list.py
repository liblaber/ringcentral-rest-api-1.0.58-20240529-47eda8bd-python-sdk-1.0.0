# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .get_message_info_response import GetMessageInfoResponse
from .messaging_navigation_info import MessagingNavigationInfo
from .messaging_paging_info import MessagingPagingInfo


@JsonMap({})
class GetMessageList(BaseModel):
    """GetMessageList

    :param uri: Link to a list of user messages, defaults to None
    :type uri: str, optional
    :param records: List of records with message information
    :type records: List[GetMessageInfoResponse]
    :param navigation: Information on navigation
    :type navigation: MessagingNavigationInfo
    :param paging: Information on paging
    :type paging: MessagingPagingInfo
    """

    def __init__(
        self,
        records: List[GetMessageInfoResponse],
        navigation: MessagingNavigationInfo,
        paging: MessagingPagingInfo,
        uri: str = None,
    ):
        if uri is not None:
            self.uri = uri
        self.records = self._define_list(records, GetMessageInfoResponse)
        self.navigation = self._define_object(navigation, MessagingNavigationInfo)
        self.paging = self._define_object(paging, MessagingPagingInfo)
