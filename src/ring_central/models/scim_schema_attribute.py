# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class ScimSchemaAttributeType(Enum):
    """An enumeration representing different categories.

    :cvar STRING: "string"
    :vartype STRING: str
    :cvar BOOLEAN: "boolean"
    :vartype BOOLEAN: str
    :cvar DECIMAL: "decimal"
    :vartype DECIMAL: str
    :cvar INTEGER: "integer"
    :vartype INTEGER: str
    :cvar DATETIME: "dateTime"
    :vartype DATETIME: str
    :cvar REFERENCE: "reference"
    :vartype REFERENCE: str
    :cvar COMPLEX: "complex"
    :vartype COMPLEX: str
    """

    STRING = "string"
    BOOLEAN = "boolean"
    DECIMAL = "decimal"
    INTEGER = "integer"
    DATETIME = "dateTime"
    REFERENCE = "reference"
    COMPLEX = "complex"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ScimSchemaAttributeType._member_map_.values())
        )


class Mutability(Enum):
    """An enumeration representing different categories.

    :cvar READONLY: "readOnly"
    :vartype READONLY: str
    :cvar READWRITE: "readWrite"
    :vartype READWRITE: str
    :cvar IMMUTABLE: "immutable"
    :vartype IMMUTABLE: str
    :cvar WRITEONLY: "writeOnly"
    :vartype WRITEONLY: str
    """

    READONLY = "readOnly"
    READWRITE = "readWrite"
    IMMUTABLE = "immutable"
    WRITEONLY = "writeOnly"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Mutability._member_map_.values()))


class Returned(Enum):
    """An enumeration representing different categories.

    :cvar ALWAYS: "always"
    :vartype ALWAYS: str
    :cvar NEVER: "never"
    :vartype NEVER: str
    :cvar DEFAULT: "default"
    :vartype DEFAULT: str
    :cvar REQUEST: "request"
    :vartype REQUEST: str
    """

    ALWAYS = "always"
    NEVER = "never"
    DEFAULT = "default"
    REQUEST = "request"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Returned._member_map_.values()))


class Uniqueness(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "none"
    :vartype NONE: str
    :cvar SERVER: "server"
    :vartype SERVER: str
    :cvar GLOBAL: "global"
    :vartype GLOBAL: str
    """

    NONE = "none"
    SERVER = "server"
    GLOBAL = "global"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Uniqueness._member_map_.values()))


@JsonMap(
    {
        "type_": "type",
        "sub_attributes": "subAttributes",
        "multi_valued": "multiValued",
        "canonical_values": "canonicalValues",
        "case_exact": "caseExact",
        "reference_types": "referenceTypes",
    }
)
class ScimSchemaAttribute(BaseModel):
    """ScimSchemaAttribute

    :param name: The name of the attribute
    :type name: str
    :param type_: type_
    :type type_: ScimSchemaAttributeType
    :param sub_attributes: sub_attributes, defaults to None
    :type sub_attributes: List[ScimSchemaAttribute], optional
    :param multi_valued: A Boolean value indicating the attribute's plurality
    :type multi_valued: bool
    :param description: The description of the attribute, defaults to None
    :type description: str, optional
    :param required: required
    :type required: bool
    :param canonical_values: A collection of suggested canonical values, defaults to None
    :type canonical_values: List[str], optional
    :param case_exact: case_exact, defaults to None
    :type case_exact: bool, optional
    :param mutability: Indicates the circumstances under which the value of the attribute can be (re)defined
    :type mutability: Mutability
    :param returned: Indicates when an attribute and associated values are returned
    :type returned: Returned
    :param uniqueness: Specifies how the service provider enforces uniqueness of attribute values
    :type uniqueness: Uniqueness
    :param reference_types: Indicates the SCIM resource types that be referenced, defaults to None
    :type reference_types: List[str], optional
    """

    def __init__(
        self,
        name: str,
        type_: ScimSchemaAttributeType,
        multi_valued: bool,
        required: bool,
        mutability: Mutability,
        returned: Returned,
        uniqueness: Uniqueness,
        sub_attributes: List[ScimSchemaAttribute] = None,
        description: str = None,
        canonical_values: List[str] = None,
        case_exact: bool = None,
        reference_types: List[str] = None,
    ):
        self.name = name
        self.type_ = self._enum_matching(type_, ScimSchemaAttributeType.list(), "type_")
        if sub_attributes is not None:
            self.sub_attributes = self._define_list(sub_attributes, ScimSchemaAttribute)
        self.multi_valued = multi_valued
        if description is not None:
            self.description = description
        self.required = required
        if canonical_values is not None:
            self.canonical_values = canonical_values
        if case_exact is not None:
            self.case_exact = case_exact
        self.mutability = self._enum_matching(
            mutability, Mutability.list(), "mutability"
        )
        self.returned = self._enum_matching(returned, Returned.list(), "returned")
        self.uniqueness = self._enum_matching(
            uniqueness, Uniqueness.list(), "uniqueness"
        )
        if reference_types is not None:
            self.reference_types = reference_types
