# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "site_restricted": "siteRestricted",
        "site_compatible": "siteCompatible",
        "added_extension_ids": "addedExtensionIds",
        "removed_extension_ids": "removedExtensionIds",
    }
)
class BulkRoleAssignResource(BaseModel):
    """BulkRoleAssignResource

    :param site_restricted: site_restricted, defaults to None
    :type site_restricted: bool, optional
    :param site_compatible: site_compatible, defaults to None
    :type site_compatible: bool, optional
    :param uri: uri, defaults to None
    :type uri: str, optional
    :param added_extension_ids: added_extension_ids, defaults to None
    :type added_extension_ids: List[str], optional
    :param removed_extension_ids: removed_extension_ids, defaults to None
    :type removed_extension_ids: List[str], optional
    """

    def __init__(
        self,
        site_restricted: bool = None,
        site_compatible: bool = None,
        uri: str = None,
        added_extension_ids: List[str] = None,
        removed_extension_ids: List[str] = None,
    ):
        if site_restricted is not None:
            self.site_restricted = site_restricted
        if site_compatible is not None:
            self.site_compatible = site_compatible
        if uri is not None:
            self.uri = uri
        if added_extension_ids is not None:
            self.added_extension_ids = added_extension_ids
        if removed_extension_ids is not None:
            self.removed_extension_ids = removed_extension_ids
