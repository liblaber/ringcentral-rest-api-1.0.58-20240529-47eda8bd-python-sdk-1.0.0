# This file was generated by liblab | https://liblab.com/

from enum import Enum


class CallType(Enum):
    """An enumeration representing different categories.

    :cvar DIRECT: "Direct"
    :vartype DIRECT: str
    :cvar FROMQUEUE: "FromQueue"
    :vartype FROMQUEUE: str
    :cvar PARKRETRIEVAL: "ParkRetrieval"
    :vartype PARKRETRIEVAL: str
    :cvar TRANSFERRED: "Transferred"
    :vartype TRANSFERRED: str
    :cvar OUTBOUND: "Outbound"
    :vartype OUTBOUND: str
    :cvar OVERFLOW: "Overflow"
    :vartype OVERFLOW: str
    """

    DIRECT = "Direct"
    FROMQUEUE = "FromQueue"
    PARKRETRIEVAL = "ParkRetrieval"
    TRANSFERRED = "Transferred"
    OUTBOUND = "Outbound"
    OVERFLOW = "Overflow"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CallType._member_map_.values()))
