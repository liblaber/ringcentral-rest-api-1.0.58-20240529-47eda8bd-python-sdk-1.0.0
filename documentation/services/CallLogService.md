# CallLogService

A list of all methods in the `CallLogService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                             |
| :---------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| [read_company_call_log](#read_company_call_log)             | Returns call log records filtered by parameters specified.                                              |
| [read_company_call_record](#read_company_call_record)       | Returns individual call log record(s) by ID. Batch syntax is supported.                                 |
| [sync_account_call_log](#sync_account_call_log)             | Synchronizes company call log records.                                                                  |
| [list_company_active_calls](#list_company_active_calls)     | Returns records of all calls that are in progress, ordered by start time in descending order.           |
| [read_user_call_log](#read_user_call_log)                   | Returns call log records filtered by parameters specified.                                              |
| [delete_user_call_log](#delete_user_call_log)               | Deletes filtered call log records.                                                                      |
| [read_user_call_record](#read_user_call_record)             | Returns call log records by ID.                                                                         |
| [sync_user_call_log](#sync_user_call_log)                   | Synchronizes the user call log records.                                                                 |
| [list_extension_active_calls](#list_extension_active_calls) | Returns records of all extension calls that are in progress, ordered by start time in descending order. |

## read_company_call_log

Returns call log records filtered by parameters specified.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-log`

**Parameters**

| Name                 | Type                                                          | Required | Description                                                                                                                                                                                                                                             |
| :------------------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| account_id           | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                            |
| extension_number     | str                                                           | ❌       | Short extension number of a user. If specified, returns call log for this particular extension only. Cannot be combined with `phoneNumber` filter                                                                                                       |
| phone_number         | str                                                           | ❌       | Phone number of a caller/callee in e.164 format without a '+' sign. If specified, all incoming/outgoing calls from/to this phone number are returned.                                                                                                   |
| direction            | [List[CallDirectionEnum]](../models/CallDirectionEnum.md)     | ❌       | The direction of call records to be included in the result. If omitted, both inbound and outbound calls are returned. Multiple values are supported                                                                                                     |
| type\_               | [List[CallTypeEnum]](../models/CallTypeEnum.md)               | ❌       | The type of call records to be included in the result. If omitted, all call types are returned. Multiple values are supported                                                                                                                           |
| view                 | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md) | ❌       | Defines the level of details for returned call records                                                                                                                                                                                                  |
| with_recording       | bool                                                          | ❌       | Deprecated, replaced with `recordingType` filter, still supported for compatibility reasons. Indicates if only recorded calls should be returned. If both `withRecording` and `recordingType` parameters are specified, then `withRecording` is ignored |
| recording_type       | [RecordingType](../models/RecordingType.md)                   | ❌       | Indicates that call records with recordings of particular type should be returned. If omitted, then calls with and without recordings are returned                                                                                                      |
| date_from            | str                                                           | ❌       | The beginning of the time range to return call records in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is `dateTo` minus 24 hours                                                                        |
| date_to              | str                                                           | ❌       | The end of the time range to return call records in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time                                                                                         |
| session_id           | str                                                           | ❌       | Internal identifier of a call session                                                                                                                                                                                                                   |
| telephony_session_id | str                                                           | ❌       | Internal identifier of a telephony session                                                                                                                                                                                                              |
| page                 | int                                                           | ❌       | Indicates the page number to retrieve. Only positive number values are accepted                                                                                                                                                                         |
| per_page             | int                                                           | ❌       | Indicates the page size (number of items)                                                                                                                                                                                                               |

**Return Type**

`CallLogResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReadCompanyCallLogView, RecordingType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
direction=[
    "Inbound"
]
type_=[
    "Voice"
]

result = sdk.call_log.read_company_call_log(
    account_id="~",
    extension_number="extensionNumber",
    phone_number="phoneNumber",
    direction=direction,
    type_=type_,
    view="Simple",
    recording_type="Automatic",
    date_from="dateFrom",
    date_to="dateTo",
    session_id="sessionId",
    telephony_session_id="telephonySessionId",
    page=1,
    per_page=100
)

print(result)
```

## read_company_call_record

