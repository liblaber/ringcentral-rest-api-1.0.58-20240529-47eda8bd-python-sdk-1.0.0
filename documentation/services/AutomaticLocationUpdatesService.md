# AutomaticLocationUpdatesService

A list of all methods in the `AutomaticLocationUpdatesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                   | Description                                                                                                                                                                                                                                        |
| :-------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_emergency_locations](#list_emergency_locations)                                                     | Returns emergency response locations for the current account.                                                                                                                                                                                      |
| [create_emergency_location](#create_emergency_location)                                                   | Creates a new emergency response location for a company.                                                                                                                                                                                           |
| [read_emergency_location](#read_emergency_location)                                                       | Returns emergency response location by ID. Available for Admin users only.                                                                                                                                                                         |
| [update_emergency_location](#update_emergency_location)                                                   | Updates the specified emergency response location.                                                                                                                                                                                                 |
| [delete_emergency_location](#delete_emergency_location)                                                   | Deletes the specified emergency response location.                                                                                                                                                                                                 |
| [get_extension_emergency_locations](#get_extension_emergency_locations)                                   | Returns a list of emergency response locations available for the particular extension.                                                                                                                                                             |
| [create_extension_emergency_location](#create_extension_emergency_location)                               | Creates a personal emergency response location for the current user.                                                                                                                                                                               |
| [get_extension_emergency_location](#get_extension_emergency_location)                                     | Returns a personal emergency response location for the current user.                                                                                                                                                                               |
| [update_extension_emergency_location](#update_extension_emergency_location)                               | Updates a personal emergency response location by the current user or admin.                                                                                                                                                                       |
| [delete_extension_emergency_location](#delete_extension_emergency_location)                               | Deletes a personal emergency response location by ID by the current user or admin. Multiple personal emergency response locations can be deleted by single API call.                                                                               |
| [read_automatic_location_updates_task](#read_automatic_location_updates_task)                             | Returns results of the task created within the frame of Automatic Location Updates feature. Currently four task types are supported: 'Wireless Points Bulk Create', 'Wireless Points Bulk Update', 'Switches Bulk Create', 'Switches Bulk Update'. |
| [list_automatic_location_updates_users](#list_automatic_location_updates_users)                           | Returns a list of users with their status of Automatic Location Updates feature.                                                                                                                                                                   |
| [assign_multiple_automatic_location_updates_users](#assign_multiple_automatic_location_updates_users)     | Enables or disables Automatic Location Updates feature for multiple account users.                                                                                                                                                                 |
| [create_multiple_wireless_points](#create_multiple_wireless_points)                                       | Creates multiple wireless points in a corporate map. The maximum number of wireless points per request is 10 000; limitation for account is 70 000.                                                                                                |
| [list_networks](#list_networks)                                                                           | Returns a corporate network map with emergency addresses assigned to the current account.                                                                                                                                                          |
| [create_network](#create_network)                                                                         | Creates a new network in a corporate ethernet map for assignment of emergency addresses to network access points.                                                                                                                                  |
| [read_network](#read_network)                                                                             | Returns the specified network with emergency addresses assigned to the current account.                                                                                                                                                            |
| [update_network](#update_network)                                                                         | Updates a network in a corporate ethernet map for assignment of emergency addresses to network access points.                                                                                                                                      |
| [delete_network](#delete_network)                                                                         | Deletes network(s) in a corporate ethernet map for Automatic Location Updates feature.                                                                                                                                                             |
| [validate_multiple_switches](#validate_multiple_switches)                                                 | Validates switches before creation or update. The maximum number of switches per request is 10 000.                                                                                                                                                |
| [list_account_switches](#list_account_switches)                                                           | Returns a corporate map of configured network switches with the assigned emergency addresses for the logged-in account.                                                                                                                            |
| [create_switch](#create_switch)                                                                           | Creates a new switch in corporate map based on chassis ID and used for Automatic Locations Update feature.                                                                                                                                         |
| [read_switch](#read_switch)                                                                               | Returns the specified switch with the assigned emergency address.                                                                                                                                                                                  |
| [update_switch](#update_switch)                                                                           | Updates switch. Partial update is not supported, all switch parameters should be specified. If null value is received or parameter is missing, its value is removed.                                                                               |
| [delete_switch](#delete_switch)                                                                           | Deletes wireless switch(es) in a network configuration for Automatic Location Updates feature.                                                                                                                                                     |
| [validate_multiple_wireless_points](#validate_multiple_wireless_points)                                   | Validates wireless points before creation or update. The maximum number of wireless points per request is 10 000.                                                                                                                                  |
| [list_wireless_points](#list_wireless_points)                                                             | Returns account wireless points configured and used for Automatic Location Updates feature.                                                                                                                                                        |
| [create_wireless_point](#create_wireless_point)                                                           | Creates a new wireless point in network configuration with the emergency address assigned.                                                                                                                                                         |
| [read_wireless_point](#read_wireless_point)                                                               | Returns the specified wireless access point of a corporate map with the emergency address assigned.                                                                                                                                                |
| [update_wireless_point](#update_wireless_point)                                                           | Updates the specified wireless access point of a corporate map by ID.                                                                                                                                                                              |
| [delete_wireless_point](#delete_wireless_point)                                                           | Deletes wireless point(s) of a corporate map by ID(s).                                                                                                                                                                                             |
| [list_devices_automatic_location_updates](#list_devices_automatic_location_updates)                       | Returns a list of common devices with their status of Automatic Location Updates feature.                                                                                                                                                          |
| [assign_multiple_devices_automatic_location_updates](#assign_multiple_devices_automatic_location_updates) | Enables or disables Automatic Location Updates feature for the specified common phones.                                                                                                                                                            |
| [create_multiple_switches](#create_multiple_switches)                                                     | Creates multiple switches in corporate map. The maximum number of switches per request is 10 000; limitation for account is 10 000.                                                                                                                |
| [update_multiple_wireless_points](#update_multiple_wireless_points)                                       | Updates wireless points in corporate map. The maximum number of wireless points per request is 10 000; limitation for account is 70 000.                                                                                                           |
| [update_multiple_switches](#update_multiple_switches)                                                     | Updates multiple switches in corporate map. The maximum number of switches per request is 10 000; limitation for account is 10 000.                                                                                                                |

## list_emergency_locations

Returns emergency response locations for the current account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-locations`

