# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "voip_feature_enabled": "voipFeatureEnabled",
        "voip_country_blocked": "voipCountryBlocked",
        "outbound_calls_enabled": "outboundCallsEnabled",
        "dscp_enabled": "dscpEnabled",
        "dscp_signaling": "dscpSignaling",
        "dscp_voice": "dscpVoice",
        "dscp_video": "dscpVideo",
    }
)
class SipFlagsResponse(BaseModel):
    """SIP flags information

    :param voip_feature_enabled: Indicates that VoIP calling feature is enabled, defaults to None
    :type voip_feature_enabled: bool, optional
    :param voip_country_blocked: Indicates that the request is sent from IP address of a country where VoIP calling is disallowed , defaults to None
    :type voip_country_blocked: bool, optional
    :param outbound_calls_enabled: Indicates that outbound calls are enabled, defaults to None
    :type outbound_calls_enabled: bool, optional
    :param dscp_enabled: dscp_enabled, defaults to None
    :type dscp_enabled: bool, optional
    :param dscp_signaling: dscp_signaling, defaults to None
    :type dscp_signaling: int, optional
    :param dscp_voice: dscp_voice, defaults to None
    :type dscp_voice: int, optional
    :param dscp_video: dscp_video, defaults to None
    :type dscp_video: int, optional
    """

    def __init__(
        self,
        voip_feature_enabled: bool = None,
        voip_country_blocked: bool = None,
        outbound_calls_enabled: bool = None,
        dscp_enabled: bool = None,
        dscp_signaling: int = None,
        dscp_voice: int = None,
        dscp_video: int = None,
    ):
        if voip_feature_enabled is not None:
            self.voip_feature_enabled = voip_feature_enabled
        if voip_country_blocked is not None:
            self.voip_country_blocked = voip_country_blocked
        if outbound_calls_enabled is not None:
            self.outbound_calls_enabled = outbound_calls_enabled
        if dscp_enabled is not None:
            self.dscp_enabled = dscp_enabled
        if dscp_signaling is not None:
            self.dscp_signaling = dscp_signaling
        if dscp_voice is not None:
            self.dscp_voice = dscp_voice
        if dscp_video is not None:
            self.dscp_video = dscp_video
