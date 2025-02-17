# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .personal_contact_resource import PersonalContactResource
from .user_contacts_navigation_info import UserContactsNavigationInfo
from .user_contacts_paging_info import UserContactsPagingInfo
from .user_contacts_groups_info import UserContactsGroupsInfo


@JsonMap({})
class ContactList(BaseModel):
    """ContactList

    :param uri: Link to the list of user personal contacts, defaults to None
    :type uri: str, optional
    :param records: List of personal contacts from the extension address book , defaults to None
    :type records: List[PersonalContactResource], optional
    :param navigation: Information on navigation, defaults to None
    :type navigation: UserContactsNavigationInfo, optional
    :param paging: Information on paging, defaults to None
    :type paging: UserContactsPagingInfo, optional
    :param groups: Information on address book groups, defaults to None
    :type groups: UserContactsGroupsInfo, optional
    """

    def __init__(
        self,
        uri: str = None,
        records: List[PersonalContactResource] = None,
        navigation: UserContactsNavigationInfo = None,
        paging: UserContactsPagingInfo = None,
        groups: UserContactsGroupsInfo = None,
    ):
        if uri is not None:
            self.uri = uri
        if records is not None:
            self.records = self._define_list(records, PersonalContactResource)
        if navigation is not None:
            self.navigation = self._define_object(
                navigation, UserContactsNavigationInfo
            )
        if paging is not None:
            self.paging = self._define_object(paging, UserContactsPagingInfo)
        if groups is not None:
            self.groups = self._define_object(groups, UserContactsGroupsInfo)
