# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "phone_number": "phoneNumber"})
class AutomaticLocationUpdatesPhoneNumberInfo(BaseModel):
    """AutomaticLocationUpdatesPhoneNumberInfo

    :param id_: Internal identifier of a phone number, defaults to None
    :type id_: int, optional
    :param phone_number: Phone number, defaults to None
    :type phone_number: str, optional
    """

    def __init__(self, id_: int = None, phone_number: str = None):
        if id_ is not None:
            self.id_ = id_
        if phone_number is not None:
            self.phone_number = phone_number
