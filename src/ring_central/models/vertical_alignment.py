# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import Union
from .base import OneOfBaseModel


class VerticalAlignment1(Enum):
    """An enumeration representing different categories.

    :cvar TOP: "top"
    :vartype TOP: str
    :cvar CENTER: "center"
    :vartype CENTER: str
    :cvar BOTTOM: "bottom"
    :vartype BOTTOM: str
    """

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, VerticalAlignment1._member_map_.values()))


class VerticalAlignmentGuard(OneOfBaseModel):
    class_list = {"VerticalAlignment1Enum": str, "str": str}


VerticalAlignment = Union[str, str]
