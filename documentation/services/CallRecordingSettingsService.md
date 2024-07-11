# CallRecordingSettingsService

A list of all methods in the `CallRecordingSettingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                   | Description                                               |
| :---------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| [read_call_recording_settings](#read_call_recording_settings)                             | Returns call recording settings.                          |
| [update_call_recording_settings](#update_call_recording_settings)                         | Updates current call recording settings.                  |
| [list_call_recording_custom_greetings](#list_call_recording_custom_greetings)             | Returns call recording custom greetings.                  |
| [delete_call_recording_custom_greeting_list](#delete_call_recording_custom_greeting_list) | Deletes call recording custom greetings.                  |
| [delete_call_recording_custom_greeting](#delete_call_recording_custom_greeting)           | Deletes call recording custom greeting(s).                |
| [update_call_recording_extension_list](#update_call_recording_extension_list)             | Creates or updates the list of extensions to be recorded. |
| [list_call_recording_extensions](#list_call_recording_extensions)                         | Returns the list of extensions to be recorded.            |

## read_call_recording_settings

Returns call recording settings.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recording`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CallRecordingSettingsResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_recording_settings.read_call_recording_settings(account_id="~")

print(result)
```

## update_call_recording_settings

Updates current call recording settings.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recording`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CallRecordingSettingsResource](../models/CallRecordingSettingsResource.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CallRecordingSettingsResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallRecordingSettingsResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallRecordingSettingsResource(
    on_demand={
        "enabled": True,
        "retention_period": 10
    },
    automatic={
        "enabled": False,
        "outbound_call_tones": True,
        "outbound_call_announcement": True,
        "allow_mute": False,
        "extension_count": 5,
        "retention_period": 5,
        "max_number_limit": 4
    },
    greetings=[
        {
            "type_": "StartRecording",
            "mode": "Default"
        }
    ]
)

result = sdk.call_recording_settings.update_call_recording_settings(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_call_recording_custom_greetings

Returns call recording custom greetings.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recording/custom-greetings`

**Parameters**

| Name       | Type                                                                                      | Required | Description                                                                                                                                                  |
| :--------- | :---------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str                                                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| type\_     | [ListCallRecordingCustomGreetingsType](../models/ListCallRecordingCustomGreetingsType.md) | ❌       |                                                                                                                                                              |

**Return Type**

`CallRecordingCustomGreetings`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListCallRecordingCustomGreetingsType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_recording_settings.list_call_recording_custom_greetings(
    account_id="~",
    type_="StartRecording"
)

print(result)
```

## delete_call_recording_custom_greeting_list

Deletes call recording custom greetings.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recording/custom-greetings`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_recording_settings.delete_call_recording_custom_greeting_list(account_id="~")

print(result)
```

## delete_call_recording_custom_greeting

Deletes call recording custom greeting(s).

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recording/custom-greetings/{greetingId}`

**Parameters**

| Name        | Type | Required | Description                                                                                                                                                  |
| :---------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id  | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| greeting_id | str  | ✅       | Internal identifier of a greeting                                                                                                                            |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_recording_settings.delete_call_recording_custom_greeting(
    account_id="~",
    greeting_id="greetingId"
)

print(result)
```

## update_call_recording_extension_list

Creates or updates the list of extensions to be recorded.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recording/bulk-assign`

**Parameters**

| Name         | Type                                                                                | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [BulkAccountCallRecordingsResource](../models/BulkAccountCallRecordingsResource.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BulkAccountCallRecordingsResource

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BulkAccountCallRecordingsResource(
    added_extensions=[
        {
            "id_": "id",
            "uri": "uri",
            "extension_number": "extensionNumber",
            "type_": "type",
            "call_direction": "Outbound"
        }
    ],
    updated_extensions=[
        {
            "id_": "id",
            "uri": "uri",
            "extension_number": "extensionNumber",
            "type_": "type",
            "call_direction": "Outbound"
        }
    ],
    removed_extensions=[
        {
            "id_": "id",
            "uri": "uri",
            "extension_number": "extensionNumber",
            "type_": "type",
            "call_direction": "Outbound"
        }
    ]
)

result = sdk.call_recording_settings.update_call_recording_extension_list(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_call_recording_extensions

Returns the list of extensions to be recorded.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recording/extensions`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CallRecordingExtensions`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_recording_settings.list_call_recording_extensions(account_id="~")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
