# PresenceService

A list of all methods in the `PresenceService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :---------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_call_queue_presence](#read_call_queue_presence)                         | Returns presence status of the call queue members.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [update_call_queue_presence](#update_call_queue_presence)                     | Updates presence status of the call queue members in the specified queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [read_account_presence](#read_account_presence)                               | Returns presence status of all extensions of an account. Please note: The presenceStatus is returned as Offline (the parameters telephonyStatus, message, userStatus and dndStatus are not returned at all) for the following extension types: Department, Announcement Only, Voicemail (Take Messages Only), Fax User, Paging Only Group, Shared Lines Group, IVR Menu, Application Extension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [read_extension_call_queue_presence](#read_extension_call_queue_presence)     | Returns a list of agent's call queues with the agent presence status (per queue).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [update_extension_call_queue_presence](#update_extension_call_queue_presence) | Updates availability of the agent for the call queues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [read_user_presence_status](#read_user_presence_status)                       | Returns the presence status of an extension or several extensions by their ID(s). The `presenceStatus` is returned as Offline (the parameters `telephonyStatus`, `message`, `userStatus` and `dndStatus` are not returned at all) for the following extension types: Department/Announcement Only/Take Messages Only (Voicemail)/Fax User/Paging Only Group/Shared Lines Group/IVR Menu/Application Extension/Park Location. If the user requests his/her own presence status, the response contains actual presence status even if the status publication is turned off. [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported. For batch requests the number of extensions in one request is limited to 30. If more extensions are included in the request, the error code 400 Bad Request is returned with the logical error code InvalidMultipartRequest and the corresponding message Extension Presence Info multipart request is limited to 30 extensions. |
| [update_user_presence_status](#update_user_presence_status)                   | Updates user-defined extension presence status, status message and DnD status by extension ID. Supported for regular User extensions only. The extension types listed do not support presence status: Department, Announcement Only, Take Messages Only (Voicemail), Fax User, Paging Only Group, Shared Lines Group, IVR Menu, Application Extension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [read_unified_presence](#read_unified_presence)                               | Returns the unified presence status of the requested user(s). The set of parameters returned by this method differs whether you return the requester's presence or any other user presence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [update_unified_presence](#update_unified_presence)                           | Updates the unified presence for the current user specified in path.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## read_call_queue_presence

Returns presence status of the call queue members.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-queues/{groupId}/presence`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id   | str  | ✅       | Internal identifier of a call queue extension                                                                                                                |

**Return Type**

`CallQueuePresence`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.presence.read_call_queue_presence(
    account_id="~",
    group_id="groupId"
)

