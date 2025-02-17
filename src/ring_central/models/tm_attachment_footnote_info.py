# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"icon_uri": "iconUri"})
class TmAttachmentFootnoteInfo(BaseModel):
    """TmAttachmentFootnoteInfo

    :param text: Text of a footer, defaults to None
    :type text: str, optional
    :param icon_uri: Link to an icon displayed to the left of a footer; sized 32x32px, defaults to None
    :type icon_uri: str, optional
    :param time: Message creation datetime in ISO 8601 format including timezone, defaults to None
    :type time: str, optional
    """

    def __init__(self, text: str = None, icon_uri: str = None, time: str = None):
        if text is not None:
            self.text = text
        if icon_uri is not None:
            self.icon_uri = icon_uri
        if time is not None:
            self.time = time
