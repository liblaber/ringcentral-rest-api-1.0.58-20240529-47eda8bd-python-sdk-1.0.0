# UserSettingsService

A list of all methods in the `UserSettingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                                                                                                                                                                 |
| :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_scaled_profile_image](#read_scaled_profile_image)           | Returns the scaled profile image of an extension. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**                                                                                                                                 |
| [post_batch_provision_users](#post_batch_provision_users)         | Creates multiple user extensions with BYOD (customer provided) devices. If "extensionNumber" is not specified, the next available extension number will be assigned.                                                                                                        |
| [bulk_delete_users_v2](#bulk_delete_users_v2)                     | Deletes user extension(s) and either keeps or destroys the assets - numbers and devices. Multiple extensions can be deleted with a single API call. **Please note:** This API cannot be tested on Sandbox.                                                                  |
| [read_extension](#read_extension)                                 | Returns basic information about a particular extension of an account.                                                                                                                                                                                                       |
| [update_extension](#update_extension)                             | Updates the user settings.                                                                                                                                                                                                                                                  |
| [list_extension_grants](#list_extension_grants)                   | Returns the list of extensions with information on grants given to the current extension regarding them. Currently the list of grants include: picking up a call, monitoring, calling or receiving a call on behalf of somebody, call delegation and calling paging groups. |
| [read_conferencing_settings](#read_conferencing_settings)         | Returns information on Free Conference Calling (FCC) feature for a given extension.                                                                                                                                                                                         |
| [update_conferencing_settings](#update_conferencing_settings)     | Updates the default conferencing number for the current extension. The number can be selected from conferencing numbers of the current extension. Updates the setting, allowing participants join the conference before host.                                               |
| [read_user_profile_image_legacy](#read_user_profile_image_legacy) | Returns a profile image of an extension.                                                                                                                                                                                                                                    |
| [create_user_profile_image](#create_user_profile_image)           | Uploads the extension profile image.                                                                                                                                                                                                                                        |
| [update_user_profile_image](#update_user_profile_image)           | Updates the extension profile image.                                                                                                                                                                                                                                        |
| [delete_user_profile_image](#delete_user_profile_image)           | Deletes the user profile image.                                                                                                                                                                                                                                             |
| [read_extension_caller_id](#read_extension_caller_id)             | Returns information on an outbound caller ID of an extension.                                                                                                                                                                                                               |
| [update_extension_caller_id](#update_extension_caller_id)         | Updates outbound caller ID information of an extension.                                                                                                                                                                                                                     |
| [read_notification_settings](#read_notification_settings)         | Returns notification settings for the current extension. Knowledge Article: [User Settings - Set Up Message Notifications](https://success.ringcentral.com/articles/RC_Knowledge_Article/9740)                                                                              |
| [update_notification_settings](#update_notification_settings)     | Updates notification settings for the current extension. Knowledge Article: [User Settings - Set Up Message Notifications](https://success.ringcentral.com/articles/RC_Knowledge_Article/9740)                                                                              |

## read_scaled_profile_image

Returns the scaled profile image of an extension. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image/{scaleSize}`

**Parameters**

| Name                         | Type                                                  | Required | Description                                                                                                                                                           |
| :--------------------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id                   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id                 | str                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| scale_size                   | [ScaleSize](../models/ScaleSize.md)                   | ✅       | Dimensions of a profile image which will be returned in response.                                                                                                     |
| content_disposition          | [ContentDisposition](../models/ContentDisposition.md) | ❌       | Whether the content is expected to be displayed in the browser, or downloaded and saved locally                                                                       |
| content_disposition_filename | str                                                   | ❌       | The default filename of the file to be downloaded                                                                                                                     |

**Return Type**

`bytes`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ScaleSize, ContentDisposition

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.read_scaled_profile_image(
    account_id="~",
    extension_id="~",
    scale_size="original",
    content_disposition="Inline",
    content_disposition_filename="contentDispositionFilename"
)

with open("output-file.ext", "wb") as f:
    f.write(result)
```

## post_batch_provision_users

Creates multiple user extensions with BYOD (customer provided) devices. If "extensionNumber" is not specified, the next available extension number will be assigned.

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/batch-provisioning/users`

**Parameters**

