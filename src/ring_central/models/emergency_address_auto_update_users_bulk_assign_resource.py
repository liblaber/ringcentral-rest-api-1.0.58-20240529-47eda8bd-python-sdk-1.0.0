# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"enabled_user_ids": "enabledUserIds", "disabled_user_ids": "disabledUserIds"})
class EmergencyAddressAutoUpdateUsersBulkAssignResource(BaseModel):
    """EmergencyAddressAutoUpdateUsersBulkAssignResource

    :param enabled_user_ids: enabled_user_ids, defaults to None
    :type enabled_user_ids: List[str], optional
    :param disabled_user_ids: disabled_user_ids, defaults to None
    :type disabled_user_ids: List[str], optional
    """

    def __init__(
        self, enabled_user_ids: List[str] = None, disabled_user_ids: List[str] = None
    ):
        if enabled_user_ids is not None:
            self.enabled_user_ids = enabled_user_ids
        if disabled_user_ids is not None:
            self.disabled_user_ids = disabled_user_ids
