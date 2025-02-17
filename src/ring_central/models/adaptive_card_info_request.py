# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .adaptive_card_info_request_item import AdaptiveCardInfoRequestItem


class AdaptiveCardInfoRequestType(Enum):
    """An enumeration representing different categories.

    :cvar CONTAINER: "Container"
    :vartype CONTAINER: str
    """

    CONTAINER = "Container"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, AdaptiveCardInfoRequestType._member_map_.values())
        )


@JsonMap({"type_": "type"})
class AdaptiveCardInfoRequest(BaseModel):
    """AdaptiveCardInfoRequest

    :param type_: type_, defaults to None
    :type type_: AdaptiveCardInfoRequestType, optional
    :param items: items, defaults to None
    :type items: List[AdaptiveCardInfoRequestItem], optional
    """

    def __init__(
        self,
        type_: AdaptiveCardInfoRequestType = None,
        items: List[AdaptiveCardInfoRequestItem] = None,
    ):
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, AdaptiveCardInfoRequestType.list(), "type_"
            )
        if items is not None:
            self.items = self._define_list(items, AdaptiveCardInfoRequestItem)
