# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .create_switch_info import CreateSwitchInfo


@JsonMap({})
class CreateMultipleSwitchesRequest(BaseModel):
    """CreateMultipleSwitchesRequest

    :param records: records, defaults to None
    :type records: List[CreateSwitchInfo], optional
    """

    def __init__(self, records: List[CreateSwitchInfo] = None):
        if records is not None:
            self.records = self._define_list(records, CreateSwitchInfo)
