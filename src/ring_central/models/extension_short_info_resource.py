# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "extension_number": "extensionNumber"})
class ExtensionShortInfoResource(BaseModel):
    """ExtensionShortInfoResource

    :param id_: Internal identifier of an extension, defaults to None
    :type id_: str, optional
    :param name: Extension name, defaults to None
    :type name: str, optional
    :param extension_number: Extension number, defaults to None
    :type extension_number: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, extension_number: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if extension_number is not None:
            self.extension_number = extension_number
