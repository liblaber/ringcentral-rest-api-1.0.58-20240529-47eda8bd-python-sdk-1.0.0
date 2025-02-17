# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"extension_number": "extensionNumber"})
class KeyInfo(BaseModel):
    """Additional info about the key

    :param extension_number: Extension's number, defaults to None
    :type extension_number: str, optional
    :param name: Extension's name, defaults to None
    :type name: str, optional
    """

    def __init__(self, extension_number: str = None, name: str = None):
        if extension_number is not None:
            self.extension_number = extension_number
        if name is not None:
            self.name = name
