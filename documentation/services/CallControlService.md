# CallControlService

A list of all methods in the `CallControlService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_call_out_call_session](#create_call_out_call_session)       | Creates a new outbound call out session. Currently this method is supported for Softphone/Hardphone only, since device IDs for WebRTC/Mobile apps cannot be obtained.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [create_conference_call_session](#create_conference_call_session)   | Initiates a conference call session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [read_call_session_status](#read_call_session_status)               | Returns the status of a call session by ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [delete_call_session](#delete_call_session)                         | Drops a call session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [create_call_party_with_bring_in](#create_call_party_with_bring_in) | Adds a new party to the call session by bringing in an established SIP call connection. The maximum number of parties to bring in is 10; only 1 call party can be added per request. Currently, the method is supported for sessions of the `Conference` origin only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [read_call_party_status](#read_call_party_status)                   | Returns a call party status by ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [update_call_party](#update_call_party)                             | Modifies a call party by ID. There is a known limitation for Mute scenario - mute via REST API doesn't work with mute placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app you need to unmute both endpoints to bring the media back.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [delete_call_party](#delete_call_party)                             | Deletes a party from a call session by ID. A party can be deleted only if supervised or parked. It is possible to delete only one conference participant per request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [unhold_call_party](#unhold_call_party)                             | Brings a party back into a call and stops to play Hold Music. There is a known limitation for Hold API - hold via REST API doesn't work with hold placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app, then you need to un-hold both endpoints to remove Hold Music and bring media back.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [call_park_party](#call_park_party)                                 | Parks a call to a virtual location from where it can further be retrieved by any user from any phone of the system. The call session and call party identifiers should be specified in path. Currently, the users can park only their own incoming calls. Up to 50 calls can be parked simultaneously. Park location starts with asterisk (\*) and ranges 801-899.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [call_flip_party](#call_flip_party)                                 | Performs call flip procedure by holding opposite party and calling to the specified target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [reply_party](#reply_party)                                         | Replies with text/pattern without picking up a call.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [bridge_call_party](#bridge_call_party)                             | Allows the user to connect multiple call session participants over a conference call bridge. The current active call session ID and party ID of the user within this session should be specified in path; the bridged call session ID and party ID of the user within that session should be specified in request body. Thus, the user connects participants of two sessions into the one conference call using his/her own party IDs from both sessions."                                                                                                                                                                                                                                                                                                                                       |
| [ignore_call_in_queue](#ignore_call_in_queue)                       | Ignores a call to a call queue agent in `Setup` or `Proceeding` state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [supervise_call_party](#supervise_call_party)                       | Allows to monitor a call party in 'Listen' mode. Input parameters are extension number of a monitored user and internal identifier of a supervisor's device. Call session and party identifiers should be specified in path. Please note that for this method dual channel audio flow is supported, which means that you need to make one more request for monitoring the second participant of a call. And as a result of each monitoring request the client receives SIP invite with the following header `p-rc-api-monitoring-ids` containing IDs of the monitored party and session. The flow is supported for calls with no more than 2 participants. Currently, this method is supported for Softphone/Hardphone devices only, since device IDs for WebRTC/Mobile apps cannot be obtained. |
| [reject_party](#reject_party)                                       | Rejects an inbound call in a "Setup" or "Proceeding" state                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [start_call_recording](#start_call_recording)                       | Starts a new call recording for the party                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [pause_resume_call_recording](#pause_resume_call_recording)         | Pause/resume recording                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [answer_call_party](#answer_call_party)                             | Answers a call on a certain device by passing the corresponding device ID in request body. Supported for call forwarding, call transfer, call flip and call queues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [transfer_call_party](#transfer_call_party)                         | Transfers an answered call to the specified call party. Applicable for a call session in "Answered" or "Hold" state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [hold_call_party](#hold_call_party)                                 | Puts the party to stand-alone mode and starts to play Hold Music according to configuration & state to peers. There is a known limitation for Hold API - hold via REST API doesn't work with hold placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app, then you need to un-hold both endpoints to remove Hold Music and bring media back.                                                                                                                                                                                                                                                                                                                                                                          |
| [pickup_call_party](#pickup_call_party)                             | Picks up a call parked to the specified park location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [forward_call_party](#forward_call_party)                           | Forwards a non-answered incoming call to the specified call party. Applicable for a call session in "Setup" or "Proceeding" state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [supervise_call_session](#supervise_call_session)                   | Allows monitoring a call session in 'Listen' mode. Input parameters should contain internal identifiers of a monitored user and a supervisor's device. Call session should be specified in path. Please note that this method supports single channel audio flow, which means that audio of both call participants is mixed and delivered to the supervisor in single audio channel. Currently this method is supported for Softphone/Hardphone only, since device IDs for WebRTC/Mobile apps cannot be obtained.                                                                                                                                                                                                                                                                                |

## create_call_out_call_session

Creates a new outbound call out session. Currently this method is supported for Softphone/Hardphone only, since device IDs for WebRTC/Mobile apps cannot be obtained.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/call-out`

