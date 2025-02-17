# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .forwarding_number_id import ForwardingNumberId


@JsonMap({})
class DeleteForwardingNumbersRequest(BaseModel):
    """DeleteForwardingNumbersRequest

    :param records: List of forwarding number IDs, defaults to None
    :type records: List[ForwardingNumberId], optional
    """

    def __init__(self, records: List[ForwardingNumberId] = None):
        if records is not None:
            self.records = self._define_list(records, ForwardingNumberId)
