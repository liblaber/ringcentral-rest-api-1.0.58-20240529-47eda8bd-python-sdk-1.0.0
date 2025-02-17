# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .cloud_recording import CloudRecording
from .paging import Paging


@JsonMap({})
class CloudRecordings(BaseModel):
    """Recordings page

    :param recordings: Recordings array
    :type recordings: List[CloudRecording]
    :param paging: Paging information
    :type paging: Paging
    """

    def __init__(self, recordings: List[CloudRecording], paging: Paging):
        self.recordings = self._define_list(recordings, CloudRecording)
        self.paging = self._define_object(paging, Paging)
