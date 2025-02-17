# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "notify_by_email": "notifyByEmail",
        "notify_by_sms": "notifyBySms",
        "advanced_email_addresses": "advancedEmailAddresses",
        "advanced_sms_email_addresses": "advancedSmsEmailAddresses",
    }
)
class OutboundFaxesInfo(BaseModel):
    """OutboundFaxesInfo

    :param notify_by_email: Email notification flag, defaults to None
    :type notify_by_email: bool, optional
    :param notify_by_sms: SMS notification flag, defaults to None
    :type notify_by_sms: bool, optional
    :param advanced_email_addresses: List of recipient email addresses for outbound fax notifications. Returned if specified, in both modes (advanced/basic). Applied in advanced mode only , defaults to None
    :type advanced_email_addresses: List[str], optional
    :param advanced_sms_email_addresses: List of recipient phone numbers for outbound fax notifications. Returned if specified, in both modes (advanced/basic). Applied in advanced mode only , defaults to None
    :type advanced_sms_email_addresses: List[str], optional
    """

    def __init__(
        self,
        notify_by_email: bool = None,
        notify_by_sms: bool = None,
        advanced_email_addresses: List[str] = None,
        advanced_sms_email_addresses: List[str] = None,
    ):
        if notify_by_email is not None:
            self.notify_by_email = notify_by_email
        if notify_by_sms is not None:
            self.notify_by_sms = notify_by_sms
        if advanced_email_addresses is not None:
            self.advanced_email_addresses = advanced_email_addresses
        if advanced_sms_email_addresses is not None:
            self.advanced_sms_email_addresses = advanced_sms_email_addresses
