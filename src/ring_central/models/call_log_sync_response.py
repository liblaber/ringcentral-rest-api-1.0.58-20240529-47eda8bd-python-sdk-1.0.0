# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .call_log_record import CallLogRecord
from .call_log_sync_info import CallLogSyncInfo


@JsonMap({"sync_info": "syncInfo"})
class CallLogSyncResponse(BaseModel):
    """CallLogSyncResponse

    :param uri: Link to the list of call log records with sync information
    :type uri: str
    :param records: List of call log records with synchronization information. For `ISync` the total number of returned records is limited to 250; this includes both new records and the old ones, specified by the recordCount parameter
    :type records: List[CallLogRecord]
    :param sync_info: sync_info
    :type sync_info: CallLogSyncInfo
    """

    def __init__(
        self, uri: str, records: List[CallLogRecord], sync_info: CallLogSyncInfo
    ):
        self.uri = uri
        self.records = self._define_list(records, CallLogRecord)
        self.sync_info = self._define_object(sync_info, CallLogSyncInfo)
