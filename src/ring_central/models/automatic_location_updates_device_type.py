# This file was generated by liblab | https://liblab.com/

from enum import Enum


class AutomaticLocationUpdatesDeviceType(Enum):
    """An enumeration representing different categories.

    :cvar HARDPHONE: "HardPhone"
    :vartype HARDPHONE: str
    :cvar SOFTPHONE: "SoftPhone"
    :vartype SOFTPHONE: str
    :cvar OTHERPHONE: "OtherPhone"
    :vartype OTHERPHONE: str
    """

    HARDPHONE = "HardPhone"
    SOFTPHONE = "SoftPhone"
    OTHERPHONE = "OtherPhone"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                AutomaticLocationUpdatesDeviceType._member_map_.values(),
            )
        )