**Parameters**

| Name                | Type                                                                        | Required | Description                                                                                                                                                                                                       |
| :------------------ | :-------------------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                      |
| site_id             | List[str]                                                                   | ❌       | Internal identifier of a site for filtering. To indicate company main site `main-site` value should be specified. Supported only if multi-site feature is enabled for the account. Multiple values are supported. |
| search_string       | str                                                                         | ❌       | Filters entries containing the specified substring in 'address' and 'name' fields. The character range is 0-64; not case-sensitive. If empty then the filter is ignored                                           |
| address_status      | [EmergencyAddressStatus](../models/EmergencyAddressStatus.md)               | ❌       |                                                                                                                                                                                                                   |
| usage_status        | [EmergencyLocationUsageStatus](../models/EmergencyLocationUsageStatus.md)   | ❌       |                                                                                                                                                                                                                   |
| domestic_country_id | str                                                                         | ❌       |                                                                                                                                                                                                                   |
| order_by            | [ListEmergencyLocationsOrderBy](../models/ListEmergencyLocationsOrderBy.md) | ❌       | Comma-separated list of fields to order results, prefixed by plus sign '+' (ascending order) or minus sign '-' (descending order)                                                                                 |
| per_page            | int                                                                         | ❌       | Indicates a page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page                                                                    |
| page                | int                                                                         | ❌       | Indicates the page number to retrieve. Only positive number values are supported                                                                                                                                  |

**Return Type**

`EmergencyLocationsResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EmergencyAddressStatus, EmergencyLocationUsageStatus, ListEmergencyLocationsOrderBy

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_id=[
    "siteId"
]

result = sdk.automatic_location_updates.list_emergency_locations(
    account_id="~",
    site_id=site_id,
    search_string="anim occaecat",
    address_status="Valid",
    usage_status="Active",
    domestic_country_id="domesticCountryId",
    order_by="+name",
    per_page=100,
    page=1
)

print(result)
```

## create_emergency_location

Creates a new emergency response location for a company.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-locations`

**Parameters**

| Name         | Type                                                                              | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [EmergencyLocationRequestResource](../models/EmergencyLocationRequestResource.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`EmergencyLocationResponseResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EmergencyLocationRequestResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EmergencyLocationRequestResource(
    id_="id",
    address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName"
    },
    name="name",
    site={
        "id_": "id",
        "name": "name"
    },
    address_status="Valid",
    usage_status="Active",
    address_format_id="addressFormatId",
    visibility="Public",
    trusted=True
)

