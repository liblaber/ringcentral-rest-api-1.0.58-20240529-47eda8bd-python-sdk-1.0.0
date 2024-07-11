# UserPermissionsService

A list of all methods in the `UserPermissionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                               |
| :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| [read_authorization_profile](#read_authorization_profile) | Returns a list of user permissions granted at authorization procedure. Please note: Some permissions may be restricted by extension type. |
| [check_user_permission](#check_user_permission)           | Checks if a certain user permission is activated for a particular extension.                                                              |
| [list_permissions](#list_permissions)                     | Returns a list of extension user permissions.                                                                                             |
| [read_permission](#read_permission)                       | Returns a user permission by ID.                                                                                                          |
| [list_permission_categories](#list_permission_categories) | Returns a list of permission categories.                                                                                                  |
| [read_permission_category](#read_permission_category)     | Returns a permission category by ID.                                                                                                      |

## read_authorization_profile

Returns a list of user permissions granted at authorization procedure. Please note: Some permissions may be restricted by extension type.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/authz-profile`

**Parameters**

| Name                | Type | Required | Description                                                                                                                                                           |
| :------------------ | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id        | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| target_extension_id | str  | ❌       |                                                                                                                                                                       |

**Return Type**

`AuthProfileResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_permissions.read_authorization_profile(
    account_id="~",
    extension_id="~",
    target_extension_id="targetExtensionId"
)

print(result)
```

## check_user_permission

Checks if a certain user permission is activated for a particular extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/authz-profile/check`

**Parameters**

| Name                | Type | Required | Description                                                                                                                                                           |
| :------------------ | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id          | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id        | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| permission_id       | str  | ❌       |                                                                                                                                                                       |
| target_extension_id | str  | ❌       |                                                                                                                                                                       |

**Return Type**

`AuthProfileCheckResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_permissions.check_user_permission(
    account_id="~",
    extension_id="~",
    permission_id="permissionId",
    target_extension_id="targetExtensionId"
)

print(result)
```

## list_permissions

Returns a list of extension user permissions.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/permission`

**Parameters**

| Name            | Type | Required | Description                                                                                                            |
| :-------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------- |
| page            | int  | ❌       | The result set page number (1-indexed) to return                                                                       |
| per_page        | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied |
| assignable      | bool | ❌       | Specifies whether to return only assignable permissions                                                                |
| service_plan_id | str  | ❌       | Internal identifier of a service plan                                                                                  |

**Return Type**

`PermissionCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_permissions.list_permissions(
    page=1,
    per_page=100,
    assignable=False,
    service_plan_id="servicePlanId"
)

print(result)
```

## read_permission

Returns a user permission by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/permission/{permissionId}`

**Parameters**

| Name          | Type | Required | Description                              |
| :------------ | :--- | :------- | :--------------------------------------- |
| permission_id | str  | ✅       | Internal identifier of a user permission |

**Return Type**

`PermissionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_permissions.read_permission(permission_id="permissionId")

print(result)
```

## list_permission_categories

Returns a list of permission categories.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/permission-category`

**Parameters**

| Name            | Type | Required | Description                                                                                                            |
| :-------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------- |
| page            | int  | ❌       | The result set page number (1-indexed) to return                                                                       |
| per_page        | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied |
| service_plan_id | str  | ❌       | Internal identifier of a service plan                                                                                  |

**Return Type**

`PermissionCategoryCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_permissions.list_permission_categories(
    page=1,
    per_page=100,
    service_plan_id="servicePlanId"
)

print(result)
```

## read_permission_category

Returns a permission category by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/permission-category/{permissionCategoryId}`

**Parameters**

| Name                   | Type | Required | Description                       |
| :--------------------- | :--- | :------- | :-------------------------------- |
| permission_category_id | str  | ✅       | Internal identifier of a category |

**Return Type**

`PermissionCategoryResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.user_permissions.read_permission_category(permission_category_id="permissionCategoryId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
