# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .adaptive_card_creator import AdaptiveCardCreator


class AdaptiveCardShortInfoType(Enum):
    """An enumeration representing different categories.

    :cvar ADAPTIVECARD: "AdaptiveCard"
    :vartype ADAPTIVECARD: str
    """

    ADAPTIVECARD = "AdaptiveCard"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, AdaptiveCardShortInfoType._member_map_.values())
        )


@JsonMap(
    {
        "id_": "id",
        "creation_time": "creationTime",
        "last_modified_time": "lastModifiedTime",
        "schema": "$schema",
        "type_": "type",
        "chat_ids": "chatIds",
    }
)
class AdaptiveCardShortInfo(BaseModel):
    """AdaptiveCardShortInfo

    :param id_: Internal identifier of an adaptive card, defaults to None
    :type id_: str, optional
    :param creation_time: Adaptive Card creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, defaults to None
    :type creation_time: str, optional
    :param last_modified_time: Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, defaults to None
    :type last_modified_time: str, optional
    :param schema: Schema of an adaptive card, defaults to None
    :type schema: str, optional
    :param type_: type_, defaults to None
    :type type_: AdaptiveCardShortInfoType, optional
    :param version: Version of an adaptive card. Filled on server-side, defaults to None
    :type version: str, optional
    :param creator: creator, defaults to None
    :type creator: AdaptiveCardCreator, optional
    :param chat_ids: Chat IDs where an adaptive card is posted or shared., defaults to None
    :type chat_ids: List[str], optional
    """

    def __init__(
        self,
        id_: str = None,
        creation_time: str = None,
        last_modified_time: str = None,
        schema: str = None,
        type_: AdaptiveCardShortInfoType = None,
        version: str = None,
        creator: AdaptiveCardCreator = None,
        chat_ids: List[str] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if creation_time is not None:
            self.creation_time = creation_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if schema is not None:
            self.schema = schema
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, AdaptiveCardShortInfoType.list(), "type_"
            )
        if version is not None:
            self.version = version
        if creator is not None:
            self.creator = self._define_object(creator, AdaptiveCardCreator)
        if chat_ids is not None:
            self.chat_ids = chat_ids
