# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ListExtensionsType(Enum):
    """An enumeration representing different categories.

    :cvar USER: "User"
    :vartype USER: str
    :cvar FAXUSER: "FaxUser"
    :vartype FAXUSER: str
    :cvar FLEXIBLEUSER: "FlexibleUser"
    :vartype FLEXIBLEUSER: str
    :cvar VIRTUALUSER: "VirtualUser"
    :vartype VIRTUALUSER: str
    :cvar DIGITALUSER: "DigitalUser"
    :vartype DIGITALUSER: str
    :cvar DEPARTMENT: "Department"
    :vartype DEPARTMENT: str
    :cvar ANNOUNCEMENT: "Announcement"
    :vartype ANNOUNCEMENT: str
    :cvar VOICEMAIL: "Voicemail"
    :vartype VOICEMAIL: str
    :cvar SHAREDLINESGROUP: "SharedLinesGroup"
    :vartype SHAREDLINESGROUP: str
    :cvar PAGINGONLY: "PagingOnly"
    :vartype PAGINGONLY: str
    :cvar IVRMENU: "IvrMenu"
    :vartype IVRMENU: str
    :cvar APPLICATIONEXTENSION: "ApplicationExtension"
    :vartype APPLICATIONEXTENSION: str
    :cvar PARKLOCATION: "ParkLocation"
    :vartype PARKLOCATION: str
    :cvar LIMITED: "Limited"
    :vartype LIMITED: str
    :cvar BOT: "Bot"
    :vartype BOT: str
    :cvar PROXYADMIN: "ProxyAdmin"
    :vartype PROXYADMIN: str
    :cvar DELEGATEDLINESGROUP: "DelegatedLinesGroup"
    :vartype DELEGATEDLINESGROUP: str
    :cvar SITE: "Site"
    :vartype SITE: str
    """

    USER = "User"
    FAXUSER = "FaxUser"
    FLEXIBLEUSER = "FlexibleUser"
    VIRTUALUSER = "VirtualUser"
    DIGITALUSER = "DigitalUser"
    DEPARTMENT = "Department"
    ANNOUNCEMENT = "Announcement"
    VOICEMAIL = "Voicemail"
    SHAREDLINESGROUP = "SharedLinesGroup"
    PAGINGONLY = "PagingOnly"
    IVRMENU = "IvrMenu"
    APPLICATIONEXTENSION = "ApplicationExtension"
    PARKLOCATION = "ParkLocation"
    LIMITED = "Limited"
    BOT = "Bot"
    PROXYADMIN = "ProxyAdmin"
    DELEGATEDLINESGROUP = "DelegatedLinesGroup"
    SITE = "Site"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ListExtensionsType._member_map_.values()))
