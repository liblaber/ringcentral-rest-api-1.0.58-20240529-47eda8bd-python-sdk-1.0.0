# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class ScimUserAddressType(Enum):
    """An enumeration representing different categories.

    :cvar WORK: "work"
    :vartype WORK: str
    """

    WORK = "work"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ScimUserAddressType._member_map_.values()))


@JsonMap(
    {"postal_code": "postalCode", "street_address": "streetAddress", "type_": "type"}
)
class ScimUserAddress(BaseModel):
    """ScimUserAddress

    :param country: country, defaults to None
    :type country: str, optional
    :param locality: locality, defaults to None
    :type locality: str, optional
    :param postal_code: postal_code, defaults to None
    :type postal_code: str, optional
    :param region: region, defaults to None
    :type region: str, optional
    :param street_address: street_address, defaults to None
    :type street_address: str, optional
    :param type_: type_
    :type type_: ScimUserAddressType
    """

    def __init__(
        self,
        type_: ScimUserAddressType,
        country: str = None,
        locality: str = None,
        postal_code: str = None,
        region: str = None,
        street_address: str = None,
    ):
        if country is not None:
            self.country = country
        if locality is not None:
            self.locality = locality
        if postal_code is not None:
            self.postal_code = postal_code
        if region is not None:
            self.region = region
        if street_address is not None:
            self.street_address = street_address
        self.type_ = self._enum_matching(type_, ScimUserAddressType.list(), "type_")
