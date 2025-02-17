# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .glip_data_export_navigation_info_uri import GlipDataExportNavigationInfoUri


@JsonMap(
    {
        "first_page": "firstPage",
        "next_page": "nextPage",
        "previous_page": "previousPage",
        "last_page": "lastPage",
    }
)
class GlipDataExportNavigationInfo(BaseModel):
    """GlipDataExportNavigationInfo

    :param first_page: first_page, defaults to None
    :type first_page: GlipDataExportNavigationInfoUri, optional
    :param next_page: next_page, defaults to None
    :type next_page: GlipDataExportNavigationInfoUri, optional
    :param previous_page: previous_page, defaults to None
    :type previous_page: GlipDataExportNavigationInfoUri, optional
    :param last_page: last_page, defaults to None
    :type last_page: GlipDataExportNavigationInfoUri, optional
    """

    def __init__(
        self,
        first_page: GlipDataExportNavigationInfoUri = None,
        next_page: GlipDataExportNavigationInfoUri = None,
        previous_page: GlipDataExportNavigationInfoUri = None,
        last_page: GlipDataExportNavigationInfoUri = None,
    ):
        if first_page is not None:
            self.first_page = self._define_object(
                first_page, GlipDataExportNavigationInfoUri
            )
        if next_page is not None:
            self.next_page = self._define_object(
                next_page, GlipDataExportNavigationInfoUri
            )
        if previous_page is not None:
            self.previous_page = self._define_object(
                previous_page, GlipDataExportNavigationInfoUri
            )
        if last_page is not None:
            self.last_page = self._define_object(
                last_page, GlipDataExportNavigationInfoUri
            )
