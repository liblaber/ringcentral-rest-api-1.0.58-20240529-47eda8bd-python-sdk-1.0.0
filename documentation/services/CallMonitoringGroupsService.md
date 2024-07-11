# CallMonitoringGroupsService

A list of all methods in the `CallMonitoringGroupsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                              |
| :------------------------------------------------------------------------ | :----------------------------------------------------------------------- |
| [list_call_monitoring_groups](#list_call_monitoring_groups)               | Returns a list of call monitoring groups filtered by an extension.       |
| [create_call_monitoring_group](#create_call_monitoring_group)             | Creates a new call monitoring group.                                     |
| [update_call_monitoring_group](#update_call_monitoring_group)             | Updates a call monitoring group name.                                    |
| [delete_call_monitoring_group](#delete_call_monitoring_group)             | Removes information about a call monitoring group specified in path.     |
| [update_call_monitoring_group_list](#update_call_monitoring_group_list)   | Updates a list of call monitoring groups.                                |
| [list_call_monitoring_group_members](#list_call_monitoring_group_members) | Returns a list of members for a call monitoring group specified in path. |

## list_call_monitoring_groups

Returns a list of call monitoring groups filtered by an extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-monitoring-groups`

**Parameters**

| Name                | Type | Required | Description                                                                                                                                                  |
| :------------------ | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| page                | int  | ❌       | Indicates a page number to retrieve. Only positive number values are allowed                                                                                 |
| per_page            | int  | ❌       | Indicates a page size (number of items)                                                                                                                      |
| member_extension_id | str  | ❌       | Internal identifier of an extension that is a member of every group within the result                                                                        |

**Return Type**

`CallMonitoringGroups`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_monitoring_groups.list_call_monitoring_groups(
    account_id="~",
    page=1,
    per_page=100,
    member_extension_id="memberExtensionId"
)

print(result)
```

## create_call_monitoring_group

Creates a new call monitoring group.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-monitoring-groups`

**Parameters**

| Name         | Type                                                                              | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateCallMonitoringGroupRequest](../models/CreateCallMonitoringGroupRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CallMonitoringGroup`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateCallMonitoringGroupRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateCallMonitoringGroupRequest(
    name="name"
)

result = sdk.call_monitoring_groups.create_call_monitoring_group(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## update_call_monitoring_group

Updates a call monitoring group name.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId}`

**Parameters**

| Name         | Type                                                                              | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateCallMonitoringGroupRequest](../models/CreateCallMonitoringGroupRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id     | str                                                                               | ✅       | Internal identifier of a call monitoring group                                                                                                               |

**Return Type**

`CallMonitoringGroup`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateCallMonitoringGroupRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateCallMonitoringGroupRequest(
    name="name"
)

result = sdk.call_monitoring_groups.update_call_monitoring_group(
    request_body=request_body,
    account_id="~",
    group_id="groupId"
)

print(result)
```

## delete_call_monitoring_group

Removes information about a call monitoring group specified in path.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id   | str  | ✅       | Internal identifier of a call monitoring group                                                                                                               |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_monitoring_groups.delete_call_monitoring_group(
    account_id="~",
    group_id="groupId"
)

print(result)
```

## update_call_monitoring_group_list

Updates a list of call monitoring groups.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId}/bulk-assign`

**Parameters**

| Name         | Type                                                              | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CallMonitoringBulkAssign](../models/CallMonitoringBulkAssign.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id     | str                                                               | ✅       | Internal identifier of a call monitoring group                                                                                                               |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallMonitoringBulkAssign

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallMonitoringBulkAssign(
    added_extensions=[
        {
            "id_": "id",
            "permissions": [
                "Monitoring"
            ]
        }
    ],
    updated_extensions=[
        {
            "id_": "id",
            "permissions": [
                "Monitoring"
            ]
        }
    ],
    removed_extensions=[
        {
            "id_": "id",
            "permissions": [
                "Monitoring"
            ]
        }
    ]
)

result = sdk.call_monitoring_groups.update_call_monitoring_group_list(
    request_body=request_body,
    account_id="~",
    group_id="groupId"
)

print(result)
```

## list_call_monitoring_group_members

Returns a list of members for a call monitoring group specified in path.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-monitoring-groups/{groupId}/members`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id   | str  | ✅       | Internal identifier of a call monitoring group                                                                                                               |
| page       | int  | ❌       | Indicates a page number to retrieve. Only positive number values are allowed                                                                                 |
| per_page   | int  | ❌       | Indicates a page size (number of items)                                                                                                                      |

**Return Type**

`CallMonitoringGroupMemberList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_monitoring_groups.list_call_monitoring_group_members(
    account_id="~",
    group_id="groupId",
    page=1,
    per_page=100
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
