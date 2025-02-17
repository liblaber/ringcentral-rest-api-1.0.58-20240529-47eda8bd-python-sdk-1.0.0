# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class CustomFieldCreateRequestCategory(Enum):
    """An enumeration representing different categories.

    :cvar USER: "User"
    :vartype USER: str
    """

    USER = "User"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                CustomFieldCreateRequestCategory._member_map_.values(),
            )
        )


@JsonMap({"display_name": "displayName"})
class CustomFieldCreateRequest(BaseModel):
    """CustomFieldCreateRequest

    :param category: Object category to attach custom fields, defaults to None
    :type category: CustomFieldCreateRequestCategory, optional
    :param display_name: Custom field display name, defaults to None
    :type display_name: str, optional
    """

    def __init__(
        self,
        category: CustomFieldCreateRequestCategory = None,
        display_name: str = None,
    ):
        if category is not None:
            self.category = self._enum_matching(
                category, CustomFieldCreateRequestCategory.list(), "category"
            )
        if display_name is not None:
            self.display_name = display_name
