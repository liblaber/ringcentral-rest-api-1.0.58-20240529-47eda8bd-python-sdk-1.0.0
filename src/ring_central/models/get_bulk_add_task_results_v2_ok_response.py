# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .add_phone_numbers_response import AddPhoneNumbersResponse
from .add_phone_numbers_task import AddPhoneNumbersTask


class GetBulkAddTaskResultsV2OkResponseGuard(OneOfBaseModel):
    class_list = {
        "AddPhoneNumbersResponse": AddPhoneNumbersResponse,
        "AddPhoneNumbersTask": AddPhoneNumbersTask,
    }


GetBulkAddTaskResultsV2OkResponse = Union[AddPhoneNumbersResponse, AddPhoneNumbersTask]
