# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class ScimPhoneNumberType(Enum):
    """An enumeration representing different categories.

    :cvar WORK: "work"
    :vartype WORK: str
    :cvar MOBILE: "mobile"
    :vartype MOBILE: str
    :cvar OTHER: "other"
    :vartype OTHER: str
    """

    WORK = "work"
    MOBILE = "mobile"
    OTHER = "other"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ScimPhoneNumberType._member_map_.values()))


@JsonMap({"type_": "type"})
class ScimPhoneNumber(BaseModel):
    """ScimPhoneNumber

    :param type_: type_
    :type type_: ScimPhoneNumberType
    :param value: value
    :type value: str
    """

    def __init__(self, type_: ScimPhoneNumberType, value: str):
        self.type_ = self._enum_matching(type_, ScimPhoneNumberType.list(), "type_")
        self.value = value
