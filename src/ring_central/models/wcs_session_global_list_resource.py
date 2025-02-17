# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .session_global_list_entry import SessionGlobalListEntry
from .rcw_paging_model import RcwPagingModel


@JsonMap({})
class WcsSessionGlobalListResource(BaseModel):
    """WcsSessionGlobalListResource

    :param records: records
    :type records: List[SessionGlobalListEntry]
    :param paging: paging
    :type paging: RcwPagingModel
    """

    def __init__(self, records: List[SessionGlobalListEntry], paging: RcwPagingModel):
        self.records = self._define_list(records, SessionGlobalListEntry)
        self.paging = self._define_object(paging, RcwPagingModel)
