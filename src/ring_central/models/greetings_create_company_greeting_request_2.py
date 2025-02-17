# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class CreateCompanyGreetingRequestType2(Enum):
    """An enumeration representing different categories.

    :cvar COMPANY: "Company"
    :vartype COMPANY: str
    :cvar STARTRECORDING: "StartRecording"
    :vartype STARTRECORDING: str
    :cvar STOPRECORDING: "StopRecording"
    :vartype STOPRECORDING: str
    :cvar AUTOMATICRECORDING: "AutomaticRecording"
    :vartype AUTOMATICRECORDING: str
    :cvar TEMPLATEGREETING: "TemplateGreeting"
    :vartype TEMPLATEGREETING: str
    """

    COMPANY = "Company"
    STARTRECORDING = "StartRecording"
    STOPRECORDING = "StopRecording"
    AUTOMATICRECORDING = "AutomaticRecording"
    TEMPLATEGREETING = "TemplateGreeting"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                CreateCompanyGreetingRequestType2._member_map_.values(),
            )
        )


@JsonMap(
    {
        "type_": "type",
        "answering_rule_id": "answeringRuleId",
        "language_id": "languageId",
    }
)
class GreetingsCreateCompanyGreetingRequest2(BaseModel):
    """GreetingsCreateCompanyGreetingRequest2

    :param type_: Type of greeting, specifying the case when the greeting is played.
    :type type_: CreateCompanyGreetingRequestType2
    :param answering_rule_id: Internal identifier of an answering rule, defaults to None
    :type answering_rule_id: str, optional
    :param language_id: Internal identifier of a language. See Get Language List , defaults to None
    :type language_id: str, optional
    :param binary: Media file to upload
    :type binary: any
    """

    def __init__(
        self,
        type_: CreateCompanyGreetingRequestType2,
        binary: any,
        answering_rule_id: str = None,
        language_id: str = None,
    ):
        self.type_ = self._enum_matching(
            type_, CreateCompanyGreetingRequestType2.list(), "type_"
        )
        if answering_rule_id is not None:
            self.answering_rule_id = answering_rule_id
        if language_id is not None:
            self.language_id = language_id
        self.binary = binary
