# CallBlockingService

A list of all methods in the `CallBlockingService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                      |
| :------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_caller_blocking_settings](#read_caller_blocking_settings)     | Returns the current caller blocking settings of a user.                                                                                                          |
| [update_caller_blocking_settings](#update_caller_blocking_settings) | Updates the current caller blocking settings of a user.                                                                                                          |
| [list_blocked_allowed_numbers](#list_blocked_allowed_numbers)       | Returns the lists of blocked and allowed phone numbers.                                                                                                          |
| [create_blocked_allowed_number](#create_blocked_allowed_number)     | Updates either blocked or allowed phone number list with a new phone number.                                                                                     |
| [read_blocked_allowed_number](#read_blocked_allowed_number)         | Returns blocked or allowed phone number(s) by their ID(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported. |
| [update_blocked_allowed_number](#update_blocked_allowed_number)     | Updates blocked or allowed phone number(s) by their ID(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported. |
| [delete_blocked_allowed_number](#delete_blocked_allowed_number)     | Deletes blocked or allowed phone number(s) by their ID(s). Batch request is supported.                                                                           |

## read_caller_blocking_settings

Returns the current caller blocking settings of a user.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`CallerBlockingSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_blocking.read_caller_blocking_settings(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_caller_blocking_settings

Updates the current caller blocking settings of a user.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking`

**Parameters**

| Name         | Type                                                                      | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CallerBlockingSettingsUpdate](../models/CallerBlockingSettingsUpdate.md) | ❌       | The request body.                                                                                                                                                     |
| account_id   | str                                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`CallerBlockingSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallerBlockingSettingsUpdate

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallerBlockingSettingsUpdate(
    mode="Specific",
    no_caller_id="BlockCallsAndFaxes",
    pay_phones="Block",
    greetings=[
        {
            "type_": "type",
            "preset": {
                "uri": "uri",
                "id_": "id",
                "name": "name"
            }
        }
    ]
)

result = sdk.call_blocking.update_caller_blocking_settings(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## list_blocked_allowed_numbers

Returns the lists of blocked and allowed phone numbers.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                             | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| page         | int                                                             | ❌       | The result set page number (1-indexed) to return                                                                                                                      |
| per_page     | int                                                             | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                                |
| status       | [BlockedNumberStatusEnum](../models/BlockedNumberStatusEnum.md) | ❌       |                                                                                                                                                                       |

**Return Type**

`BlockedAllowedPhoneNumbersList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BlockedNumberStatusEnum

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_blocking.list_blocked_allowed_numbers(
    account_id="~",
    extension_id="~",
    page=1,
    per_page=100,
    status="Blocked"
)

print(result)
```

## create_blocked_allowed_number

Updates either blocked or allowed phone number list with a new phone number.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers`

**Parameters**

| Name         | Type                                                                      | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AddBlockedAllowedPhoneNumber](../models/AddBlockedAllowedPhoneNumber.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`BlockedAllowedPhoneNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AddBlockedAllowedPhoneNumber

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddBlockedAllowedPhoneNumber(
    phone_number="phoneNumber",
    label="label",
    status="Blocked"
)

result = sdk.call_blocking.create_blocked_allowed_number(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_blocked_allowed_number

Returns blocked or allowed phone number(s) by their ID(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers/{blockedNumberId}`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                           |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id        | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id      | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| blocked_number_id | str  | ✅       | Internal identifier of a blocked number entry                                                                                                                         |

**Return Type**

`BlockedAllowedPhoneNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_blocking.read_blocked_allowed_number(
    account_id="~",
    extension_id="~",
    blocked_number_id="blockedNumberId"
)

print(result)
```

## update_blocked_allowed_number

Updates blocked or allowed phone number(s) by their ID(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers/{blockedNumberId}`

**Parameters**

| Name              | Type                                                                      | Required | Description                                                                                                                                                           |
| :---------------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body      | [AddBlockedAllowedPhoneNumber](../models/AddBlockedAllowedPhoneNumber.md) | ❌       | The request body.                                                                                                                                                     |
| account_id        | str                                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id      | str                                                                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| blocked_number_id | str                                                                       | ✅       | Internal identifier of a blocked number entry                                                                                                                         |

**Return Type**

`BlockedAllowedPhoneNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AddBlockedAllowedPhoneNumber

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddBlockedAllowedPhoneNumber(
    phone_number="phoneNumber",
    label="label",
    status="Blocked"
)

result = sdk.call_blocking.update_blocked_allowed_number(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    blocked_number_id="blockedNumberId"
)

print(result)
```

## delete_blocked_allowed_number

Deletes blocked or allowed phone number(s) by their ID(s). Batch request is supported.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/caller-blocking/phone-numbers/{blockedNumberId}`

**Parameters**

| Name              | Type | Required | Description                                                                                                                                                           |
| :---------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id        | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id      | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| blocked_number_id | str  | ✅       | Internal identifier of a blocked number entry                                                                                                                         |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_blocking.delete_blocked_allowed_number(
    account_id="~",
    extension_id="~",
    blocked_number_id="blockedNumberId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
