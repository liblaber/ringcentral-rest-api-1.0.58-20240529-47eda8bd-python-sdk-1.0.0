# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"min_seconds": "minSeconds", "max_seconds": "maxSeconds"})
class CallSegmentLengthFilter(BaseModel):
    """Duration bounds for the segment

    :param min_seconds: Minimum duration of segment in seconds, defaults to None
    :type min_seconds: int, optional
    :param max_seconds: Maximum duration of segment in seconds, defaults to None
    :type max_seconds: int, optional
    """

    def __init__(self, min_seconds: int = None, max_seconds: int = None):
        if min_seconds is not None:
            self.min_seconds = min_seconds
        if max_seconds is not None:
            self.max_seconds = max_seconds
