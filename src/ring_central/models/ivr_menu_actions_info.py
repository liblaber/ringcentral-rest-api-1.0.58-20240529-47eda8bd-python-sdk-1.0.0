# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .ivr_menu_extension_info import IvrMenuExtensionInfo


class IvrMenuActionsInfoAction(Enum):
    """An enumeration representing different categories.

    :cvar CONNECT: "Connect"
    :vartype CONNECT: str
    :cvar VOICEMAIL: "Voicemail"
    :vartype VOICEMAIL: str
    :cvar DIALBYNAME: "DialByName"
    :vartype DIALBYNAME: str
    :cvar TRANSFER: "Transfer"
    :vartype TRANSFER: str
    :cvar REPEAT: "Repeat"
    :vartype REPEAT: str
    :cvar RETURNTOROOT: "ReturnToRoot"
    :vartype RETURNTOROOT: str
    :cvar RETURNTOPREVIOUS: "ReturnToPrevious"
    :vartype RETURNTOPREVIOUS: str
    :cvar DISCONNECT: "Disconnect"
    :vartype DISCONNECT: str
    :cvar RETURNTOTOPLEVELMENU: "ReturnToTopLevelMenu"
    :vartype RETURNTOTOPLEVELMENU: str
    :cvar DONOTHING: "DoNothing"
    :vartype DONOTHING: str
    :cvar CONNECTTOOPERATOR: "ConnectToOperator"
    :vartype CONNECTTOOPERATOR: str
    """

    CONNECT = "Connect"
    VOICEMAIL = "Voicemail"
    DIALBYNAME = "DialByName"
    TRANSFER = "Transfer"
    REPEAT = "Repeat"
    RETURNTOROOT = "ReturnToRoot"
    RETURNTOPREVIOUS = "ReturnToPrevious"
    DISCONNECT = "Disconnect"
    RETURNTOTOPLEVELMENU = "ReturnToTopLevelMenu"
    DONOTHING = "DoNothing"
    CONNECTTOOPERATOR = "ConnectToOperator"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, IvrMenuActionsInfoAction._member_map_.values())
        )


@JsonMap({"phone_number": "phoneNumber"})
class IvrMenuActionsInfo(BaseModel):
    """IvrMenuActionsInfo

    :param input: Key. The following values are supported: numeric: '1' to '9' Star Hash NoInput , defaults to None
    :type input: str, optional
    :param action: Internal identifier of an answering rule, defaults to None
    :type action: IvrMenuActionsInfoAction, optional
    :param extension: For 'Connect' or 'Voicemail' actions only. Extension reference, defaults to None
    :type extension: IvrMenuExtensionInfo, optional
    :param phone_number: For 'Transfer' action only. PSTN number in E.164 format, defaults to None
    :type phone_number: str, optional
    """

    def __init__(
        self,
        input: str = None,
        action: IvrMenuActionsInfoAction = None,
        extension: IvrMenuExtensionInfo = None,
        phone_number: str = None,
    ):
        if input is not None:
            self.input = input
        if action is not None:
            self.action = self._enum_matching(
                action, IvrMenuActionsInfoAction.list(), "action"
            )
        if extension is not None:
            self.extension = self._define_object(extension, IvrMenuExtensionInfo)
        if phone_number is not None:
            self.phone_number = phone_number
