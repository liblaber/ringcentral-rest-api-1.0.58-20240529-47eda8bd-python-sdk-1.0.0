# This file was generated by liblab | https://liblab.com/

from enum import Enum


class TypeGroup(Enum):
    """An enumeration representing different categories.

    :cvar USER: "User"
    :vartype USER: str
    :cvar NONUSER: "NonUser"
    :vartype NONUSER: str
    """

    USER = "User"
    NONUSER = "NonUser"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TypeGroup._member_map_.values()))
