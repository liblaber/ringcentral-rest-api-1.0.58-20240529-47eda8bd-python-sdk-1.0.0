# SmsService

A list of all methods in the `SmsService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_sms_message](#create_sms_message) | Creates and sends a new text message or multiple messages. You can send SMS messages simultaneously to different recipients up to 40 requests per minute; this limitation is relevant for all client applications. Sending and receiving SMS is available for Toll-Free Numbers within the USA. You can send up to 10 attachments in a single MMS message; the size of all attachments linked is limited up to 1500000 bytes. |
| [create_mms](#create_mms)                 | Creates and sends a new media message or multiple messages. Sending MMS messages simultaneously to different recipients is limited up to 50 requests per minute; relevant for all client applications.                                                                                                                                                                                                                        |

## create_sms_message

Creates and sends a new text message or multiple messages. You can send SMS messages simultaneously to different recipients up to 40 requests per minute; this limitation is relevant for all client applications. Sending and receiving SMS is available for Toll-Free Numbers within the USA. You can send up to 10 attachments in a single MMS message; the size of all attachments linked is limited up to 1500000 bytes.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/sms`

**Parameters**

| Name         | Type                                              | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateSmsMessage](../models/CreateSmsMessage.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                               | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`GetSmsMessageInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateSmsMessage

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateSmsMessage(
    from_={
        "phone_number": "phoneNumber"
    },
    to=[
        {
            "phone_number": "phoneNumber"
        }
    ],
    text="text",
    country={
        "id_": "id",
        "iso_code": "ex"
    }
)

result = sdk.sms.create_sms_message(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## create_mms

Creates and sends a new media message or multiple messages. Sending MMS messages simultaneously to different recipients is limited up to 50 requests per minute; relevant for all client applications.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/mms`

**Parameters**

| Name         | Type                      | Required | Description                                                                                                                                                           |
| :----------- | :------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [dict](../models/dict.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`GetSmsMessageInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateMmsMessage

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "from_": {
        "phone_number": "phoneNumber"
    },
    "to": [
        {
            "phone_number": "phoneNumber"
        }
    ],
    "text": "text",
    "country": {
        "id_": "id",
        "iso_code": "ex"
    },
    "attachments": [
        "attachments"
    ]
}

result = sdk.sms.create_mms(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
