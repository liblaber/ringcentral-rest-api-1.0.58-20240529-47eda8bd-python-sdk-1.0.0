# This file was generated by liblab | https://liblab.com/

from enum import Enum


class DeviceFeatureEnum(Enum):
    """An enumeration representing different categories.

    :cvar BLA: "BLA"
    :vartype BLA: str
    :cvar COMMONPHONE: "CommonPhone"
    :vartype COMMONPHONE: str
    :cvar INTERCOM: "Intercom"
    :vartype INTERCOM: str
    :cvar PAGING: "Paging"
    :vartype PAGING: str
    :cvar HELD: "HELD"
    :vartype HELD: str
    """

    BLA = "BLA"
    COMMONPHONE = "CommonPhone"
    INTERCOM = "Intercom"
    PAGING = "Paging"
    HELD = "HELD"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DeviceFeatureEnum._member_map_.values()))
