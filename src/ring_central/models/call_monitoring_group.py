# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class CallMonitoringGroup(BaseModel):
    """CallMonitoringGroup

    :param uri: Link to a call monitoring group resource, defaults to None
    :type uri: str, optional
    :param id_: Internal identifier of a group, defaults to None
    :type id_: str, optional
    :param name: Name of a group, defaults to None
    :type name: str, optional
    """

    def __init__(self, uri: str = None, id_: str = None, name: str = None):
        if uri is not None:
            self.uri = uri
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
