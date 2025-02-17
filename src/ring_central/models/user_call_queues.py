# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .queue_short_info_resource import QueueShortInfoResource


@JsonMap({})
class UserCallQueues(BaseModel):
    """UserCallQueues

    :param records: List of queues where an extension is an agent, defaults to None
    :type records: List[QueueShortInfoResource], optional
    """

    def __init__(self, records: List[QueueShortInfoResource] = None):
        if records is not None:
            self.records = self._define_list(records, QueueShortInfoResource)
