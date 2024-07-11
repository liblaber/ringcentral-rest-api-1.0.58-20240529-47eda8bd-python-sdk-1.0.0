# CallForwardingService

A list of all methods in the `CallForwardingService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                                                                                                            |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_forwarding_numbers](#list_forwarding_numbers)     | Returns the list of extension phone numbers used for call forwarding and call flip. The returned list contains all the extension phone numbers used for call forwarding and call flip. |
| [create_forwarding_number](#create_forwarding_number)   | Adds a new forwarding number to the forwarding number list.                                                                                                                            |
| [delete_forwarding_numbers](#delete_forwarding_numbers) | Deletes multiple forwarding numbers from the forwarding number list by IDs.                                                                                                            |
| [read_forwarding_number](#read_forwarding_number)       | Returns a specific forwarding number.                                                                                                                                                  |
| [update_forwarding_number](#update_forwarding_number)   | Updates the existing forwarding number from the forwarding number list.                                                                                                                |
| [delete_forwarding_number](#delete_forwarding_number)   | Deletes a forwarding number from the forwarding number list by its ID.                                                                                                                 |

## list_forwarding_numbers

Returns the list of extension phone numbers used for call forwarding and call flip. The returned list contains all the extension phone numbers used for call forwarding and call flip.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| page         | int  | ❌       | The result set page number (1-indexed) to return                                                                                                                      |
| per_page     | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                                |

**Return Type**

`GetExtensionForwardingNumberListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_forwarding.list_forwarding_numbers(
    account_id="~",
    extension_id="~",
    page=1,
    per_page=100
)

print(result)
```

## create_forwarding_number

Adds a new forwarding number to the forwarding number list.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateForwardingNumberRequest](../models/CreateForwardingNumberRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`ForwardingNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateForwardingNumberRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateForwardingNumberRequest(
    flip_number=2,
    phone_number="phoneNumber",
    label="label",
    type_="PhoneLine",
    device={
        "id_": "id"
    }
)

result = sdk.call_forwarding.create_forwarding_number(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## delete_forwarding_numbers

Deletes multiple forwarding numbers from the forwarding number list by IDs.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number`

**Parameters**

| Name         | Type                                                                          | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [DeleteForwardingNumbersRequest](../models/DeleteForwardingNumbersRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import DeleteForwardingNumbersRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = DeleteForwardingNumbersRequest(
    records=[
        {
            "forwarding_number_id": "forwardingNumberId"
        }
    ]
)

result = sdk.call_forwarding.delete_forwarding_numbers(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_forwarding_number

Returns a specific forwarding number.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number/{forwardingNumberId}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                           |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id         | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| forwarding_number_id | str  | ✅       | Internal identifier of a forwarding number (returned in response in the 'id' field)                                                                                   |

**Return Type**

`ForwardingNumberResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_forwarding.read_forwarding_number(
    account_id="~",
    extension_id="~",
    forwarding_number_id="forwardingNumberId"
)

print(result)
```

## update_forwarding_number

Updates the existing forwarding number from the forwarding number list.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number/{forwardingNumberId}`

**Parameters**

| Name                 | Type                                                                        | Required | Description                                                                                                                                                           |
| :------------------- | :-------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [UpdateForwardingNumberRequest](../models/UpdateForwardingNumberRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id           | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id         | str                                                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| forwarding_number_id | str                                                                         | ✅       | Internal identifier of a forwarding number (returned in response in the 'id' field)                                                                                   |

**Return Type**

`ForwardingNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateForwardingNumberRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateForwardingNumberRequest(
    phone_number="phoneNumber",
    label="label",
    flip_number="flipNumber",
    type_="Home"
)

result = sdk.call_forwarding.update_forwarding_number(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    forwarding_number_id="forwardingNumberId"
)

print(result)
```

## delete_forwarding_number

Deletes a forwarding number from the forwarding number list by its ID.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/forwarding-number/{forwardingNumberId}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                           |
| :------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id         | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| forwarding_number_id | str  | ✅       | Internal identifier of a forwarding number (returned in response in the 'id' field)                                                                                   |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_forwarding.delete_forwarding_number(
    account_id="~",
    extension_id="~",
    forwarding_number_id="forwardingNumberId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
