# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"speaker_id": "speakerId"})
class DiarizeSegment(BaseModel):
    """DiarizeSegment

    :param speaker_id: speaker_id
    :type speaker_id: str
    :param start: start
    :type start: float
    :param end: end
    :type end: float
    :param confidence: confidence, defaults to None
    :type confidence: float, optional
    """

    def __init__(
        self, speaker_id: str, start: float, end: float, confidence: float = None
    ):
        self.speaker_id = speaker_id
        self.start = start
        self.end = end
        if confidence is not None:
            self.confidence = confidence
