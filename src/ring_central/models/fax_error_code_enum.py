# This file was generated by liblab | https://liblab.com/

from enum import Enum


class FaxErrorCodeEnum(Enum):
    """An enumeration representing different categories.

    :cvar ALLLINESINUSE: "AllLinesInUse"
    :vartype ALLLINESINUSE: str
    :cvar UNDEFINED: "Undefined"
    :vartype UNDEFINED: str
    :cvar NOFAXSENDPERMISSION: "NoFaxSendPermission"
    :vartype NOFAXSENDPERMISSION: str
    :cvar NOINTERNATIONALPERMISSION: "NoInternationalPermission"
    :vartype NOINTERNATIONALPERMISSION: str
    :cvar NOFAXMACHINE: "NoFaxMachine"
    :vartype NOFAXMACHINE: str
    :cvar NOANSWER: "NoAnswer"
    :vartype NOANSWER: str
    :cvar LINEBUSY: "LineBusy"
    :vartype LINEBUSY: str
    :cvar CALLERHUNGUP: "CallerHungUp"
    :vartype CALLERHUNGUP: str
    :cvar NOTENOUGHCREDITS: "NotEnoughCredits"
    :vartype NOTENOUGHCREDITS: str
    :cvar SENTPARTIALLY: "SentPartially"
    :vartype SENTPARTIALLY: str
    :cvar INTERNATIONALCALLINGDISABLED: "InternationalCallingDisabled"
    :vartype INTERNATIONALCALLINGDISABLED: str
    :cvar DESTINATIONCOUNTRYDISABLED: "DestinationCountryDisabled"
    :vartype DESTINATIONCOUNTRYDISABLED: str
    :cvar UNKNOWNCOUNTRYCODE: "UnknownCountryCode"
    :vartype UNKNOWNCOUNTRYCODE: str
    :cvar NOTACCEPTED: "NotAccepted"
    :vartype NOTACCEPTED: str
    :cvar INVALIDNUMBER: "InvalidNumber"
    :vartype INVALIDNUMBER: str
    :cvar CALLDECLINED: "CallDeclined"
    :vartype CALLDECLINED: str
    :cvar TOOMANYCALLSPERLINE: "TooManyCallsPerLine"
    :vartype TOOMANYCALLSPERLINE: str
    :cvar CALLFAILED: "CallFailed"
    :vartype CALLFAILED: str
    :cvar RENDERINGFAILED: "RenderingFailed"
    :vartype RENDERINGFAILED: str
    :cvar TOOMANYPAGES: "TooManyPages"
    :vartype TOOMANYPAGES: str
    :cvar RETURNTODBQUEUE: "ReturnToDBQueue"
    :vartype RETURNTODBQUEUE: str
    :cvar NOCALLTIME: "NoCallTime"
    :vartype NOCALLTIME: str
    :cvar WRONGNUMBER: "WrongNumber"
    :vartype WRONGNUMBER: str
    :cvar PROHIBITEDNUMBER: "ProhibitedNumber"
    :vartype PROHIBITEDNUMBER: str
    :cvar INTERNALERROR: "InternalError"
    :vartype INTERNALERROR: str
    :cvar FAXSENDINGPROHIBITED: "FaxSendingProhibited"
    :vartype FAXSENDINGPROHIBITED: str
    :cvar THEPHONEISBLACKLISTED: "ThePhoneIsBlacklisted"
    :vartype THEPHONEISBLACKLISTED: str
    :cvar USERNOTFOUND: "UserNotFound"
    :vartype USERNOTFOUND: str
    :cvar CONVERTERROR: "ConvertError"
    :vartype CONVERTERROR: str
    :cvar DBGENERALERROR: "DBGeneralError"
    :vartype DBGENERALERROR: str
    :cvar SKYPEBILLINGFAILED: "SkypeBillingFailed"
    :vartype SKYPEBILLINGFAILED: str
    :cvar ACCOUNTSUSPENDED: "AccountSuspended"
    :vartype ACCOUNTSUSPENDED: str
    :cvar PROHIBITEDDESTINATION: "ProhibitedDestination"
    :vartype PROHIBITEDDESTINATION: str
    :cvar INTERNATIONALDISABLED: "InternationalDisabled"
    :vartype INTERNATIONALDISABLED: str
    """

    ALLLINESINUSE = "AllLinesInUse"
    UNDEFINED = "Undefined"
    NOFAXSENDPERMISSION = "NoFaxSendPermission"
    NOINTERNATIONALPERMISSION = "NoInternationalPermission"
    NOFAXMACHINE = "NoFaxMachine"
    NOANSWER = "NoAnswer"
    LINEBUSY = "LineBusy"
    CALLERHUNGUP = "CallerHungUp"
    NOTENOUGHCREDITS = "NotEnoughCredits"
    SENTPARTIALLY = "SentPartially"
    INTERNATIONALCALLINGDISABLED = "InternationalCallingDisabled"
    DESTINATIONCOUNTRYDISABLED = "DestinationCountryDisabled"
    UNKNOWNCOUNTRYCODE = "UnknownCountryCode"
    NOTACCEPTED = "NotAccepted"
    INVALIDNUMBER = "InvalidNumber"
    CALLDECLINED = "CallDeclined"
    TOOMANYCALLSPERLINE = "TooManyCallsPerLine"
    CALLFAILED = "CallFailed"
    RENDERINGFAILED = "RenderingFailed"
    TOOMANYPAGES = "TooManyPages"
    RETURNTODBQUEUE = "ReturnToDBQueue"
    NOCALLTIME = "NoCallTime"
    WRONGNUMBER = "WrongNumber"
    PROHIBITEDNUMBER = "ProhibitedNumber"
    INTERNALERROR = "InternalError"
    FAXSENDINGPROHIBITED = "FaxSendingProhibited"
    THEPHONEISBLACKLISTED = "ThePhoneIsBlacklisted"
    USERNOTFOUND = "UserNotFound"
    CONVERTERROR = "ConvertError"
    DBGENERALERROR = "DBGeneralError"
    SKYPEBILLINGFAILED = "SkypeBillingFailed"
    ACCOUNTSUSPENDED = "AccountSuspended"
    PROHIBITEDDESTINATION = "ProhibitedDestination"
    INTERNATIONALDISABLED = "InternationalDisabled"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, FaxErrorCodeEnum._member_map_.values()))
