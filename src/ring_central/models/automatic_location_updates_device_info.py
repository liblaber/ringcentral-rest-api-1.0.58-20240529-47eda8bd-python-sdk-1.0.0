# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .automatic_location_updates_device_type import AutomaticLocationUpdatesDeviceType
from .automatic_location_updates_model_info import AutomaticLocationUpdatesModelInfo
from .automatic_location_updates_site_info import AutomaticLocationUpdatesSiteInfo
from .automatic_location_updates_phone_line import AutomaticLocationUpdatesPhoneLine


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "feature_enabled": "featureEnabled",
        "phone_lines": "phoneLines",
    }
)
class AutomaticLocationUpdatesDeviceInfo(BaseModel):
    """AutomaticLocationUpdatesDeviceInfo

    :param id_: Internal identifier of a device, defaults to None
    :type id_: str, optional
    :param type_: Device type, defaults to None
    :type type_: AutomaticLocationUpdatesDeviceType, optional
    :param serial: Serial number for HardPhone (is returned only when the phone is shipped and provisioned), defaults to None
    :type serial: str, optional
    :param feature_enabled: Specifies if Automatic Location Updates feature is enabled, defaults to None
    :type feature_enabled: bool, optional
    :param name: Device name, defaults to None
    :type name: str, optional
    :param model: HardPhone model information, defaults to None
    :type model: AutomaticLocationUpdatesModelInfo, optional
    :param site: Site data. If multi-site feature is turned on for the account, then ID of a site must be specified. In order to assign a wireless point to the main site (company) site ID should be set to `main-site` , defaults to None
    :type site: AutomaticLocationUpdatesSiteInfo, optional
    :param phone_lines: Phone lines information, defaults to None
    :type phone_lines: List[AutomaticLocationUpdatesPhoneLine], optional
    """

    def __init__(
        self,
        id_: str = None,
        type_: AutomaticLocationUpdatesDeviceType = None,
        serial: str = None,
        feature_enabled: bool = None,
        name: str = None,
        model: AutomaticLocationUpdatesModelInfo = None,
        site: AutomaticLocationUpdatesSiteInfo = None,
        phone_lines: List[AutomaticLocationUpdatesPhoneLine] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, AutomaticLocationUpdatesDeviceType.list(), "type_"
            )
        if serial is not None:
            self.serial = serial
        if feature_enabled is not None:
            self.feature_enabled = feature_enabled
        if name is not None:
            self.name = name
        if model is not None:
            self.model = self._define_object(model, AutomaticLocationUpdatesModelInfo)
        if site is not None:
            self.site = self._define_object(site, AutomaticLocationUpdatesSiteInfo)
        if phone_lines is not None:
            self.phone_lines = self._define_list(
                phone_lines, AutomaticLocationUpdatesPhoneLine
            )
