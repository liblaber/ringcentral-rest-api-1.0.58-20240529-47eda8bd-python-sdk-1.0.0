# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class ServicePlanInfoFreemiumProductType(Enum):
    """An enumeration representing different categories.

    :cvar FREYJA: "Freyja"
    :vartype FREYJA: str
    :cvar PHOENIX: "Phoenix"
    :vartype PHOENIX: str
    """

    FREYJA = "Freyja"
    PHOENIX = "Phoenix"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                ServicePlanInfoFreemiumProductType._member_map_.values(),
            )
        )


@JsonMap({"id_": "id", "freemium_product_type": "freemiumProductType"})
class ServicePlanInfo(BaseModel):
    """Information on account service plan

    :param id_: Internal identifier of a service plan, defaults to None
    :type id_: str, optional
    :param name: Name of a service plan, defaults to None
    :type name: str, optional
    :param edition: Edition of a service plan, defaults to None
    :type edition: str, optional
    :param freemium_product_type: freemium_product_type, defaults to None
    :type freemium_product_type: ServicePlanInfoFreemiumProductType, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        edition: str = None,
        freemium_product_type: ServicePlanInfoFreemiumProductType = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if edition is not None:
            self.edition = edition
        if freemium_product_type is not None:
            self.freemium_product_type = self._enum_matching(
                freemium_product_type,
                ServicePlanInfoFreemiumProductType.list(),
                "freemium_product_type",
            )