print(result)
```

## update_call_queue_presence

Updates presence status of the call queue members in the specified queue.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-queues/{groupId}/presence`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CallQueueUpdatePresence](../models/CallQueueUpdatePresence.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| group_id     | str                                                             | ✅       | Internal identifier of a call queue extension                                                                                                                |

**Return Type**

`CallQueuePresence`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallQueueUpdatePresence

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallQueueUpdatePresence(
    records=[
        {
            "member": {
                "id_": "id"
            },
            "accept_current_queue_calls": False
        }
    ]
)

result = sdk.presence.update_call_queue_presence(
    request_body=request_body,
    account_id="~",
    group_id="groupId"
)

print(result)
```

## read_account_presence

Returns presence status of all extensions of an account. Please note: The presenceStatus is returned as Offline (the parameters telephonyStatus, message, userStatus and dndStatus are not returned at all) for the following extension types: Department, Announcement Only, Voicemail (Take Messages Only), Fax User, Paging Only Group, Shared Lines Group, IVR Menu, Application Extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/presence`

**Parameters**

| Name                     | Type | Required | Description                                                                                                                                                  |
| :----------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id               | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| detailed_telephony_state | bool | ❌       | Whether to return detailed telephony state                                                                                                                   |
| sip_data                 | bool | ❌       | Whether to return SIP data                                                                                                                                   |
| page                     | int  | ❌       | Page number for account presence information                                                                                                                 |
| per_page                 | int  | ❌       | Number for account presence information items per page                                                                                                       |

**Return Type**

`AccountPresenceInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.presence.read_account_presence(
    account_id="~",
    detailed_telephony_state=True,
    sip_data=True,
    page=5,
    per_page=10
)

print(result)
```

## read_extension_call_queue_presence

Returns a list of agent's call queues with the agent presence status (per queue).

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/call-queue-presence`

**Parameters**

| Name                   | Type | Required | Description                                                                                                                                                           |
| :--------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id             | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id           | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| editable_member_status | bool | ❌       | Filtering by the flag 'Allow members to change their Queue Status'. If 'true' only queues where user can change his availability status are returned                  |

**Return Type**

`ExtensionCallQueuePresenceList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.presence.read_extension_call_queue_presence(
    account_id="~",
    extension_id="~",
    editable_member_status=False
)

print(result)
```

## update_extension_call_queue_presence

Updates availability of the agent for the call queues.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/call-queue-presence`

**Parameters**

| Name         | Type                                                                                      | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ExtensionCallQueueUpdatePresenceList](../models/ExtensionCallQueueUpdatePresenceList.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`ExtensionCallQueuePresenceList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ExtensionCallQueueUpdatePresenceList

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ExtensionCallQueueUpdatePresenceList(
    records=[
        {
            "call_queue": {
                "id_": "id"
            },
            "accept_calls": False
        }
    ]
)

result = sdk.presence.update_extension_call_queue_presence(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_user_presence_status

Returns the presence status of an extension or several extensions by their ID(s). The `presenceStatus` is returned as Offline (the parameters `telephonyStatus`, `message`, `userStatus` and `dndStatus` are not returned at all) for the following extension types: Department/Announcement Only/Take Messages Only (Voicemail)/Fax User/Paging Only Group/Shared Lines Group/IVR Menu/Application Extension/Park Location. If the user requests his/her own presence status, the response contains actual presence status even if the status publication is turned off. [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported. For batch requests the number of extensions in one request is limited to 30. If more extensions are included in the request, the error code 400 Bad Request is returned with the logical error code InvalidMultipartRequest and the corresponding message Extension Presence Info multipart request is limited to 30 extensions.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/presence`

**Parameters**

| Name                     | Type | Required | Description                                                                                                                                                           |
| :----------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id               | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id             | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| detailed_telephony_state | bool | ❌       | Specifies whether to return a detailed telephony state or not                                                                                                         |
| sip_data                 | bool | ❌       | Specifies whether to return SIP data or not                                                                                                                           |

**Return Type**

`GetPresenceInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.presence.read_user_presence_status(
    account_id="~",
    extension_id="~",
    detailed_telephony_state=True,
    sip_data=True
)

print(result)
```

## update_user_presence_status

Updates user-defined extension presence status, status message and DnD status by extension ID. Supported for regular User extensions only. The extension types listed do not support presence status: Department, Announcement Only, Take Messages Only (Voicemail), Fax User, Paging Only Group, Shared Lines Group, IVR Menu, Application Extension.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/presence`

**Parameters**

| Name         | Type                                                    | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [PresenceInfoRequest](../models/PresenceInfoRequest.md) | ❌       | The request body.                                                                                                                                                     |
| account_id   | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                     | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`PresenceInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PresenceInfoRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PresenceInfoRequest(
    user_status="Offline",
    dnd_status="TakeAllCalls",
    message="cill",
    allow_see_my_presence=False,
    ring_on_monitored_call=False,
    pick_up_calls_on_hold=True,
    caller_id_visibility="All"
)

result = sdk.presence.update_user_presence_status(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_unified_presence

Returns the unified presence status of the requested user(s). The set of parameters returned by this method differs whether you return the requester's presence or any other user presence.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/unified-presence`

**Parameters**

| Name         | Type | Required | Description                                                                                                                             |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session                  |
| extension_id | str  | ✅       | Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session |

**Return Type**

`UnifiedPresence`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.presence.read_unified_presence(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_unified_presence

Updates the unified presence for the current user specified in path.

- HTTP Method: `PATCH`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/unified-presence`

**Parameters**

| Name         | Type                                                        | Required | Description                                                                                                                             |
| :----------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateUnifiedPresence](../models/UpdateUnifiedPresence.md) | ✅       | The request body.                                                                                                                       |
| account_id   | str                                                         | ✅       | Internal identifier of a RingCentral account or tilde (~) to indicate the account logged-in within the current session                  |
| extension_id | str                                                         | ✅       | Internal identifier of an extension or tilde (~) to indicate the extension assigned to the account logged-in within the current session |

**Return Type**

`UnifiedPresence`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateUnifiedPresence

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateUnifiedPresence(
    glip={
        "visibility": "Visible",
        "availability": "Available"
    },
    telephony={
        "availability": "TakeAllCalls"
    }
)

result = sdk.presence.update_unified_presence(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
