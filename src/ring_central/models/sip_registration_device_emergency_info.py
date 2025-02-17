# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import Union
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .sip_registration_device_location_info import SipRegistrationDeviceLocationInfo
from .device_emergency_service_address_resource_default import (
    DeviceEmergencyServiceAddressResourceDefault,
)
from .device_emergency_service_address_resource_au import (
    DeviceEmergencyServiceAddressResourceAu,
)
from .device_emergency_service_address_resource_fr import (
    DeviceEmergencyServiceAddressResourceFr,
)


class AddressGuard(OneOfBaseModel):
    class_list = {
        "DeviceEmergencyServiceAddressResourceDefault": DeviceEmergencyServiceAddressResourceDefault,
        "DeviceEmergencyServiceAddressResourceAu": DeviceEmergencyServiceAddressResourceAu,
        "DeviceEmergencyServiceAddressResourceFr": DeviceEmergencyServiceAddressResourceFr,
    }


Address = Union[
    DeviceEmergencyServiceAddressResourceDefault,
    DeviceEmergencyServiceAddressResourceAu,
    DeviceEmergencyServiceAddressResourceFr,
]


class SipRegistrationDeviceEmergencyInfoAddressStatus(Enum):
    """An enumeration representing different categories.

    :cvar VALID: "Valid"
    :vartype VALID: str
    :cvar INVALID: "Invalid"
    :vartype INVALID: str
    :cvar PROCESSING: "Processing"
    :vartype PROCESSING: str
    """

    VALID = "Valid"
    INVALID = "Invalid"
    PROCESSING = "Processing"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                SipRegistrationDeviceEmergencyInfoAddressStatus._member_map_.values(),
            )
        )


class SipRegistrationDeviceEmergencyInfoVisibility(Enum):
    """An enumeration representing different categories.

    :cvar PRIVATE: "Private"
    :vartype PRIVATE: str
    :cvar PUBLIC: "Public"
    :vartype PUBLIC: str
    """

    PRIVATE = "Private"
    PUBLIC = "Public"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                SipRegistrationDeviceEmergencyInfoVisibility._member_map_.values(),
            )
        )


class SipRegistrationDeviceEmergencyInfoSyncStatus(Enum):
    """An enumeration representing different categories.

    :cvar VERIFIED: "Verified"
    :vartype VERIFIED: str
    :cvar UPDATED: "Updated"
    :vartype UPDATED: str
    :cvar DELETED: "Deleted"
    :vartype DELETED: str
    :cvar NOTREQUIRED: "NotRequired"
    :vartype NOTREQUIRED: str
    :cvar UNSUPPORTED: "Unsupported"
    :vartype UNSUPPORTED: str
    :cvar FAILED: "Failed"
    :vartype FAILED: str
    """

    VERIFIED = "Verified"
    UPDATED = "Updated"
    DELETED = "Deleted"
    NOTREQUIRED = "NotRequired"
    UNSUPPORTED = "Unsupported"
    FAILED = "Failed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                SipRegistrationDeviceEmergencyInfoSyncStatus._member_map_.values(),
            )
        )


class SipRegistrationDeviceEmergencyInfoAddressEditableStatus(Enum):
    """An enumeration representing different categories.

    :cvar MAINDEVICE: "MainDevice"
    :vartype MAINDEVICE: str
    :cvar ANYDEVICE: "AnyDevice"
    :vartype ANYDEVICE: str
    """

    MAINDEVICE = "MainDevice"
    ANYDEVICE = "AnyDevice"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                SipRegistrationDeviceEmergencyInfoAddressEditableStatus._member_map_.values(),
            )
        )


@JsonMap(
    {
        "out_of_country": "outOfCountry",
        "address_status": "addressStatus",
        "sync_status": "syncStatus",
        "address_editable_status": "addressEditableStatus",
        "address_required": "addressRequired",
        "address_location_only": "addressLocationOnly",
    }
)
class SipRegistrationDeviceEmergencyInfo(BaseModel):
    """Emergency response location settings of a device

    :param address: address, defaults to None
    :type address: Address, optional
    :param location: Company emergency response location details, defaults to None
    :type location: SipRegistrationDeviceLocationInfo, optional
    :param out_of_country: Specifies if emergency address is out of country, defaults to None
    :type out_of_country: bool, optional
    :param address_status: Emergency address status, defaults to None
    :type address_status: SipRegistrationDeviceEmergencyInfoAddressStatus, optional
    :param visibility: Specifies whether to return only private or only public (company) ERLs (Emergency Response Locations) , defaults to None
    :type visibility: SipRegistrationDeviceEmergencyInfoVisibility, optional
    :param sync_status: Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress` parameter is set to `true` , defaults to None
    :type sync_status: SipRegistrationDeviceEmergencyInfoSyncStatus, optional
    :param address_editable_status: Ability to register new emergency address for a phone line using devices sharing this line or only main device (line owner) , defaults to None
    :type address_editable_status: SipRegistrationDeviceEmergencyInfoAddressEditableStatus, optional
    :param address_required: Indicates if emergency address is required for the country of a phone line, defaults to None
    :type address_required: bool, optional
    :param address_location_only: Indicates if out of country emergency address is not allowed for the country of a phone line, defaults to None
    :type address_location_only: bool, optional
    """

    def __init__(
        self,
        address: Address = None,
        location: SipRegistrationDeviceLocationInfo = None,
        out_of_country: bool = None,
        address_status: SipRegistrationDeviceEmergencyInfoAddressStatus = None,
        visibility: SipRegistrationDeviceEmergencyInfoVisibility = None,
        sync_status: SipRegistrationDeviceEmergencyInfoSyncStatus = None,
        address_editable_status: SipRegistrationDeviceEmergencyInfoAddressEditableStatus = None,
        address_required: bool = None,
        address_location_only: bool = None,
    ):
        if address is not None:
            self.address = AddressGuard.return_one_of(address)
        if location is not None:
            self.location = self._define_object(
                location, SipRegistrationDeviceLocationInfo
            )
        if out_of_country is not None:
            self.out_of_country = out_of_country
        if address_status is not None:
            self.address_status = self._enum_matching(
                address_status,
                SipRegistrationDeviceEmergencyInfoAddressStatus.list(),
                "address_status",
            )
        if visibility is not None:
            self.visibility = self._enum_matching(
                visibility,
                SipRegistrationDeviceEmergencyInfoVisibility.list(),
                "visibility",
            )
        if sync_status is not None:
            self.sync_status = self._enum_matching(
                sync_status,
                SipRegistrationDeviceEmergencyInfoSyncStatus.list(),
                "sync_status",
            )
        if address_editable_status is not None:
            self.address_editable_status = self._enum_matching(
                address_editable_status,
                SipRegistrationDeviceEmergencyInfoAddressEditableStatus.list(),
                "address_editable_status",
            )
        if address_required is not None:
            self.address_required = address_required
        if address_location_only is not None:
            self.address_location_only = address_location_only
