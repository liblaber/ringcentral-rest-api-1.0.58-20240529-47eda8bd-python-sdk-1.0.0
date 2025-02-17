# This file was generated by liblab | https://liblab.com/

from enum import Enum


class QueueSlaOptions(Enum):
    """An enumeration representing different categories.

    :cvar INSLA: "InSla"
    :vartype INSLA: str
    :cvar OUTSLA: "OutSla"
    :vartype OUTSLA: str
    """

    INSLA = "InSla"
    OUTSLA = "OutSla"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, QueueSlaOptions._member_map_.values()))
