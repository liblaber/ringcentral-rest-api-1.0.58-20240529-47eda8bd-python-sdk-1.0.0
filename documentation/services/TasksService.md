# TasksService

A list of all methods in the `TasksService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                               |
| :------------------------------------------ | :-------------------------------------------------------- |
| [read_task_new](#read_task_new)             | Returns information about the specified task(s) by ID(s). |
| [patch_task_new](#patch_task_new)           | Updates the specified task by ID.                         |
| [delete_task_new](#delete_task_new)         | Deletes the specified task.                               |
| [complete_task_new](#complete_task_new)     | Completes a task in the specified chat.                   |
| [list_chat_tasks_new](#list_chat_tasks_new) | Returns the list of tasks of the specified chat.          |
| [create_task_new](#create_task_new)         | Creates a task in the specified chat.                     |

## read_task_new

Returns information about the specified task(s) by ID(s).

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/tasks/{taskId}`

**Parameters**

| Name    | Type | Required | Description                                         |
| :------ | :--- | :------- | :-------------------------------------------------- |
| task_id | str  | ✅       | Task identifier or comma separated list of task IDs |

**Return Type**

`TmTaskInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.tasks.read_task_new(task_id="taskId")

print(result)
```

## patch_task_new

Updates the specified task by ID.

- HTTP Method: `PATCH`
- Endpoint: `/team-messaging/v1/tasks/{taskId}`

**Parameters**

| Name         | Type                                                    | Required | Description                   |
| :----------- | :------------------------------------------------------ | :------- | :---------------------------- |
| request_body | [TmUpdateTaskRequest](../models/TmUpdateTaskRequest.md) | ❌       | The request body.             |
| task_id      | str                                                     | ✅       | Internal identifier of a task |

**Return Type**

`TmTaskList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmUpdateTaskRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmUpdateTaskRequest(
    subject="subject",
    assignees=[
        {
            "id_": "id"
        }
    ],
    completeness_condition="Simple",
    start_date="startDate",
    due_date="dueDate",
    color="Black",
    section="section",
    description="description",
    recurrence={
        "schedule": "None",
        "ending_condition": "None",
        "ending_after": 4,
        "ending_on": "endingOn"
    },
    attachments=[
        {
            "id_": "id",
            "type_": "File"
        }
    ]
)

result = sdk.tasks.patch_task_new(
    request_body=request_body,
    task_id="taskId"
)

print(result)
```

## delete_task_new

Deletes the specified task.

- HTTP Method: `DELETE`
- Endpoint: `/team-messaging/v1/tasks/{taskId}`

**Parameters**

| Name    | Type | Required | Description                   |
| :------ | :--- | :------- | :---------------------------- |
| task_id | str  | ✅       | Internal identifier of a task |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.tasks.delete_task_new(task_id="taskId")

print(result)
```

## complete_task_new

Completes a task in the specified chat.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/tasks/{taskId}/complete`

**Parameters**

| Name         | Type                                                        | Required | Description                   |
| :----------- | :---------------------------------------------------------- | :------- | :---------------------------- |
| request_body | [TmCompleteTaskRequest](../models/TmCompleteTaskRequest.md) | ✅       | The request body.             |
| task_id      | str                                                         | ✅       | Internal identifier of a task |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCompleteTaskRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCompleteTaskRequest(
    status="Incomplete",
    assignees=[
        {
            "id_": "id"
        }
    ],
    completeness_percentage=93
)

result = sdk.tasks.complete_task_new(
    request_body=request_body,
    task_id="taskId"
)

print(result)
```

## list_chat_tasks_new

Returns the list of tasks of the specified chat.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/chats/{chatId}/tasks`

**Parameters**

| Name               | Type                                                                | Required | Description                                                                                                                                        |
| :----------------- | :------------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| chat_id            | str                                                                 | ✅       | Internal identifier of a chat                                                                                                                      |
| creation_time_to   | str                                                                 | ❌       | The end datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, e.g. 2019-03-10T18:23:45Z  |
| creation_time_from | str                                                                 | ❌       | The start datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, e.g. 2016-02-23T00:00:00 |
| creator_id         | List[str]                                                           | ❌       | Internal identifier of a task creator                                                                                                              |
| status             | [List[ListChatTasksNewStatus]](../models/ListChatTasksNewStatus.md) | ❌       | Task execution status                                                                                                                              |
| assignment_status  | [AssignmentStatus](../models/AssignmentStatus.md)                   | ❌       | Task assignment status                                                                                                                             |
| assignee_id        | List[str]                                                           | ❌       | Internal identifier of a task assignee                                                                                                             |
| assignee_status    | [AssigneeStatus](../models/AssigneeStatus.md)                       | ❌       | Task execution status by assignee(-s) specified in assigneeId                                                                                      |
| page_token         | str                                                                 | ❌       | Token of the current page. If token is omitted then the first page should be returned                                                              |
| record_count       | int                                                                 | ❌       | Number of records to be returned per screen                                                                                                        |

**Return Type**

`TmTaskList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AssignmentStatus, AssigneeStatus

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
creator_id=[
    "creatorId"
]
status=[
    "Pending"
]
assignee_id=[
    "assigneeId"
]

result = sdk.tasks.list_chat_tasks_new(
    chat_id="chatId",
    creation_time_to="now",
    creation_time_from="creationTimeFrom",
    creator_id=creator_id,
    status=status,
    assignment_status="Unassigned",
    assignee_id=assignee_id,
    assignee_status="Pending",
    page_token="pageToken",
    record_count=30
)

print(result)
```

## create_task_new

Creates a task in the specified chat.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/chats/{chatId}/tasks`

**Parameters**

| Name         | Type                                                    | Required | Description                   |
| :----------- | :------------------------------------------------------ | :------- | :---------------------------- |
| request_body | [TmCreateTaskRequest](../models/TmCreateTaskRequest.md) | ✅       | The request body.             |
| chat_id      | str                                                     | ✅       | Internal identifier of a chat |

**Return Type**

`TmTaskInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreateTaskRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreateTaskRequest(
    subject="subject",
    assignees=[
        {
            "id_": "id"
        }
    ],
    completeness_condition="Simple",
    start_date="startDate",
    due_date="dueDate",
    color="Black",
    section="section",
    description="description",
    recurrence={
        "schedule": "None",
        "ending_condition": "None",
        "ending_after": 4,
        "ending_on": "endingOn"
    },
    attachments=[
        {
            "id_": "id",
            "type_": "File"
        }
    ]
)

result = sdk.tasks.create_task_new(
    request_body=request_body,
    chat_id="chatId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
