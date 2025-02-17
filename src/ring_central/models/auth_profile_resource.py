# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .active_permission_resource import ActivePermissionResource


@JsonMap({})
class AuthProfileResource(BaseModel):
    """AuthProfileResource

    :param uri: uri, defaults to None
    :type uri: str, optional
    :param permissions: permissions, defaults to None
    :type permissions: List[ActivePermissionResource], optional
    """

    def __init__(
        self, uri: str = None, permissions: List[ActivePermissionResource] = None
    ):
        if uri is not None:
            self.uri = uri
        if permissions is not None:
            self.permissions = self._define_list(permissions, ActivePermissionResource)
