# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .address_book_bulk_upload_resource import AddressBookBulkUploadResource
from .error_entity import ErrorEntity


@JsonMap({"affected_items": "affectedItems"})
class AddressBookBulkUploadTaskResult(BaseModel):
    """AddressBookBulkUploadTaskResult

    :param affected_items: affected_items, defaults to None
    :type affected_items: List[AddressBookBulkUploadResource], optional
    :param errors: errors, defaults to None
    :type errors: List[ErrorEntity], optional
    """

    def __init__(
        self,
        affected_items: List[AddressBookBulkUploadResource] = None,
        errors: List[ErrorEntity] = None,
    ):
        if affected_items is not None:
            self.affected_items = self._define_list(
                affected_items, AddressBookBulkUploadResource
            )
        if errors is not None:
            self.errors = self._define_list(errors, ErrorEntity)
