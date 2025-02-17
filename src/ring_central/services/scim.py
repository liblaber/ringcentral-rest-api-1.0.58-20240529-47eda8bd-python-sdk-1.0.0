# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.scim_user_search_response import ScimUserSearchResponse
from ..models.scim_user_response import ScimUserResponse
from ..models.scim_user_patch import ScimUserPatch
from ..models.scim_user import ScimUser
from ..models.scim_search_request import ScimSearchRequest
from ..models.scim_schema_search_response import ScimSchemaSearchResponse
from ..models.scim_schema_response import ScimSchemaResponse
from ..models.scim_resource_type_search_response import ScimResourceTypeSearchResponse
from ..models.scim_resource_type_response import ScimResourceTypeResponse
from ..models.scim_provider_config import ScimProviderConfig


class ScimService(BaseService):

    @cast_models
    def scim_list_schemas2(self) -> ScimSchemaSearchResponse:
        """Returns the list of schemas

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimSchemaSearchResponse
        """

        serialized_request = (
            Serializer(f"{self.base_url}/scim/v2/Schemas", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ScimSchemaSearchResponse._unmap(response)

    @cast_models
    def scim_get_schema2(self, uri: str) -> ScimSchemaResponse:
        """Returns SCIM schema

        :param uri: Schema URI
        :type uri: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimSchemaResponse
        """

        Validator(str).validate(uri)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Schemas/{{uri}}", self.get_default_headers()
            )
            .add_path("uri", uri)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ScimSchemaResponse._unmap(response)

    @cast_models
    def scim_search_via_get2(
        self, filter: str = None, start_index: int = None, count: int = None
    ) -> ScimUserSearchResponse:
        """Returns the list of users satisfying search criteria

        :param filter: Only support 'userName' or 'email' filter expressions for now, defaults to None
        :type filter: str, optional
        :param start_index: Start index (1-based), defaults to None
        :type start_index: int, optional
        :param count: Page size, defaults to None
        :type count: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimUserSearchResponse
        """

        Validator(str).is_optional().validate(filter)
        Validator(int).is_optional().validate(start_index)
        Validator(int).is_optional().validate(count)

        serialized_request = (
            Serializer(f"{self.base_url}/scim/v2/Users", self.get_default_headers())
            .add_query("filter", filter)
            .add_query("startIndex", start_index)
            .add_query("count", count)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ScimUserSearchResponse._unmap(response)

    @cast_models
    def scim_create_user2(self, request_body: ScimUser) -> ScimUserResponse:
        """Creates a new user

        :param request_body: The request body.
        :type request_body: ScimUser
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimUserResponse
        """

        Validator(ScimUser).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/scim/v2/Users", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ScimUserResponse._unmap(response)

    @cast_models
    def scim_search_via_post2(
        self, request_body: ScimSearchRequest
    ) -> ScimUserSearchResponse:
        """Returns the list of users satisfying search criteria

        :param request_body: The request body.
        :type request_body: ScimSearchRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimUserSearchResponse
        """

        Validator(ScimSearchRequest).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/.search", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ScimUserSearchResponse._unmap(response)

    @cast_models
    def scim_get_user2(self, scim_user_id: str) -> ScimUserResponse:
        """Returns a user by ID

        :param scim_user_id: User ID
        :type scim_user_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimUserResponse
        """

        Validator(str).validate(scim_user_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/{{scimUserId}}",
                self.get_default_headers(),
            )
            .add_path("scimUserId", scim_user_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ScimUserResponse._unmap(response)

    @cast_models
    def scim_update_user2(
        self, request_body: ScimUser, scim_user_id: str
    ) -> ScimUserResponse:
        """Updates a user

        :param request_body: The request body.
        :type request_body: ScimUser
        :param scim_user_id: User ID
        :type scim_user_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimUserResponse
        """

        Validator(ScimUser).validate(request_body)
        Validator(str).validate(scim_user_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/{{scimUserId}}",
                self.get_default_headers(),
            )
            .add_path("scimUserId", scim_user_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ScimUserResponse._unmap(response)

    @cast_models
    def scim_patch_user2(
        self, request_body: ScimUserPatch, scim_user_id: str
    ) -> ScimUserResponse:
        """Updates a user (partial update)

        :param request_body: The request body.
        :type request_body: ScimUserPatch
        :param scim_user_id: User ID
        :type scim_user_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimUserResponse
        """

        Validator(ScimUserPatch).validate(request_body)
        Validator(str).validate(scim_user_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/{{scimUserId}}",
                self.get_default_headers(),
            )
            .add_path("scimUserId", scim_user_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ScimUserResponse._unmap(response)

    @cast_models
    def scim_delete_user2(self, scim_user_id: str):
        """Deletes a user

        :param scim_user_id: User ID
        :type scim_user_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(scim_user_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/{{scimUserId}}",
                self.get_default_headers(),
            )
            .add_path("scimUserId", scim_user_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def scim_get_provider_config2(self) -> ScimProviderConfig:
        """Returns SCIM service provider configuration

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimProviderConfig
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/ServiceProviderConfig",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ScimProviderConfig._unmap(response)

    @cast_models
    def scim_list_resource_types2(self) -> ScimResourceTypeSearchResponse:
        """Returns the list of supported SCIM resource types

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimResourceTypeSearchResponse
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/ResourceTypes", self.get_default_headers()
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ScimResourceTypeSearchResponse._unmap(response)

    @cast_models
    def scim_get_resource_type2(self, type_: str) -> ScimResourceTypeResponse:
        """Returns resource type by ID

        :param type_: Resource type
        :type type_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: ScimResourceTypeResponse
        """

        Validator(str).validate(type_)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/ResourceTypes/{{type}}",
                self.get_default_headers(),
            )
            .add_path("type", type_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ScimResourceTypeResponse._unmap(response)
