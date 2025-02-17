# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .company_answering_rule_callers_info_request import (
    CompanyAnsweringRuleCallersInfoRequest,
)
from .company_answering_rule_called_number_info_request import (
    CompanyAnsweringRuleCalledNumberInfoRequest,
)
from .company_answering_rule_schedule_info import CompanyAnsweringRuleScheduleInfo
from .company_answering_rule_extension_info_request import (
    CompanyAnsweringRuleExtensionInfoRequest,
)
from .greeting_info import GreetingInfo


class CompanyAnsweringRuleInfoType(Enum):
    """An enumeration representing different categories.

    :cvar BUSINESSHOURS: "BusinessHours"
    :vartype BUSINESSHOURS: str
    :cvar AFTERHOURS: "AfterHours"
    :vartype AFTERHOURS: str
    :cvar CUSTOM: "Custom"
    :vartype CUSTOM: str
    """

    BUSINESSHOURS = "BusinessHours"
    AFTERHOURS = "AfterHours"
    CUSTOM = "Custom"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, CompanyAnsweringRuleInfoType._member_map_.values())
        )


class CompanyAnsweringRuleInfoCallHandlingAction(Enum):
    """An enumeration representing different categories.

    :cvar OPERATOR: "Operator"
    :vartype OPERATOR: str
    :cvar DISCONNECT: "Disconnect"
    :vartype DISCONNECT: str
    :cvar BYPASS: "Bypass"
    :vartype BYPASS: str
    """

    OPERATOR = "Operator"
    DISCONNECT = "Disconnect"
    BYPASS = "Bypass"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                CompanyAnsweringRuleInfoCallHandlingAction._member_map_.values(),
            )
        )


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "called_numbers": "calledNumbers",
        "call_handling_action": "callHandlingAction",
    }
)
class CompanyAnsweringRuleInfo(BaseModel):
    """CompanyAnsweringRuleInfo

    :param id_: Internal identifier of an answering rule, defaults to None
    :type id_: str, optional
    :param uri: Canonical URI of an answering rule, defaults to None
    :type uri: str, optional
    :param enabled: Specifies if the rule is active or inactive, defaults to None
    :type enabled: bool, optional
    :param type_: Type of an answering rule, defaults to None
    :type type_: CompanyAnsweringRuleInfoType, optional
    :param name: Name of an answering rule specified by user. Max number of symbols is 30. The default value is 'My Rule N' where 'N' is the first free number, defaults to None
    :type name: str, optional
    :param callers: Answering rule will be applied when calls are received from the specified caller(s), defaults to None
    :type callers: List[CompanyAnsweringRuleCallersInfoRequest], optional
    :param called_numbers: Answering rule will be applied when calling the specified number(s), defaults to None
    :type called_numbers: List[CompanyAnsweringRuleCalledNumberInfoRequest], optional
    :param schedule: Schedule when an answering rule should be applied, defaults to None
    :type schedule: CompanyAnsweringRuleScheduleInfo, optional
    :param call_handling_action: Specifies how incoming calls are forwarded. The default value is 'Operator' 'Operator' - play company greeting and forward to operator extension 'Disconnect' - play company greeting and disconnect 'Bypass' - bypass greeting to go to selected extension = ['Operator', 'Disconnect', 'Bypass'], defaults to None
    :type call_handling_action: CompanyAnsweringRuleInfoCallHandlingAction, optional
    :param extension: Extension to which the call is forwarded in 'Bypass' mode, defaults to None
    :type extension: CompanyAnsweringRuleExtensionInfoRequest, optional
    :param greetings: Greetings applied for an answering rule; only predefined greetings can be applied, see Dictionary Greeting List, defaults to None
    :type greetings: List[GreetingInfo], optional
    """

    def __init__(
        self,
        id_: str = None,
        uri: str = None,
        enabled: bool = None,
        type_: CompanyAnsweringRuleInfoType = None,
        name: str = None,
        callers: List[CompanyAnsweringRuleCallersInfoRequest] = None,
        called_numbers: List[CompanyAnsweringRuleCalledNumberInfoRequest] = None,
        schedule: CompanyAnsweringRuleScheduleInfo = None,
        call_handling_action: CompanyAnsweringRuleInfoCallHandlingAction = None,
        extension: CompanyAnsweringRuleExtensionInfoRequest = None,
        greetings: List[GreetingInfo] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if uri is not None:
            self.uri = uri
        if enabled is not None:
            self.enabled = enabled
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, CompanyAnsweringRuleInfoType.list(), "type_"
            )
        if name is not None:
            self.name = name
        if callers is not None:
            self.callers = self._define_list(
                callers, CompanyAnsweringRuleCallersInfoRequest
            )
        if called_numbers is not None:
            self.called_numbers = self._define_list(
                called_numbers, CompanyAnsweringRuleCalledNumberInfoRequest
            )
        if schedule is not None:
            self.schedule = self._define_object(
                schedule, CompanyAnsweringRuleScheduleInfo
            )
        if call_handling_action is not None:
            self.call_handling_action = self._enum_matching(
                call_handling_action,
                CompanyAnsweringRuleInfoCallHandlingAction.list(),
                "call_handling_action",
            )
        if extension is not None:
            self.extension = self._define_object(
                extension, CompanyAnsweringRuleExtensionInfoRequest
            )
        if greetings is not None:
            self.greetings = self._define_list(greetings, GreetingInfo)
