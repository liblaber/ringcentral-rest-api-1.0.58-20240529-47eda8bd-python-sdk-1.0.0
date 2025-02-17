# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .template_info import TemplateInfo
from .visibility_type import VisibilityType
from .site import Site


@JsonMap({"id_": "id", "display_name": "displayName"})
class MessageTemplateResponse(BaseModel):
    """MessageTemplateResponse

    :param id_: Internal identifier of a template, defaults to None
    :type id_: str, optional
    :param display_name: Name of a template, defaults to None
    :type display_name: str, optional
    :param body: Text message template information, defaults to None
    :type body: TemplateInfo, optional
    :param scope: Specifies if a template is available on a user (Personal) or a company (Company) level, defaults to None
    :type scope: VisibilityType, optional
    :param site: Specifies a site that message template is associated with. Supported only if the Sites feature is enabled.  The default is `main-site` value. , defaults to None
    :type site: Site, optional
    """

    def __init__(
        self,
        id_: str = None,
        display_name: str = None,
        body: TemplateInfo = None,
        scope: VisibilityType = None,
        site: Site = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if display_name is not None:
            self.display_name = display_name
        if body is not None:
            self.body = self._define_object(body, TemplateInfo)
        if scope is not None:
            self.scope = self._enum_matching(scope, VisibilityType.list(), "scope")
        if site is not None:
            self.site = self._define_object(site, Site)
