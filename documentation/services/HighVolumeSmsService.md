# HighVolumeSmsService

A list of all methods in the `HighVolumeSmsService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                                                                                           |
| :-------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [aggregate_a2_psms_statuses](#aggregate_a2_psms_statuses) | Retrieves a set of message counts by message status and error codes filtered by dates, batchId and message direction.                                                                                                 |
| [list_a2_psms](#list_a2_psms)                             | Returns the list of outbound/inbound A2P messages sent from/to A2P phone numbers of the current account. The list can be filtered by message batch ID and/or phone number.                                            |
| [read_a2_psms](#read_a2_psms)                             | Returns the details of an A2P SMS message by ID.                                                                                                                                                                      |
| [read_a2_psms_opt_outs](#read_a2_psms_opt_outs)           | Returns the list of numbers opted out from the account. The list can be filtered by `to`/`from` phone number query parameters. Specifying `text/csv` in the `Accept` header lets download the data in the CSV format. |
| [add_a2_psms_opt_outs](#add_a2_psms_opt_outs)             | Adds multiple opt-outs and/or opt-ins for the specified sender number and a set of recipient numbers.                                                                                                                 |
| [list_a2_p_batches](#list_a2_p_batches)                   | Returns the list of A2P batches sent from the current account. The list can be filtered by message batch ID and/or from phone number.                                                                                 |
| [create_a2_psms](#create_a2_psms)                         | Allows to send high volume of A2P (Application-to-Person) SMS messages (in message batches). Only phone number with the `A2PSmsSender` feature can be used as a sender.                                               |
| [read_a2_p_batch](#read_a2_p_batch)                       | Returns information on a message batch.                                                                                                                                                                               |

## aggregate_a2_psms_statuses

Retrieves a set of message counts by message status and error codes filtered by dates, batchId and message direction.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/statuses`

**Parameters**

| Name         | Type                                              | Required | Description                                                                                                                                                             |
| :----------- | :------------------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)            |
| batch_id     | str                                               | ❌       | Internal identifier of a message batch to filter the response                                                                                                           |
| direction    | [SmsDirectionEnum](../models/SmsDirectionEnum.md) | ❌       | Direction of a message to filter the message list result. By default, there is no filter applied - both Inbound and Outbound messages are returned                      |
| date_from    | str                                               | ❌       | The end of the time range to filter the results in ISO 8601 format including timezone. Default is the 'dateTo' minus 24 hours                                           |
| date_to      | str                                               | ❌       | The end of the time range to filter the results in ISO 8601 format including timezone. Default is the current time                                                      |
| phone_number | List[str]                                         | ❌       | List of phone numbers (specified in 'to' or 'from' fields of a message) to filter the results. Maximum number of phone numbers allowed to be specified as filters is 15 |

**Return Type**

`MessageStatusesResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SmsDirectionEnum

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
phone_number=[
    "phoneNumber"
]

result = sdk.high_volume_sms.aggregate_a2_psms_statuses(
    account_id="~",
    batch_id="batchId",
    direction="Inbound",
    date_from="dateFrom",
    date_to="dateTo",
    phone_number=phone_number
)

print(result)
```

## list_a2_psms

Returns the list of outbound/inbound A2P messages sent from/to A2P phone numbers of the current account. The list can be filtered by message batch ID and/or phone number.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/messages`

**Parameters**

| Name         | Type                                              | Required | Description                                                                                                                                                             |
| :----------- | :------------------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)            |
| batch_id     | str                                               | ❌       | Internal identifier of a message batch to filter the response                                                                                                           |
| direction    | [SmsDirectionEnum](../models/SmsDirectionEnum.md) | ❌       | Direction of a message to filter the message list result. By default, there is no filter applied - both Inbound and Outbound messages are returned                      |
| date_from    | str                                               | ❌       | The end of the time range to filter the results in ISO 8601 format including timezone. Default is the 'dateTo' minus 24 hours                                           |
| date_to      | str                                               | ❌       | The end of the time range to filter the results in ISO 8601 format including timezone. Default is the current time                                                      |
| view         | [ListA2PsmsView](../models/ListA2PsmsView.md)     | ❌       | Indicates if the response has to be detailed, includes text in the response if detailed                                                                                 |
| phone_number | List[str]                                         | ❌       | List of phone numbers (specified in 'to' or 'from' fields of a message) to filter the results. Maximum number of phone numbers allowed to be specified as filters is 15 |
| page_token   | str                                               | ❌       | The page token of the page to be retrieved.                                                                                                                             |
| per_page     | int                                               | ❌       | The number of messages to be returned per request                                                                                                                       |

**Return Type**

`MessageListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SmsDirectionEnum, ListA2PsmsView

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
phone_number=[
    "phoneNumber"
]

