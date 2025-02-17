# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class DisabledFilterInfo(BaseModel):
    """DisabledFilterInfo

    :param filter: Event filter that is disabled for the user
    :type filter: str
    :param reason: Reason why the filter is disabled for the user
    :type reason: str
    :param message: Error message, defaults to None
    :type message: str, optional
    """

    def __init__(self, filter: str, reason: str, message: str = None):
        self.filter = filter
        self.reason = reason
        if message is not None:
            self.message = message
