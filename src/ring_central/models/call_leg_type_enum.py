# This file was generated by liblab | https://liblab.com/

from enum import Enum


class CallLegTypeEnum(Enum):
    """An enumeration representing different categories.

    :cvar SIPFORWARDING: "SipForwarding"
    :vartype SIPFORWARDING: str
    :cvar SERVICEMINUS2: "ServiceMinus2"
    :vartype SERVICEMINUS2: str
    :cvar SERVICEMINUS3: "ServiceMinus3"
    :vartype SERVICEMINUS3: str
    :cvar PSTNTOSIP: "PstnToSip"
    :vartype PSTNTOSIP: str
    :cvar ACCEPT: "Accept"
    :vartype ACCEPT: str
    :cvar FINDME: "FindMe"
    :vartype FINDME: str
    :cvar FOLLOWME: "FollowMe"
    :vartype FOLLOWME: str
    :cvar TESTCALL: "TestCall"
    :vartype TESTCALL: str
    :cvar FAXSENT: "FaxSent"
    :vartype FAXSENT: str
    :cvar CALLBACK: "CallBack"
    :vartype CALLBACK: str
    :cvar CALLINGCARD: "CallingCard"
    :vartype CALLINGCARD: str
    :cvar RINGDIRECTLY: "RingDirectly"
    :vartype RINGDIRECTLY: str
    :cvar RINGOUTWEBTOSUBSCRIBER: "RingOutWebToSubscriber"
    :vartype RINGOUTWEBTOSUBSCRIBER: str
    :cvar RINGOUTWEBTOCALLER: "RingOutWebToCaller"
    :vartype RINGOUTWEBTOCALLER: str
    :cvar SIPTOPSTNMETERED: "SipToPstnMetered"
    :vartype SIPTOPSTNMETERED: str
    :cvar RINGOUTCLIENTTOSUBSCRIBER: "RingOutClientToSubscriber"
    :vartype RINGOUTCLIENTTOSUBSCRIBER: str
    :cvar RINGOUTCLIENTTOCALLER: "RingOutClientToCaller"
    :vartype RINGOUTCLIENTTOCALLER: str
    :cvar RINGME: "RingMe"
    :vartype RINGME: str
    :cvar TRANSFERCALL: "TransferCall"
    :vartype TRANSFERCALL: str
    :cvar SIPTOPSTNUNMETERED: "SipToPstnUnmetered"
    :vartype SIPTOPSTNUNMETERED: str
    :cvar RINGOUTDEVICETOSUBSCRIBER: "RingOutDeviceToSubscriber"
    :vartype RINGOUTDEVICETOSUBSCRIBER: str
    :cvar RINGOUTDEVICETOCALLER: "RingOutDeviceToCaller"
    :vartype RINGOUTDEVICETOCALLER: str
    :cvar RINGOUTONELEGTOCALLER: "RingOutOneLegToCaller"
    :vartype RINGOUTONELEGTOCALLER: str
    :cvar EXTENSIONTOEXTENSION: "ExtensionToExtension"
    :vartype EXTENSIONTOEXTENSION: str
    :cvar CALLPARK: "CallPark"
    :vartype CALLPARK: str
    :cvar PAGINGSERVER: "PagingServer"
    :vartype PAGINGSERVER: str
    :cvar HUNTING: "Hunting"
    :vartype HUNTING: str
    :cvar OUTGOINGFREESPDL: "OutgoingFreeSpDl"
    :vartype OUTGOINGFREESPDL: str
    :cvar PARKLOCATION: "ParkLocation"
    :vartype PARKLOCATION: str
    :cvar CONFERENCECALL: "ConferenceCall"
    :vartype CONFERENCECALL: str
    :cvar MOBILEAPP: "MobileApp"
    :vartype MOBILEAPP: str
    :cvar MOVETOCONFERENCE: "MoveToConference"
    :vartype MOVETOCONFERENCE: str
    :cvar UNKNOWN: "Unknown"
    :vartype UNKNOWN: str
    :cvar MEETINGSCALL: "MeetingsCall"
    :vartype MEETINGSCALL: str
    :cvar SILENTMONITORING: "SilentMonitoring"
    :vartype SILENTMONITORING: str
    :cvar MONITORING: "Monitoring"
    :vartype MONITORING: str
    :cvar PICKUP: "Pickup"
    :vartype PICKUP: str
    :cvar IMSCALL: "ImsCall"
    :vartype IMSCALL: str
    :cvar JOINCALL: "JoinCall"
    :vartype JOINCALL: str
    :cvar TEXTRELAY: "TextRelay"
    :vartype TEXTRELAY: str
    """

    SIPFORWARDING = "SipForwarding"
    SERVICEMINUS2 = "ServiceMinus2"
    SERVICEMINUS3 = "ServiceMinus3"
    PSTNTOSIP = "PstnToSip"
    ACCEPT = "Accept"
    FINDME = "FindMe"
    FOLLOWME = "FollowMe"
    TESTCALL = "TestCall"
    FAXSENT = "FaxSent"
    CALLBACK = "CallBack"
    CALLINGCARD = "CallingCard"
    RINGDIRECTLY = "RingDirectly"
    RINGOUTWEBTOSUBSCRIBER = "RingOutWebToSubscriber"
    RINGOUTWEBTOCALLER = "RingOutWebToCaller"
    SIPTOPSTNMETERED = "SipToPstnMetered"
    RINGOUTCLIENTTOSUBSCRIBER = "RingOutClientToSubscriber"
    RINGOUTCLIENTTOCALLER = "RingOutClientToCaller"
    RINGME = "RingMe"
    TRANSFERCALL = "TransferCall"
    SIPTOPSTNUNMETERED = "SipToPstnUnmetered"
    RINGOUTDEVICETOSUBSCRIBER = "RingOutDeviceToSubscriber"
    RINGOUTDEVICETOCALLER = "RingOutDeviceToCaller"
    RINGOUTONELEGTOCALLER = "RingOutOneLegToCaller"
    EXTENSIONTOEXTENSION = "ExtensionToExtension"
    CALLPARK = "CallPark"
    PAGINGSERVER = "PagingServer"
    HUNTING = "Hunting"
    OUTGOINGFREESPDL = "OutgoingFreeSpDl"
    PARKLOCATION = "ParkLocation"
    CONFERENCECALL = "ConferenceCall"
    MOBILEAPP = "MobileApp"
    MOVETOCONFERENCE = "MoveToConference"
    UNKNOWN = "Unknown"
    MEETINGSCALL = "MeetingsCall"
    SILENTMONITORING = "SilentMonitoring"
    MONITORING = "Monitoring"
    PICKUP = "Pickup"
    IMSCALL = "ImsCall"
    JOINCALL = "JoinCall"
    TEXTRELAY = "TextRelay"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CallLegTypeEnum._member_map_.values()))
