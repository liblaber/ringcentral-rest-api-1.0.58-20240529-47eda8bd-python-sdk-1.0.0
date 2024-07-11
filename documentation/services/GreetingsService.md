# GreetingsService

A list of all methods in the `GreetingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                                                                                                                            |
| :-------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_account_greeting_content](#read_account_greeting_content) | Returns account-level greeting media contents. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**                               |
| [read_greeting_content](#read_greeting_content)                 | Returns extension-level greeting media contents. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**                             |
| [create_company_greeting](#create_company_greeting)             | Creates a custom company greeting.                                                                                                                                     |
| [create_custom_user_greeting](#create_custom_user_greeting)     | Creates custom greeting for an extension user.                                                                                                                         |
| [read_custom_greeting](#read_custom_greeting)                   | Returns a custom user greeting by ID.                                                                                                                                  |
| [list_standard_greetings](#list_standard_greetings)             | Returns the list of predefined standard greetings. Custom greetings recorded by user are not returned in response to this request. See Get Extension Custom Greetings. |
| [read_standard_greeting](#read_standard_greeting)               | Returns a standard greeting by ID.                                                                                                                                     |

## read_account_greeting_content

Returns account-level greeting media contents. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/greeting/{greetingId}/content`

**Parameters**

| Name                         | Type                                                  | Required | Description                                                                                                                                                  |
| :--------------------------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id                   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| greeting_id                  | str                                                   | ✅       | Internal identifier of a greeting                                                                                                                            |
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

result = sdk.greetings.read_account_greeting_content(
    account_id="~",
    greeting_id="greetingId",
    content_disposition="Inline",
    content_disposition_filename="contentDispositionFilename"
)

print(result)
```

## read_greeting_content

Returns extension-level greeting media contents. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/greeting/{greetingId}/content`

**Parameters**

| Name                         | Type                                                  | Required | Description                                                                                                                                                           |
| :--------------------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id                   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id                 | str                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| greeting_id                  | str                                                   | ✅       | Internal identifier of a greeting                                                                                                                                     |
| content_disposition          | [ContentDisposition](../models/ContentDisposition.md) | ❌       | Whether the content is expected to be displayed in the browser, or downloaded and saved locally                                                                       |
| content_disposition_filename | str                                                   | ❌       | The default filename of the file to be downloaded                                                                                                                     |

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

result = sdk.greetings.read_greeting_content(
    account_id="~",
    extension_id="~",
    greeting_id="greetingId",
    content_disposition="Inline",
    content_disposition_filename="contentDispositionFilename"
)

print(result)
```

## create_company_greeting

Creates a custom company greeting.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/greeting`

**Parameters**

| Name         | Type                    | Required | Description                                                                                                                                                  |
| :----------- | :---------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [any](../models/any.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CustomCompanyGreetingInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import GreetingsCreateCompanyGreetingRequest1

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "type_": "Company",
    "answering_rule": {
        "id_": "id"
    },
    "language_id": "languageId",
    "binary": "binary"
}

result = sdk.greetings.create_company_greeting(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## create_custom_user_greeting

Creates custom greeting for an extension user.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/greeting`

**Parameters**

| Name         | Type                    | Required | Description                                                                                                                                                                                |
| :----------- | :---------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [any](../models/any.md) | ✅       | The request body.                                                                                                                                                                          |
| account_id   | str                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                               |
| extension_id | str                     | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                      |
| apply        | bool                    | ❌       | Specifies whether to apply an answering rule or not. If set to true then `answeringRule` parameter is mandatory. If set to false, then the answering rule is not applied even if specified |

**Return Type**

`CustomUserGreetingInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import GreetingsCreateCustomUserGreetingRequest1

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "type_": "Introductory",
    "answering_rule": {
        "id_": "id"
    },
    "binary": "binary"
}

result = sdk.greetings.create_custom_user_greeting(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    apply=True
)

print(result)
```

## read_custom_greeting

Returns a custom user greeting by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/greeting/{greetingId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| greeting_id  | str  | ✅       | Internal identifier of a greeting                                                                                                                                     |

**Return Type**

`CustomUserGreetingInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.greetings.read_custom_greeting(
    account_id="~",
    extension_id="~",
    greeting_id="greetingId"
)

print(result)
```

## list_standard_greetings

Returns the list of predefined standard greetings. Custom greetings recorded by user are not returned in response to this request. See Get Extension Custom Greetings.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/greeting`

**Parameters**

| Name       | Type                                                                          | Required | Description                                                                                                            |
| :--------- | :---------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------- |
| page       | int                                                                           | ❌       | The result set page number (1-indexed) to return                                                                       |
| per_page   | int                                                                           | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied |
| type\_     | [ListStandardGreetingsType](../models/ListStandardGreetingsType.md)           | ❌       | Type of greeting, specifying the case when the greeting is played                                                      |
| usage_type | [ListStandardGreetingsUsageType](../models/ListStandardGreetingsUsageType.md) | ❌       | Usage type of greeting, specifying if the greeting is applied for user extension or department (call queue) extension  |

**Return Type**

`DictionaryGreetingList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListStandardGreetingsType, ListStandardGreetingsUsageType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.greetings.list_standard_greetings(
    page=1,
    per_page=100,
    type_="Introductory",
    usage_type="UserExtensionAnsweringRule"
)

print(result)
```

## read_standard_greeting

Returns a standard greeting by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/greeting/{greetingId}`

**Parameters**

| Name        | Type | Required | Description                       |
| :---------- | :--- | :------- | :-------------------------------- |
| greeting_id | str  | ✅       | Internal identifier of a greeting |

**Return Type**

`DictionaryGreetingInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.greetings.read_standard_greeting(greeting_id="greetingId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