result = sdk.high_volume_sms.list_a2_psms(
    account_id="~",
    batch_id="batchId",
    direction="Inbound",
    date_from="dateFrom",
    date_to="dateTo",
    view="Simple",
    phone_number=phone_number,
    page_token="pageToken",
    per_page=1000
)

print(result)
```

## read_a2_psms

Returns the details of an A2P SMS message by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/messages/{messageId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| message_id | str  | ✅       | Internal identifier of a message to be retrieved                                                                                                             |

**Return Type**

`MessageDetailsResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.high_volume_sms.read_a2_psms(
    account_id="~",
    message_id="messageId"
)

print(result)
```

## read_a2_psms_opt_outs

Returns the list of numbers opted out from the account. The list can be filtered by `to`/`from` phone number query parameters. Specifying `text/csv` in the `Accept` header lets download the data in the CSV format.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/opt-outs`

**Parameters**

| Name       | Type                                                            | Required | Description                                                                                                                                                                |
| :--------- | :-------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)               |
| from\_     | str                                                             | ❌       | The sender's phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format for filtering messages. The asterisk value "\*" means any number in `from` field |
| to         | str                                                             | ❌       | The receiver's phone number (`to` field) in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format for filtering messages                                            |
| status     | [ReadA2PsmsOptOutsStatus](../models/ReadA2PsmsOptOutsStatus.md) | ❌       | The status (opted out, opted in, or both) to be used as the filter                                                                                                         |
| page_token | str                                                             | ❌       | The page token of the page to be retrieved                                                                                                                                 |
| per_page   | int                                                             | ❌       | The number of records to be returned for the page                                                                                                                          |

**Return Type**

`OptOutListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReadA2PsmsOptOutsStatus

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.high_volume_sms.read_a2_psms_opt_outs(
    account_id="~",
    from_="from",
    to="to",
    status="optout",
    page_token="pageToken",
    per_page=1000
)

print(result)
```

## add_a2_psms_opt_outs

Adds multiple opt-outs and/or opt-ins for the specified sender number and a set of recipient numbers.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/opt-outs/bulk-assign`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [OptOutBulkAssignRequest](../models/OptOutBulkAssignRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`OptOutBulkAssignResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import OptOutBulkAssignRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = OptOutBulkAssignRequest(
    from_="+15551234455",
    opt_outs=[
        "optOuts"
    ],
    opt_ins=[
        "optIns"
    ]
)

result = sdk.high_volume_sms.add_a2_psms_opt_outs(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_a2_p_batches

Returns the list of A2P batches sent from the current account. The list can be filtered by message batch ID and/or from phone number.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/batches`

**Parameters**

| Name       | Type                                                            | Required | Description                                                                                                                                                  |
| :--------- | :-------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| date_from  | str                                                             | ❌       | The end of the time range to filter the results in ISO 8601 format including timezone. Default is the 'dateTo' minus 24 hours                                |
| date_to    | str                                                             | ❌       | The end of the time range to filter the results in ISO 8601 format including timezone. Default is the current time                                           |
| from\_     | str                                                             | ❌       | Phone number in E.164 format from which the messages are going to be sent                                                                                    |
| status     | [List[ListA2PBatchesStatus]](../models/ListA2PBatchesStatus.md) | ❌       | A list of batch statuses to filter the results                                                                                                               |
| page_token | str                                                             | ❌       | The page token of the page to be retrieved                                                                                                                   |
| per_page   | int                                                             | ❌       | The number of records to be returned per page                                                                                                                |

**Return Type**

`BatchListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
status=[
    "Queued"
]

result = sdk.high_volume_sms.list_a2_p_batches(
    account_id="~",
    date_from="dateFrom",
    date_to="dateTo",
    from_="from",
    status=status,
    page_token="pageToken",
    per_page=3
)

print(result)
```

## create_a2_psms

Allows to send high volume of A2P (Application-to-Person) SMS messages (in message batches). Only phone number with the `A2PSmsSender` feature can be used as a sender.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/batches`

**Parameters**

| Name         | Type                                                                | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MessageBatchCreateRequest](../models/MessageBatchCreateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`MessageBatchResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MessageBatchCreateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MessageBatchCreateRequest(
    from_="+15551234567",
    text="Hello, World!",
    messages=[
        {
            "to": [
                "to"
            ],
            "text": "Hello, World!"
        }
    ]
)

result = sdk.high_volume_sms.create_a2_psms(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_a2_p_batch

Returns information on a message batch.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/a2p-sms/batches/{batchId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| batch_id   | str  | ✅       | Internal identifier of a message batch to be retrieved                                                                                                       |

**Return Type**

`MessageBatchResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.high_volume_sms.read_a2_p_batch(
    account_id="~",
    batch_id="batchId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
