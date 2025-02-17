# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .switch_validated import SwitchValidated


@JsonMap({})
class ValidateMultipleSwitchesResponse(BaseModel):
    """ValidateMultipleSwitchesResponse

    :param records: records, defaults to None
    :type records: List[SwitchValidated], optional
    """

    def __init__(self, records: List[SwitchValidated] = None):
        if records is not None:
            self.records = self._define_list(records, SwitchValidated)
