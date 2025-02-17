# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"preferred_area_code": "preferredAreaCode"})
class PhoneNumberDefinitionPreferredAreaCode(BaseModel):
    """To use as selection hint when a "toll" number to be selected from the number pool.

    :param preferred_area_code: Preferred area code to use if numbers available
    :type preferred_area_code: str
    """

    def __init__(self, preferred_area_code: str):
        self.preferred_area_code = self._pattern_matching(
            preferred_area_code, "^[1-9]\d{1,3}$", "preferred_area_code"
        )
