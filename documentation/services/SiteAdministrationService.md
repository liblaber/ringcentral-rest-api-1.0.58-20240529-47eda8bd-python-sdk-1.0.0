# SiteAdministrationService

A list of all methods in the `SiteAdministrationService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                               |
| :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| [list_administered_sites](#list_administered_sites)               | Returns a list of sites administered by the current user.                                                 |
| [update_user_administered_sites](#update_user_administered_sites) | Updates the sites administered by the current user. Please note: Only IDs of records are used for update. |

## list_administered_sites

Returns a list of sites administered by the current user.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/administered-sites`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`BusinessSiteCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.site_administration.list_administered_sites(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_user_administered_sites

Updates the sites administered by the current user. Please note: Only IDs of records are used for update.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/administered-sites`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [BusinessSiteCollectionRequest](../models/BusinessSiteCollectionRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`BusinessSiteCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BusinessSiteCollectionRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BusinessSiteCollectionRequest(
    records=[
        {
            "uri": "uri",
            "id_": "id",
            "email": "email",
            "code": "code",
            "name": "name",
            "extension_number": "extensionNumber",
            "caller_id_name": "callerIdName",
            "operator": {
                "id_": "id",
                "name": "name",
                "extension_number": "extensionNumber"
            },
            "regional_settings": {
                "timezone": {
                    "uri": "uri",
                    "id_": "id",
                    "name": "name",
                    "description": "description",
                    "bias": "bias"
                },
                "home_country": {
                    "uri": "uri",
                    "id_": "id",
                    "name": "name",
                    "iso_code": "isoCode",
                    "calling_code": "callingCode",
                    "emergency_calling": True,
                    "number_selling": True,
                    "login_allowed": True,
                    "free_softphone_line": True,
                    "signup_allowed": False
                },
                "language": {
                    "id_": "id",
                    "name": "name",
                    "locale_code": "localeCode"
                },
                "greeting_language": {
                    "id_": "id",
                    "name": "name",
                    "locale_code": "localeCode"
                },
                "formatting_locale": {
                    "id_": "id",
                    "name": "name",
                    "locale_code": "localeCode"
                },
                "time_format": "12h",
                "currency": {
                    "id_": "id",
                    "code": "code",
                    "name": "name",
                    "symbol": "symbol",
                    "minor_symbol": "minorSymbol"
                }
            },
            "business_address": {
                "street": "street",
                "city": "city",
                "state": "state",
                "zip": "zip",
                "country": "country"
            }
        }
    ]
)

result = sdk.site_administration.update_user_administered_sites(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
