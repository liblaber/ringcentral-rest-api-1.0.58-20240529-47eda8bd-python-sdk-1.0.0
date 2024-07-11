# MultiSiteService

A list of all methods in the `MultiSiteService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                             |
| :---------------------------------------------------- | :------------------------------------------------------ |
| [list_sites](#list_sites)                             | Returns a list of sites for the specified account.      |
| [create_site](#create_site)                           | Creates a site for the specified account.               |
| [read_site](#read_site)                               | Returns a site by ID.                                   |
| [update_site](#update_site)                           | Updates a site specified in path.                       |
| [delete_site](#delete_site)                           | Deletes a site specified in path.                       |
| [assign_multiple_sites](#assign_multiple_sites)       | Assigns multiple sites to an account specified in path. |
| [list_site_members](#list_site_members)               | Returns members of a site specified in path.            |
| [read_site_ivr_settings](#read_site_ivr_settings)     | Returns IVR settings for a site specified in path.      |
| [update_site_ivr_settings](#update_site_ivr_settings) | Updates IVR settings for a site specified in path.      |

## list_sites

Returns a list of sites for the specified account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`SitesList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.multi_site.list_sites(account_id="~")

print(result)
```

## create_site

Creates a site for the specified account.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites`

**Parameters**

| Name         | Type                                                | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateSiteRequest](../models/CreateSiteRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`SiteInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateSiteRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateSiteRequest(
    name="name",
    extension_number="extensionNumber",
    caller_id_name="callerIdName",
    email="email",
    business_address={
        "country": "country",
        "state": "state",
        "city": "city",
        "street": "street",
        "zip": "zip"
    },
    regional_settings={
        "home_country": {
            "id_": "id",
            "uri": "uri",
            "name": "name",
            "iso_code": "isoCode",
            "calling_code": "callingCode"
        },
        "timezone": {
            "id_": "id",
            "uri": "uri",
            "name": "name",
            "description": "description",
            "bias": "bias"
        },
        "language": {
            "id_": "id",
            "locale_code": "localeCode",
            "name": "name"
        },
        "greeting_language": {
            "id_": "id",
            "locale_code": "localeCode",
            "name": "name"
        },
        "formatting_locale": {
            "id_": "id",
            "locale_code": "localeCode",
            "name": "name"
        },
        "time_format": "12h"
    },
    operator={
        "id_": "id"
    },
    code="code"
)

result = sdk.multi_site.create_site(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_site

Returns a site by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites/{siteId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_id    | str  | ✅       | Internal identifier of a site. _Please note_ that `siteId` cannot take the 'main-site' value                                                                 |

**Return Type**

`SiteInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.multi_site.read_site(
    account_id="~",
    site_id="siteId"
)

print(result)
```

## update_site

Updates a site specified in path.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites/{siteId}`

**Parameters**

| Name         | Type                                                | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [SiteUpdateRequest](../models/SiteUpdateRequest.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_id      | str                                                 | ✅       | Internal identifier of a site. _Please note_ that `siteId` cannot take the 'main-site' value                                                                 |

**Return Type**

`SiteInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SiteUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SiteUpdateRequest(
    name="name",
    extension_number="extensionNumber",
    caller_id_name="callerIdName",
    email="email",
    business_address={
        "country": "country",
        "state": "state",
        "city": "city",
        "street": "street",
        "zip": "zip"
    },
    regional_settings={
        "home_country": {
            "id_": "id",
            "uri": "uri",
            "name": "name",
            "iso_code": "isoCode",
            "calling_code": "callingCode"
        },
        "timezone": {
            "id_": "id",
            "uri": "uri",
            "name": "name",
            "description": "description",
            "bias": "bias"
        },
        "language": {
            "id_": "id",
            "locale_code": "localeCode",
            "name": "name"
        },
        "greeting_language": {
            "id_": "id",
            "locale_code": "localeCode",
            "name": "name"
        },
        "formatting_locale": {
            "id_": "id",
            "locale_code": "localeCode",
            "name": "name"
        },
        "time_format": "12h"
    },
    operator={
        "id_": "id",
        "uri": "uri",
        "extension_number": "extensionNumber",
        "name": "name"
    }
)

result = sdk.multi_site.update_site(
    request_body=request_body,
    account_id="~",
    site_id="siteId"
)

print(result)
```

## delete_site

Deletes a site specified in path.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites/{siteId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_id    | str  | ✅       | Internal identifier of a site. _Please note_ that `siteId` cannot take the 'main-site' value                                                                 |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.multi_site.delete_site(
    account_id="~",
    site_id="siteId"
)

print(result)
```

## assign_multiple_sites

Assigns multiple sites to an account specified in path.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites/{siteId}/bulk-assign`

**Parameters**

| Name         | Type                                                        | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [SiteMembersBulkUpdate](../models/SiteMembersBulkUpdate.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_id      | str                                                         | ✅       | Internal identifier of a site. _Please note_ that `siteId` cannot take the 'main-site' value                                                                 |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SiteMembersBulkUpdate

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SiteMembersBulkUpdate(
    removed_extension_ids=[
        "removedExtensionIds"
    ],
    added_extension_ids=[
        "addedExtensionIds"
    ]
)

result = sdk.multi_site.assign_multiple_sites(
    request_body=request_body,
    account_id="~",
    site_id="siteId"
)

print(result)
```

## list_site_members

Returns members of a site specified in path.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites/{siteId}/members`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_id    | str  | ✅       | Internal identifier of a site. _Please note_ that `siteId` cannot take the 'main-site' value                                                                 |

**Return Type**

`SiteMembersList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.multi_site.list_site_members(
    account_id="~",
    site_id="siteId"
)

print(result)
```

## read_site_ivr_settings

Returns IVR settings for a site specified in path.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites/{siteId}/ivr`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_id    | str  | ✅       | Internal identifier of a site. _Please note_ that `siteId` cannot take the 'main-site' value                                                                 |

**Return Type**

`SiteIvrSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.multi_site.read_site_ivr_settings(
    account_id="~",
    site_id="siteId"
)

print(result)
```

## update_site_ivr_settings

Updates IVR settings for a site specified in path.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/sites/{siteId}/ivr`

**Parameters**

| Name         | Type                                                        | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [SiteIvrSettingsUpdate](../models/SiteIvrSettingsUpdate.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_id      | str                                                         | ✅       | Internal identifier of a site. _Please note_ that `siteId` cannot take the 'main-site' value                                                                 |

**Return Type**

`SiteIvrSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SiteIvrSettingsUpdate

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SiteIvrSettingsUpdate(
    top_menu={
        "id_": "id"
    },
    actions=[
        {
            "input": "Star",
            "action": "Repeat",
            "extension": {
                "id_": "id"
            }
        }
    ]
)

result = sdk.multi_site.update_site_ivr_settings(
    request_body=request_body,
    account_id="~",
    site_id="siteId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
