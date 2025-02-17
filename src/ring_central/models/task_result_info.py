# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .task_result_record import TaskResultRecord


@JsonMap({})
class TaskResultInfo(BaseModel):
    """Task detailed result. Returned for failed and completed tasks

    :param records: Detailed task results by elements from initial request, defaults to None
    :type records: List[TaskResultRecord], optional
    """

    def __init__(self, records: List[TaskResultRecord] = None):
        if records is not None:
            self.records = self._define_list(records, TaskResultRecord)
