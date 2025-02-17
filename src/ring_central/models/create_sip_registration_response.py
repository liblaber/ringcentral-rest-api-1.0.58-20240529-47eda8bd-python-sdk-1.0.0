# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .sip_registration_device_info import SipRegistrationDeviceInfo
from .sip_info_response import SipInfoResponse
from .sip_flags_response import SipFlagsResponse


@JsonMap(
    {
        "sip_info": "sipInfo",
        "sip_info_pstn": "sipInfoPstn",
        "sip_flags": "sipFlags",
        "sip_error_codes": "sipErrorCodes",
        "polling_interval": "pollingInterval",
    }
)
class CreateSipRegistrationResponse(BaseModel):
    """CreateSipRegistrationResponse

    :param device: device
    :type device: SipRegistrationDeviceInfo
    :param sip_info: SIP settings for device
    :type sip_info: List[SipInfoResponse]
    :param sip_info_pstn: SIP PSTN settings for device, defaults to None
    :type sip_info_pstn: List[SipInfoResponse], optional
    :param sip_flags: SIP flags information
    :type sip_flags: SipFlagsResponse
    :param sip_error_codes: sip_error_codes, defaults to None
    :type sip_error_codes: List[str], optional
    :param polling_interval: Suggested interval in seconds to periodically call SIP-provision API and update the local cache , defaults to None
    :type polling_interval: int, optional
    """

    def __init__(
        self,
        device: SipRegistrationDeviceInfo,
        sip_info: List[SipInfoResponse],
        sip_flags: SipFlagsResponse,
        sip_info_pstn: List[SipInfoResponse] = None,
        sip_error_codes: List[str] = None,
        polling_interval: int = None,
    ):
        self.device = self._define_object(device, SipRegistrationDeviceInfo)
        self.sip_info = self._define_list(sip_info, SipInfoResponse)
        if sip_info_pstn is not None:
            self.sip_info_pstn = self._define_list(sip_info_pstn, SipInfoResponse)
        self.sip_flags = self._define_object(sip_flags, SipFlagsResponse)
        if sip_error_codes is not None:
            self.sip_error_codes = sip_error_codes
        if polling_interval is not None:
            self.polling_interval = polling_interval
