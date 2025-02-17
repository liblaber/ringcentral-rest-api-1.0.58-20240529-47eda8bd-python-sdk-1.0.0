# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .cai_error_code_response import CaiErrorCodeResponse


@JsonMap({})
class CaiErrorResponse(BaseModel):
    """CaiErrorResponse

    :param errors: errors, defaults to None
    :type errors: List[CaiErrorCodeResponse], optional
    """

    def __init__(self, errors: List[CaiErrorCodeResponse] = None):
        if errors is not None:
            self.errors = self._define_list(errors, CaiErrorCodeResponse)
