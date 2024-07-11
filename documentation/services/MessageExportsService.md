# MessageExportsService

A list of all methods in the `MessageExportsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                               |
| :---------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| [create_message_store_report](#create_message_store_report)             | Creates a task to collect all account messages within the specified time interval. Maximum number of simultaneous tasks per account is 2. |
| [read_message_store_report_task](#read_message_store_report_task)       | Returns the current status of a task on report creation.                                                                                  |
| [read_message_store_report_archive](#read_message_store_report_archive) | Returns the created report with message data not including attachments.                                                                   |

## create_message_store_report

Creates a task to collect all account messages within the specified time interval. Maximum number of simultaneous tasks per account is 2.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-report`

**Parameters**

| Name         | Type                                                                            | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateMessageStoreReportRequest](../models/CreateMessageStoreReportRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`MessageStoreReport`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateMessageStoreReportRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateMessageStoreReportRequest(
    date_to="dateTo",
    date_from="dateFrom",
    message_types=[
        "Fax"
    ]
)

result = sdk.message_exports.create_message_store_report(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_message_store_report_task

Returns the current status of a task on report creation.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-report/{taskId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| task_id    | str  | ✅       | Internal identifier of a task                                                                                                                                |

**Return Type**

`MessageStoreReport`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.message_exports.read_message_store_report_task(
    account_id="~",
    task_id="taskId"
)

print(result)
```

## read_message_store_report_archive

Returns the created report with message data not including attachments.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-report/{taskId}/archive`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| task_id    | str  | ✅       | Internal identifier of a task                                                                                                                                |

**Return Type**

`MessageStoreReportArchive`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.message_exports.read_message_store_report_archive(
    account_id="~",
    task_id="taskId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
