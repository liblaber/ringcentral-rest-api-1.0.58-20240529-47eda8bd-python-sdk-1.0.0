# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_forwarding_number_request import UpdateForwardingNumberRequest
from ..models.get_extension_forwarding_number_list_response import (
    GetExtensionForwardingNumberListResponse,
)
from ..models.forwarding_number_resource import ForwardingNumberResource
from ..models.forwarding_number_info import ForwardingNumberInfo
from ..models.delete_forwarding_numbers_request import DeleteForwardingNumbersRequest
from ..models.create_forwarding_number_request import CreateForwardingNumberRequest


class CallForwardingService(BaseService):

    @cast_models
    def list_forwarding_numbers(
        self, account_id: str, extension_id: str, page: int = None, per_page: int = None
    ) -> GetExtensionForwardingNumberListResponse:
        """Returns the list of extension phone numbers used for call forwarding
        and call flip. The returned list contains all the extension phone numbers
        used for call forwarding and call flip.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param page: The result set page number (1-indexed) to return, defaults to None
        :type page: int, optional
        :param per_page: The number of items per page. If provided value in the request
        is greater than a maximum, the maximum value is applied, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: GetExtensionForwardingNumberListResponse
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(int).is_optional().min(1).max(1000).validate(page)
        Validator(int).is_optional().min(1).max(1000).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/forwarding-number",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_query("page", page, explode=False)
            .add_query("perPage", per_page, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetExtensionForwardingNumberListResponse._unmap(response)

    @cast_models
    def create_forwarding_number(
        self,
        request_body: CreateForwardingNumberRequest,
        account_id: str,
        extension_id: str,
    ) -> ForwardingNumberInfo:
        """Adds a new forwarding number to the forwarding number list.

        :param request_body: The request body.
        :type request_body: CreateForwardingNumberRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ForwardingNumberInfo
        """

        Validator(CreateForwardingNumberRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/forwarding-number",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ForwardingNumberInfo._unmap(response)

    @cast_models
    def delete_forwarding_numbers(
        self,
        request_body: DeleteForwardingNumbersRequest,
        account_id: str,
        extension_id: str,
    ):
        """Deletes multiple forwarding numbers from the forwarding number list by IDs.

        :param request_body: The request body.
        :type request_body: DeleteForwardingNumbersRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(DeleteForwardingNumbersRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/forwarding-number",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("DELETE")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def read_forwarding_number(
        self, account_id: str, extension_id: str, forwarding_number_id: str
    ) -> ForwardingNumberResource:
        """Returns a specific forwarding number.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param forwarding_number_id: Internal identifier of a forwarding number (returned in response in the 'id' field)
        :type forwarding_number_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ForwardingNumberResource
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(str).validate(forwarding_number_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/forwarding-number/{{forwardingNumberId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_path("forwardingNumberId", forwarding_number_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ForwardingNumberResource._unmap(response)

    @cast_models
    def update_forwarding_number(
        self,
        request_body: UpdateForwardingNumberRequest,
        account_id: str,
        extension_id: str,
        forwarding_number_id: str,
    ) -> ForwardingNumberInfo:
        """Updates the existing forwarding number from the forwarding number list.

        :param request_body: The request body.
        :type request_body: UpdateForwardingNumberRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param forwarding_number_id: Internal identifier of a forwarding number (returned in response in the 'id' field)
        :type forwarding_number_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: ForwardingNumberInfo
        """

        Validator(UpdateForwardingNumberRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(str).validate(forwarding_number_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/forwarding-number/{{forwardingNumberId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_path("forwardingNumberId", forwarding_number_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ForwardingNumberInfo._unmap(response)

    @cast_models
    def delete_forwarding_number(
        self, account_id: str, extension_id: str, forwarding_number_id: str
    ):
        """Deletes a forwarding number from the forwarding number list by its ID.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param forwarding_number_id: Internal identifier of a forwarding number (returned in response in the 'id' field)
        :type forwarding_number_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(str).validate(forwarding_number_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/forwarding-number/{{forwardingNumberId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_path("forwardingNumberId", forwarding_number_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response
