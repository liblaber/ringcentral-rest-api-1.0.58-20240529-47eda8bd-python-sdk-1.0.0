# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "enabled_device_ids": "enabledDeviceIds",
        "disabled_device_ids": "disabledDeviceIds",
    }
)
class AssignMultipleDevicesAutomaticLocationUpdates(BaseModel):
    """AssignMultipleDevicesAutomaticLocationUpdates

    :param enabled_device_ids: enabled_device_ids, defaults to None
    :type enabled_device_ids: List[str], optional
    :param disabled_device_ids: disabled_device_ids, defaults to None
    :type disabled_device_ids: List[str], optional
    """

    def __init__(
        self,
        enabled_device_ids: List[str] = None,
        disabled_device_ids: List[str] = None,
    ):
        if enabled_device_ids is not None:
            self.enabled_device_ids = enabled_device_ids
        if disabled_device_ids is not None:
            self.disabled_device_ids = disabled_device_ids
