# This file was generated by liblab | https://liblab.com/

from enum import Enum


class PhoneLineTypeEnum(Enum):
    """An enumeration representing different categories.

    :cvar UNKNOWN: "Unknown"
    :vartype UNKNOWN: str
    :cvar STANDALONE: "Standalone"
    :vartype STANDALONE: str
    :cvar STANDALONEFREE: "StandaloneFree"
    :vartype STANDALONEFREE: str
    :cvar BLAPRIMARY: "BlaPrimary"
    :vartype BLAPRIMARY: str
    :cvar BLASECONDARY: "BlaSecondary"
    :vartype BLASECONDARY: str
    """

    UNKNOWN = "Unknown"
    STANDALONE = "Standalone"
    STANDALONEFREE = "StandaloneFree"
    BLAPRIMARY = "BlaPrimary"
    BLASECONDARY = "BlaSecondary"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, PhoneLineTypeEnum._member_map_.values()))
