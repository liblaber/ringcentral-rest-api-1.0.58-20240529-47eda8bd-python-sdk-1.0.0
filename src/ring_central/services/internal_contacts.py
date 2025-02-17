# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.type_group import TypeGroup
from ..models.search_directory_extension_type import SearchDirectoryExtensionType
from ..models.search_directory_entries_request import SearchDirectoryEntriesRequest
from ..models.per_page import PerPage
from ..models.list_directory_entries_type import ListDirectoryEntriesType
from ..models.federation_types import FederationTypes
from ..models.federation_resource import FederationResource
from ..models.directory_resource import DirectoryResource
from ..models.contact_resource import ContactResource


class InternalContactsService(BaseService):

    @cast_models
    def list_directory_entries(
        self,
        account_id: str,
        show_federated: bool = None,
        type_: ListDirectoryEntriesType = None,
        type_group: TypeGroup = None,
        page: int = None,
        per_page: PerPage = None,
        site_id: str = None,
        if_none_match: str = None,
    ) -> DirectoryResource:
        """Returns contact information on corporate users of federated accounts. Please note: 1. `User`, `DigitalUser`, `VirtualUser` and `FaxUser` types are returned as `User` type. 2. `ApplicationExtension` type is not returned. 3. Only extensions in `Enabled`, `Disabled` and `NotActivated` state are returned.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param show_federated: If `true` then contacts of all accounts in federation are returned. If `false` then only contacts of the current account are returned, and account section is eliminated in this case, defaults to None
        :type show_federated: bool, optional
        :param type_: Type of an extension. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology, defaults to None
        :type type_: ListDirectoryEntriesType, optional
        :param type_group: Type of extension group, defaults to None
        :type type_group: TypeGroup, optional
        :param page: Page number, defaults to None
        :type page: int, optional
        :param per_page: Records count to be returned per one page. It can be either integer or string with the specific keyword values:
        - `all` - all records are returned in one page
        - `max` - maximum count of records that can be returned in one page, defaults to None
        :type per_page: PerPage, optional
        :param site_id: Internal identifier of the business site to which extensions belong, defaults to None
        :type site_id: str, optional
        :param if_none_match: User in GET requests to skip retrieving the data if the provided value matches current `ETag` associated with this resource.
        The server checks the current resource ETag and returns the data only if mismatches the `If-None-Match` value,
        otherwise `HTTP 304 Not Modified` status is returned., defaults to None
        :type if_none_match: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Paged collection of all contacts information for a given account. Records can be empty if no data found.
        :rtype: DirectoryResource
        """

        Validator(str).validate(account_id)
        Validator(bool).is_optional().validate(show_federated)
        Validator(ListDirectoryEntriesType).is_optional().validate(type_)
        Validator(TypeGroup).is_optional().validate(type_group)
        Validator(int).is_optional().validate(page)
        Validator(PerPage).is_optional().validate(per_page)
        Validator(str).is_optional().validate(site_id)
        Validator(str).is_optional().validate(if_none_match)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/directory/entries",
                self.get_default_headers(),
            )
            .add_header("If-None-Match", if_none_match)
            .add_path("accountId", account_id)
            .add_query("showFederated", show_federated)
            .add_query("type", type_)
            .add_query("typeGroup", type_group)
            .add_query("page", page)
            .add_query("perPage", per_page)
            .add_query("siteId", site_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return DirectoryResource._unmap(response)

    @cast_models
    def read_directory_entry(self, account_id: str, entry_id: str) -> ContactResource:
        """Returns contact information on a particular corporate user of a federated account.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param entry_id: Internal identifier of extension to read information for
        :type entry_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Contact information for given parameters. If value doesn't found then empty body will be returned
        :rtype: ContactResource
        """

        Validator(str).validate(account_id)
        Validator(str).validate(entry_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/directory/entries/{{entryId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("entryId", entry_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ContactResource._unmap(response)

    @cast_models
    def search_directory_entries(
        self,
        request_body: SearchDirectoryEntriesRequest,
        account_id: str,
        account_id_1: str = None,
        department: str = None,
        site_id: str = None,
        extension_status: str = None,
        extension_type: SearchDirectoryExtensionType = None,
    ) -> DirectoryResource:
        """Returns contact information on corporate users of federated accounts according to the specified filtering and ordering.

        :param request_body: The request body.
        :type request_body: SearchDirectoryEntriesRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param account_id_1: A list of Account IDs, defaults to None
        :type account_id_1: str, optional
        :param department: A list of department names, defaults to None
        :type department: str, optional
        :param site_id: A list of Site IDs, defaults to None
        :type site_id: str, optional
        :param extension_status: Extension current state, defaults to None
        :type extension_status: str, optional
        :param extension_type: Extension types, defaults to None
        :type extension_type: SearchDirectoryExtensionType, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Paged collection of all contacts information for a given account according to filtering and ordering. Records can be empty if no data found
        :rtype: DirectoryResource
        """

        Validator(SearchDirectoryEntriesRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).is_optional().validate(account_id_1)
        Validator(str).is_optional().validate(department)
        Validator(str).is_optional().validate(site_id)
        Validator(str).is_optional().validate(extension_status)
        Validator(SearchDirectoryExtensionType).is_optional().validate(extension_type)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/directory/entries/search",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_query("accountId", account_id_1)
            .add_query("department", department)
            .add_query("siteId", site_id)
            .add_query("extensionStatus", extension_status)
            .add_query("extensionType", extension_type)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return DirectoryResource._unmap(response)

    @cast_models
    def read_directory_federation(
        self,
        account_id: str,
        types: FederationTypes = None,
        rc_extension_id: str = None,
    ) -> FederationResource:
        """Returns information on a federation and associated accounts.

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param types: Filter by federation types. Default is Regular, defaults to None
        :type types: FederationTypes, optional
        :param rc_extension_id: RingCentral extension id, defaults to None
        :type rc_extension_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of found federations. Records array can be empty if no data found
        :rtype: FederationResource
        """

        Validator(str).validate(account_id)
        Validator(FederationTypes).is_optional().validate(types)
        Validator(str).is_optional().validate(rc_extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/directory/federation",
                self.get_default_headers(),
            )
            .add_header("RCExtensionId", rc_extension_id)
            .add_path("accountId", account_id)
            .add_query("types", types)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return FederationResource._unmap(response)
