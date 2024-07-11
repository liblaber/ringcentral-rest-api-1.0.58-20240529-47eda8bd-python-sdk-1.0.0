# BridgeManagementService

A list of all methods in the `BridgeManagementService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                                                                                                                                                                                                          |
| :------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_bridge](#create_bridge)                   | Creates a new bridge for the user specified by **accountId** and **extensionId** identifiers. The request body should contain JSON object which describes properties of the new bridge. The bridge can be created by a user himself, his delegate or any user who has the **Super Admin** privilege. |
| [get_default_bridge](#get_default_bridge)         | Returns a default bridge (PMI) for the user specified by **accountId** and **extensionId** identifiers.                                                                                                                                                                                              |
| [get_bridge_by_pstn_pin](#get_bridge_by_pstn_pin) | Finds a bridge by Host or Participant PSTN PIN.                                                                                                                                                                                                                                                      |
| [get_bridge_by_web_pin](#get_bridge_by_web_pin)   | Finds a bridge by short identifier (Web PIN). Also it can be used to find a default bridge by the alias (personal meeting name).                                                                                                                                                                     |
| [get_bridge](#get_bridge)                         | Returns a bridge by bridgeId identifier.                                                                                                                                                                                                                                                             |
| [update_bridge](#update_bridge)                   | Updates a bridge by bridgeId identifier. The request body should contain JSON object with updating properties. Update can only be done by bridge owner, his delegate or any user who has the **Super Admin** privilege.                                                                              |
| [delete_bridge](#delete_bridge)                   | Deletes a bridge by bridgeId identifier. Deletion can only be done by bridge owner, his delegate or any user who has the **Super Admin** privilege.                                                                                                                                                  |

## create_bridge

Creates a new bridge for the user specified by **accountId** and **extensionId** identifiers. The request body should contain JSON object which describes properties of the new bridge. The bridge can be created by a user himself, his delegate or any user who has the **Super Admin** privilege.

- HTTP Method: `POST`
- Endpoint: `/rcvideo/v2/account/{accountId}/extension/{extensionId}/bridges`

**Parameters**

| Name         | Type                                                    | Required | Description          |
| :----------- | :------------------------------------------------------ | :------- | :------------------- |
| request_body | [CreateBridgeRequest](../models/CreateBridgeRequest.md) | ❌       | The request body.    |
| account_id   | str                                                     | ✅       | Account identifier   |
| extension_id | str                                                     | ✅       | Extension identifier |

**Return Type**

`BridgeResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateBridgeRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateBridgeRequest(
    name="Weekly Meeting with Joseph",
    type_="Instant",
    pins={
        "pstn": {
            "host": "432331057631",
            "participant": "013409241367"
        },
        "web": "018209241352"
    },
    security={
        "password_protected": True,
        "password": "Wq123ygs15",
        "no_guests": True,
        "same_account": False,
        "e2ee": False
    },
    preferences={
        "join": {
            "audio_muted": False,
            "video_muted": True,
            "waiting_room_required": "Nobody",
            "pstn": {
                "bridge_id": "bridgeId",
                "prompt_announcement": True,
                "prompt_participants": True
            }
        },
        "play_tones": "On",
        "music_on_hold": True,
        "join_before_host": True,
        "screen_sharing": True,
        "recordings_mode": "Auto",
        "transcriptions_mode": "Auto",
        "recordings": {
            "everyone_can_control": {
                "enabled": True,
                "locked": True
            },
            "auto_shared": {
                "enabled": True,
                "locked": False
            }
        },
        "allow_everyone_transcribe_meetings": True
    }
)

result = sdk.bridge_management.create_bridge(
    request_body=request_body,
    account_id="accountId",
    extension_id="extensionId"
)

print(result)
```

## get_default_bridge

Returns a default bridge (PMI) for the user specified by **accountId** and **extensionId** identifiers.

- HTTP Method: `GET`
- Endpoint: `/rcvideo/v2/account/{accountId}/extension/{extensionId}/bridges/default`

**Parameters**

| Name         | Type | Required | Description          |
| :----------- | :--- | :------- | :------------------- |
| account_id   | str  | ✅       | Account identifier   |
| extension_id | str  | ✅       | Extension identifier |

**Return Type**

`BridgeResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bridge_management.get_default_bridge(
    account_id="accountId",
    extension_id="extensionId"
)