Returns individual call log record(s) by ID. Batch syntax is supported.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-log/{callRecordId}`

**Parameters**

| Name           | Type                                                          | Required | Description                                                                                                                                                  |
| :------------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id     | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| call_record_id | List[str]                                                     | ✅       | Internal identifier of a call log record. Multiple values are supported                                                                                      |
| view           | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md) | ❌       | Defines the level of details for returned call records                                                                                                       |

**Return Type**

`CallLogRecord`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReadCompanyCallLogView

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
call_record_id=[
    "callRecordId"
]

result = sdk.call_log.read_company_call_record(
    account_id="~",
    call_record_id=call_record_id,
    view="Simple"
)

print(result)
```

## sync_account_call_log

Synchronizes company call log records.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-log-sync`

**Parameters**

| Name           | Type                                                                  | Required | Description                                                                                                                                                                                                                                                |
| :------------- | :-------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id     | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                               |
| sync_type      | [SyncAccountCallLogSyncType](../models/SyncAccountCallLogSyncType.md) | ❌       | Type of call log synchronization request                                                                                                                                                                                                                   |
| sync_token     | str                                                                   | ❌       | Value of syncToken property of last sync request response. Mandatory parameter for 'ISync' sync type                                                                                                                                                       |
| date_from      | str                                                                   | ❌       | The start datetime for resulting records in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is the current moment                                                                                              |
| record_count   | int                                                                   | ❌       | For `FSync` mode this parameter is mandatory, it limits the number of records to be returned in response. For `ISync` mode this parameter specifies the number of records to extend the sync frame with to the past (the maximum number of records is 250) |
| status_group   | [List[StatusGroup]](../models/StatusGroup.md)                         | ❌       | Type of calls to be returned                                                                                                                                                                                                                               |
| view           | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md)         | ❌       | Defines the level of details for returned call records                                                                                                                                                                                                     |
| show_deleted   | bool                                                                  | ❌       | Supported for `ISync` mode. Indicates that deleted call records should be returned                                                                                                                                                                         |
| with_recording | bool                                                                  | ❌       | Deprecated, replaced with `recordingType` filter, still supported for compatibility reasons. Indicates if only recorded calls should be returned. If both `withRecording` and `recordingType` parameters are specified, then `withRecording` is ignored    |
| recording_type | [RecordingType](../models/RecordingType.md)                           | ❌       | Indicates that call records with recordings of particular type should be returned. If omitted, then calls with and without recordings are returned                                                                                                         |

**Return Type**

`CallLogSyncResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SyncAccountCallLogSyncType, ReadCompanyCallLogView, RecordingType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
status_group=[
    "Missed"
]

result = sdk.call_log.sync_account_call_log(
    account_id="~",
    sync_type="FSync",
    sync_token="syncToken",
    date_from="dateFrom",
    record_count=9,
    status_group=status_group,
    view="Simple",
    show_deleted=False,
    recording_type="Automatic"
)

print(result)
```

## list_company_active_calls

Returns records of all calls that are in progress, ordered by start time in descending order.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/active-calls`

**Parameters**

| Name            | Type                                                          | Required | Description                                                                                                                                                  |
| :-------------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| direction       | [List[CallDirectionEnum]](../models/CallDirectionEnum.md)     | ❌       | The direction of call records to be included in the result. If omitted, both inbound and outbound calls are returned. Multiple values are supported          |
| view            | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md) | ❌       | Defines the level of details for returned call records                                                                                                       |
| type\_          | [List[CallTypeEnum]](../models/CallTypeEnum.md)               | ❌       | The type of call records to be included in the result. If omitted, all call types are returned. Multiple values are supported                                |
| transport       | [List[CallTransportEnum]](../models/CallTransportEnum.md)     | ❌       | The type of call transport. Multiple values are supported. By default, this filter is disabled                                                               |
| conference_type | [List[ConferenceType]](../models/ConferenceType.md)           | ❌       | Conference call type: RCC or RC Meetings. If not specified, no conference call filter applied                                                                |
| page            | int                                                           | ❌       | Indicates the page number to retrieve. Only positive number values are accepted                                                                              |
| per_page        | int                                                           | ❌       | Indicates the page size (number of items)                                                                                                                    |

**Return Type**

`CallLogResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReadCompanyCallLogView

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
direction=[
    "Inbound"
]
type_=[
    "Voice"
]
transport=[
    "PSTN"
]
conference_type=[
    "AudioConferencing"
]

result = sdk.call_log.list_company_active_calls(
    account_id="~",
    direction=direction,
    view="Simple",
    type_=type_,
    transport=transport,
    conference_type=conference_type,
    page=1,
    per_page=100
)

print(result)
```

