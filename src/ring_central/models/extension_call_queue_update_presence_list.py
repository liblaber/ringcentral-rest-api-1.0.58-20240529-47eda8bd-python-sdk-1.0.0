# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .extension_call_queue_update_presence import ExtensionCallQueueUpdatePresence


@JsonMap({})
class ExtensionCallQueueUpdatePresenceList(BaseModel):
    """ExtensionCallQueueUpdatePresenceList

    :param records: records, defaults to None
    :type records: List[ExtensionCallQueueUpdatePresence], optional
    """

    def __init__(self, records: List[ExtensionCallQueueUpdatePresence] = None):
        if records is not None:
            self.records = self._define_list(records, ExtensionCallQueueUpdatePresence)
