# CustomFieldsService

A list of all methods in the `CustomFieldsService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                                     |
| :------------------------------------------ | :-------------------------------------------------------------- |
| [list_custom_fields](#list_custom_fields)   | Returns the list of created custom fields.                      |
| [create_custom_field](#create_custom_field) | Creates custom field attached to the object.                    |
| [update_custom_field](#update_custom_field) | Updates custom field by ID specified in path.                   |
| [delete_custom_field](#delete_custom_field) | Deletes custom field(s) by ID(s) with the corresponding values. |

## list_custom_fields

Returns the list of created custom fields.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/custom-fields`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CustomFieldList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.custom_fields.list_custom_fields(account_id="~")

print(result)
```

## create_custom_field

Creates custom field attached to the object.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/custom-fields`

**Parameters**

| Name         | Type                                                              | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CustomFieldCreateRequest](../models/CustomFieldCreateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CustomFieldModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CustomFieldCreateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CustomFieldCreateRequest(
    category="User",
    display_name="displayName"
)

result = sdk.custom_fields.create_custom_field(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## update_custom_field

Updates custom field by ID specified in path.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/custom-fields/{fieldId}`

**Parameters**

| Name         | Type                                                              | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CustomFieldUpdateRequest](../models/CustomFieldUpdateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| field_id     | str                                                               | ✅       | Custom field identifier                                                                                                                                      |

**Return Type**

`CustomFieldModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CustomFieldUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CustomFieldUpdateRequest(
    display_name="displayName"
)

result = sdk.custom_fields.update_custom_field(
    request_body=request_body,
    account_id="~",
    field_id="fieldId"
)

print(result)
```

## delete_custom_field

Deletes custom field(s) by ID(s) with the corresponding values.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/custom-fields/{fieldId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| field_id   | str  | ✅       | Custom field identifier                                                                                                                                      |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.custom_fields.delete_custom_field(
    account_id="~",
    field_id="fieldId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
