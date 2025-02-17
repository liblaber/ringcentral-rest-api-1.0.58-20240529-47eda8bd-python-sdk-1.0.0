# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .company_answering_rule_callers_info_request import (
    CompanyAnsweringRuleCallersInfoRequest,
)
from .company_answering_rule_called_number_info import (
    CompanyAnsweringRuleCalledNumberInfo,
)
from .company_answering_rule_schedule_info_request import (
    CompanyAnsweringRuleScheduleInfoRequest,
)
from .greeting_info import GreetingInfo


class CompanyAnsweringRuleUpdateCallHandlingAction(Enum):
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
                CompanyAnsweringRuleUpdateCallHandlingAction._member_map_.values(),
            )
        )


class CompanyAnsweringRuleUpdateType(Enum):
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
            map(lambda x: x.value, CompanyAnsweringRuleUpdateType._member_map_.values())
        )


@JsonMap(
    {
        "called_numbers": "calledNumbers",
        "call_handling_action": "callHandlingAction",
        "type_": "type",
    }
)
class CompanyAnsweringRuleUpdate(BaseModel):
    """CompanyAnsweringRuleUpdate

    :param enabled: Specifies if a rule is active or inactive. The default value is `true`, defaults to None
    :type enabled: bool, optional
    :param name: Name of an answering rule specified by user. Max number of symbols is 30. The default value is 'My Rule N' where 'N' is the first free number , defaults to None
    :type name: str, optional
    :param callers: Answering rule will be applied when calls are received from the specified caller(s) , defaults to None
    :type callers: List[CompanyAnsweringRuleCallersInfoRequest], optional
    :param called_numbers: Answering rule will be applied when calling the specified number(s), defaults to None
    :type called_numbers: List[CompanyAnsweringRuleCalledNumberInfo], optional
    :param schedule: Schedule when an answering rule should be applied, defaults to None
    :type schedule: CompanyAnsweringRuleScheduleInfoRequest, optional
    :param call_handling_action: Specifies how incoming calls are forwarded. The default value is 'Operator' 'Operator' - play company greeting and forward to operator extension 'Disconnect' - play company greeting and disconnect 'Bypass' - bypass greeting to go to selected extension = ['Operator', 'Disconnect','Bypass'], defaults to None
    :type call_handling_action: CompanyAnsweringRuleUpdateCallHandlingAction, optional
    :param type_: Type of an answering rule, defaults to None
    :type type_: CompanyAnsweringRuleUpdateType, optional
    :param extension: extension, defaults to None
    :type extension: CompanyAnsweringRuleCallersInfoRequest, optional
    :param greetings: Greetings applied for an answering rule; only predefined greetings can be applied, see Dictionary Greeting List , defaults to None
    :type greetings: List[GreetingInfo], optional
    """

    def __init__(
        self,
        enabled: bool = None,
        name: str = None,
        callers: List[CompanyAnsweringRuleCallersInfoRequest] = None,
        called_numbers: List[CompanyAnsweringRuleCalledNumberInfo] = None,
        schedule: CompanyAnsweringRuleScheduleInfoRequest = None,
        call_handling_action: CompanyAnsweringRuleUpdateCallHandlingAction = None,
        type_: CompanyAnsweringRuleUpdateType = None,
        extension: CompanyAnsweringRuleCallersInfoRequest = None,
        greetings: List[GreetingInfo] = None,
    ):
        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if callers is not None:
            self.callers = self._define_list(
                callers, CompanyAnsweringRuleCallersInfoRequest
            )
        if called_numbers is not None:
            self.called_numbers = self._define_list(
                called_numbers, CompanyAnsweringRuleCalledNumberInfo
            )
        if schedule is not None:
            self.schedule = self._define_object(
                schedule, CompanyAnsweringRuleScheduleInfoRequest
            )
        if call_handling_action is not None:
            self.call_handling_action = self._enum_matching(
                call_handling_action,
                CompanyAnsweringRuleUpdateCallHandlingAction.list(),
                "call_handling_action",
            )
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, CompanyAnsweringRuleUpdateType.list(), "type_"
            )
        if extension is not None:
            self.extension = self._define_object(
                extension, CompanyAnsweringRuleCallersInfoRequest
            )
        if greetings is not None:
            self.greetings = self._define_list(greetings, GreetingInfo)
