# RoleManagementService

A list of all methods in the `RoleManagementService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                         |
| :------------------------------------------------------------------------------ | :------------------------------------------------------------------ |
| [list_assigned_roles](#list_assigned_roles)                                     | Returns a list of roles assigned to the current account.            |
| [list_user_roles](#list_user_roles)                                             | Returns a list of account user roles.                               |
| [create_custom_role](#create_custom_role)                                       | Creates a custom user role.                                         |
| [read_default_role](#read_default_role)                                         | Returns the default user role of the current account.               |
| [update_default_user_role](#update_default_user_role)                           | Updates the account default user role.                              |
| [read_user_role](#read_user_role)                                               | Returns a user role assigned to the current account.                |
| [update_user_role](#update_user_role)                                           | Updates a user role assigned to the current account by ID.          |
| [delete_custom_role](#delete_custom_role)                                       | Deletes a custom user role by ID.                                   |
| [assign_multiple_user_roles](#assign_multiple_user_roles)                       | Assigns multiple user roles.                                        |
| [list_of_available_for_assigning_roles](#list_of_available_for_assigning_roles) | Returns a list of roles which can be assigned to a given extension. |
| [list_user_assigned_roles](#list_user_assigned_roles)                           | Returns a list of roles assigned to the current extension.          |
| [update_user_assigned_roles](#update_user_assigned_roles)                       | Updates a list of roles assigned to the current user.               |
| [assign_default_role](#assign_default_role)                                     | Assigns the default role to the currently logged-in user extension. |
| [list_standard_user_role](#list_standard_user_role)                             | Returns a list of standard user roles.                              |
| [read_standard_user_role](#read_standard_user_role)                             | Returns a standard user role by ID.                                 |

## list_assigned_roles

Returns a list of roles assigned to the current account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/assigned-role`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                  |
| :---------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id  | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| show_hidden | bool | ❌       | Specifies if hidden roles are shown or not                                                                                                                   |

**Return Type**

`ExtensionWithRolesCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.list_assigned_roles(
    account_id="~",
    show_hidden=False
)

print(result)
```

## list_user_roles

Returns a list of account user roles.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| custom     | bool | ❌       | Specifies whether to return custom roles or predefined roles only. If not specified, all roles are returned                                                  |
| page       | int  | ❌       | The result set page number (1-indexed) to return                                                                                                             |
| per_page   | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                       |

**Return Type**

`RolesCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.list_user_roles(
    account_id="~",
    custom=False,
    page=1,
    per_page=100
)

print(result)
```

## create_custom_role

Creates a custom user role.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role`

**Parameters**

| Name         | Type                                      | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [RoleResource](../models/RoleResource.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import RoleResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RoleResource(
    uri="uri",
    id_="id",
    display_name="Super Admin",
    description="Primary company administrator role",
    site_compatible=False,
    custom=True,
    scope="Account",
    hidden=False,
    last_updated="lastUpdated",
    permissions=[
        {
            "uri": "uri",
            "id_": "id",
            "site_compatible": "Compatible",
            "read_only": True,
            "assignable": False,
            "permissions_capabilities": {
                "enabled": False,
                "manage_enabled": True,
                "grant_enabled": True
            }
        }
    ]
)

result = sdk.role_management.create_custom_role(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_default_role

Returns the default user role of the current account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role/default`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`DefaultUserRole`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.read_default_role(account_id="~")

