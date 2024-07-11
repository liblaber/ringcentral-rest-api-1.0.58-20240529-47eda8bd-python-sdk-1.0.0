# GetPresenceInfo

**Properties**

| Name                   | Type                              | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--------------------- | :-------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uri                    | str                               | ❌       | Canonical URI of a presence info resource                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| allow_see_my_presence  | bool                              | ❌       | If set to `true` - enables other extensions to see the extension presence status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| caller_id_visibility   | GetPresenceInfoCallerIdVisibility | ❌       | Configures the user presence visibility. When the `allowSeeMyPresence` parameter is set to `true`, the following visibility options are supported via this parameter - All, None, PermittedUsers                                                                                                                                                                                                                                                                                                                                                                                                     |
| dnd_status             | GetPresenceInfoDndStatus          | ❌       | Extended DnD (Do not Disturb) status. Cannot be set for Department/Announcement/Voicemail (Take Messages Only)/Fax User/Shared Lines Group/Paging Only Group/IVR Menu/Application Extension/Park Location extensions. The 'DoNotAcceptDepartmentCalls' and 'TakeDepartmentCallsOnly' values are applicable only for extensions - members of a Department; if these values are set for department outsiders, the 400 Bad Request error code is returned. The 'TakeDepartmentCallsOnly' status can be set through the old RingCentral user interface and is available for some migrated accounts only. |
| extension              | GetPresenceExtensionInfo          | ❌       | Information on extension, for which this presence data is returned                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| message                | str                               | ❌       | Custom status message (as previously published by user)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| pick_up_calls_on_hold  | bool                              | ❌       | If `true` enables the extension user to pick up a monitored line on hold                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| presence_status        | GetPresenceInfoPresenceStatus     | ❌       | Aggregated presence status, calculated from a number of sources                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ring_on_monitored_call | bool                              | ❌       | If `true` enables to ring extension phone, if any user monitored by this extension is ringing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| telephony_status       | GetPresenceInfoTelephonyStatus    | ❌       | Telephony presence status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| user_status            | GetPresenceInfoUserStatus         | ❌       | User-defined presence status (as previously published by the user)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| meeting_status         | GetPresenceInfoMeetingStatus      | ❌       | RingCentral Meetings presence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| active_calls           | List[ActiveCallInfo]              | ❌       | Information on active calls                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

# GetPresenceInfoCallerIdVisibility

Configures the user presence visibility. When the `allowSeeMyPresence` parameter is set to `true`, the following visibility options are supported via this parameter - All, None, PermittedUsers

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| ALL            | str  | ✅       | "All"            |
| NONE           | str  | ✅       | "None"           |
| PERMITTEDUSERS | str  | ✅       | "PermittedUsers" |

# GetPresenceInfoDndStatus

Extended DnD (Do not Disturb) status. Cannot be set for Department/Announcement/Voicemail (Take Messages Only)/Fax User/Shared Lines Group/Paging Only Group/IVR Menu/Application Extension/Park Location extensions. The 'DoNotAcceptDepartmentCalls' and 'TakeDepartmentCallsOnly' values are applicable only for extensions - members of a Department; if these values are set for department outsiders, the 400 Bad Request error code is returned. The 'TakeDepartmentCallsOnly' status can be set through the old RingCentral user interface and is available for some migrated accounts only.

**Properties**

| Name                       | Type | Required | Description                  |
| :------------------------- | :--- | :------- | :--------------------------- |
| TAKEALLCALLS               | str  | ✅       | "TakeAllCalls"               |
| DONOTACCEPTANYCALLS        | str  | ✅       | "DoNotAcceptAnyCalls"        |
| DONOTACCEPTDEPARTMENTCALLS | str  | ✅       | "DoNotAcceptDepartmentCalls" |
| TAKEDEPARTMENTCALLSONLY    | str  | ✅       | "TakeDepartmentCallsOnly"    |

# GetPresenceInfoPresenceStatus

Aggregated presence status, calculated from a number of sources

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| OFFLINE   | str  | ✅       | "Offline"   |
| BUSY      | str  | ✅       | "Busy"      |
| AVAILABLE | str  | ✅       | "Available" |

# GetPresenceInfoTelephonyStatus

Telephony presence status

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| NOCALL        | str  | ✅       | "NoCall"        |
| CALLCONNECTED | str  | ✅       | "CallConnected" |
| RINGING       | str  | ✅       | "Ringing"       |
| ONHOLD        | str  | ✅       | "OnHold"        |
| PARKEDCALL    | str  | ✅       | "ParkedCall"    |

# GetPresenceInfoUserStatus

User-defined presence status (as previously published by the user)

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| OFFLINE   | str  | ✅       | "Offline"   |
| BUSY      | str  | ✅       | "Busy"      |
| AVAILABLE | str  | ✅       | "Available" |

# GetPresenceInfoMeetingStatus

RingCentral Meetings presence

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| CONNECTED    | str  | ✅       | "Connected"    |
| DISCONNECTED | str  | ✅       | "Disconnected" |

<!-- This file was generated by liblab | https://liblab.com/ -->
