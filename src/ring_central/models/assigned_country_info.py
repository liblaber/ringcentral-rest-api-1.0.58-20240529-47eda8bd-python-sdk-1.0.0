# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "iso_code": "isoCode"})
class AssignedCountryInfo(BaseModel):
    """Information on a country assigned to an extension user. Returned for the User extension type only

    :param id_: Internal identifier of an assigned country, defaults to None
    :type id_: str, optional
    :param uri: Canonical URI of an assigned country resource, defaults to None
    :type uri: str, optional
    :param iso_code: Country code according to the ISO standard, see [ISO 3166](https://www.iso.org/iso-3166-country-codes.html), defaults to None
    :type iso_code: str, optional
    :param name: Official name of a country, defaults to None
    :type name: str, optional
    """

    def __init__(
        self, id_: str = None, uri: str = None, iso_code: str = None, name: str = None
    ):
        if id_ is not None:
            self.id_ = id_
        if uri is not None:
            self.uri = uri
        if iso_code is not None:
            self.iso_code = iso_code
        if name is not None:
            self.name = name
