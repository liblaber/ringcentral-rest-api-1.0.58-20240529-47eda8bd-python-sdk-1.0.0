# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "extension_number": "extensionNumber"})
class CallQueueMemberInfo(BaseModel):
    """CallQueueMemberInfo

    :param uri: Link to a call queue member, defaults to None
    :type uri: str, optional
    :param id_: Internal identifier of a call queue member, defaults to None
    :type id_: int, optional
    :param extension_number: Extension number of a call queue member, defaults to None
    :type extension_number: str, optional
    """

    def __init__(self, uri: str = None, id_: int = None, extension_number: str = None):
        if uri is not None:
            self.uri = uri
        if id_ is not None:
            self.id_ = id_
        if extension_number is not None:
            self.extension_number = extension_number
