# RingOutService

A list of all methods in the `RingOutService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                  |
| :------------------------------------------------------ | :------------------------------------------- |
| [create_ring_out_call](#create_ring_out_call)           | Makes a 2-legged RingOut call.               |
| [read_ring_out_call_status](#read_ring_out_call_status) | Returns a status of a 2-legged RingOut call. |
| [delete_ring_out_call](#delete_ring_out_call)           | Cancels a 2-legged RingOut call.             |

## create_ring_out_call

Makes a 2-legged RingOut call.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/ring-out`

**Parameters**

| Name         | Type                                                  | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MakeRingOutRequest](../models/MakeRingOutRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`GetRingOutStatusResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MakeRingOutRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MakeRingOutRequest(
    from_={
        "phone_number": "phoneNumber",
        "forwarding_number_id": "forwardingNumberId"
    },
    to={
        "phone_number": "phoneNumber"
    },
    caller_id={
        "phone_number": "phoneNumber"
    },
    play_prompt=True,
    country={
        "id_": "id"
    }
)

result = sdk.ring_out.create_ring_out_call(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_ring_out_call_status

Returns a status of a 2-legged RingOut call.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/ring-out/{ringoutId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| ringout_id   | str  | ✅       | Internal identifier of a RingOut call                                                                                                                                 |

**Return Type**

`GetRingOutStatusResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ring_out.read_ring_out_call_status(
    account_id="~",
    extension_id="~",
    ringout_id="ringoutId"
)

print(result)
```

## delete_ring_out_call

Cancels a 2-legged RingOut call.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/ring-out/{ringoutId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| ringout_id   | str  | ✅       | Internal identifier of a RingOut call                                                                                                                                 |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.ring_out.delete_ring_out_call(
    account_id="~",
    extension_id="~",
    ringout_id="ringoutId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