| Name         | Type                                                                  | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [BatchProvisionUsersRequest](../models/BatchProvisionUsersRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`BatchProvisionUsersResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BatchProvisionUsersRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BatchProvisionUsersRequest(
    records=[
        {
            "extension_number": "205",
            "status": "Enabled",
            "contact": {
                "first_name": "John",
                "last_name": "Smith",
                "email": "john.smith@acme.com",
                "mobile_number": "+16501234567",
                "email_as_login_name": True
            },
            "cost_center": {
                "id_": "224149"
            },
            "roles": [
                {
                    "id_": "1"
                }
            ],
            "devices": [
                {
                    "device_info": {
                        "type_": "OtherPhone",
                        "emergency": {
                            "address": {
                                "street": "20 Davis Dr",
                                "street2": "nostrud",
                                "city": "Belmont",
                                "state": "CA",
                                "zip": "94002",
                                "country": "US"
                            }
                        },
                        "phone_info": {
                            "toll_type": "Toll"
                        }
                    }
                }
            ],
            "send_welcome_email": True
        }
    ]
)

result = sdk.user_settings.post_batch_provision_users(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## bulk_delete_users_v2

Deletes user extension(s) and either keeps or destroys the assets - numbers and devices. Multiple extensions can be deleted with a single API call. **Please note:** This API cannot be tested on Sandbox.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v2/accounts/{accountId}/extensions`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [BulkDeleteUsersRequest](../models/BulkDeleteUsersRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`BulkDeleteUsersResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BulkDeleteUsersRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BulkDeleteUsersRequest(
    keep_assets_in_inventory=True,
    records=[
        {
            "id_": "12345"
        }
    ]
)

result = sdk.user_settings.bulk_delete_users_v2(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_extension

Returns basic information about a particular extension of an account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`GetExtensionInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.read_extension(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_extension

Updates the user settings.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ExtensionUpdateRequest](../models/ExtensionUpdateRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`GetExtensionInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ExtensionUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ExtensionUpdateRequest(
    status="Disabled",
    status_info={
        "comment": "comment",
        "reason": "SuspendedVoluntarily",
        "till": "till"
    },
    extension_number="extensionNumber",
    contact={
        "first_name": "firstName",
        "last_name": "lastName",
        "company": "company",
        "job_title": "jobTitle",
        "email": "email",
        "business_phone": "businessPhone",
        "mobile_phone": "mobilePhone",
        "business_address": {
            "country": "country",
            "state": "state",
            "city": "city",
            "street": "street",
            "zip": "zip"
        },
        "email_as_login_name": False,
        "pronounced_name": {
            "type_": "Default",
            "text": "text",
            "prompt": {
                "id_": "id",
                "content_uri": "contentUri",
                "content_type": "audio/mpeg"
            }
        },
        "department": "department"
    },
    regional_settings={
        "home_country": {
            "id_": "id"
        },
        "timezone": {
            "id_": "id"
        },
        "language": {
            "id_": "id"
        },
        "greeting_language": {
            "id_": "id"
        },
        "formatting_locale": {
            "id_": "id"
        },
        "currency": {
            "id_": "id"
        },
        "time_format": "12h"
    },
    setup_wizard_state="NotStarted",
    partner_id="partnerId",
    ivr_pin="ivrPin",
    password="password",
    call_queue_info={
        "sla_goal": 0,
        "sla_threshold_seconds": 7,
        "include_abandoned_calls": False,
        "abandoned_threshold_seconds": 10
    },
    transition={
        "send_welcome_emails_to_users": True,
        "send_welcome_email": True
    },
    custom_fields=[
        {
            "id_": "id",
            "value": "value",
            "display_name": "displayName"
        }
    ],
    site={
        "id_": "id"
    },
    type_="User",
    sub_type="VideoPro",
    references=[
        {
            "ref": "ref",
            "type_": "PartnerId",
            "ref_acc_id": "refAccId"
        }
    ]
)

result = sdk.user_settings.update_extension(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## list_extension_grants

Returns the list of extensions with information on grants given to the current extension regarding them. Currently the list of grants include: picking up a call, monitoring, calling or receiving a call on behalf of somebody, call delegation and calling paging groups.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/grant`

**Parameters**

| Name           | Type                                        | Required | Description                                                                                                                                                                                           |
| :------------- | :------------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id     | str                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                          |
| extension_id   | str                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                                 |
| extension_type | [ExtensionType](../models/ExtensionType.md) | ❌       | Type of extension to be returned. Multiple values are supported. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology |
| page           | int                                         | ❌       | Indicates a page number to retrieve. Only positive number values are allowed                                                                                                                          |
| per_page       | int                                         | ❌       | Indicates a page size (number of items)                                                                                                                                                               |

**Return Type**

`GetExtensionGrantListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ExtensionType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.list_extension_grants(
    account_id="~",
    extension_id="~",
    extension_type="User",
    page=1,
    per_page=100
)

print(result)
```

## read_conferencing_settings

Returns information on Free Conference Calling (FCC) feature for a given extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/conferencing`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| country_id   | str  | ❌       | Internal identifier of a country. If not specified, the response is returned for the brand country                                                                    |

**Return Type**

`GetConferencingInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.read_conferencing_settings(
    account_id="~",
    extension_id="~",
    country_id="countryId"
)

print(result)
```

## update_conferencing_settings

Updates the default conferencing number for the current extension. The number can be selected from conferencing numbers of the current extension. Updates the setting, allowing participants join the conference before host.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/conferencing`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateConferencingInfoRequest](../models/UpdateConferencingInfoRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`GetConferencingInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateConferencingInfoRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateConferencingInfoRequest(
    phone_numbers=[
        {
            "phone_number": "phoneNumber",
            "default": True
        }
    ],
    allow_join_before_host=False
)

result = sdk.user_settings.update_conferencing_settings(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_user_profile_image_legacy

Returns a profile image of an extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`bytes`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.read_user_profile_image_legacy(
    account_id="~",
    extension_id="~"
)

with open("output-image.png", "wb") as f:
    f.write(result)
```

## create_user_profile_image

Uploads the extension profile image.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image`

**Parameters**

| Name         | Type                      | Required | Description                                                                                                                                                           |
| :----------- | :------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [dict](../models/dict.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateUserProfileImageRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "image": "image"
}

result = sdk.user_settings.create_user_profile_image(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_user_profile_image

Updates the extension profile image.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image`

**Parameters**

| Name         | Type                      | Required | Description                                                                                                                                                           |
| :----------- | :------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [dict](../models/dict.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateUserProfileImageRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "image": "image"
}

result = sdk.user_settings.update_user_profile_image(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## delete_user_profile_image

Deletes the user profile image.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/profile-image`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.delete_user_profile_image(
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_extension_caller_id

Returns information on an outbound caller ID of an extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-id`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`ExtensionCallerIdInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.read_extension_caller_id(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_extension_caller_id

Updates outbound caller ID information of an extension.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-id`

**Parameters**

| Name         | Type                                                                      | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ExtensionCallerIdInfoRequest](../models/ExtensionCallerIdInfoRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`ExtensionCallerIdInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ExtensionCallerIdInfoRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ExtensionCallerIdInfoRequest(
    uri="uri",
    by_device=[
        {
            "device": {
                "id_": "id"
            },
            "caller_id": {
                "type_": "type",
                "phone_info": {
                    "id_": "id"
                }
            }
        }
    ],
    by_feature=[
        {
            "feature": "RingOut",
            "caller_id": {
                "type_": "type",
                "phone_info": {
                    "id_": "id"
                }
            }
        }
    ],
    extension_name_for_outbound_calls=False,
    extension_number_for_internal_calls=False
)

result = sdk.user_settings.update_extension_caller_id(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_notification_settings

Returns notification settings for the current extension. Knowledge Article: [User Settings - Set Up Message Notifications](https://success.ringcentral.com/articles/RC_Knowledge_Article/9740)

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/notification-settings`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`NotificationSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_settings.read_notification_settings(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_notification_settings

Updates notification settings for the current extension. Knowledge Article: [User Settings - Set Up Message Notifications](https://success.ringcentral.com/articles/RC_Knowledge_Article/9740)

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/notification-settings`

**Parameters**

| Name         | Type                                                                                | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [NotificationSettingsUpdateRequest](../models/NotificationSettingsUpdateRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                                 | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`NotificationSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import NotificationSettingsUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = NotificationSettingsUpdateRequest(
    email_addresses=[
        "emailAddresses"
    ],
    sms_email_addresses=[
        "smsEmailAddresses"
    ],
    advanced_mode=False,
    voicemails={
        "notify_by_email": False,
        "notify_by_sms": True,
        "advanced_email_addresses": [
            "advancedEmailAddresses"
        ],
        "advanced_sms_email_addresses": [
            "advancedSmsEmailAddresses"
        ],
        "include_attachment": False,
        "include_transcription": False,
        "mark_as_read": True
    },
    inbound_faxes={
        "notify_by_email": True,
        "notify_by_sms": True,
        "advanced_email_addresses": [
            "advancedEmailAddresses"
        ],
        "advanced_sms_email_addresses": [
            "advancedSmsEmailAddresses"
        ],
        "include_attachment": False,
        "mark_as_read": False
    },
    outbound_faxes={
        "notify_by_email": True,
        "notify_by_sms": False,
        "advanced_email_addresses": [
            "advancedEmailAddresses"
        ],
        "advanced_sms_email_addresses": [
            "advancedSmsEmailAddresses"
        ]
    },
    inbound_texts={
        "notify_by_email": True,
        "notify_by_sms": False,
        "advanced_email_addresses": [
            "advancedEmailAddresses"
        ],
        "advanced_sms_email_addresses": [
            "advancedSmsEmailAddresses"
        ]
    },
    missed_calls={
        "notify_by_email": True,
        "notify_by_sms": True,
        "advanced_email_addresses": [
            "advancedEmailAddresses"
        ],
        "advanced_sms_email_addresses": [
            "advancedSmsEmailAddresses"
        ]
    },
    include_managers=True
)

result = sdk.user_settings.update_notification_settings(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
