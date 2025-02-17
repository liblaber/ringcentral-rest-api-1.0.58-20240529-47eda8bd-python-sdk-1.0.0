# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.business_site_collection_resource import BusinessSiteCollectionResource
from ..models.business_site_collection_request import BusinessSiteCollectionRequest


class SiteAdministrationService(BaseService):

    @cast_models
    def list_administered_sites(
        self, account_id: str, extension_id: str
    ) -> BusinessSiteCollectionResource:
        """Returns a list of sites administered by the current user.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of user administered sites
        :rtype: BusinessSiteCollectionResource
        """

        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/administered-sites",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return BusinessSiteCollectionResource._unmap(response)

    @cast_models
    def update_user_administered_sites(
        self,
        request_body: BusinessSiteCollectionRequest,
        account_id: str,
        extension_id: str,
    ) -> BusinessSiteCollectionResource:
        """Updates the sites administered by the current user.
        Please note: Only IDs of records are used for update.

        :param request_body: The request body.
        :type request_body: BusinessSiteCollectionRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Updated list of user administered sites
        :rtype: BusinessSiteCollectionResource
        """

        Validator(BusinessSiteCollectionRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/administered-sites",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return BusinessSiteCollectionResource._unmap(response)