## read_user_call_log

Returns call log records filtered by parameters specified.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log`

**Parameters**

| Name                 | Type                                                          | Required | Description                                                                                                                                                                                                                                             |
| :------------------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| account_id           | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                            |
| extension_id         | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                                                                                   |
| extension_number     | str                                                           | ❌       | Short extension number of a user. If specified, returns call log for this particular extension only. Cannot be combined with `phoneNumber` filter                                                                                                       |
| phone_number         | str                                                           | ❌       | Phone number of a caller/callee in e.164 format without a '+' sign. If specified, all incoming/outgoing calls from/to this phone number are returned.                                                                                                   |
| show_blocked         | bool                                                          | ❌       | Indicates then calls from/to blocked numbers are returned                                                                                                                                                                                               |
| direction            | [List[CallDirectionEnum]](../models/CallDirectionEnum.md)     | ❌       | The direction of call records to be included in the result. If omitted, both inbound and outbound calls are returned. Multiple values are supported                                                                                                     |
| session_id           | str                                                           | ❌       | Internal identifier of a call session                                                                                                                                                                                                                   |
| type\_               | [List[CallTypeEnum]](../models/CallTypeEnum.md)               | ❌       | The type of call records to be included in the result. If omitted, all call types are returned. Multiple values are supported                                                                                                                           |
| transport            | [List[CallTransportEnum]](../models/CallTransportEnum.md)     | ❌       | The type of call transport. Multiple values are supported. By default, this filter is disabled                                                                                                                                                          |
| view                 | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md) | ❌       | Defines the level of details for returned call records                                                                                                                                                                                                  |
| with_recording       | bool                                                          | ❌       | Deprecated, replaced with `recordingType` filter, still supported for compatibility reasons. Indicates if only recorded calls should be returned. If both `withRecording` and `recordingType` parameters are specified, then `withRecording` is ignored |
| recording_type       | [RecordingType](../models/RecordingType.md)                   | ❌       | Indicates that call records with recordings of particular type should be returned. If omitted, then calls with and without recordings are returned                                                                                                      |
| date_to              | str                                                           | ❌       | The end of the time range to return call records in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time                                                                                         |
| date_from            | str                                                           | ❌       | The beginning of the time range to return call records in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is `dateTo` minus 24 hours                                                                        |
| telephony_session_id | str                                                           | ❌       | Internal identifier of a telephony session                                                                                                                                                                                                              |
| page                 | int                                                           | ❌       | Indicates the page number to retrieve. Only positive number values are allowed                                                                                                                                                                          |
| per_page             | int                                                           | ❌       | Indicates the page size (number of items). The default value is 100. The maximum value for `Simple` view is 1000, for `Detailed` view - 250                                                                                                             |
| show_deleted         | bool                                                          | ❌       | Indicates that deleted calls records should be returned                                                                                                                                                                                                 |

**Return Type**

`CallLogResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReadCompanyCallLogView, RecordingType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
direction=[
    "Inbound"
]
type_=[
    "Voice"
]
transport=[
    "PSTN"
]

result = sdk.call_log.read_user_call_log(
    account_id="~",
    extension_id="~",
    extension_number="extensionNumber",
    phone_number="phoneNumber",
    show_blocked=True,
    direction=direction,
    session_id="sessionId",
    type_=type_,
    transport=transport,
    view="Simple",
    recording_type="Automatic",
    date_to="dateTo",
    date_from="dateFrom",
    telephony_session_id="telephonySessionId",
    page=1,
    per_page=100,
    show_deleted=False
)

print(result)
```

## delete_user_call_log

Deletes filtered call log records.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| date_to      | str  | ❌       | The time boundary to delete all older records in ISO 8601 format including timezone, for example _2016-03-10T18:07:52.534Z_. The default value is current time        |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_log.delete_user_call_log(
    account_id="~",
    extension_id="~",
    date_to="dateTo"
)

print(result)
```

## read_user_call_record

Returns call log records by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log/{callRecordId}`

**Parameters**

| Name           | Type                                                          | Required | Description                                                                                                                                                           |
| :------------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id     | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id   | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| call_record_id | List[str]                                                     | ✅       | Internal identifier of a call log record. Multiple values are supported                                                                                               |
| view           | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md) | ❌       | Defines the level of details for returned call records                                                                                                                |

**Return Type**

`CallLogRecord`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReadCompanyCallLogView

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
call_record_id=[
    "callRecordId"
]

result = sdk.call_log.read_user_call_record(
    account_id="~",
    extension_id="~",
    call_record_id=call_record_id,
    view="Simple"
)

print(result)
```

