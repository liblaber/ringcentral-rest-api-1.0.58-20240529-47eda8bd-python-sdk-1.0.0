# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .call_log_record_device_info import CallLogRecordDeviceInfo


@JsonMap(
    {
        "phone_number": "phoneNumber",
        "extension_number": "extensionNumber",
        "extension_id": "extensionId",
        "dialed_phone_number": "dialedPhoneNumber",
    }
)
class CallLogToParty(BaseModel):
    """CallLogToParty

    :param phone_number: Phone number of a party. Usually it is a plain number including country and area code like 18661234567. But sometimes it could be returned from database with some formatting applied, for example (866)123-4567. This property is filled in all cases where parties communicate by means of global phone numbers, for example when calling to direct numbers or sending/receiving SMS, defaults to None
    :type phone_number: str, optional
    :param extension_number: Extension short number (usually 3 or 4 digits). This property is filled when parties communicate by means of short internal numbers, for example when calling to other extension or sending/receiving Company Pager message, defaults to None
    :type extension_number: str, optional
    :param extension_id: Internal identifier of an extension, defaults to None
    :type extension_id: str, optional
    :param name: Symbolic name associated with a party. If the phone does not belong to the known extension, only the location is returned, the name is not determined then, defaults to None
    :type name: str, optional
    :param location: Contains party location (city, state) if one can be determined from phoneNumber. This property is filled only when phoneNumber is not empty and server can calculate location information from it (for example, this information is unavailable for US toll-free numbers), defaults to None
    :type location: str, optional
    :param device: device, defaults to None
    :type device: CallLogRecordDeviceInfo, optional
    :param dialed_phone_number: Dialed phone number without any format modifications. Returned for outbound calls, defaults to None
    :type dialed_phone_number: str, optional
    """

    def __init__(
        self,
        phone_number: str = None,
        extension_number: str = None,
        extension_id: str = None,
        name: str = None,
        location: str = None,
        device: CallLogRecordDeviceInfo = None,
        dialed_phone_number: str = None,
    ):
        if phone_number is not None:
            self.phone_number = phone_number
        if extension_number is not None:
            self.extension_number = extension_number
        if extension_id is not None:
            self.extension_id = extension_id
        if name is not None:
            self.name = name
        if location is not None:
            self.location = location
        if device is not None:
            self.device = self._define_object(device, CallLogRecordDeviceInfo)
        if dialed_phone_number is not None:
            self.dialed_phone_number = dialed_phone_number
