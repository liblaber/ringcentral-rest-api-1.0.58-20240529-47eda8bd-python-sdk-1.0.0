# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import Union
from .base import OneOfBaseModel


class PerPage2(Enum):
    """An enumeration representing different categories.

    :cvar MAX: "max"
    :vartype MAX: str
    :cvar ALL: "all"
    :vartype ALL: str
    """

    MAX = "max"
    ALL = "all"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PerPage2._member_map_.values()))


class PerPageGuard(OneOfBaseModel):
    class_list = {"int": int, "PerPage2Enum": str}


PerPage = Union[int, str]
