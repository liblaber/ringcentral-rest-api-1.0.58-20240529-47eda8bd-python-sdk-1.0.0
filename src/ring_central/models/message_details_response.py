# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .sms_status_enum import SmsStatusEnum
from .sms_direction_enum import SmsDirectionEnum


@JsonMap(
    {
        "id_": "id",
        "from_": "from",
        "creation_time": "creationTime",
        "last_modified_time": "lastModifiedTime",
        "message_status": "messageStatus",
        "segment_count": "segmentCount",
        "batch_id": "batchId",
        "error_code": "errorCode",
    }
)
class MessageDetailsResponse(BaseModel):
    """Complete details of the message

    :param id_: Internal identifier of a message, defaults to None
    :type id_: str, optional
    :param from_: Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format from which the message was sent, defaults to None
    :type from_: str, optional
    :param to: List of phone numbers in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format to which the message was sent, defaults to None
    :type to: List[str], optional
    :param text: Text of a message, maximum number of characters is 1000, defaults to None
    :type text: str, optional
    :param creation_time: The time when this is message was created., defaults to None
    :type creation_time: str, optional
    :param last_modified_time: The time when this message was last updated., defaults to None
    :type last_modified_time: str, optional
    :param message_status: Current status of a message, defaults to None
    :type message_status: SmsStatusEnum, optional
    :param segment_count: Number of segments of a message, defaults to None
    :type segment_count: int, optional
    :param cost: Cost of a message, defaults to None
    :type cost: float, optional
    :param batch_id: The batch in which the message was submitted, defaults to None
    :type batch_id: str, optional
    :param direction: Direction of the SMS message, defaults to None
    :type direction: SmsDirectionEnum, optional
    :param error_code: The RC error code of the message sending failure reason, defaults to None
    :type error_code: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        from_: str = None,
        to: List[str] = None,
        text: str = None,
        creation_time: str = None,
        last_modified_time: str = None,
        message_status: SmsStatusEnum = None,
        segment_count: int = None,
        cost: float = None,
        batch_id: str = None,
        direction: SmsDirectionEnum = None,
        error_code: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if from_ is not None:
            self.from_ = from_
        if to is not None:
            self.to = to
        if text is not None:
            self.text = text
        if creation_time is not None:
            self.creation_time = creation_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if message_status is not None:
            self.message_status = self._enum_matching(
                message_status, SmsStatusEnum.list(), "message_status"
            )
        if segment_count is not None:
            self.segment_count = segment_count
        if cost is not None:
            self.cost = cost
        if batch_id is not None:
            self.batch_id = batch_id
        if direction is not None:
            self.direction = self._enum_matching(
                direction, SmsDirectionEnum.list(), "direction"
            )
        if error_code is not None:
            self.error_code = error_code
