# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .blocked_number_status_enum import BlockedNumberStatusEnum


@JsonMap({"id_": "id", "phone_number": "phoneNumber"})
class BlockedAllowedPhoneNumberInfo(BaseModel):
    """Information on a blocked/allowed phone number

    :param uri: Link to a blocked/allowed phone number, defaults to None
    :type uri: str, optional
    :param id_: Internal identifier of a blocked/allowed phone number, defaults to None
    :type id_: str, optional
    :param phone_number: A blocked/allowed phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format, defaults to None
    :type phone_number: str, optional
    :param label: Custom name of a blocked/allowed phone number, defaults to None
    :type label: str, optional
    :param status: Status of a phone number, defaults to None
    :type status: BlockedNumberStatusEnum, optional
    """

    def __init__(
        self,
        uri: str = None,
        id_: str = None,
        phone_number: str = None,
        label: str = None,
        status: BlockedNumberStatusEnum = None,
    ):
        if uri is not None:
            self.uri = uri
        if id_ is not None:
            self.id_ = id_
        if phone_number is not None:
            self.phone_number = phone_number
        if label is not None:
            self.label = label
        if status is not None:
            self.status = self._enum_matching(
                status, BlockedNumberStatusEnum.list(), "status"
            )
