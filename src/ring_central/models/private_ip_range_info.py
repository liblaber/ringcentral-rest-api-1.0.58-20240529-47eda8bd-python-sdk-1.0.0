# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .common_emergency_location_address_info import (
    CommonEmergencyLocationAddressInfo,
    CommonEmergencyLocationAddressInfoGuard,
)
from .common_emergency_location_address_info_default import (
    CommonEmergencyLocationAddressInfoDefault,
)
from .common_emergency_location_address_info_au import (
    CommonEmergencyLocationAddressInfoAu,
)
from .common_emergency_location_address_info_fr import (
    CommonEmergencyLocationAddressInfoFr,
)
from .emergency_location_info import EmergencyLocationInfo


@JsonMap(
    {
        "id_": "id",
        "start_ip": "startIp",
        "end_ip": "endIp",
        "emergency_address": "emergencyAddress",
        "emergency_location_id": "emergencyLocationId",
        "emergency_location": "emergencyLocation",
    }
)
class PrivateIpRangeInfo(BaseModel):
    """PrivateIpRangeInfo

    :param id_: id_, defaults to None
    :type id_: str, optional
    :param start_ip: start_ip, defaults to None
    :type start_ip: str, optional
    :param end_ip: end_ip, defaults to None
    :type end_ip: str, optional
    :param name: Network name, defaults to None
    :type name: str, optional
    :param emergency_address: emergency_address, defaults to None
    :type emergency_address: CommonEmergencyLocationAddressInfo, optional
    :param emergency_location_id: Emergency response location (address) internal identifier. Only one of a pair `emergencyAddress` or `emergencyLocationId` should be specified, otherwise an error is returned , defaults to None
    :type emergency_location_id: str, optional
    :param matched: matched, defaults to None
    :type matched: bool, optional
    :param emergency_location: Emergency response location information, defaults to None
    :type emergency_location: EmergencyLocationInfo, optional
    """

    def __init__(
        self,
        id_: str = None,
        start_ip: str = None,
        end_ip: str = None,
        name: str = None,
        emergency_address: CommonEmergencyLocationAddressInfo = None,
        emergency_location_id: str = None,
        matched: bool = None,
        emergency_location: EmergencyLocationInfo = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if start_ip is not None:
            self.start_ip = start_ip
        if end_ip is not None:
            self.end_ip = end_ip
        if name is not None:
            self.name = name
        if emergency_address is not None:
            self.emergency_address = (
                CommonEmergencyLocationAddressInfoGuard.return_one_of(emergency_address)
            )
        if emergency_location_id is not None:
            self.emergency_location_id = emergency_location_id
        if matched is not None:
            self.matched = matched
        if emergency_location is not None:
            self.emergency_location = self._define_object(
                emergency_location, EmergencyLocationInfo
            )
