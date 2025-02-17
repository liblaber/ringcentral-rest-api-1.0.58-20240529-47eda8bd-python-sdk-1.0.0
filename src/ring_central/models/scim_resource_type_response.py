# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .scim_schema_extension import ScimSchemaExtension
from .scim_meta import ScimMeta


class ScimResourceTypeResponseSchema(Enum):
    """An enumeration representing different categories.

    :cvar URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_USER: "urn:ietf:params:scim:schemas:core:2.0:User"
    :vartype URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_USER: str
    """

    URN_IETF_PARAMS_SCIM_SCHEMAS_CORE_2_0_USER = (
        "urn:ietf:params:scim:schemas:core:2.0:User"
    )

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ScimResourceTypeResponseSchema._member_map_.values())
        )


@JsonMap({"id_": "id", "schema_extensions": "schemaExtensions"})
class ScimResourceTypeResponse(BaseModel):
    """ScimResourceTypeResponse

    :param id_: Unique resource type ID, same value as the "name" attribute, defaults to None
    :type id_: str, optional
    :param name: Resource type name
    :type name: str
    :param endpoint: The resource type's HTTP-addressable endpoint
    :type endpoint: str
    :param description: Description of the resource type, defaults to None
    :type description: str, optional
    :param schema: schema
    :type schema: ScimResourceTypeResponseSchema
    :param schema_extensions: schema_extensions, defaults to None
    :type schema_extensions: List[ScimSchemaExtension], optional
    :param meta: Resource metadata, defaults to None
    :type meta: ScimMeta, optional
    """

    def __init__(
        self,
        name: str,
        endpoint: str,
        schema: ScimResourceTypeResponseSchema,
        id_: str = None,
        description: str = None,
        schema_extensions: List[ScimSchemaExtension] = None,
        meta: ScimMeta = None,
    ):
        if id_ is not None:
            self.id_ = id_
        self.name = name
        self.endpoint = endpoint
        if description is not None:
            self.description = description
        self.schema = self._enum_matching(
            schema, ScimResourceTypeResponseSchema.list(), "schema"
        )
        if schema_extensions is not None:
            self.schema_extensions = self._define_list(
                schema_extensions, ScimSchemaExtension
            )
        if meta is not None:
            self.meta = self._define_object(meta, ScimMeta)
