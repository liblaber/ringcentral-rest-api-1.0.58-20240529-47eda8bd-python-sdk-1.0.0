# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .custom_field_model import CustomFieldModel


@JsonMap({})
class CustomFieldList(BaseModel):
    """CustomFieldList

    :param records: records, defaults to None
    :type records: List[CustomFieldModel], optional
    """

    def __init__(self, records: List[CustomFieldModel] = None):
        if records is not None:
            self.records = self._define_list(records, CustomFieldModel)
