# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .meeting_info import MeetingInfo
from .meeting_recording_info import MeetingRecordingInfo


@JsonMap({})
class MeetingRecordings(BaseModel):
    """MeetingRecordings

    :param meeting: meeting, defaults to None
    :type meeting: MeetingInfo, optional
    :param recordings: recordings, defaults to None
    :type recordings: List[MeetingRecordingInfo], optional
    """

    def __init__(
        self, meeting: MeetingInfo = None, recordings: List[MeetingRecordingInfo] = None
    ):
        if meeting is not None:
            self.meeting = self._define_object(meeting, MeetingInfo)
        if recordings is not None:
            self.recordings = self._define_list(recordings, MeetingRecordingInfo)
