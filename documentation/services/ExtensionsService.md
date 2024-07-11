# ExtensionsService

A list of all methods in the `ExtensionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                         |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| [extension_bulk_update](#extension_bulk_update)                   | Updates multiple extensions at once. Maximum 500 extensions can be updated per request.                             |
| [get_extension_bulk_update_task](#get_extension_bulk_update_task) | Returns a status of a task to update multiple extensions.                                                           |
| [list_user_templates](#list_user_templates)                       | Returns the list of user templates for the current account.                                                         |
| [read_user_template](#read_user_template)                         | Returns the user template by ID.                                                                                    |
| [list_extensions](#list_extensions)                               | Returns the list of extensions created for a particular account. All types of extensions are included in this list. |
| [create_extension](#create_extension)                             | Creates an extension.                                                                                               |

## extension_bulk_update

Updates multiple extensions at once. Maximum 500 extensions can be updated per request.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension-bulk-update`

**Parameters**

| Name         | Type                                                                  | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ExtensionBulkUpdateRequest](../models/ExtensionBulkUpdateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`ExtensionBulkUpdateTaskResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ExtensionBulkUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ExtensionBulkUpdateRequest(
    records=[
        {
            "id_": "id",
            "status": "Disabled",
            "status_info": {
                "comment": "comment",
                "reason": "SuspendedVoluntarily",
                "till": "till"
            },
            "reason": "reason",
            "comment": "comment",
            "extension_number": "extensionNumber",
            "contact": {
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
            "regional_settings": {
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
            "setup_wizard_state": "NotStarted",
            "partner_id": "partnerId",
            "ivr_pin": "ivrPin",
            "password": "password",
            "call_queue_info": {
                "sla_goal": 0,
                "sla_threshold_seconds": 7,
                "include_abandoned_calls": False,
                "abandoned_threshold_seconds": 10
            },
            "transition": {
                "send_welcome_emails_to_users": True,
                "send_welcome_email": True
            },
            "cost_center": {
                "id_": "id",
                "name": "name"
            },
            "custom_fields": [
                {
                    "id_": "id",
                    "value": "value",
                    "display_name": "displayName"
                }
            ],
            "hidden": True,
            "site": {
                "id_": "id",
                "uri": "uri",
                "name": "name",
                "code": "code"
            },
            "type_": "User",
            "references": [
                {
                    "ref": "ref",
                    "type_": "PartnerId",
                    "ref_acc_id": "refAccId"
                }
            ]
        }
    ]
)

result = sdk.extensions.extension_bulk_update(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## get_extension_bulk_update_task

Returns a status of a task to update multiple extensions.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension-bulk-update/tasks/{taskId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| task_id    | str  | ✅       | Internal identifier of a task                                                                                                                                |

**Return Type**

`ExtensionBulkUpdateTaskResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.extensions.get_extension_bulk_update_task(
    account_id="~",
    task_id="taskId"
)

print(result)
```

## list_user_templates

Returns the list of user templates for the current account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/templates`

**Parameters**

| Name       | Type                                                        | Required | Description                                                                                                                                                  |
| :--------- | :---------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| type\_     | [ListUserTemplatesType](../models/ListUserTemplatesType.md) | ❌       | Type of template                                                                                                                                             |
| page       | int                                                         | ❌       | Indicates a page number to retrieve. Only positive number values are allowed. Default value is '1'                                                           |
| per_page   | int                                                         | ❌       | Indicates a page size (number of items). If not specified, the value is '100' by default                                                                     |

**Return Type**

`UserTemplates`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListUserTemplatesType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.extensions.list_user_templates(
    account_id="~",
    type_="UserSettings",
    page=1,
    per_page=100
)

print(result)
```

## read_user_template

Returns the user template by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/templates/{templateId}`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                  |
| :---------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id  | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| template_id | str  | ✅       | Internal identifier of a template                                                                                                                            |

**Return Type**

`TemplateInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.extensions.read_user_template(
    account_id="~",
    template_id="templateId"
)

print(result)
```

## list_extensions

Returns the list of extensions created for a particular account. All types of extensions are included in this list.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension`

**Parameters**

| Name             | Type                                                            | Required | Description                                                                                                                                                                                                |
| :--------------- | :-------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id       | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                               |
| extension_number | str                                                             | ❌       | Extension short number to filter records                                                                                                                                                                   |
| email            | str                                                             | ❌       | Extension email address. Multiple values are accepted                                                                                                                                                      |
| page             | int                                                             | ❌       | Indicates a page number to retrieve. Only positive number values are allowed                                                                                                                               |
| per_page         | int                                                             | ❌       | Indicates a page size (number of items)                                                                                                                                                                    |
| status           | [List[ListExtensionsStatus]](../models/ListExtensionsStatus.md) | ❌       | Extension current state. Multiple values are supported. If 'Unassigned' is specified, then extensions without `extensionNumber` attribute are returned. If not specified, then all extensions are returned |
| type\_           | [List[ListExtensionsType]](../models/ListExtensionsType.md)     | ❌       | Extension type. Multiple values are supported. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                        |

**Return Type**

`GetExtensionListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
status=[
    "Enabled"
]
type_=[
    "User"
]

result = sdk.extensions.list_extensions(
    account_id="~",
    extension_number="extensionNumber",
    email="email",
    page=1,
    per_page=100,
    status=status,
    type_=type_
)

print(result)
```

## create_extension

Creates an extension.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension`

**Parameters**

| Name         | Type                                                              | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ExtensionCreationRequest](../models/ExtensionCreationRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`ExtensionCreationResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ExtensionCreationRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ExtensionCreationRequest(
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
    extension_number="extensionNumber",
    cost_center={
        "id_": "id",
        "name": "name"
    },
    custom_fields=[
        {
            "id_": "id",
            "value": "value",
            "display_name": "displayName"
        }
    ],
    password="password",
    references=[
        {
            "ref": "ref",
            "type_": "PartnerId",
            "ref_acc_id": "refAccId"
        }
    ],
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
    partner_id="partnerId",
    ivr_pin="ivrPin",
    setup_wizard_state="NotStarted",
    site={
        "id_": "id",
        "uri": "uri",
        "name": "name",
        "extension_number": "extensionNumber",
        "caller_id_name": "callerIdName",
        "email": "email",
        "business_address": {
            "country": "country",
            "state": "state",
            "city": "city",
            "street": "street",
            "zip": "zip"
        },
        "regional_settings": {
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
        "operator": {
            "id_": "id",
            "uri": "uri",
            "extension_number": "extensionNumber",
            "name": "name"
        },
        "code": "code"
    },
    status="Enabled",
    status_info={
        "comment": "comment",
        "reason": "SuspendedVoluntarily",
        "till": "till"
    },
    type_="User",
    hidden=True
)

result = sdk.extensions.create_extension(
    request_body=request_body,
    account_id="~"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