## sync_user_call_log

Synchronizes the user call log records.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/call-log-sync`

**Parameters**

| Name           | Type                                                                  | Required | Description                                                                                                                                                                                                                                                |
| :------------- | :-------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id     | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                               |
| extension_id   | str                                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                                                                                      |
| sync_type      | [SyncAccountCallLogSyncType](../models/SyncAccountCallLogSyncType.md) | ❌       | Type of call log synchronization request                                                                                                                                                                                                                   |
| sync_token     | str                                                                   | ❌       | A `syncToken` value from the previous sync response (for `ISync` mode only, mandatory)                                                                                                                                                                     |
| date_from      | str                                                                   | ❌       | The start datetime for resulting records in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is the current moment                                                                                              |
| record_count   | int                                                                   | ❌       | For `FSync` mode this parameter is mandatory, it limits the number of records to be returned in response. For `ISync` mode this parameter specifies the number of records to extend the sync frame with to the past (the maximum number of records is 250) |
| status_group   | [List[StatusGroup]](../models/StatusGroup.md)                         | ❌       | Type of calls to be returned                                                                                                                                                                                                                               |
| view           | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md)         | ❌       | Defines the level of details for returned call records                                                                                                                                                                                                     |
| show_deleted   | bool                                                                  | ❌       | Supported for `ISync` mode. Indicates that deleted call records should be returned                                                                                                                                                                         |
| with_recording | bool                                                                  | ❌       | Deprecated, replaced with `recordingType` filter, still supported for compatibility reasons. Indicates if only recorded calls should be returned. If both `withRecording` and `recordingType` parameters are specified, then `withRecording` is ignored    |
| recording_type | [RecordingType](../models/RecordingType.md)                           | ❌       | Indicates that call records with recordings of particular type should be returned. If omitted, then calls with and without recordings are returned                                                                                                         |

**Return Type**

`CallLogSyncResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SyncAccountCallLogSyncType, ReadCompanyCallLogView, RecordingType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
status_group=[
    "Missed"
]

result = sdk.call_log.sync_user_call_log(
    account_id="~",
    extension_id="~",
    sync_type="FSync",
    sync_token="syncToken",
    date_from="dateFrom",
    record_count=6,
    status_group=status_group,
    view="Simple",
    show_deleted=False,
    recording_type="Automatic"
)

print(result)
```

## list_extension_active_calls

Returns records of all extension calls that are in progress, ordered by start time in descending order.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/active-calls`

**Parameters**

| Name            | Type                                                          | Required | Description                                                                                                                                                           |
| :-------------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id    | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| direction       | [List[CallDirectionEnum]](../models/CallDirectionEnum.md)     | ❌       | The direction of call records to be included in the result. If omitted, both inbound and outbound calls are returned. Multiple values are supported                   |
| view            | [ReadCompanyCallLogView](../models/ReadCompanyCallLogView.md) | ❌       | Defines the level of details for returned call records                                                                                                                |
| type\_          | [List[CallTypeEnum]](../models/CallTypeEnum.md)               | ❌       | The type of call records to be included in the result. If omitted, all call types are returned. Multiple values are supported                                         |
| transport       | [List[CallTransportEnum]](../models/CallTransportEnum.md)     | ❌       | The type of call transport. Multiple values are supported. By default, this filter is disabled                                                                        |
| conference_type | [List[ConferenceType]](../models/ConferenceType.md)           | ❌       | Conference call type: RCC or RC Meetings. If not specified, no conference call filter applied                                                                         |
| page            | int                                                           | ❌       | Indicates the page number to retrieve. Only positive number values are allowed                                                                                        |
| per_page        | int                                                           | ❌       | Indicates the page size (number of items)                                                                                                                             |

**Return Type**

`CallLogResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReadCompanyCallLogView

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
direction=[
    "Inbound"
]
type_=[
    "Voice"
]
transport=[
    "PSTN"
]
conference_type=[
    "AudioConferencing"
]

result = sdk.call_log.list_extension_active_calls(
    account_id="~",
    extension_id="~",
    direction=direction,
    view="Simple",
    type_=type_,
    transport=transport,
    conference_type=conference_type,
    page=1,
    per_page=100
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
