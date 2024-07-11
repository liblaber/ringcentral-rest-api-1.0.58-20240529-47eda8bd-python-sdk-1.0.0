# ScimService

A list of all methods in the `ScimService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                          |
| :------------------------------------------------------ | :--------------------------------------------------- |
| [scim_list_schemas2](#scim_list_schemas2)               | Returns the list of schemas                          |
| [scim_get_schema2](#scim_get_schema2)                   | Returns SCIM schema                                  |
| [scim_search_via_get2](#scim_search_via_get2)           | Returns the list of users satisfying search criteria |
| [scim_create_user2](#scim_create_user2)                 | Creates a new user                                   |
| [scim_search_via_post2](#scim_search_via_post2)         | Returns the list of users satisfying search criteria |
| [scim_get_user2](#scim_get_user2)                       | Returns a user by ID                                 |
| [scim_update_user2](#scim_update_user2)                 | Updates a user                                       |
| [scim_patch_user2](#scim_patch_user2)                   | Updates a user (partial update)                      |
| [scim_delete_user2](#scim_delete_user2)                 | Deletes a user                                       |
| [scim_get_provider_config2](#scim_get_provider_config2) | Returns SCIM service provider configuration          |
| [scim_list_resource_types2](#scim_list_resource_types2) | Returns the list of supported SCIM resource types    |
| [scim_get_resource_type2](#scim_get_resource_type2)     | Returns resource type by ID                          |

## scim_list_schemas2

Returns the list of schemas

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Schemas`

**Return Type**

`ScimSchemaSearchResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_list_schemas2()

print(result)
```

## scim_get_schema2

Returns SCIM schema

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Schemas/{uri}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| uri  | str  | ✅       | Schema URI  |

**Return Type**

`ScimSchemaResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_get_schema2(uri="uri")

print(result)
```

## scim_search_via_get2

Returns the list of users satisfying search criteria

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Users`

**Parameters**

| Name        | Type | Required | Description                                                   |
| :---------- | :--- | :------- | :------------------------------------------------------------ |
| filter      | str  | ❌       | Only support 'userName' or 'email' filter expressions for now |
| start_index | int  | ❌       | Start index (1-based)                                         |
| count       | int  | ❌       | Page size                                                     |

**Return Type**

`ScimUserSearchResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_search_via_get2(
    filter="filter",
    start_index=1,
    count=100
)

print(result)
```

## scim_create_user2

Creates a new user

- HTTP Method: `POST`
- Endpoint: `/scim/v2/Users`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [ScimUser](../models/ScimUser.md) | ✅       | The request body. |

**Return Type**

`ScimUserResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ScimUser

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ScimUser(
    active=True,
    addresses=[
        {
            "country": "country",
            "locality": "locality",
            "postal_code": "postalCode",
            "region": "region",
            "street_address": "streetAddress",
            "type_": "work"
        }
    ],
    emails=[
        {
            "type_": "work",
            "value": "value"
        }
    ],
    external_id="externalId",
    id_="id",
    name={
        "family_name": "familyName",
        "given_name": "givenName"
    },
    phone_numbers=[
        {
            "type_": "work",
            "value": "value"
        }
    ],
    photos=[
        {
            "type_": "photo",
            "value": "value"
        }
    ],
    schemas=[
        "urn:ietf:params:scim:schemas:core:2.0:User"
    ],
    title="title",
    urn_ietf_params_scim_schemas_extension_enterprise_2_0_user={
        "department": "department"
    },
    user_name="userName"
)

result = sdk.scim.scim_create_user2(request_body=request_body)

print(result)
```

## scim_search_via_post2

Returns the list of users satisfying search criteria

- HTTP Method: `POST`
- Endpoint: `/scim/v2/Users/.search`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [ScimSearchRequest](../models/ScimSearchRequest.md) | ✅       | The request body. |

**Return Type**

`ScimUserSearchResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ScimSearchRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ScimSearchRequest(
    count=1,
    filter="filter",
    schemas=[
        "urn:ietf:params:scim:api:messages:2.0:SearchRequest"
    ],
    start_index=4
)

