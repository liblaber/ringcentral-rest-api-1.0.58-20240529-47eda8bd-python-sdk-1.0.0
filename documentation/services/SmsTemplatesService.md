# SmsTemplatesService

A list of all methods in the `SmsTemplatesService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                    |
| :------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_company_message_templates](#list_company_message_templates)   | Returns a list of company text message templates.                                                                                                                              |
| [create_company_message_template](#create_company_message_template) | Creates a new text message template on a company level. Maximum number of company templates is 50.                                                                             |
| [read_company_message_template](#read_company_message_template)     | Returns a company text message template by ID.                                                                                                                                 |
| [update_company_message_template](#update_company_message_template) | Updates a company text message template.                                                                                                                                       |
| [delete_company_message_template](#delete_company_message_template) | Deletes a company text message template.                                                                                                                                       |
| [list_user_message_templates](#list_user_message_templates)         | Returns a list of user's personal text message templates.                                                                                                                      |
| [create_user_message_template](#create_user_message_template)       | Creates a user personal text message template. Maximum number of personal templates is 25 per user. Max length of the `body` property is 1000 symbols (2-byte UTF-16 encoded). |
| [read_user_message_template](#read_user_message_template)           | Returns a user personal text message template by ID.                                                                                                                           |
| [update_user_message_template](#update_user_message_template)       | Updates a user personal text message template.                                                                                                                                 |
| [delete_user_message_template](#delete_user_message_template)       | Deletes a user personal text message template.                                                                                                                                 |

## list_company_message_templates

Returns a list of company text message templates.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-templates`

**Parameters**

| Name       | Type      | Required | Description                                                                                                                                                  |
| :--------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| site_ids   | List[str] | ❌       | Site ID(s) to filter company message templates, associated with particular sites By default the value is all - templates with all sites will be returned     |

**Return Type**

`MessageTemplatesListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_ids=[
    "siteIds"
]

result = sdk.sms_templates.list_company_message_templates(
    account_id="~",
    site_ids=site_ids
)

print(result)
```

## create_company_message_template

Creates a new text message template on a company level. Maximum number of company templates is 50.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-templates`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MessageTemplateRequest](../models/MessageTemplateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`MessageTemplateResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MessageTemplateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MessageTemplateRequest(
    display_name="displayName",
    body={
        "text": "text"
    },
    site={
        "id_": "id",
        "name": "name"
    }
)

result = sdk.sms_templates.create_company_message_template(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_company_message_template

Returns a company text message template by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-templates/{templateId}`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                  |
| :---------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id  | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| template_id | str  | ✅       | Internal identifier of a text message template                                                                                                               |

**Return Type**

`MessageTemplateResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.sms_templates.read_company_message_template(
    account_id="~",
    template_id="templateId"
)

print(result)
```

## update_company_message_template

Updates a company text message template.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-templates/{templateId}`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MessageTemplateRequest](../models/MessageTemplateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| template_id  | str                                                           | ✅       | Internal identifier of a text message template                                                                                                               |

**Return Type**

`MessageTemplateResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MessageTemplateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MessageTemplateRequest(
    display_name="displayName",
    body={
        "text": "text"
    },
    site={
        "id_": "id",
        "name": "name"
    }
)

result = sdk.sms_templates.update_company_message_template(
    request_body=request_body,
    account_id="~",
    template_id="templateId"
)

print(result)
```

## delete_company_message_template

Deletes a company text message template.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-templates/{templateId}`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                  |
| :---------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id  | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| template_id | str  | ✅       | Internal identifier of a text message template                                                                                                               |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.sms_templates.delete_company_message_template(
    account_id="~",
    template_id="templateId"
)

print(result)
```

## list_user_message_templates

Returns a list of user's personal text message templates.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store-templates`

**Parameters**

| Name         | Type                                          | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| site_ids     | List[str]                                     | ❌       | Site ID(s) to filter user message templates, associated with particular sites. By default the value is all - templates with all sites will be returned                |
| scope        | [VisibilityType](../models/VisibilityType.md) | ❌       | Message templates scope. By default the value is all - both Personal and Company templates will be returned                                                           |

**Return Type**

`MessageTemplatesListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import VisibilityType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
site_ids=[
    "siteIds"
]

result = sdk.sms_templates.list_user_message_templates(
    account_id="~",
    extension_id="~",
    site_ids=site_ids,
    scope="Company"
)

print(result)
```

## create_user_message_template

Creates a user personal text message template. Maximum number of personal templates is 25 per user. Max length of the `body` property is 1000 symbols (2-byte UTF-16 encoded).

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store-templates`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MessageTemplateRequest](../models/MessageTemplateRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`MessageTemplateResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MessageTemplateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MessageTemplateRequest(
    display_name="displayName",
    body={
        "text": "text"
    },
    site={
        "id_": "id",
        "name": "name"
    }
)

result = sdk.sms_templates.create_user_message_template(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_user_message_template

Returns a user personal text message template by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store-templates/{templateId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| template_id  | str  | ✅       | Internal identifier of a text message template                                                                                                                        |

**Return Type**

`MessageTemplateResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.sms_templates.read_user_message_template(
    account_id="~",
    extension_id="~",
    template_id="templateId"
)

print(result)
```

## update_user_message_template

Updates a user personal text message template.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store-templates/{templateId}`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MessageTemplateRequest](../models/MessageTemplateRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| template_id  | str                                                           | ✅       | Internal identifier of a text message template                                                                                                                        |

**Return Type**

`MessageTemplateResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MessageTemplateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MessageTemplateRequest(
    display_name="displayName",
    body={
        "text": "text"
    },
    site={
        "id_": "id",
        "name": "name"
    }
)

result = sdk.sms_templates.update_user_message_template(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    template_id="templateId"
)

print(result)
```

## delete_user_message_template

Deletes a user personal text message template.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store-templates/{templateId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| template_id  | str  | ✅       | Internal identifier of a text message template                                                                                                                        |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.sms_templates.delete_user_message_template(
    account_id="~",
    extension_id="~",
    template_id="templateId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
