# PresenceInfoResponse

**Properties**

| Name                   | Type                                   | Required | Description                                                                                                                                                                                      |
| :--------------------- | :------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uri                    | str                                    | ❌       | Link to the presence resource                                                                                                                                                                    |
| user_status            | PresenceInfoResponseUserStatus         | ❌       |                                                                                                                                                                                                  |
| dnd_status             | PresenceInfoResponseDndStatus          | ❌       |                                                                                                                                                                                                  |
| message                | str                                    | ❌       |                                                                                                                                                                                                  |
| allow_see_my_presence  | bool                                   | ❌       |                                                                                                                                                                                                  |
| caller_id_visibility   | PresenceInfoResponseCallerIdVisibility | ❌       | Configures the user presence visibility. When the `allowSeeMyPresence` parameter is set to `true`, the following visibility options are supported via this parameter - All, None, PermittedUsers |
| ring_on_monitored_call | bool                                   | ❌       |                                                                                                                                                                                                  |
| pick_up_calls_on_hold  | bool                                   | ❌       |                                                                                                                                                                                                  |
| active_calls           | List[ActiveCallInfo]                   | ❌       |                                                                                                                                                                                                  |
| extension              | GetPresenceExtensionInfo               | ❌       | Information on extension, for which this presence data is returned                                                                                                                               |
| meeting_status         | PresenceInfoResponseMeetingStatus      | ❌       | Meetings presence status                                                                                                                                                                         |
| telephony_status       | PresenceInfoResponseTelephonyStatus    | ❌       | Telephony presence status. Returned if telephony status is changed                                                                                                                               |
| presence_status        | PresenceInfoResponsePresenceStatus     | ❌       | Aggregated presence status, calculated from a number of sources                                                                                                                                  |

# PresenceInfoResponseUserStatus

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| OFFLINE   | str  | ✅       | "Offline"   |
| BUSY      | str  | ✅       | "Busy"      |
| AVAILABLE | str  | ✅       | "Available" |

# PresenceInfoResponseDndStatus

**Properties**

| Name                       | Type | Required | Description                  |
| :------------------------- | :--- | :------- | :--------------------------- |
| TAKEALLCALLS               | str  | ✅       | "TakeAllCalls"               |
| DONOTACCEPTDEPARTMENTCALLS | str  | ✅       | "DoNotAcceptDepartmentCalls" |
| TAKEDEPARTMENTCALLSONLY    | str  | ✅       | "TakeDepartmentCallsOnly"    |
| DONOTACCEPTANYCALLS        | str  | ✅       | "DoNotAcceptAnyCalls"        |
| UNKNOWN                    | str  | ✅       | "Unknown"                    |

# PresenceInfoResponseCallerIdVisibility

Configures the user presence visibility. When the `allowSeeMyPresence` parameter is set to `true`, the following visibility options are supported via this parameter - All, None, PermittedUsers

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| ALL            | str  | ✅       | "All"            |
| NONE           | str  | ✅       | "None"           |
| PERMITTEDUSERS | str  | ✅       | "PermittedUsers" |

# PresenceInfoResponseMeetingStatus

Meetings presence status

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| CONNECTED    | str  | ✅       | "Connected"    |
| DISCONNECTED | str  | ✅       | "Disconnected" |

# PresenceInfoResponseTelephonyStatus

Telephony presence status. Returned if telephony status is changed

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| NOCALL        | str  | ✅       | "NoCall"        |
| CALLCONNECTED | str  | ✅       | "CallConnected" |
| RINGING       | str  | ✅       | "Ringing"       |
| ONHOLD        | str  | ✅       | "OnHold"        |
| PARKEDCALL    | str  | ✅       | "ParkedCall"    |

# PresenceInfoResponsePresenceStatus

Aggregated presence status, calculated from a number of sources

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| OFFLINE   | str  | ✅       | "Offline"   |
| BUSY      | str  | ✅       | "Busy"      |
| AVAILABLE | str  | ✅       | "Available" |

<!-- This file was generated by liblab | https://liblab.com/ -->
