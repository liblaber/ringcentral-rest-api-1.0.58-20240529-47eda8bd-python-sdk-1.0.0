# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .call_queue_member_id import CallQueueMemberId


@JsonMap({"accept_current_queue_calls": "acceptCurrentQueueCalls"})
class CallQueueUpdateMemberPresence(BaseModel):
    """CallQueueUpdateMemberPresence

    :param member: Call queue member information, defaults to None
    :type member: CallQueueMemberId, optional
    :param accept_current_queue_calls: Call queue member availability for calls of this queue, defaults to None
    :type accept_current_queue_calls: bool, optional
    """

    def __init__(
        self, member: CallQueueMemberId = None, accept_current_queue_calls: bool = None
    ):
        if member is not None:
            self.member = self._define_object(member, CallQueueMemberId)
        if accept_current_queue_calls is not None:
            self.accept_current_queue_calls = accept_current_queue_calls
