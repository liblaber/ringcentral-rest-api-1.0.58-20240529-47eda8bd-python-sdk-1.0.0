# InternalContactsService

A list of all methods in the `InternalContactsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                                                                                                                                                                                                                                    |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_directory_entries](#list_directory_entries)       | Returns contact information on corporate users of federated accounts. Please note: 1. `User`, `DigitalUser`, `VirtualUser` and `FaxUser` types are returned as `User` type. 2. `ApplicationExtension` type is not returned. 3. Only extensions in `Enabled`, `Disabled` and `NotActivated` state are returned. |
| [read_directory_entry](#read_directory_entry)           | Returns contact information on a particular corporate user of a federated account.                                                                                                                                                                                                                             |
| [search_directory_entries](#search_directory_entries)   | Returns contact information on corporate users of federated accounts according to the specified filtering and ordering.                                                                                                                                                                                        |
| [read_directory_federation](#read_directory_federation) | Returns information on a federation and associated accounts.                                                                                                                                                                                                                                                   |

## list_directory_entries

Returns contact information on corporate users of federated accounts. Please note: 1. `User`, `DigitalUser`, `VirtualUser` and `FaxUser` types are returned as `User` type. 2. `ApplicationExtension` type is not returned. 3. Only extensions in `Enabled`, `Disabled` and `NotActivated` state are returned.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/directory/entries`

**Parameters**

| Name           | Type                                                              | Required | Description                                                                                                                                                                                                                                                                                       |
| :------------- | :---------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| account_id     | str                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                                                                      |
| show_federated | bool                                                              | ❌       | If `true` then contacts of all accounts in federation are returned. If `false` then only contacts of the current account are returned, and account section is eliminated in this case                                                                                                             |
| type\_         | [ListDirectoryEntriesType](../models/ListDirectoryEntriesType.md) | ❌       | Type of an extension. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                                                                                                                                        |
| type_group     | [TypeGroup](../models/TypeGroup.md)                               | ❌       | Type of extension group                                                                                                                                                                                                                                                                           |
| page           | int                                                               | ❌       | Page number                                                                                                                                                                                                                                                                                       |
| per_page       | [PerPage](../models/PerPage.md)                                   | ❌       | Records count to be returned per one page. It can be either integer or string with the specific keyword values: - `all` - all records are returned in one page - `max` - maximum count of records that can be returned in one page                                                                |
| site_id        | str                                                               | ❌       | Internal identifier of the business site to which extensions belong                                                                                                                                                                                                                               |
| if_none_match  | str                                                               | ❌       | User in GET requests to skip retrieving the data if the provided value matches current `ETag` associated with this resource. The server checks the current resource ETag and returns the data only if mismatches the `If-None-Match` value, otherwise `HTTP 304 Not Modified` status is returned. |

**Return Type**

`DirectoryResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListDirectoryEntriesType, TypeGroup

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
per_page=1000

result = sdk.internal_contacts.list_directory_entries(
    account_id="~",
    show_federated=True,
    type_="User",
    type_group="User",
    page=1,
    per_page=per_page,
    site_id="siteId",
    if_none_match="If-None-Match"
)

print(result)
```

## read_directory_entry

Returns contact information on a particular corporate user of a federated account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/directory/entries/{entryId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| entry_id   | str  | ✅       | Internal identifier of extension to read information for                                                                                                     |

**Return Type**

`ContactResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.internal_contacts.read_directory_entry(
    account_id="~",
    entry_id="entryId"
)

print(result)
```

## search_directory_entries

Returns contact information on corporate users of federated accounts according to the specified filtering and ordering.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/directory/entries/search`

**Parameters**

| Name             | Type                                                                        | Required | Description                                                                                                                                                  |
| :--------------- | :-------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body     | [SearchDirectoryEntriesRequest](../models/SearchDirectoryEntriesRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id       | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| account_id_1     | str                                                                         | ❌       | A list of Account IDs                                                                                                                                        |
| department       | str                                                                         | ❌       | A list of department names                                                                                                                                   |
| site_id          | str                                                                         | ❌       | A list of Site IDs                                                                                                                                           |
| extension_status | str                                                                         | ❌       | Extension current state                                                                                                                                      |
| extension_type   | [SearchDirectoryExtensionType](../models/SearchDirectoryExtensionType.md)   | ❌       | Extension types                                                                                                                                              |

**Return Type**

`DirectoryResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SearchDirectoryEntriesRequest, SearchDirectoryExtensionType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SearchDirectoryEntriesRequest(
    search_string="searchString",
    search_fields=[
        "firstName"
    ],
    show_federated=True,
    show_admin_only_contacts=True,
    extension_type="User",
    site_id="872781797006",
    show_external_contacts=True,
    account_ids=[
        "accountIds"
    ],
    department="department",
    site_ids=[
        "siteIds"
    ],
    extension_statuses=[
        "Enabled"
    ],
    extension_types=[
        "User"
    ],
    order_by=[
        {
            "index": 1,
            "field_name": "firstName",
            "direction": "Asc"
        }
    ],
    page=3,
    per_page=5
)

result = sdk.internal_contacts.search_directory_entries(
    request_body=request_body,
    account_id="~",
    account_id_1="400131426008",
    department="North office",
    site_id="872781797006",
    extension_status="Enabled",
    extension_type="User"
)

print(result)
```

## read_directory_federation

Returns information on a federation and associated accounts.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/directory/federation`

**Parameters**

| Name            | Type                                            | Required | Description                                                                                                                                                  |
| :-------------- | :---------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| types           | [FederationTypes](../models/FederationTypes.md) | ❌       | Filter by federation types. Default is Regular                                                                                                               |
| rc_extension_id | str                                             | ❌       | RingCentral extension id                                                                                                                                     |

**Return Type**

`FederationResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import FederationTypes

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.internal_contacts.read_directory_federation(
    account_id="~",
    types="All",
    rc_extension_id="RCExtensionId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
