# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .switch_site_info import SwitchSiteInfo
from .emergency_address_info import EmergencyAddressInfo, EmergencyAddressInfoGuard
from .emergency_location_info import EmergencyLocationInfo


@JsonMap(
    {
        "chassis_id": "chassisId",
        "emergency_address": "emergencyAddress",
        "emergency_location": "emergencyLocation",
    }
)
class CreateSwitchInfo(BaseModel):
    """CreateSwitchInfo

    :param chassis_id: Unique identifier of a network switch. The supported formats are: XX:XX:XX:XX:XX:XX (symbols 0-9 and A-F) for MAC address and X.X.X.X for IP address (symbols 0-255)
    :type chassis_id: str
    :param port: Switch entity extension for better diversity. Should be used together with chassisId., defaults to None
    :type port: str, optional
    :param name: Name of a network switch, defaults to None
    :type name: str, optional
    :param site: site, defaults to None
    :type site: SwitchSiteInfo, optional
    :param emergency_address: emergency_address, defaults to None
    :type emergency_address: EmergencyAddressInfo, optional
    :param emergency_location: Emergency response location information, defaults to None
    :type emergency_location: EmergencyLocationInfo, optional
    """

    def __init__(
        self,
        chassis_id: str,
        port: str = None,
        name: str = None,
        site: SwitchSiteInfo = None,
        emergency_address: EmergencyAddressInfo = None,
        emergency_location: EmergencyLocationInfo = None,
    ):
        self.chassis_id = chassis_id
        if port is not None:
            self.port = port
        if name is not None:
            self.name = name
        if site is not None:
            self.site = self._define_object(site, SwitchSiteInfo)
        if emergency_address is not None:
            self.emergency_address = EmergencyAddressInfoGuard.return_one_of(
                emergency_address
            )
        if emergency_location is not None:
            self.emergency_location = self._define_object(
                emergency_location, EmergencyLocationInfo
            )
