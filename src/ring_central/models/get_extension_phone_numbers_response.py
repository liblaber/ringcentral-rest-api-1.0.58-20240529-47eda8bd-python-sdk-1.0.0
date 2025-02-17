# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .user_phone_number_info import UserPhoneNumberInfo
from .page_navigation_model import PageNavigationModel
from .enumerated_paging_model import EnumeratedPagingModel


@JsonMap({})
class GetExtensionPhoneNumbersResponse(BaseModel):
    """GetExtensionPhoneNumbersResponse

    :param uri: Link to the user phone number list resource, defaults to None
    :type uri: str, optional
    :param records: List of phone numbers
    :type records: List[UserPhoneNumberInfo]
    :param navigation: Links to other pages of the current result set
    :type navigation: PageNavigationModel
    :param paging: paging
    :type paging: EnumeratedPagingModel
    """

    def __init__(
        self,
        records: List[UserPhoneNumberInfo],
        navigation: PageNavigationModel,
        paging: EnumeratedPagingModel,
        uri: str = None,
    ):
        if uri is not None:
            self.uri = uri
        self.records = self._define_list(records, UserPhoneNumberInfo)
        self.navigation = self._define_object(navigation, PageNavigationModel)
        self.paging = self._define_object(paging, EnumeratedPagingModel)
