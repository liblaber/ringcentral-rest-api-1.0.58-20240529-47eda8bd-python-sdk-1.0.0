# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .speaker_insights_unit import SpeakerInsightsUnit


@JsonMap({"speaker_count": "speakerCount"})
class SpeakerInsightsObject(BaseModel):
    """SpeakerInsightsObject

    :param speaker_count: speaker_count, defaults to None
    :type speaker_count: int, optional
    :param insights: insights, defaults to None
    :type insights: List[SpeakerInsightsUnit], optional
    """

    def __init__(
        self, speaker_count: int = None, insights: List[SpeakerInsightsUnit] = None
    ):
        if speaker_count is not None:
            self.speaker_count = speaker_count
        if insights is not None:
            self.insights = self._define_list(insights, SpeakerInsightsUnit)
