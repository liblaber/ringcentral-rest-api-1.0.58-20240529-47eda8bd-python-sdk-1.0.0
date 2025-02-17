# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .fixed_order_agents_extension_info import FixedOrderAgentsExtensionInfo


@JsonMap({})
class FixedOrderAgents(BaseModel):
    """FixedOrderAgents

    :param extension: extension, defaults to None
    :type extension: FixedOrderAgentsExtensionInfo, optional
    :param index: Ordinal of an agent (call queue member), defaults to None
    :type index: int, optional
    """

    def __init__(
        self, extension: FixedOrderAgentsExtensionInfo = None, index: int = None
    ):
        if extension is not None:
            self.extension = self._define_object(
                extension, FixedOrderAgentsExtensionInfo
            )
        if index is not None:
            self.index = index