print(result)
```

## update_default_user_role

Updates the account default user role.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role/default`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [DefaultUserRoleRequest](../models/DefaultUserRoleRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`DefaultUserRole`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import DefaultUserRoleRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = DefaultUserRoleRequest(
    id_="id"
)

result = sdk.role_management.update_default_user_role(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_user_role

Returns a user role assigned to the current account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role/{roleId}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| role_id              | str  | ✅       | Internal identifier of a role                                                                                                                                |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| advanced_permissions | bool | ❌       | Specifies whether to return advanced permissions capabilities within `permissionsCapabilities` resource. The default value is false.                         |

**Return Type**

`RoleResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.read_user_role(
    role_id="roleId",
    account_id="~",
    advanced_permissions=True
)

print(result)
```

## update_user_role

Updates a user role assigned to the current account by ID.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role/{roleId}`

**Parameters**

| Name         | Type                                      | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [RoleResource](../models/RoleResource.md) | ✅       | The request body.                                                                                                                                            |
| role_id      | str                                       | ✅       | Internal identifier of a role                                                                                                                                |
| account_id   | str                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`RoleResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import RoleResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RoleResource(
    uri="uri",
    id_="id",
    display_name="Super Admin",
    description="Primary company administrator role",
    site_compatible=False,
    custom=True,
    scope="Account",
    hidden=False,
    last_updated="lastUpdated",
    permissions=[
        {
            "uri": "uri",
            "id_": "id",
            "site_compatible": "Compatible",
            "read_only": True,
            "assignable": False,
            "permissions_capabilities": {
                "enabled": False,
                "manage_enabled": True,
                "grant_enabled": True
            }
        }
    ]
)

result = sdk.role_management.update_user_role(
    request_body=request_body,
    role_id="roleId",
    account_id="~"
)

print(result)
```

## delete_custom_role

Deletes a custom user role by ID.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role/{roleId}`

**Parameters**

| Name          | Type | Required | Description                                                                                                                                                  |
| :------------ | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| role_id       | str  | ✅       | Internal identifier of a role                                                                                                                                |
| account_id    | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| validate_only | bool | ❌       | Specifies that role should be validated prior to deletion, whether it can be deleted or not                                                                  |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.delete_custom_role(
    role_id="roleId",
    account_id="~",
    validate_only=True
)

print(result)
```

## assign_multiple_user_roles

Assigns multiple user roles.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/user-role/{roleId}/bulk-assign`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [BulkRoleAssignResource](../models/BulkRoleAssignResource.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| role_id      | str                                                           | ✅       | Internal identifier of a role                                                                                                                                |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BulkRoleAssignResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BulkRoleAssignResource(
    site_restricted=True,
    site_compatible=False,
    uri="uri",
    added_extension_ids=[
        "addedExtensionIds"
    ],
    removed_extension_ids=[
        "removedExtensionIds"
    ]
)

result = sdk.role_management.assign_multiple_user_roles(
    request_body=request_body,
    account_id="~",
    role_id="roleId"
)

print(result)
```

## list_of_available_for_assigning_roles

Returns a list of roles which can be assigned to a given extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/assignable-roles`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| page         | int  | ❌       | The result set page number (1-indexed) to return                                                                                                                      |
| per_page     | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                                |

**Return Type**

`RolesCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.list_of_available_for_assigning_roles(
    account_id="~",
    extension_id="~",
    page=1,
    per_page=100
)

print(result)
```

## list_user_assigned_roles

Returns a list of roles assigned to the current extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/assigned-role`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| show_hidden  | bool | ❌       | Specifies if hidden roles are shown or not                                                                                                                            |

**Return Type**

`AssignedRolesResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.list_user_assigned_roles(
    account_id="~",
    extension_id="~",
    show_hidden=True
)

print(result)
```

## update_user_assigned_roles

Updates a list of roles assigned to the current user.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/assigned-role`

**Parameters**

| Name         | Type                                                        | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AssignedRolesResource](../models/AssignedRolesResource.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`AssignedRolesResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AssignedRolesResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AssignedRolesResource(
    uri="uri",
    records=[
        {
            "uri": "uri",
            "id_": "id",
            "auto_assigned": False,
            "display_name": "displayName",
            "site_compatible": False,
            "site_restricted": False
        }
    ]
)

result = sdk.role_management.update_user_assigned_roles(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## assign_default_role

Assigns the default role to the currently logged-in user extension.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/assigned-role/default`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`AssignedRolesResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.assign_default_role(
    account_id="~",
    extension_id="~"
)

print(result)
```

## list_standard_user_role

Returns a list of standard user roles.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/user-role`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                          |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------- |
| service_plan_id      | str  | ❌       | Internal identifier of a service plan.                                                                                               |
| page                 | int  | ❌       | The result set page number (1-indexed) to return                                                                                     |
| per_page             | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied               |
| advanced_permissions | bool | ❌       | Specifies whether to return advanced permissions capabilities within `permissionsCapabilities` resource. The default value is false. |

**Return Type**

`RolesCollectionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.list_standard_user_role(
    service_plan_id="servicePlanId",
    page=1,
    per_page=100,
    advanced_permissions=True
)

print(result)
```

## read_standard_user_role

Returns a standard user role by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/user-role/{roleId}`

**Parameters**

| Name    | Type | Required | Description                   |
| :------ | :--- | :------- | :---------------------------- |
| role_id | str  | ✅       | Internal identifier of a role |

**Return Type**

`RoleResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.role_management.read_standard_user_role(role_id="roleId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
