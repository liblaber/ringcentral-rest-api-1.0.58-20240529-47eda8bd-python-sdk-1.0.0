# ComplianceExportsService

A list of all methods in the `ComplianceExportsService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                                                                                                                                                                                                                                        |
| :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_data_export_tasks_new](#list_data_export_tasks_new)   | Returns the list of Glip data export tasks.                                                                                                                                                                                                                                                                        |
| [create_data_export_task_new](#create_data_export_task_new) | Creates a task for Glip data export and returns a link at which the exported data will be available in future once the task is implemented. The exported data can be downloaded by calling Get Data Export Task method with the specified task ID. Simultaneously no more than 2 tasks per company can be created. |
| [read_data_export_task_new](#read_data_export_task_new)     | Returns the links for downloading Glip data exported within the specified task. If the export task is still in progress, then only the task status will be returned. If the data is ready for downloading, then the list of URLs will be returned.                                                                 |

## list_data_export_tasks_new

Returns the list of Glip data export tasks.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/data-export`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :------------------------------------------------------------------ |
| status   | [ListDataExportTasksNewStatus](../models/ListDataExportTasksNewStatus.md) | ❌       | Status of the task(s) to be returned. Multiple values are supported |
| page     | int                                                                       | ❌       | Page number to be retrieved; value range is > 0                     |
| per_page | int                                                                       | ❌       | Number of records to be returned per page; value range is 1 - 250   |

**Return Type**

`DataExportTaskList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListDataExportTasksNewStatus

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.compliance_exports.list_data_export_tasks_new(
    status="Accepted",
    page=1,
    per_page=30
)

print(result)
```

## create_data_export_task_new

Creates a task for Glip data export and returns a link at which the exported data will be available in future once the task is implemented. The exported data can be downloaded by calling Get Data Export Task method with the specified task ID. Simultaneously no more than 2 tasks per company can be created.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/data-export`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateDataExportTaskRequest](../models/CreateDataExportTaskRequest.md) | ❌       | The request body. |

**Return Type**

`DataExportTask`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateDataExportTaskRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateDataExportTaskRequest(
    time_from="timeFrom",
    time_to="timeTo",
    contacts=[
        {
            "id_": "id",
            "email": "email"
        }
    ],
    chat_ids=[
        "chatIds"
    ]
)

result = sdk.compliance_exports.create_data_export_task_new(request_body=request_body)

print(result)
```

## read_data_export_task_new

Returns the links for downloading Glip data exported within the specified task. If the export task is still in progress, then only the task status will be returned. If the data is ready for downloading, then the list of URLs will be returned.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/data-export/{taskId}`

**Parameters**

| Name    | Type | Required | Description                                   |
| :------ | :--- | :------- | :-------------------------------------------- |
| task_id | str  | ✅       | Internal identifier of a task to be retrieved |

**Return Type**

`DataExportTask`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.compliance_exports.read_data_export_task_new(task_id="taskId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
