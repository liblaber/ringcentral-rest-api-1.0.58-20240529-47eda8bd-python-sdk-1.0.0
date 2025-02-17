# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .tm_attachment_info import TmAttachmentInfo


@JsonMap({})
class TmCreatePostRequest(BaseModel):
    """Post data. At least one attribute should be provided (text or attachments)

    :param text: Text of a post. Maximum length is 10000 symbols. Mentions can be added in .md format `![:Type](id)`, defaults to None
    :type text: str, optional
    :param attachments: Identifier(s) of attachments. Maximum number of attachments is 25, defaults to None
    :type attachments: List[TmAttachmentInfo], optional
    """

    def __init__(self, text: str = None, attachments: List[TmAttachmentInfo] = None):
        if text is not None:
            self.text = text
        if attachments is not None:
            self.attachments = self._define_list(attachments, TmAttachmentInfo)
