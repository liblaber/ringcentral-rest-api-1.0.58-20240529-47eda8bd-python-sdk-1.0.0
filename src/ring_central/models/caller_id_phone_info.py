# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "phone_number": "phoneNumber"})
class CallerIdPhoneInfo(BaseModel):
    """CallerIdPhoneInfo

    :param id_: Internal identifier of a phone number, defaults to None
    :type id_: str, optional
    :param uri: Link to a phone number resource, defaults to None
    :type uri: str, optional
    :param phone_number: Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (with '+' sign) format , defaults to None
    :type phone_number: str, optional
    """

    def __init__(self, id_: str = None, uri: str = None, phone_number: str = None):
        if id_ is not None:
            self.id_ = id_
        if uri is not None:
            self.uri = uri
        if phone_number is not None:
            self.phone_number = phone_number
