# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "bulk_item_successful": "bulkItemSuccessful",
        "bulk_item_errors": "bulkItemErrors",
        "id_": "id",
        "phone_number": "phoneNumber",
    }
)
class DeletePhoneNumbersResponseItem(BaseModel):
    """DeletePhoneNumbersResponseItem

    :param bulk_item_successful: Indicates if this item was processed successfully during bulk operation. If false, `bulkItemErrors` attribute contains the list of errors
    :type bulk_item_successful: bool
    :param bulk_item_errors: The list of errors occurred during processing of particular item of bulk operation. Returned only if `bulkItemSuccessful` is false , defaults to None
    :type bulk_item_errors: List[dict], optional
    :param id_: Internal unique identifier of a phone number, defaults to None
    :type id_: str, optional
    :param phone_number: Phone number in e.164 format (with '+' prefix), defaults to None
    :type phone_number: str, optional
    """

    def __init__(
        self,
        bulk_item_successful: bool,
        bulk_item_errors: List[dict] = None,
        id_: str = None,
        phone_number: str = None,
    ):
        self.bulk_item_successful = bulk_item_successful
        if bulk_item_errors is not None:
            self.bulk_item_errors = bulk_item_errors
        if id_ is not None:
            self.id_ = self._pattern_matching(id_, "^[1-9]\d{1,14}$", "id_")
        if phone_number is not None:
            self.phone_number = self._pattern_matching(
                phone_number, "^\+[1-9]\d{1,14}$", "phone_number"
            )
