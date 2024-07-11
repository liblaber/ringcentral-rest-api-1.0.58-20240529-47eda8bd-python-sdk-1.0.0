# IvrService

A list of all methods in the `IvrService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                   |
| :-------------------------------------------------- | :-------------------------------------------- |
| [read_ivr_prompt_content](#read_ivr_prompt_content) | Returns media content of an IVR prompt by ID. |
| [list_ivr_prompts](#list_ivr_prompts)               | Returns the list of IVR prompts.              |
| [create_ivr_prompt](#create_ivr_prompt)             | Creates an IVR prompt.                        |
| [read_ivr_prompt](#read_ivr_prompt)                 | Returns an IVR prompt by ID.                  |
| [update_ivr_prompt](#update_ivr_prompt)             | Updates an IVR prompt by ID                   |
| [delete_ivr_prompt](#delete_ivr_prompt)             | Deletes an IVR prompt by ID.                  |
| [read_ivr_menu_list](#read_ivr_menu_list)           | Returns a company IVR menus.                  |
| [create_ivr_menu](#create_ivr_menu)                 | Creates a company IVR menu.                   |
| [read_ivr_menu](#read_ivr_menu)                     | Returns a company IVR menu by ID.             |
| [update_ivr_menu](#update_ivr_menu)                 | Updates a company IVR menu by ID.             |

## read_ivr_prompt_content

Returns media content of an IVR prompt by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-prompts/{promptId}/content`

**Parameters**

| Name                         | Type                                                  | Required | Description                                                                                                                                                  |
| :--------------------------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id                   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| prompt_id                    | str                                                   | ✅       | Internal identifier of an IVR prompt                                                                                                                         |
| content_disposition          | [ContentDisposition](../models/ContentDisposition.md) | ❌       | Whether the content is expected to be displayed in the browser, or downloaded and saved locally                                                              |
| content_disposition_filename | str                                                   | ❌       | The default filename of the file to be downloaded                                                                                                            |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ContentDisposition

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ivr.read_ivr_prompt_content(
    account_id="~",
    prompt_id="promptId",
    content_disposition="Inline",
    content_disposition_filename="contentDispositionFilename"
)

print(result)
```

## list_ivr_prompts

Returns the list of IVR prompts.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-prompts`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`IvrPrompts`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ivr.list_ivr_prompts(account_id="~")

print(result)
```

## create_ivr_prompt

Creates an IVR prompt.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-prompts`

**Parameters**

| Name         | Type                      | Required | Description                                                                                                                                                  |
| :----------- | :------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [dict](../models/dict.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`PromptInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateIvrPromptRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "attachment": "attachment",
    "name": "name"
}

result = sdk.ivr.create_ivr_prompt(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_ivr_prompt

Returns an IVR prompt by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-prompts/{promptId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| prompt_id  | str  | ✅       | Internal identifier of an IVR prompt                                                                                                                         |

**Return Type**

`PromptInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ivr.read_ivr_prompt(
    account_id="~",
    prompt_id="promptId"
)

print(result)
```

## update_ivr_prompt

Updates an IVR prompt by ID

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-prompts/{promptId}`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateIvrPromptRequest](../models/UpdateIvrPromptRequest.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| prompt_id    | str                                                           | ✅       | Internal identifier of an IVR prompt                                                                                                                         |

**Return Type**

`PromptInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateIvrPromptRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateIvrPromptRequest(
    filename="filename"
)

result = sdk.ivr.update_ivr_prompt(
    request_body=request_body,
    account_id="~",
    prompt_id="promptId"
)

print(result)
```

## delete_ivr_prompt

Deletes an IVR prompt by ID.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-prompts/{promptId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| prompt_id  | str  | ✅       | Internal identifier of an IVR prompt                                                                                                                         |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ivr.delete_ivr_prompt(
    account_id="~",
    prompt_id="promptId"
)

print(result)
```

## read_ivr_menu_list

Returns a company IVR menus.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-menus`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`IvrMenuList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ivr.read_ivr_menu_list(account_id="~")

print(result)
```

## create_ivr_menu

Creates a company IVR menu.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-menus`

**Parameters**

| Name         | Type                                    | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [IvrMenuInfo](../models/IvrMenuInfo.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`IvrMenuInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import IvrMenuInfo

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = IvrMenuInfo(
    id_="id",
    uri="uri",
    name="name",
    extension_number="extensionNumber",
    site={
        "id_": "id",
        "name": "name"
    },
    prompt={
        "mode": "Audio",
        "audio": {
            "uri": "uri",
            "id_": "id"
        },
        "text": "text",
        "language": {
            "uri": "uri",
            "id_": "id",
            "name": "name",
            "locale_code": "localeCode"
        }
    },
    actions=[
        {
            "input": "input",
            "action": "Connect",
            "extension": {
                "uri": "uri",
                "id_": "id",
                "name": "name"
            },
            "phone_number": "phoneNumber"
        }
    ]
)

result = sdk.ivr.create_ivr_menu(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_ivr_menu

Returns a company IVR menu by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-menus/{ivrMenuId}`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                  |
| :---------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id  | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| ivr_menu_id | str  | ✅       | Internal identifier of an IVR menu                                                                                                                           |

**Return Type**

`IvrMenuInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ivr.read_ivr_menu(
    account_id="~",
    ivr_menu_id="ivrMenuId"
)

print(result)
```

## update_ivr_menu

Updates a company IVR menu by ID.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/ivr-menus/{ivrMenuId}`

**Parameters**

| Name         | Type                                    | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [IvrMenuInfo](../models/IvrMenuInfo.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| ivr_menu_id  | str                                     | ✅       | Internal identifier of an IVR menu                                                                                                                           |

**Return Type**

`IvrMenuInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import IvrMenuInfo

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = IvrMenuInfo(
    id_="id",
    uri="uri",
    name="name",
    extension_number="extensionNumber",
    site={
        "id_": "id",
        "name": "name"
    },
    prompt={
        "mode": "Audio",
        "audio": {
            "uri": "uri",
            "id_": "id"
        },
        "text": "text",
        "language": {
            "uri": "uri",
            "id_": "id",
            "name": "name",
            "locale_code": "localeCode"
        }
    },
    actions=[
        {
            "input": "input",
            "action": "Connect",
            "extension": {
                "uri": "uri",
                "id_": "id",
                "name": "name"
            },
            "phone_number": "phoneNumber"
        }
    ]
)

result = sdk.ivr.update_ivr_menu(
    request_body=request_body,
    account_id="~",
    ivr_menu_id="ivrMenuId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
