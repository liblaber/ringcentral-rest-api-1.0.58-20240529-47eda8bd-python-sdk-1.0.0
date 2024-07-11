# CallRecordingsService

A list of all methods in the `CallRecordingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                                                       |
| :---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_call_recording_content](#read_call_recording_content)       | Returns media content of a call recording (`audio/mpeg` or `audio/wav`) **This API must be called via media API entry point, e.g. https://media.ringcentral.com** |
| [delete_company_call_recordings](#delete_company_call_recordings) | Deletes company call recordings by their IDs. _Please note:_ This method deletes the recording file itself, not the record of it in the call log.                 |
| [read_call_recording](#read_call_recording)                       | Returns call recordings by ID(s).                                                                                                                                 |

## read_call_recording_content

Returns media content of a call recording (`audio/mpeg` or `audio/wav`) **This API must be called via media API entry point, e.g. https://media.ringcentral.com**

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/recording/{recordingId}/content`

**Parameters**

| Name                         | Type                                                  | Required | Description                                                                                                                                                  |
| :--------------------------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id                   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| recording_id                 | str                                                   | ✅       | Internal identifier of a call recording (returned in Call Log)                                                                                               |
| content_disposition          | [ContentDisposition](../models/ContentDisposition.md) | ❌       | Whether the content is expected to be displayed in the browser, or downloaded and saved locally                                                              |
| content_disposition_filename | str                                                   | ❌       | The default filename of the file to be downloaded                                                                                                            |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ContentDisposition

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_recordings.read_call_recording_content(
    account_id="~",
    recording_id="625387632786",
    content_disposition="Inline",
    content_disposition_filename="contentDispositionFilename"
)

print(result)
```

## delete_company_call_recordings

Deletes company call recordings by their IDs. _Please note:_ This method deletes the recording file itself, not the record of it in the call log.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/call-recordings`

**Parameters**

| Name         | Type                                              | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CallRecordingIds](../models/CallRecordingIds.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CallRecordingIds

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CallRecordingIds(
    records=[
        "records"
    ]
)

result = sdk.call_recordings.delete_company_call_recordings(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_call_recording

Returns call recordings by ID(s).

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/recording/{recordingId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                  |
| :----------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| recording_id | str  | ✅       | Internal identifier of a call recording (returned in Call Log)                                                                                               |

**Return Type**

`GetCallRecordingResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_recordings.read_call_recording(
    account_id="~",
    recording_id="625387632786"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