**Parameters**

| Name         | Type                                                  | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MakeCallOutRequest](../models/MakeCallOutRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CallSession`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MakeCallOutRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MakeCallOutRequest(
    from_={
        "device_id": "59474004"
    },
    to={
        "phone_number": "+16502223366",
        "extension_number": "103"
    },
    country_id=10
)

result = sdk.call_control.create_call_out_call_session(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## create_conference_call_session

Initiates a conference call session.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/conference`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CallSession`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.create_conference_call_session(account_id="~")

print(result)
```

## read_call_session_status

Returns the status of a call session by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |
| timestamp            | str  | ❌       | The date and time of a call session latest change                                                                                                            |
| timeout              | str  | ❌       | The time frame of awaiting for a status change before sending the resulting one in response                                                                  |

**Return Type**

`CallSessionObject`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.read_call_session_status(
    account_id="~",
    telephony_session_id="telephonySessionId",
    timestamp="timestamp",
    timeout="timeout"
)

print(result)
```

## delete_call_session

Drops a call session.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.delete_call_session(
    account_id="~",
    telephony_session_id="telephonySessionId"
)

print(result)
```

## create_call_party_with_bring_in

Adds a new party to the call session by bringing in an established SIP call connection. The maximum number of parties to bring in is 10; only 1 call party can be added per request. Currently, the method is supported for sessions of the `Conference` origin only.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/bring-in`

**Parameters**

| Name                 | Type                                            | Required | Description                                                                                                                                                  |
| :------------------- | :---------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [AddPartyRequest](../models/AddPartyRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                             | ✅       | Internal identifier of a call session                                                                                                                        |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AddPartyRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddPartyRequest(
    session_id="sessionId",
    party_id="partyId"
)

result = sdk.call_control.create_call_party_with_bring_in(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId"
)

print(result)
```

## read_call_party_status

Returns a call party status by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str  | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.read_call_party_status(
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## update_call_party

Modifies a call party by ID. There is a known limitation for Mute scenario - mute via REST API doesn't work with mute placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app you need to unmute both endpoints to bring the media back.

- HTTP Method: `PATCH`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}`

**Parameters**

| Name                 | Type                                                  | Required | Description                                                                                                                                                  |
| :------------------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [PartyUpdateRequest](../models/PartyUpdateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                                   | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                                   | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PartyUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PartyUpdateRequest(
    party={
        "muted": True,
        "stand_alone": True
    }
)

result = sdk.call_control.update_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## delete_call_party

Deletes a party from a call session by ID. A party can be deleted only if supervised or parked. It is possible to delete only one conference participant per request.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str  | ✅       | Internal identifier of a call party                                                                                                                          |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.delete_call_party(
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## unhold_call_party

Brings a party back into a call and stops to play Hold Music. There is a known limitation for Hold API - hold via REST API doesn't work with hold placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app, then you need to un-hold both endpoints to remove Hold Music and bring media back.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/unhold`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str  | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.unhold_call_party(
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## call_park_party

Parks a call to a virtual location from where it can further be retrieved by any user from any phone of the system. The call session and call party identifiers should be specified in path. Currently, the users can park only their own incoming calls. Up to 50 calls can be parked simultaneously. Park location starts with asterisk (\*) and ranges 801-899.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/park`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str  | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.call_park_party(
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## call_flip_party

Performs call flip procedure by holding opposite party and calling to the specified target

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/flip`

**Parameters**

| Name                 | Type                                        | Required | Description                                                                                                                                                  |
| :------------------- | :------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [CallPartyFlip](../models/CallPartyFlip.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                         | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                         | ✅       | Internal identifier of a call party                                                                                                                          |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallPartyFlip

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallPartyFlip(
    call_flip_id="callFlipId"
)

result = sdk.call_control.call_flip_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## reply_party

Replies with text/pattern without picking up a call.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/reply`

**Parameters**

| Name                 | Type                                          | Required | Description                                                                                                                                                  |
| :------------------- | :-------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [CallPartyReply](../models/CallPartyReply.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                           | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                           | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`ReplyParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallPartyReply

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallPartyReply(
    reply_with_text="replyWithText",
    reply_with_pattern={
        "pattern": "WillCallYouBack",
        "time": 5,
        "time_unit": "Minute"
    }
)

result = sdk.call_control.reply_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## bridge_call_party

Allows the user to connect multiple call session participants over a conference call bridge. The current active call session ID and party ID of the user within this session should be specified in path; the bridged call session ID and party ID of the user within that session should be specified in request body. Thus, the user connects participants of two sessions into the one conference call using his/her own party IDs from both sessions."

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/bridge`

**Parameters**

| Name                 | Type                                                    | Required | Description                                                                                                                                                  |
| :------------------- | :------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [BridgeTargetRequest](../models/BridgeTargetRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                                     | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                                     | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BridgeTargetRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BridgeTargetRequest(
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

result = sdk.call_control.bridge_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## ignore_call_in_queue

Ignores a call to a call queue agent in `Setup` or `Proceeding` state.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/ignore`

**Parameters**

| Name                 | Type                                                | Required | Description                                                                                                                                                  |
| :------------------- | :-------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [IgnoreRequestBody](../models/IgnoreRequestBody.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                                 | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                                 | ✅       | Internal identifier of a call party                                                                                                                          |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import IgnoreRequestBody

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = IgnoreRequestBody(
    device_id="400020454008"
)

result = sdk.call_control.ignore_call_in_queue(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## supervise_call_party

Allows to monitor a call party in 'Listen' mode. Input parameters are extension number of a monitored user and internal identifier of a supervisor's device. Call session and party identifiers should be specified in path. Please note that for this method dual channel audio flow is supported, which means that you need to make one more request for monitoring the second participant of a call. And as a result of each monitoring request the client receives SIP invite with the following header `p-rc-api-monitoring-ids` containing IDs of the monitored party and session. The flow is supported for calls with no more than 2 participants. Currently, this method is supported for Softphone/Hardphone devices only, since device IDs for WebRTC/Mobile apps cannot be obtained.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/supervise`

**Parameters**

| Name                 | Type                                                        | Required | Description                                                                                                                                                  |
| :------------------- | :---------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [PartySuperviseRequest](../models/PartySuperviseRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                                         | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                                         | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`PartySuperviseResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PartySuperviseRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PartySuperviseRequest(
    mode="Listen",
    supervisor_device_id="191888004",
    agent_extension_id="400378008008",
    auto_answer=True,
    media_sdp="sendOnly"
)

result = sdk.call_control.supervise_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## reject_party

Rejects an inbound call in a "Setup" or "Proceeding" state

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/reject`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str  | ✅       | Internal identifier of a call party                                                                                                                          |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.reject_party(
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## start_call_recording

Starts a new call recording for the party

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/recordings`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                                                  |
| :------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id           | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str  | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str  | ✅       | Internal identifier of a call party                                                                                                                          |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_control.start_call_recording(
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## pause_resume_call_recording

Pause/resume recording

- HTTP Method: `PATCH`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/recordings/{recordingId}`

**Parameters**

| Name                 | Type                                                    | Required | Description                                                                                                                                                  |
| :------------------- | :------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [CallRecordingUpdate](../models/CallRecordingUpdate.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                                     | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                                     | ✅       | Internal identifier of a call party                                                                                                                          |
| recording_id         | str                                                     | ✅       | Internal identifier of a recording                                                                                                                           |
| brand_id             | str                                                     | ✅       | Identifies a brand of a logged-in user or a brand of a sign-up session                                                                                       |

**Return Type**

`CallRecording`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallRecordingUpdate

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallRecordingUpdate(
    active=False
)

result = sdk.call_control.pause_resume_call_recording(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId",
    recording_id="recordingId",
    brand_id="~"
)

print(result)
```

## answer_call_party

Answers a call on a certain device by passing the corresponding device ID in request body. Supported for call forwarding, call transfer, call flip and call queues.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/answer`

**Parameters**

| Name                 | Type                                      | Required | Description                                                                                                                                                  |
| :------------------- | :---------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [AnswerTarget](../models/AnswerTarget.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                       | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                       | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AnswerTarget

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AnswerTarget(
    device_id="400018633008"
)

result = sdk.call_control.answer_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## transfer_call_party

Transfers an answered call to the specified call party. Applicable for a call session in "Answered" or "Hold" state.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/transfer`

**Parameters**

| Name                 | Type                                          | Required | Description                                                                                                                                                  |
| :------------------- | :-------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [TransferTarget](../models/TransferTarget.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                           | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                           | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TransferTarget

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TransferTarget(
    phone_number="phoneNumber",
    voicemail="voicemail",
    park_orbit="parkOrbit",
    extension_number="extensionNumber"
)

result = sdk.call_control.transfer_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## hold_call_party

Puts the party to stand-alone mode and starts to play Hold Music according to configuration & state to peers. There is a known limitation for Hold API - hold via REST API doesn't work with hold placed via RingCentral apps or HardPhone. It means that if you muted participant via Call Control API and RingCentral Desktop app, then you need to un-hold both endpoints to remove Hold Music and bring media back.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/hold`

**Parameters**

| Name                 | Type                                                      | Required | Description                                                                                                                                                  |
| :------------------- | :-------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [HoldCallPartyRequest](../models/HoldCallPartyRequest.md) | ❌       | The request body.                                                                                                                                            |
| account_id           | str                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                                       | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                                       | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import HoldCallPartyRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = HoldCallPartyRequest(
    proto="Auto"
)

result = sdk.call_control.hold_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## pickup_call_party

Picks up a call parked to the specified park location.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/pickup`

**Parameters**

| Name                 | Type                                      | Required | Description                                                                                                                                                  |
| :------------------- | :---------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [PickupTarget](../models/PickupTarget.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                       | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                       | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`CallParty`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PickupTarget

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PickupTarget(
    device_id="400018633008"
)

result = sdk.call_control.pickup_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## forward_call_party

Forwards a non-answered incoming call to the specified call party. Applicable for a call session in "Setup" or "Proceeding" state.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/parties/{partyId}/forward`

**Parameters**

| Name                 | Type                                        | Required | Description                                                                                                                                                  |
| :------------------- | :------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [ForwardTarget](../models/ForwardTarget.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                         | ✅       | Internal identifier of a call session                                                                                                                        |
| party_id             | str                                         | ✅       | Internal identifier of a call party                                                                                                                          |

**Return Type**

`ForwardCallPartyResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ForwardTarget

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ForwardTarget(
    phone_number="phoneNumber",
    voicemail="voicemail",
    extension_number="extensionNumber"
)

result = sdk.call_control.forward_call_party(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId",
    party_id="partyId"
)

print(result)
```

## supervise_call_session

Allows monitoring a call session in 'Listen' mode. Input parameters should contain internal identifiers of a monitored user and a supervisor's device. Call session should be specified in path. Please note that this method supports single channel audio flow, which means that audio of both call participants is mixed and delivered to the supervisor in single audio channel. Currently this method is supported for Softphone/Hardphone only, since device IDs for WebRTC/Mobile apps cannot be obtained.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/telephony/sessions/{telephonySessionId}/supervise`

**Parameters**

| Name                 | Type                                                                    | Required | Description                                                                                                                                                  |
| :------------------- | :---------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [SuperviseCallSessionRequest](../models/SuperviseCallSessionRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id           | str                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| telephony_session_id | str                                                                     | ✅       | Internal identifier of a call session                                                                                                                        |

**Return Type**

`SuperviseCallSessionResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SuperviseCallSessionRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SuperviseCallSessionRequest(
    mode="Listen",
    supervisor_device_id="191888004",
    agent_extension_id="400378008008",
    auto_answer=True,
    media_sdp="sendOnly"
)

result = sdk.call_control.supervise_call_session(
    request_body=request_body,
    account_id="~",
    telephony_session_id="telephonySessionId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