result = sdk.automatic_location_updates.create_emergency_location(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_emergency_location

Returns emergency response location by ID. Available for Admin users only.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-locations/{locationId}`

**Parameters**

| Name                   | Type | Required | Description                                                                                                                                                  |
| :--------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id             | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| location_id            | str  | ✅       | Internal identifier of an emergency response location                                                                                                        |
| sync_emergency_address | bool | ❌       |                                                                                                                                                              |

**Return Type**

`CommonEmergencyLocationResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.read_emergency_location(
    account_id="~",
    location_id="locationId",
    sync_emergency_address=True
)

print(result)
```

## update_emergency_location

Updates the specified emergency response location.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-locations/{locationId}`

**Parameters**

| Name         | Type                                                                              | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [EmergencyLocationRequestResource](../models/EmergencyLocationRequestResource.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| location_id  | str                                                                               | ✅       | Internal identifier of an emergency response location                                                                                                        |

**Return Type**

`EmergencyLocationResponseResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EmergencyLocationRequestResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EmergencyLocationRequestResource(
    id_="id",
    address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName"
    },
    name="name",
    site={
        "id_": "id",
        "name": "name"
    },
    address_status="Valid",
    usage_status="Active",
    address_format_id="addressFormatId",
    visibility="Public",
    trusted=True
)

result = sdk.automatic_location_updates.update_emergency_location(
    request_body=request_body,
    account_id="~",
    location_id="locationId"
)

print(result)
```

## delete_emergency_location

Deletes the specified emergency response location.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-locations/{locationId}`

**Parameters**

| Name            | Type | Required | Description                                                                                                                                                  |
| :-------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| location_id     | str  | ✅       | Internal identifier of an emergency response location                                                                                                        |
| validate_only   | bool | ❌       | Flag indicating that validation of emergency location(s) is required before deletion                                                                         |
| new_location_id | str  | ❌       | Internal identifier of an emergency response location that should be used instead of a deleted one.                                                          |

**Return Type**

`GetLocationDeletionMultiResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.delete_emergency_location(
    account_id="~",
    location_id="locationId",
    validate_only=True,
    new_location_id="newLocationId"
)

print(result)
```

## get_extension_emergency_locations

Returns a list of emergency response locations available for the particular extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/emergency-locations`

**Parameters**

| Name                | Type                                                                                        | Required | Description                                                                                                                                                                                                       |
| :------------------ | :------------------------------------------------------------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str                                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                      |
| extension_id        | str                                                                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                                             |
| site_id             | List[str]                                                                                   | ❌       | Internal identifier of a site for filtering. To indicate company main site `main-site` value should be specified. Supported only if multi-site feature is enabled for the account. Multiple values are supported. |
| search_string       | str                                                                                         | ❌       | Filters entries by the specified substring (search by chassis ID, switch name or address) The characters range is 0-64 (if empty the filter is ignored)                                                           |
| domestic_country_id | str                                                                                         | ❌       |                                                                                                                                                                                                                   |
| order_by            | [GetExtensionEmergencyLocationsOrderBy](../models/GetExtensionEmergencyLocationsOrderBy.md) | ❌       | Comma-separated list of fields to order results prefixed by '+' sign (ascending order) or '-' sign (descending order). The default sorting is by `name`                                                           |
| per_page            | int                                                                                         | ❌       | Indicates a page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page                                                                    |
| page                | int                                                                                         | ❌       | Indicates a page number to retrieve. Only positive number values are supported                                                                                                                                    |
| visibility          | str                                                                                         | ❌       |                                                                                                                                                                                                                   |

**Return Type**

`EmergencyLocationsResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import GetExtensionEmergencyLocationsOrderBy

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_id=[
    "siteId"
]

result = sdk.automatic_location_updates.get_extension_emergency_locations(
    account_id="~",
    extension_id="~",
    site_id=site_id,
    search_string="searchString",
    domestic_country_id="domesticCountryId",
    order_by="+name",
    per_page=3,
    page=1,
    visibility="visibility"
)

print(result)
```

## create_extension_emergency_location

Creates a personal emergency response location for the current user.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/emergency-locations`

**Parameters**

| Name         | Type                                                                                  | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateUserEmergencyLocationRequest](../models/CreateUserEmergencyLocationRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`EmergencyLocationResponseResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateUserEmergencyLocationRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateUserEmergencyLocationRequest(
    name="name",
    address_format_id="addressFormatId",
    trusted=False,
    address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName"
    }
)

result = sdk.automatic_location_updates.create_extension_emergency_location(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## get_extension_emergency_location

Returns a personal emergency response location for the current user.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/emergency-locations/{locationId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| location_id  | str  | ✅       | Internal identifier of an emergency response location                                                                                                                 |

**Return Type**

`CommonEmergencyLocationResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.get_extension_emergency_location(
    account_id="~",
    extension_id="~",
    location_id="locationId"
)

print(result)
```

## update_extension_emergency_location

Updates a personal emergency response location by the current user or admin.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/emergency-locations/{locationId}`

**Parameters**

| Name         | Type                                                                              | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [EmergencyLocationRequestResource](../models/EmergencyLocationRequestResource.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                               | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| location_id  | str                                                                               | ✅       | Internal identifier of an emergency response location                                                                                                                 |

**Return Type**

`EmergencyLocationResponseResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EmergencyLocationRequestResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EmergencyLocationRequestResource(
    id_="id",
    address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName"
    },
    name="name",
    site={
        "id_": "id",
        "name": "name"
    },
    address_status="Valid",
    usage_status="Active",
    address_format_id="addressFormatId",
    visibility="Public",
    trusted=True
)

result = sdk.automatic_location_updates.update_extension_emergency_location(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    location_id="locationId"
)

print(result)
```

## delete_extension_emergency_location

Deletes a personal emergency response location by ID by the current user or admin. Multiple personal emergency response locations can be deleted by single API call.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/emergency-locations/{locationId}`

**Parameters**

| Name          | Type | Required | Description                                                                                                                                                           |
| :------------ | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id    | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id  | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| location_id   | str  | ✅       | Internal identifier of an emergency response location                                                                                                                 |
| validate_only | bool | ❌       | Flag indicating that only validation of Emergency Response Locations to be deleted is required                                                                        |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.delete_extension_emergency_location(
    account_id="~",
    extension_id="~",
    location_id="locationId",
    validate_only=True
)

print(result)
```

## read_automatic_location_updates_task

Returns results of the task created within the frame of Automatic Location Updates feature. Currently four task types are supported: 'Wireless Points Bulk Create', 'Wireless Points Bulk Update', 'Switches Bulk Create', 'Switches Bulk Update'.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/tasks/{taskId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| task_id    | str  | ✅       |                                                                                                                                                              |

**Return Type**

`AutomaticLocationUpdatesTaskInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.read_automatic_location_updates_task(
    account_id="~",
    task_id="taskId"
)

print(result)
```

## list_automatic_location_updates_users

Returns a list of users with their status of Automatic Location Updates feature.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/users`

**Parameters**

| Name            | Type                                                                                              | Required | Description                                                                                                                                                                                                                             |
| :-------------- | :------------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str                                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                            |
| type\_          | [List[ListAutomaticLocationUpdatesUsersType]](../models/ListAutomaticLocationUpdatesUsersType.md) | ❌       | Extension type. Multiple values are supported                                                                                                                                                                                           |
| search_string   | str                                                                                               | ❌       | Filters entries containing the specified substring in user name, extension or department. The characters range is 0-64; not case-sensitive. If empty then the filter is ignored                                                         |
| department      | List[str]                                                                                         | ❌       | Department name to filter the users. The value range is 0-64; not case-sensitive. If not specified then the parameter is ignored. Multiple values are supported                                                                         |
| site_id         | List[str]                                                                                         | ❌       | Internal identifier of a site for filtering. To indicate company main site `main-site` value should be specified. Supported only if multi-site feature is enabled for the account. Multiple values are supported.                       |
| feature_enabled | bool                                                                                              | ❌       | Filters entries by their status of Automatic Location Updates feature                                                                                                                                                                   |
| order_by        | str                                                                                               | ❌       | Comma-separated list of fields to order results prefixed by plus sign '+' (ascending order) or minus sign '-' (descending order). Supported values: 'name', 'modelName', 'siteName', 'featureEnabled'. The default sorting is by `name` |
| per_page        | int                                                                                               | ❌       | Indicates a page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page                                                                                          |
| page            | int                                                                                               | ❌       | Indicates a page number to retrieve. Only positive number values are supported                                                                                                                                                          |

**Return Type**

`AutomaticLocationUpdatesUserList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
type_=[
    "User"
]
department=[
    "department"
]
site_id=[
    "siteId"
]

result = sdk.automatic_location_updates.list_automatic_location_updates_users(
    account_id="~",
    type_=type_,
    search_string="searchString",
    department=department,
    site_id=site_id,
    feature_enabled=True,
    order_by="orderBy",
    per_page=6,
    page=1
)

print(result)
```

## assign_multiple_automatic_location_updates_users

Enables or disables Automatic Location Updates feature for multiple account users.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/users/bulk-assign`

**Parameters**

| Name         | Type                                                                                                                | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [EmergencyAddressAutoUpdateUsersBulkAssignResource](../models/EmergencyAddressAutoUpdateUsersBulkAssignResource.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EmergencyAddressAutoUpdateUsersBulkAssignResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EmergencyAddressAutoUpdateUsersBulkAssignResource(
    enabled_user_ids=[
        "enabledUserIds"
    ],
    disabled_user_ids=[
        "disabledUserIds"
    ]
)

result = sdk.automatic_location_updates.assign_multiple_automatic_location_updates_users(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## create_multiple_wireless_points

Creates multiple wireless points in a corporate map. The maximum number of wireless points per request is 10 000; limitation for account is 70 000.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points-bulk-create`

**Parameters**

| Name         | Type                                                                                    | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateMultipleWirelessPointsRequest](../models/CreateMultipleWirelessPointsRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CreateMultipleWirelessPointsResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateMultipleWirelessPointsRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateMultipleWirelessPointsRequest(
    records=[
        {
            "bssid": "bssid",
            "name": "name",
            "site": {
                "id_": "id",
                "name": "name"
            },
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip",
                "customer_name": "customerName",
                "sync_status": "Verified"
            },
            "emergency_location": {
                "id_": "id",
                "name": "name",
                "address_format_id": "addressFormatId"
            }
        }
    ]
)

result = sdk.automatic_location_updates.create_multiple_wireless_points(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_networks

Returns a corporate network map with emergency addresses assigned to the current account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks`

**Parameters**

| Name          | Type      | Required | Description                                                                                                                                                                                                       |
| :------------ | :-------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id    | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                      |
| site_id       | List[str] | ❌       | Internal identifier of a site for filtering. To indicate company main site `main-site` value should be specified. Supported only if multi-site feature is enabled for the account. Multiple values are supported. |
| search_string | str       | ❌       | Filters entries by the specified substring (search by chassis ID, switch name or address) The characters range is 0-64 (if empty the filter is ignored)                                                           |
| order_by      | str       | ❌       | Comma-separated list of fields to order results prefixed by '+' sign (ascending order) or '-' sign (descending order). The default sorting is by `name`                                                           |
| per_page      | int       | ❌       | Indicates a page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page'                                                                   |
| page          | int       | ❌       | Indicates a page number to retrieve. Only positive number values are supported                                                                                                                                    |

**Return Type**

`NetworksList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_id=[
    "siteId"
]

result = sdk.automatic_location_updates.list_networks(
    account_id="~",
    site_id=site_id,
    search_string="searchString",
    order_by="orderBy",
    per_page=2,
    page=1
)

print(result)
```

## create_network

Creates a new network in a corporate ethernet map for assignment of emergency addresses to network access points.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks`

**Parameters**

| Name         | Type                                                      | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateNetworkRequest](../models/CreateNetworkRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`NetworkInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateNetworkRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateNetworkRequest(
    name="name",
    site={
        "id_": "id",
        "uri": "uri",
        "name": "name",
        "code": "code"
    },
    public_ip_ranges=[
        {
            "id_": "id",
            "start_ip": "startIp",
            "end_ip": "endIp",
            "matched": True
        }
    ],
    private_ip_ranges=[
        {
            "id_": "id",
            "start_ip": "startIp",
            "end_ip": "endIp",
            "name": "name",
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "customer_name": "customerName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip"
            },
            "emergency_location_id": "emergencyLocationId",
            "emergency_location": {
                "id_": "id",
                "name": "name",
                "address_format_id": "addressFormatId"
            }
        }
    ]
)

result = sdk.automatic_location_updates.create_network(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_network

Returns the specified network with emergency addresses assigned to the current account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks/{networkId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| network_id | str  | ✅       | Internal identifier of a network                                                                                                                             |

**Return Type**

`NetworkInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.read_network(
    account_id="~",
    network_id="networkId"
)

print(result)
```

## update_network

Updates a network in a corporate ethernet map for assignment of emergency addresses to network access points.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks/{networkId}`

**Parameters**

| Name         | Type                                                      | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateNetworkRequest](../models/UpdateNetworkRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| network_id   | str                                                       | ✅       | Internal identifier of a network                                                                                                                             |

**Return Type**

`NetworkInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateNetworkRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateNetworkRequest(
    id_="2874044",
    name="name",
    site={
        "id_": "id",
        "uri": "uri",
        "name": "name",
        "code": "code"
    },
    public_ip_ranges=[
        {
            "id_": "id",
            "start_ip": "startIp",
            "end_ip": "endIp",
            "matched": True
        }
    ],
    private_ip_ranges=[
        {
            "id_": "id",
            "start_ip": "startIp",
            "end_ip": "endIp",
            "name": "name",
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "customer_name": "customerName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip"
            },
            "emergency_location_id": "emergencyLocationId",
            "emergency_location": {
                "id_": "id",
                "name": "name",
                "address_format_id": "addressFormatId"
            }
        }
    ]
)

result = sdk.automatic_location_updates.update_network(
    request_body=request_body,
    account_id="~",
    network_id="networkId"
)

print(result)
```

## delete_network

Deletes network(s) in a corporate ethernet map for Automatic Location Updates feature.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/networks/{networkId}`

**Parameters**

| Name       | Type      | Required | Description                                                                                                                                                  |
| :--------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| network_id | List[str] | ✅       | Internal identifier of a network                                                                                                                             |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
network_id=[
    "networkId"
]

result = sdk.automatic_location_updates.delete_network(
    account_id="~",
    network_id=network_id
)

print(result)
```

## validate_multiple_switches

Validates switches before creation or update. The maximum number of switches per request is 10 000.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches-bulk-validate`

**Parameters**

| Name         | Type                                                                            | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ValidateMultipleSwitchesRequest](../models/ValidateMultipleSwitchesRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`ValidateMultipleSwitchesResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ValidateMultipleSwitchesRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ValidateMultipleSwitchesRequest(
    records=[
        {
            "uri": "uri",
            "id_": "id",
            "chassis_id": "chassisId",
            "port": "port",
            "name": "name",
            "site": {
                "id_": "id",
                "name": "name"
            },
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip",
                "customer_name": "customerName",
                "sync_status": "Verified"
            },
            "emergency_location": {
                "id_": "id",
                "name": "name",
                "address_format_id": "addressFormatId"
            }
        }
    ]
)

result = sdk.automatic_location_updates.validate_multiple_switches(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_account_switches

Returns a corporate map of configured network switches with the assigned emergency addresses for the logged-in account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches`

**Parameters**

| Name          | Type      | Required | Description                                                                                                                                                                                                       |
| :------------ | :-------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id    | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                      |
| site_id       | List[str] | ❌       | Internal identifier of a site for filtering. To indicate company main site `main-site` value should be specified. Supported only if multi-site feature is enabled for the account. Multiple values are supported. |
| search_string | str       | ❌       | Filters entries by the specified substring (search by chassis ID, switch name or address) The characters range is 0-64 (if empty the filter is ignored)                                                           |
| order_by      | str       | ❌       | Comma-separated list of fields to order results prefixed by '+' sign (ascending order) or '-' sign (descending order). The default sorting is by `name`                                                           |
| per_page      | int       | ❌       | Indicates a page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page'                                                                   |
| page          | int       | ❌       | Indicates a page number to retrieve. Only positive number values are supported                                                                                                                                    |

**Return Type**

`SwitchesList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_id=[
    "siteId"
]

result = sdk.automatic_location_updates.list_account_switches(
    account_id="~",
    site_id=site_id,
    search_string="searchString",
    order_by="orderBy",
    per_page=10,
    page=1
)

print(result)
```

## create_switch

Creates a new switch in corporate map based on chassis ID and used for Automatic Locations Update feature.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches`

**Parameters**

| Name         | Type                                              | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateSwitchInfo](../models/CreateSwitchInfo.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`SwitchInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateSwitchInfo

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateSwitchInfo(
    chassis_id="chassisId",
    port="port",
    name="name",
    site={
        "id_": "id",
        "name": "name"
    },
    emergency_address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName",
        "sync_status": "Verified"
    },
    emergency_location={
        "id_": "id",
        "name": "name",
        "address_format_id": "addressFormatId"
    }
)

result = sdk.automatic_location_updates.create_switch(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_switch

Returns the specified switch with the assigned emergency address.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches/{switchId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| switch_id  | str  | ✅       |                                                                                                                                                              |

**Return Type**

`SwitchInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.read_switch(
    account_id="~",
    switch_id="switchId"
)

print(result)
```

## update_switch

Updates switch. Partial update is not supported, all switch parameters should be specified. If null value is received or parameter is missing, its value is removed.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches/{switchId}`

**Parameters**

| Name         | Type                                              | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateSwitchInfo](../models/UpdateSwitchInfo.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| switch_id    | str                                               | ✅       |                                                                                                                                                              |

**Return Type**

`SwitchInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateSwitchInfo

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateSwitchInfo(
    id_="id",
    chassis_id="chassisId",
    port="port",
    name="name",
    site={
        "id_": "id",
        "name": "name"
    },
    emergency_address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName",
        "sync_status": "Verified"
    }
)

result = sdk.automatic_location_updates.update_switch(
    request_body=request_body,
    account_id="~",
    switch_id="switchId"
)

print(result)
```

## delete_switch

Deletes wireless switch(es) in a network configuration for Automatic Location Updates feature.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches/{switchId}`

**Parameters**

| Name       | Type      | Required | Description                                                                                                                                                  |
| :--------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| switch_id  | List[str] | ✅       |                                                                                                                                                              |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
switch_id=[
    "switchId"
]

result = sdk.automatic_location_updates.delete_switch(
    account_id="~",
    switch_id=switch_id
)

print(result)
```

## validate_multiple_wireless_points

Validates wireless points before creation or update. The maximum number of wireless points per request is 10 000.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points-bulk-validate`

**Parameters**

| Name         | Type                                                                                        | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ValidateMultipleWirelessPointsRequest](../models/ValidateMultipleWirelessPointsRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`ValidateMultipleWirelessPointsResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ValidateMultipleWirelessPointsRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ValidateMultipleWirelessPointsRequest(
    records=[
        {
            "uri": "uri",
            "id_": "id",
            "bssid": "bssid",
            "name": "name",
            "site": {
                "id_": "id",
                "name": "name"
            },
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip",
                "customer_name": "customerName",
                "sync_status": "Verified"
            },
            "emergency_location": {
                "id_": "id",
                "name": "name",
                "address_format_id": "addressFormatId"
            },
            "emergency_location_id": "emergencyLocationId"
        }
    ]
)

result = sdk.automatic_location_updates.validate_multiple_wireless_points(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_wireless_points

Returns account wireless points configured and used for Automatic Location Updates feature.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points`

**Parameters**

| Name          | Type      | Required | Description                                                                                                                                                                                                       |
| :------------ | :-------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id    | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                      |
| site_id       | List[str] | ❌       | Internal identifier of a site for filtering. To indicate company main site `main-site` value should be specified. Supported only if multi-site feature is enabled for the account. Multiple values are supported. |
| search_string | str       | ❌       | Filters entries by the specified substring (search by chassis ID, switch name or address) The characters range is 0-64 (if empty the filter is ignored)                                                           |
| order_by      | str       | ❌       | Comma-separated list of fields to order results prefixed by '+' sign (ascending order) or '-' sign (descending order).The default sorting is by `name`                                                            |
| per_page      | int       | ❌       | Indicates a page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page                                                                    |
| page          | int       | ❌       | Indicates the page number to retrieve. Only positive number values are supported                                                                                                                                  |

**Return Type**

`WirelessPointsList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_id=[
    "siteId"
]

result = sdk.automatic_location_updates.list_wireless_points(
    account_id="~",
    site_id=site_id,
    search_string="searchString",
    order_by="orderBy",
    per_page=0,
    page=1
)

print(result)
```

## create_wireless_point

Creates a new wireless point in network configuration with the emergency address assigned.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points`

**Parameters**

| Name         | Type                                                    | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateWirelessPoint](../models/CreateWirelessPoint.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`WirelessPointInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateWirelessPoint

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateWirelessPoint(
    bssid="bssid",
    name="name",
    site={
        "id_": "id",
        "name": "name"
    },
    emergency_address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName",
        "sync_status": "Verified"
    },
    emergency_location={
        "id_": "id",
        "name": "name",
        "address_format_id": "addressFormatId"
    }
)

result = sdk.automatic_location_updates.create_wireless_point(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_wireless_point

Returns the specified wireless access point of a corporate map with the emergency address assigned.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points/{pointId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| point_id   | str  | ✅       | Internal identifier of a point                                                                                                                               |

**Return Type**

`WirelessPointInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.automatic_location_updates.read_wireless_point(
    account_id="~",
    point_id="pointId"
)

print(result)
```

## update_wireless_point

Updates the specified wireless access point of a corporate map by ID.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points/{pointId}`

**Parameters**

| Name         | Type                                                    | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateWirelessPoint](../models/UpdateWirelessPoint.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| point_id     | str                                                     | ✅       | Internal identifier of a wireless point                                                                                                                      |

**Return Type**

`WirelessPointInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateWirelessPoint

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateWirelessPoint(
    id_="id",
    bssid="bssid",
    name="name",
    site={
        "id_": "id",
        "name": "name"
    },
    emergency_address={
        "country": "country",
        "country_id": "countryId",
        "country_iso_code": "countryIsoCode",
        "country_name": "countryName",
        "state": "state",
        "state_id": "stateId",
        "state_iso_code": "stateIsoCode",
        "state_name": "stateName",
        "city": "city",
        "street": "street",
        "street2": "street2",
        "zip": "zip",
        "customer_name": "customerName",
        "sync_status": "Verified"
    }
)

result = sdk.automatic_location_updates.update_wireless_point(
    request_body=request_body,
    account_id="~",
    point_id="pointId"
)

print(result)
```

## delete_wireless_point

Deletes wireless point(s) of a corporate map by ID(s).

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points/{pointId}`

**Parameters**

| Name       | Type      | Required | Description                                                                                                                                                  |
| :--------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| point_id   | List[str] | ✅       | Internal identifier of a wireless point                                                                                                                      |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
point_id=[
    "pointId"
]

result = sdk.automatic_location_updates.delete_wireless_point(
    account_id="~",
    point_id=point_id
)

print(result)
```

## list_devices_automatic_location_updates

Returns a list of common devices with their status of Automatic Location Updates feature.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/devices`

**Parameters**

| Name            | Type      | Required | Description                                                                                                                                                                                                                             |
| :-------------- | :-------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                            |
| site_id         | List[str] | ❌       | Internal identifier of a site for filtering. To indicate company main site `main-site` value should be specified. Supported only if multi-site feature is enabled for the account. Multiple values are supported.                       |
| feature_enabled | bool      | ❌       | Filters entries by their status of Automatic Location Updates feature                                                                                                                                                                   |
| model_id        | str       | ❌       | Internal identifier of a device model for filtering. Multiple values are supported                                                                                                                                                      |
| compatible_only | bool      | ❌       | Filters devices which support HELD protocol                                                                                                                                                                                             |
| search_string   | str       | ❌       | Filters entries which have device name or model name containing the mentioned substring. The value should be split by spaces; the range is 0 - 64 characters, not case-sensitive. If empty the filter is ignored                        |
| order_by        | str       | ❌       | Comma-separated list of fields to order results prefixed by plus sign '+' (ascending order) or minus sign '-' (descending order). Supported values: 'name', 'modelName', 'siteName', 'featureEnabled'. The default sorting is by `name` |
| per_page        | int       | ❌       | Indicates a page size (number of items). The values supported: `Max` or numeric value. If not specified, 100 records are returned per one page                                                                                          |
| page            | int       | ❌       | Indicates a page number to retrieve. Only positive number values are supported                                                                                                                                                          |

**Return Type**

`ListDevicesAutomaticLocationUpdates`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_id=[
    "siteId"
]

result = sdk.automatic_location_updates.list_devices_automatic_location_updates(
    account_id="~",
    site_id=site_id,
    feature_enabled=False,
    model_id="modelId",
    compatible_only=True,
    search_string="searchString",
    order_by="orderBy",
    per_page=4,
    page=1
)

print(result)
```

## assign_multiple_devices_automatic_location_updates

Enables or disables Automatic Location Updates feature for the specified common phones.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/devices/bulk-assign`

**Parameters**

| Name         | Type                                                                                                        | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AssignMultipleDevicesAutomaticLocationUpdates](../models/AssignMultipleDevicesAutomaticLocationUpdates.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AssignMultipleDevicesAutomaticLocationUpdates

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AssignMultipleDevicesAutomaticLocationUpdates(
    enabled_device_ids=[
        "enabledDeviceIds"
    ],
    disabled_device_ids=[
        "disabledDeviceIds"
    ]
)

result = sdk.automatic_location_updates.assign_multiple_devices_automatic_location_updates(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## create_multiple_switches

Creates multiple switches in corporate map. The maximum number of switches per request is 10 000; limitation for account is 10 000.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches-bulk-create`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateMultipleSwitchesRequest](../models/CreateMultipleSwitchesRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CreateMultipleSwitchesResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateMultipleSwitchesRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateMultipleSwitchesRequest(
    records=[
        {
            "chassis_id": "chassisId",
            "port": "port",
            "name": "name",
            "site": {
                "id_": "id",
                "name": "name"
            },
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip",
                "customer_name": "customerName",
                "sync_status": "Verified"
            },
            "emergency_location": {
                "id_": "id",
                "name": "name",
                "address_format_id": "addressFormatId"
            }
        }
    ]
)

result = sdk.automatic_location_updates.create_multiple_switches(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## update_multiple_wireless_points

Updates wireless points in corporate map. The maximum number of wireless points per request is 10 000; limitation for account is 70 000.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/wireless-points-bulk-update`

**Parameters**

| Name         | Type                                                                                    | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateMultipleWirelessPointsRequest](../models/UpdateMultipleWirelessPointsRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`UpdateMultipleWirelessPointsResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateMultipleWirelessPointsRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateMultipleWirelessPointsRequest(
    records=[
        {
            "id_": "id",
            "bssid": "bssid",
            "name": "name",
            "site": {
                "id_": "id",
                "name": "name"
            },
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip",
                "customer_name": "customerName",
                "sync_status": "Verified"
            }
        }
    ]
)

result = sdk.automatic_location_updates.update_multiple_wireless_points(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## update_multiple_switches

Updates multiple switches in corporate map. The maximum number of switches per request is 10 000; limitation for account is 10 000.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/emergency-address-auto-update/switches-bulk-update`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateMultipleSwitchesRequest](../models/UpdateMultipleSwitchesRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`UpdateMultipleSwitchesResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateMultipleSwitchesRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateMultipleSwitchesRequest(
    records=[
        {
            "id_": "id",
            "chassis_id": "chassisId",
            "port": "port",
            "name": "name",
            "site": {
                "id_": "id",
                "name": "name"
            },
            "emergency_address": {
                "country": "country",
                "country_id": "countryId",
                "country_iso_code": "countryIsoCode",
                "country_name": "countryName",
                "state": "state",
                "state_id": "stateId",
                "state_iso_code": "stateIsoCode",
                "state_name": "stateName",
                "city": "city",
                "street": "street",
                "street2": "street2",
                "zip": "zip",
                "customer_name": "customerName",
                "sync_status": "Verified"
            }
        }
    ]
)

result = sdk.automatic_location_updates.update_multiple_switches(
    request_body=request_body,
    account_id="~"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
