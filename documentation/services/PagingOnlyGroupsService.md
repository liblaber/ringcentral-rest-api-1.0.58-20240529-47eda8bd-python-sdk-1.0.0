# PagingOnlyGroupsService

A list of all methods in the `PagingOnlyGroupsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                   | Description                                              |
| :---------------------------------------------------------------------------------------- | :------------------------------------------------------- |
| [list_paging_group_users](#list_paging_group_users)                                       | Returns a list of users allowed to page this group.      |
| [assign_multiple_paging_group_users_devices](#assign_multiple_paging_group_users_devices) | Adds and/or removes paging group users and devices.      |
| [list_paging_group_devices](#list_paging_group_devices)                                   | Returns a list of paging devices assigned to this group. |

## list_paging_group_users

Returns a list of users allowed to page this group.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/paging-only-groups/{pagingOnlyGroupId}/users`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| paging_only_group_id | str  | ✅       | Internal identifier of a paging group                                                                                                                        |
| page                 | int  | ❌       | Indicates a page number to retrieve. Only positive number values are accepted                                                                                |
| per_page             | int  | ❌       | Indicates a page size (number of items)                                                                                                                      |

**Return Type**

`PagingOnlyGroupUsers`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.paging_only_groups.list_paging_group_users(
    account_id="~",
    paging_only_group_id="pagingOnlyGroupId",
    page=1,
    per_page=100
)

print(result)
```

## assign_multiple_paging_group_users_devices

Adds and/or removes paging group users and devices.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/paging-only-groups/{pagingOnlyGroupId}/bulk-assign`

**Parameters**

| Name                 | Type                                                          | Required | Description                                                                                                                                                  |
| :------------------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [EditPagingGroupRequest](../models/EditPagingGroupRequest.md) | ❌       | The request body.                                                                                                                                            |
| account_id           | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| paging_only_group_id | str                                                           | ✅       | Internal identifier of a paging group                                                                                                                        |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EditPagingGroupRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EditPagingGroupRequest(
    added_user_ids=[
        "addedUserIds"
    ],
    removed_user_ids=[
        "removedUserIds"
    ],
    added_device_ids=[
        "addedDeviceIds"
    ],
    removed_device_ids=[
        "removedDeviceIds"
    ]
)

result = sdk.paging_only_groups.assign_multiple_paging_group_users_devices(
    request_body=request_body,
    account_id="~",
    paging_only_group_id="pagingOnlyGroupId"
)

print(result)
```

## list_paging_group_devices

Returns a list of paging devices assigned to this group.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/paging-only-groups/{pagingOnlyGroupId}/devices`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| paging_only_group_id | str  | ✅       | Internal identifier of a paging group                                                                                                                        |
| page                 | int  | ❌       | Indicates a page number to retrieve. Only positive number values are accepted                                                                                |
| per_page             | int  | ❌       | Indicates a page size (number of items)                                                                                                                      |

**Return Type**

`PagingOnlyGroupDevices`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.paging_only_groups.list_paging_group_devices(
    account_id="~",
    paging_only_group_id="pagingOnlyGroupId",
    page=1,
    per_page=100
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
