# IdentitiesService

A list of all methods in the `IdentitiesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [soc_msg_list_identities](#soc_msg_list_identities) | List identities by creation date. The default order is descending. The account context of this request is determined by the RC Account Id associated with the access token provided in the Authorization header. The query parameters provided shall be considered an AND operation to filter the list. A query parameter not specified or a query parameter provided with no value is treated as not required for filtering the list. |
| [soc_msg_get_identity](#soc_msg_get_identity)       | Renders an identity from given id.                                                                                                                                                                                                                                                                                                                                                                                                     |

## soc_msg_list_identities

List identities by creation date. The default order is descending. The account context of this request is determined by the RC Account Id associated with the access token provided in the Authorization header. The query parameters provided shall be considered an AND operation to filter the list. A query parameter not specified or a query parameter provided with no value is treated as not required for filtering the list.

- HTTP Method: `GET`
- Endpoint: `/cx/social-messaging/v1/identities`

**Parameters**

| Name               | Type                                                            | Required | Description                                                                                                             |
| :----------------- | :-------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| source_id          | str                                                             | ❌       | Filter based on the specified sourceId.                                                                                 |
| identity_group_ids | List[str]                                                       | ❌       | Filter based on the specified identityGroupIds (separated by commas).                                                   |
| user_id            | str                                                             | ❌       | Filter based on the specified userId.                                                                                   |
| uuid               | str                                                             | ❌       | Filter based on the specified uuid.                                                                                     |
| order_by           | [SocMsgCreationTimeOrder](../models/SocMsgCreationTimeOrder.md) | ❌       | Order results by specified field.                                                                                       |
| page_token         | str                                                             | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |
| per_page           | int                                                             | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |

**Return Type**

`IdentitiesList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SocMsgCreationTimeOrder

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
identity_group_ids=[
    "identityGroupIds"
]

result = sdk.identities.soc_msg_list_identities(
    source_id="sourceId",
    identity_group_ids=identity_group_ids,
    user_id="userId",
    uuid="uuid",
    order_by="-creationTime",
    page_token="pageToken",
    per_page=100
)

print(result)
```

## soc_msg_get_identity

Renders an identity from given id.

- HTTP Method: `GET`
- Endpoint: `/cx/social-messaging/v1/identities/{identityId}`

**Parameters**

| Name        | Type | Required | Description          |
| :---------- | :--- | :------- | :------------------- |
| identity_id | str  | ✅       | Identity identifier. |

**Return Type**

`IdentityModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.identities.soc_msg_get_identity(identity_id="506d9e817aa58d1259000f12")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