result = sdk.scim.scim_search_via_post2(request_body=request_body)

print(result)
```

## scim_get_user2

Returns a user by ID

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Users/{scimUserId}`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| scim_user_id | str  | ✅       | User ID     |

**Return Type**

`ScimUserResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_get_user2(scim_user_id="scimUserId")

print(result)
```

## scim_update_user2

Updates a user

- HTTP Method: `PUT`
- Endpoint: `/scim/v2/Users/{scimUserId}`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [ScimUser](../models/ScimUser.md) | ✅       | The request body. |
| scim_user_id | str                               | ✅       | User ID           |

**Return Type**

`ScimUserResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ScimUser

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ScimUser(
    active=True,
    addresses=[
        {
            "country": "country",
            "locality": "locality",
            "postal_code": "postalCode",
            "region": "region",
            "street_address": "streetAddress",
            "type_": "work"
        }
    ],
    emails=[
        {
            "type_": "work",
            "value": "value"
        }
    ],
    external_id="externalId",
    id_="id",
    name={
        "family_name": "familyName",
        "given_name": "givenName"
    },
    phone_numbers=[
        {
            "type_": "work",
            "value": "value"
        }
    ],
    photos=[
        {
            "type_": "photo",
            "value": "value"
        }
    ],
    schemas=[
        "urn:ietf:params:scim:schemas:core:2.0:User"
    ],
    title="title",
    urn_ietf_params_scim_schemas_extension_enterprise_2_0_user={
        "department": "department"
    },
    user_name="userName"
)

result = sdk.scim.scim_update_user2(
    request_body=request_body,
    scim_user_id="scimUserId"
)

print(result)
```

## scim_patch_user2

Updates a user (partial update)

- HTTP Method: `PATCH`
- Endpoint: `/scim/v2/Users/{scimUserId}`

**Parameters**

| Name         | Type                                        | Required | Description       |
| :----------- | :------------------------------------------ | :------- | :---------------- |
| request_body | [ScimUserPatch](../models/ScimUserPatch.md) | ✅       | The request body. |
| scim_user_id | str                                         | ✅       | User ID           |

**Return Type**

`ScimUserResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ScimUserPatch

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ScimUserPatch(
    operations=[
        {
            "op": "add",
            "path": "path",
            "value": "value"
        }
    ],
    schemas=[
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    ]
)

result = sdk.scim.scim_patch_user2(
    request_body=request_body,
    scim_user_id="scimUserId"
)

print(result)
```

## scim_delete_user2

Deletes a user

- HTTP Method: `DELETE`
- Endpoint: `/scim/v2/Users/{scimUserId}`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| scim_user_id | str  | ✅       | User ID     |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_delete_user2(scim_user_id="scimUserId")

print(result)
```

## scim_get_provider_config2

Returns SCIM service provider configuration

- HTTP Method: `GET`
- Endpoint: `/scim/v2/ServiceProviderConfig`

**Return Type**

`ScimProviderConfig`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_get_provider_config2()

print(result)
```

## scim_list_resource_types2

Returns the list of supported SCIM resource types

- HTTP Method: `GET`
- Endpoint: `/scim/v2/ResourceTypes`

**Return Type**

`ScimResourceTypeSearchResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_list_resource_types2()

print(result)
```

## scim_get_resource_type2

Returns resource type by ID

- HTTP Method: `GET`
- Endpoint: `/scim/v2/ResourceTypes/{type}`

**Parameters**

| Name   | Type | Required | Description   |
| :----- | :--- | :------- | :------------ |
| type\_ | str  | ✅       | Resource type |

**Return Type**

`ScimResourceTypeResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.scim_get_resource_type2(type_="type")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
