# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .params_info import ParamsInfo
from .reason_info import ReasonInfo


@JsonMap({"id_": "id"})
class FeatureInfo(BaseModel):
    """FeatureInfo

    :param id_: Internal identifier of a feature, defaults to None
    :type id_: str, optional
    :param available: Specifies if the feature is available for the current user according to services enabled for the account, type, entitlements and permissions of the extension. If the authorized user gets features of the other extension, only features that can be delegated are returned (such as configuration by administrators). , defaults to None
    :type available: bool, optional
    :param params: params, defaults to None
    :type params: List[ParamsInfo], optional
    :param reason: Reason for the feature unavailability. Returned only if `available` is set to `false` , defaults to None
    :type reason: ReasonInfo, optional
    """

    def __init__(
        self,
        id_: str = None,
        available: bool = None,
        params: List[ParamsInfo] = None,
        reason: ReasonInfo = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if available is not None:
            self.available = available
        if params is not None:
            self.params = self._define_list(params, ParamsInfo)
        if reason is not None:
            self.reason = self._define_object(reason, ReasonInfo)
