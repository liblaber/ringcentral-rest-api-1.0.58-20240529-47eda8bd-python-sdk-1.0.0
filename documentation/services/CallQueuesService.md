# CallQueuesService

A list of all methods in the `CallQueuesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                                                                                                                                                                                 |
| :-------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [list_call_queues](#list_call_queues)                                       | Returns a call queue list.                                                                                                                                                                                                                  |
| [read_call_queue_info](#read_call_queue_info)                               | Returns basic information on a call queue group extension.                                                                                                                                                                                  |
| [update_call_queue_info](#update_call_queue_info)                           | Updates information on a call queue group extension.                                                                                                                                                                                        |
| [assign_multiple_call_queue_members](#assign_multiple_call_queue_members)   | Assigns multiple call queue members to call queue group.                                                                                                                                                                                    |
| [list_call_queue_members](#list_call_queue_members)                         | Returns a list of call queue group members.                                                                                                                                                                                                 |
| [update_user_call_queues](#update_user_call_queues)                         | Updates a list of call queues where the user is an agent. This is a full update request, which means that if any call queue where the user is an agent is not mentioned in request, then the user is automatically removed from this queue. |
| [get_call_queue_overflow_settings](#get_call_queue_overflow_settings)       | Returns overflow settings for a call queue specified in path.                                                                                                                                                                               |
| [update_call_queue_overflow_settings](#update_call_queue_overflow_settings) | Updates overflow settings for a call queue specified in path.                                                                                                                                                                               |

## list_call_queues

Returns a call queue list.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-queues`

**Parameters**

| Name                | Type | Required | Description                                                                                                                                                  |
| :------------------ | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| page                | int  | ❌       | Indicates a page number to retrieve. Only positive number values are accepted                                                                                |
| per_page            | int  | ❌       | Indicates a page size (number of items)                                                                                                                      |
| member_extension_id | str  | ❌       | Internal identifier of an extension that is a member of every group within the result                                                                        |

**Return Type**

`CallQueues`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_queues.list_call_queues(
    account_id="~",
    page=1,
    per_page=100,
    member_extension_id="memberExtensionId"
)

print(result)
```

## read_call_queue_info

Returns basic information on a call queue group extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-queues/{groupId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id   | str  | ✅       |                                                                                                                                                              |

**Return Type**

`CallQueueDetails`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_queues.read_call_queue_info(
    account_id="~",
    group_id="groupId"
)

print(result)
```

## update_call_queue_info

Updates information on a call queue group extension.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-queues/{groupId}`

**Parameters**

| Name         | Type                                              | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CallQueueDetails](../models/CallQueueDetails.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id     | str                                               | ✅       | Internal identifier of a call queue group                                                                                                                    |

**Return Type**

`CallQueueDetails`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallQueueDetails

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallQueueDetails(
    uri="uri",
    id_="id",
    extension_number="extensionNumber",
    name="name",
    status="Enabled",
    sub_type="Emergency",
    service_level_settings={
        "sla_goal": 7,
        "sla_threshold_seconds": 4,
        "include_abandoned_calls": False,
        "abandoned_threshold_seconds": 5
    },
    editable_member_status=True,
    alert_timer=5
)

result = sdk.call_queues.update_call_queue_info(
    request_body=request_body,
    account_id="~",
    group_id="groupId"
)

print(result)
```

## assign_multiple_call_queue_members

Assigns multiple call queue members to call queue group.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-queues/{groupId}/bulk-assign`

**Parameters**

| Name         | Type                                                                    | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CallQueueBulkAssignResource](../models/CallQueueBulkAssignResource.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id     | str                                                                     | ✅       | Internal identifier of a call queue group                                                                                                                    |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallQueueBulkAssignResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallQueueBulkAssignResource(
    added_extension_ids=[
        "addedExtensionIds"
    ],
    removed_extension_ids=[
        "removedExtensionIds"
    ]
)

result = sdk.call_queues.assign_multiple_call_queue_members(
    request_body=request_body,
    account_id="~",
    group_id="groupId"
)

print(result)
```

## list_call_queue_members

Returns a list of call queue group members.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-queues/{groupId}/members`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id   | str  | ✅       | Internal identifier of a call queue group                                                                                                                    |
| page       | int  | ❌       | Indicates a page number to retrieve. Only positive number values are allowed                                                                                 |
| per_page   | int  | ❌       | Indicates a page size (number of items)                                                                                                                      |

**Return Type**

`CallQueueMembers`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_queues.list_call_queue_members(
    account_id="~",
    group_id="groupId",
    page=1,
    per_page=100
)

print(result)
```

## update_user_call_queues

Updates a list of call queues where the user is an agent. This is a full update request, which means that if any call queue where the user is an agent is not mentioned in request, then the user is automatically removed from this queue.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/call-queues`

**Parameters**

| Name         | Type                                          | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UserCallQueues](../models/UserCallQueues.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`UserCallQueues`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UserCallQueues

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UserCallQueues(
    records=[
        {
            "id_": "id",
            "name": "name"
        }
    ]
)

result = sdk.call_queues.update_user_call_queues(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## get_call_queue_overflow_settings

Returns overflow settings for a call queue specified in path.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{callQueueId}/overflow-settings`

**Parameters**

| Name          | Type | Required | Description                                                                                                                                                  |
| :------------ | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id    | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| call_queue_id | str  | ✅       | Internal identifier of a call queue                                                                                                                          |

**Return Type**

`CallQueueOverflowSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_queues.get_call_queue_overflow_settings(
    account_id="~",
    call_queue_id="callQueueId"
)

print(result)
```

## update_call_queue_overflow_settings

Updates overflow settings for a call queue specified in path.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{callQueueId}/overflow-settings`

**Parameters**

| Name          | Type                                                                                              | Required | Description                                                                                                                                                  |
| :------------ | :------------------------------------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body  | [CallQueueOverflowSettingsRequestResource](../models/CallQueueOverflowSettingsRequestResource.md) | ✅       | The request body.                                                                                                                                            |
| account_id    | str                                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| call_queue_id | str                                                                                               | ✅       | Internal identifier of a call queue                                                                                                                          |

**Return Type**

`CallQueueOverflowSettings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallQueueOverflowSettingsRequestResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallQueueOverflowSettingsRequestResource(
    enabled=True,
    items=[
        {
            "id_": "id"
        }
    ]
)

result = sdk.call_queues.update_call_queue_overflow_settings(
    request_body=request_body,
    account_id="~",
    call_queue_id="callQueueId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
