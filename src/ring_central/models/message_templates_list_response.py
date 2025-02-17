# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .message_template_response import MessageTemplateResponse


@JsonMap({})
class MessageTemplatesListResponse(BaseModel):
    """MessageTemplatesListResponse

    :param records: List of text message templates, defaults to None
    :type records: List[MessageTemplateResponse], optional
    """

    def __init__(self, records: List[MessageTemplateResponse] = None):
        if records is not None:
            self.records = self._define_list(records, MessageTemplateResponse)
