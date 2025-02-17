# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_user_profile_image_request import UpdateUserProfileImageRequest
from ..models.update_conferencing_info_request import UpdateConferencingInfoRequest
from ..models.scale_size import ScaleSize
from ..models.notification_settings_update_request import (
    NotificationSettingsUpdateRequest,
)
from ..models.notification_settings import NotificationSettings
from ..models.get_extension_info_response import GetExtensionInfoResponse
from ..models.get_extension_grant_list_response import GetExtensionGrantListResponse
from ..models.get_conferencing_info_response import GetConferencingInfoResponse
from ..models.extension_update_request import ExtensionUpdateRequest
from ..models.extension_type import ExtensionType
from ..models.extension_caller_id_info_request import ExtensionCallerIdInfoRequest
from ..models.extension_caller_id_info import ExtensionCallerIdInfo
from ..models.create_user_profile_image_request import CreateUserProfileImageRequest
from ..models.content_disposition import ContentDisposition
from ..models.bulk_delete_users_response import BulkDeleteUsersResponse
from ..models.bulk_delete_users_request import BulkDeleteUsersRequest
from ..models.batch_provision_users_response import BatchProvisionUsersResponse
from ..models.batch_provision_users_request import BatchProvisionUsersRequest


class UserSettingsService(BaseService):

    @cast_models
    def read_scaled_profile_image(
        self,
        account_id: str,
        extension_id: str,
        scale_size: ScaleSize,
        content_disposition: ContentDisposition = None,
        content_disposition_filename: str = None,
    ) -> bytes:
        """Returns the scaled profile image of an extension.

        **This API must be called via media API entry point, e.g. https://media.ringcentral.com**

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param scale_size: Dimensions of a profile image which will be returned in response.
        :type scale_size: ScaleSize
        :param content_disposition: Whether the content is expected to be displayed in the browser, or downloaded and saved locally, defaults to None
        :type content_disposition: ContentDisposition, optional
        :param content_disposition_filename: The default filename of the file to be downloaded, defaults to None
        :type content_disposition_filename: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: bytes
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(ScaleSize).validate(scale_size)
        Validator(ContentDisposition).is_optional().validate(content_disposition)
        Validator(str).is_optional().validate(content_disposition_filename)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/profile-image/{{scaleSize}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_path("scaleSize", scale_size)
            .add_query("contentDisposition", content_disposition)
            .add_query("contentDispositionFilename", content_disposition_filename)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def post_batch_provision_users(
        self, request_body: BatchProvisionUsersRequest, account_id: str
    ) -> BatchProvisionUsersResponse:
        """Creates multiple user extensions with BYOD (customer provided) devices.
        If "extensionNumber" is not specified, the next available extension number will be assigned.

        :param request_body: The request body.
        :type request_body: BatchProvisionUsersRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response (partial success is possible)
        :rtype: BatchProvisionUsersResponse
        """

        Validator(BatchProvisionUsersRequest).validate(request_body)
        Validator(str).validate(account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v2/accounts/{{accountId}}/batch-provisioning/users",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return BatchProvisionUsersResponse._unmap(response)

    @cast_models
    def bulk_delete_users_v2(
        self, request_body: BulkDeleteUsersRequest, account_id: str
    ) -> BulkDeleteUsersResponse:
        """Deletes user extension(s) and either keeps or destroys the assets - numbers and devices.
        Multiple extensions can be deleted with a single API call.

        **Please note:** This API cannot be tested on Sandbox.

        :param request_body: The request body.
        :type request_body: BulkDeleteUsersRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: BulkDeleteUsersResponse
        """

        Validator(BulkDeleteUsersRequest).validate(request_body)
        Validator(str).validate(account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v2/accounts/{{accountId}}/extensions",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .serialize()
            .set_method("DELETE")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return BulkDeleteUsersResponse._unmap(response)

    @cast_models
    def read_extension(
        self, account_id: str, extension_id: str
    ) -> GetExtensionInfoResponse:
        """Returns basic information about a particular extension of an account.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Extension information
        :rtype: GetExtensionInfoResponse
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetExtensionInfoResponse._unmap(response)

    @cast_models
    def update_extension(
        self, request_body: ExtensionUpdateRequest, account_id: str, extension_id: str
    ) -> GetExtensionInfoResponse:
        """Updates the user settings.

        :param request_body: The request body.
        :type request_body: ExtensionUpdateRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success
        :rtype: GetExtensionInfoResponse
        """

        Validator(ExtensionUpdateRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetExtensionInfoResponse._unmap(response)

    @cast_models
    def delete_extension(
        self,
        account_id: str,
        extension_id: str,
        save_phone_lines: bool = None,
        save_phone_numbers: bool = None,
    ):
        """Deletes extension(s) by ID(s). When an extension is being deleted
        the default API behavior is as follows:

        - user's direct numbers are preserved by becoming additional company numbers;
        - user's digital lines (both device & associated phone number) are deleted.

        You can change this behavior using the filters:

        - create unassigned extensions for each digital line of the deleted extension by
          setting the query parameter `savePhoneLines` to `true` in request path;
        - remove direct numbers of the deleted extension by setting the `savePhoneNumbers`
          query parameter to `false` in request path

        **Note!** Since this API is now deprecated, please use the following API method `DELETE /restapi/v2/accounts/{accountId}/extensions` for users deletion.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param save_phone_lines: save_phone_lines, defaults to None
        :type save_phone_lines: bool, optional
        :param save_phone_numbers: save_phone_numbers, defaults to None
        :type save_phone_numbers: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(bool).is_optional().validate(save_phone_lines)
        Validator(bool).is_optional().validate(save_phone_numbers)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_query("savePhoneLines", save_phone_lines)
            .add_query("savePhoneNumbers", save_phone_numbers)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def list_extension_grants(
        self,
        account_id: str,
        extension_id: str,
        extension_type: ExtensionType = None,
        page: int = None,
        per_page: int = None,
    ) -> GetExtensionGrantListResponse:
        """Returns the list of extensions with information on grants
        given to the current extension regarding them. Currently the list of grants
        include: picking up a call, monitoring, calling or receiving a call on behalf
        of somebody, call delegation and calling paging groups.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param extension_type: Type of extension to be returned. Multiple values are supported.
        Please note that legacy 'Department' extension type corresponds
        to 'Call Queue' extensions in modern RingCentral product terminology, defaults to None
        :type extension_type: ExtensionType, optional
        :param page: Indicates a page number to retrieve. Only positive number values
        are allowed, defaults to None
        :type page: int, optional
        :param per_page: Indicates a page size (number of items), defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of extension grants
        :rtype: GetExtensionGrantListResponse
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(ExtensionType).is_optional().validate(extension_type)
        Validator(int).is_optional().validate(page)
        Validator(int).is_optional().validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/grant",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_query("extensionType", extension_type)
            .add_query("page", page)
            .add_query("perPage", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetExtensionGrantListResponse._unmap(response)

    @cast_models
    def read_conferencing_settings(
        self, account_id: str, extension_id: str, country_id: str = None
    ) -> GetConferencingInfoResponse:
        """Returns information on Free Conference Calling (FCC) feature
        for a given extension.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        :param country_id: Internal identifier of a country. If not specified, the response
        is returned for the brand country, defaults to None
        :type country_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success
        :rtype: GetConferencingInfoResponse
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)
        Validator(str).is_optional().validate(country_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/conferencing",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .add_query("countryId", country_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetConferencingInfoResponse._unmap(response)

    @cast_models
    def update_conferencing_settings(
        self,
        request_body: UpdateConferencingInfoRequest,
        account_id: str,
        extension_id: str,
    ) -> GetConferencingInfoResponse:
        """Updates the default conferencing number for the current extension.
        The number can be selected from conferencing numbers of the current extension.
        Updates the setting, allowing participants join the conference before host.

        :param request_body: The request body.
        :type request_body: UpdateConferencingInfoRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Updated user conferencing settings
        :rtype: GetConferencingInfoResponse
        """

        Validator(UpdateConferencingInfoRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/conferencing",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetConferencingInfoResponse._unmap(response)

    @cast_models
    def read_user_profile_image_legacy(
        self, account_id: str, extension_id: str
    ) -> bytes:
        """Returns a profile image of an extension.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: User Profile Image (Media Data)
        :rtype: bytes
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/profile-image",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def create_user_profile_image(
        self, request_body: dict, account_id: str, extension_id: str
    ):
        """Uploads the extension profile image.

        :param request_body: The request body.
        :type request_body: dict
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

        Validator(dict).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/profile-image",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def update_user_profile_image(
        self, request_body: dict, account_id: str, extension_id: str
    ):
        """Updates the extension profile image.

        :param request_body: The request body.
        :type request_body: dict
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

        Validator(dict).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/profile-image",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body, "multipart/form-data")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def delete_user_profile_image(self, account_id: str, extension_id: str):
        """Deletes the user profile image.

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

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/profile-image",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def read_extension_caller_id(
        self, account_id: str, extension_id: str
    ) -> ExtensionCallerIdInfo:
        """Returns information on an outbound caller ID of an extension.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Caller ID information
        :rtype: ExtensionCallerIdInfo
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/caller-id",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ExtensionCallerIdInfo._unmap(response)

    @cast_models
    def update_extension_caller_id(
        self,
        request_body: ExtensionCallerIdInfoRequest,
        account_id: str,
        extension_id: str,
    ) -> ExtensionCallerIdInfo:
        """Updates outbound caller ID information of an extension.

        :param request_body: The request body.
        :type request_body: ExtensionCallerIdInfoRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Updated caller ID information
        :rtype: ExtensionCallerIdInfo
        """

        Validator(ExtensionCallerIdInfoRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/caller-id",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ExtensionCallerIdInfo._unmap(response)

    @cast_models
    def read_notification_settings(
        self, account_id: str, extension_id: str
    ) -> NotificationSettings:
        """Returns notification settings for the current extension.

        Knowledge Article: [User Settings - Set Up Message Notifications](https://success.ringcentral.com/articles/RC_Knowledge_Article/9740)

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Notification settings
        :rtype: NotificationSettings
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/notification-settings",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return NotificationSettings._unmap(response)

    @cast_models
    def update_notification_settings(
        self,
        request_body: NotificationSettingsUpdateRequest,
        account_id: str,
        extension_id: str,
    ) -> NotificationSettings:
        """Updates notification settings for the current extension.
        Knowledge Article: [User Settings - Set Up Message Notifications](https://success.ringcentral.com/articles/RC_Knowledge_Article/9740)

        :param request_body: The request body.
        :type request_body: NotificationSettingsUpdateRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Updated notification settings
        :rtype: NotificationSettings
        """

        Validator(NotificationSettingsUpdateRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/notification-settings",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return NotificationSettings._unmap(response)