print(result)
```

## get_bridge_by_pstn_pin

Finds a bridge by Host or Participant PSTN PIN.

- HTTP Method: `GET`
- Endpoint: `/rcvideo/v2/bridges/pin/pstn/{pin}`

**Parameters**

| Name         | Type | Required | Description                                                                                                         |
| :----------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------ |
| pin          | str  | ✅       | Host or Participant PSTN PIN                                                                                        |
| phone_number | str  | ❌       | Phone number to find a phone group for PSTN PIN. If it is not specified, then the default phone group will be used. |
| pw           | str  | ❌       | Bridge hash password                                                                                                |

**Return Type**

`BridgeResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bridge_management.get_bridge_by_pstn_pin(
    pin="pin",
    phone_number="phoneNumber",
    pw="pw"
)

print(result)
```

## get_bridge_by_web_pin

Finds a bridge by short identifier (Web PIN). Also it can be used to find a default bridge by the alias (personal meeting name).

- HTTP Method: `GET`
- Endpoint: `/rcvideo/v2/bridges/pin/web/{pin}`

**Parameters**

| Name | Type | Required | Description                                                        |
| :--- | :--- | :------- | :----------------------------------------------------------------- |
| pin  | str  | ✅       | Bridge short identifier (Web PIN) or alias (personal meeting name) |
| pw   | str  | ❌       | Bridge hash password                                               |

**Return Type**

`BridgeResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bridge_management.get_bridge_by_web_pin(
    pin="pin",
    pw="pw"
)

print(result)
```

## get_bridge

Returns a bridge by bridgeId identifier.

- HTTP Method: `GET`
- Endpoint: `/rcvideo/v2/bridges/{bridgeId}`

**Parameters**

| Name      | Type | Required | Description          |
| :-------- | :--- | :------- | :------------------- |
| bridge_id | str  | ✅       | Bridge identifier    |
| pw        | str  | ❌       | Bridge hash password |

**Return Type**

`BridgeResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bridge_management.get_bridge(
    bridge_id="bridgeId",
    pw="pw"
)

print(result)
```

## update_bridge

Updates a bridge by bridgeId identifier. The request body should contain JSON object with updating properties. Update can only be done by bridge owner, his delegate or any user who has the **Super Admin** privilege.

- HTTP Method: `PATCH`
- Endpoint: `/rcvideo/v2/bridges/{bridgeId}`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [UpdateBridgeRequest](../models/UpdateBridgeRequest.md) | ✅       | The request body. |
| bridge_id    | str                                                     | ✅       | Bridge identifier |

**Return Type**

`BridgeResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateBridgeRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateBridgeRequest(
    name="Weekly Meeting with Joseph",
    pins={
        "bridge_id": "bridgeId",
        "web": "018209241352"
    },
    security={
        "password_protected": True,
        "password": "Wq123ygs15",
        "no_guests": True,
        "same_account": False,
        "e2ee": False
    },
    preferences={
        "join": {
            "audio_muted": False,
            "video_muted": True,
            "waiting_room_required": "Nobody",
            "pstn": {
                "bridge_id": "bridgeId",
                "prompt_announcement": True,
                "prompt_participants": True
            }
        },
        "play_tones": "On",
        "music_on_hold": True,
        "join_before_host": True,
        "screen_sharing": True,
        "recordings_mode": "Auto",
        "transcriptions_mode": "Auto",
        "recordings": {
            "everyone_can_control": {
                "enabled": True,
                "locked": True
            },
            "auto_shared": {
                "enabled": True,
                "locked": False
            }
        },
        "allow_everyone_transcribe_meetings": True
    }
)

result = sdk.bridge_management.update_bridge(
    request_body=request_body,
    bridge_id="bridgeId"
)

print(result)
```

## delete_bridge

Deletes a bridge by bridgeId identifier. Deletion can only be done by bridge owner, his delegate or any user who has the **Super Admin** privilege.

- HTTP Method: `DELETE`
- Endpoint: `/rcvideo/v2/bridges/{bridgeId}`

**Parameters**

| Name      | Type | Required | Description       |
| :-------- | :--- | :------- | :---------------- |
| bridge_id | str  | ✅       | Bridge identifier |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bridge_management.delete_bridge(bridge_id="bridgeId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
