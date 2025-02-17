# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .call_queue_id import CallQueueId


@JsonMap({"call_queue": "callQueue", "accept_calls": "acceptCalls"})
class ExtensionCallQueueUpdatePresence(BaseModel):
    """ExtensionCallQueueUpdatePresence

    :param call_queue: Call queue information, defaults to None
    :type call_queue: CallQueueId, optional
    :param accept_calls: Call queue agent availability for calls of this queue, defaults to None
    :type accept_calls: bool, optional
    """

    def __init__(self, call_queue: CallQueueId = None, accept_calls: bool = None):
        if call_queue is not None:
            self.call_queue = self._define_object(call_queue, CallQueueId)
        if accept_calls is not None:
            self.accept_calls = accept_calls
