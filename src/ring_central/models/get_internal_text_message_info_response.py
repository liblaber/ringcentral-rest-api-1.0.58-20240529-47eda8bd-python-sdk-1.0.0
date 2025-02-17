# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .message_attachment_info import MessageAttachmentInfo
from .message_availability_enum import MessageAvailabilityEnum
from .conversation_info import ConversationInfo
from .message_direction_enum import MessageDirectionEnum
from .message_store_caller_info_response_from import MessageStoreCallerInfoResponseFrom
from .message_status_enum import MessageStatusEnum
from .message_priority_enum import MessagePriorityEnum
from .message_read_status_enum import MessageReadStatusEnum
from .message_store_caller_info_response_to import MessageStoreCallerInfoResponseTo


class GetInternalTextMessageInfoResponseType(Enum):
    """An enumeration representing different categories.

    :cvar FAX: "Fax"
    :vartype FAX: str
    :cvar SMS: "SMS"
    :vartype SMS: str
    :cvar VOICEMAIL: "VoiceMail"
    :vartype VOICEMAIL: str
    :cvar PAGER: "Pager"
    :vartype PAGER: str
    :cvar TEXT: "Text"
    :vartype TEXT: str
    """

    FAX = "Fax"
    SMS = "SMS"
    VOICEMAIL = "VoiceMail"
    PAGER = "Pager"
    TEXT = "Text"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                GetInternalTextMessageInfoResponseType._member_map_.values(),
            )
        )


@JsonMap(
    {
        "id_": "id",
        "conversation_id": "conversationId",
        "creation_time": "creationTime",
        "from_": "from",
        "last_modified_time": "lastModifiedTime",
        "message_status": "messageStatus",
        "pg_to_department": "pgToDepartment",
        "read_status": "readStatus",
        "type_": "type",
    }
)
class GetInternalTextMessageInfoResponse(BaseModel):
    """GetInternalTextMessageInfoResponse

    :param id_: Internal identifier of a message, defaults to None
    :type id_: int, optional
    :param uri: Canonical URI of a message, defaults to None
    :type uri: str, optional
    :param attachments: The list of message attachments, defaults to None
    :type attachments: List[MessageAttachmentInfo], optional
    :param availability: Message availability status. Message in 'Deleted' state is still preserved with all its attachments and can be restored. 'Purged' means that all attachments are already deleted and the message itself is about to be physically deleted shortly , defaults to None
    :type availability: MessageAvailabilityEnum, optional
    :param conversation_id: SMS and Pager only. Identifier of a conversation that the message belongs to , defaults to None
    :type conversation_id: int, optional
    :param conversation: SMS and Pager only. Information about a conversation the message belongs to, defaults to None
    :type conversation: ConversationInfo, optional
    :param creation_time: Message creation date/time in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z , defaults to None
    :type creation_time: str, optional
    :param direction: Text message direction. Note that for some message types not all directions are allowed. For example voicemail messages can be only inbound , defaults to None
    :type direction: MessageDirectionEnum, optional
    :param from_: Sender information, defaults to None
    :type from_: MessageStoreCallerInfoResponseFrom, optional
    :param last_modified_time: Date/time when the message was modified on server in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z , defaults to None
    :type last_modified_time: str, optional
    :param message_status: Message status. Different message types may have different allowed status values. For outbound faxes the aggregated message status is returned. If, for outbound message, a status for at least one recipient is 'Queued', then the 'Queued' value is returned. If a status for at least one recipient is 'SendingFailed', then the 'SendingFailed' value is returned. In other cases the 'Sent' status is returned , defaults to None
    :type message_status: MessageStatusEnum, optional
    :param pg_to_department: Pager only. `true` if at least one of a message recipients is 'Department' extension , defaults to None
    :type pg_to_department: bool, optional
    :param priority: Message priority, defaults to None
    :type priority: MessagePriorityEnum, optional
    :param read_status: Message read status, defaults to None
    :type read_status: MessageReadStatusEnum, optional
    :param subject: Message subject. For SMS and Pager messages it replicates message text which is also returned as an attachment , defaults to None
    :type subject: str, optional
    :param to: Recipient information, defaults to None
    :type to: List[MessageStoreCallerInfoResponseTo], optional
    :param type_: Message type, defaults to None
    :type type_: GetInternalTextMessageInfoResponseType, optional
    """

    def __init__(
        self,
        id_: int = None,
        uri: str = None,
        attachments: List[MessageAttachmentInfo] = None,
        availability: MessageAvailabilityEnum = None,
        conversation_id: int = None,
        conversation: ConversationInfo = None,
        creation_time: str = None,
        direction: MessageDirectionEnum = None,
        from_: MessageStoreCallerInfoResponseFrom = None,
        last_modified_time: str = None,
        message_status: MessageStatusEnum = None,
        pg_to_department: bool = None,
        priority: MessagePriorityEnum = None,
        read_status: MessageReadStatusEnum = None,
        subject: str = None,
        to: List[MessageStoreCallerInfoResponseTo] = None,
        type_: GetInternalTextMessageInfoResponseType = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if uri is not None:
            self.uri = uri
        if attachments is not None:
            self.attachments = self._define_list(attachments, MessageAttachmentInfo)
        if availability is not None:
            self.availability = self._enum_matching(
                availability, MessageAvailabilityEnum.list(), "availability"
            )
        if conversation_id is not None:
            self.conversation_id = conversation_id
        if conversation is not None:
            self.conversation = self._define_object(conversation, ConversationInfo)
        if creation_time is not None:
            self.creation_time = creation_time
        if direction is not None:
            self.direction = self._enum_matching(
                direction, MessageDirectionEnum.list(), "direction"
            )
        if from_ is not None:
            self.from_ = self._define_object(from_, MessageStoreCallerInfoResponseFrom)
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time
        if message_status is not None:
            self.message_status = self._enum_matching(
                message_status, MessageStatusEnum.list(), "message_status"
            )
        if pg_to_department is not None:
            self.pg_to_department = pg_to_department
        if priority is not None:
            self.priority = self._enum_matching(
                priority, MessagePriorityEnum.list(), "priority"
            )
        if read_status is not None:
            self.read_status = self._enum_matching(
                read_status, MessageReadStatusEnum.list(), "read_status"
            )
        if subject is not None:
            self.subject = subject
        if to is not None:
            self.to = self._define_list(to, MessageStoreCallerInfoResponseTo)
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, GetInternalTextMessageInfoResponseType.list(), "type_"
            )
