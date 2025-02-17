# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"error_code": "errorCode"})
class RejectedRecipientResponseResource(BaseModel):
    """The rejected recipient details

    :param index: The index of the messages list in the send batch request where the invalid recipient was found, defaults to None
    :type index: int, optional
    :param to: The invalid recipient number as found in the request, defaults to None
    :type to: List[str], optional
    :param error_code: The error code, defaults to None
    :type error_code: str, optional
    :param description: The description of the error, defaults to None
    :type description: str, optional
    """

    def __init__(
        self,
        index: int = None,
        to: List[str] = None,
        error_code: str = None,
        description: str = None,
    ):
        if index is not None:
            self.index = index
        if to is not None:
            self.to = to
        if error_code is not None:
            self.error_code = error_code
        if description is not None:
            self.description = description
