# HistoricalRecordingsService

A list of all methods in the `HistoricalRecordingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rcw_history_admin_list_recordings](#rcw_history_admin_list_recordings)   | Returns the list of webinar recordings (Administrator's interface). The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403.                                                                                                                                                                              |
| [rcw_history_admin_get_recording](#rcw_history_admin_get_recording)       | Returns the webinar recording by ID (Administrator's interface). The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403.                                                                                                                                                                                 |
| [rcw_history_list_recordings](#rcw_history_list_recordings)               | Returns the list of webinar recordings for a given webinar host user                                                                                                                                                                                                                                                                         |
| [rcw_history_get_recording](#rcw_history_get_recording)                   | Returns the webinar recording by ID (Webinar host's interface). This API also returns sharing link if sharing is enabled.                                                                                                                                                                                                                    |
| [rcw_history_get_recording_download](#rcw_history_get_recording_download) | Returns the webinar recording download link (both Webinar host's and admin interface). If called by a webinar host, the API returns error (403) if recording downloading is prohibited by company settings. The admin user who has "WebinarSettings" permission should be able to download recording regardless of current company settings. |

## rcw_history_admin_list_recordings

Returns the list of webinar recordings (Administrator's interface). The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/company/recordings`

**Parameters**

| Name               | Type                                                            | Required | Description                                                                                                             |
| :----------------- | :-------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| creation_time_from | str                                                             | ✅       | The beginning of the time window by 'creationTime' .                                                                    |
| creation_time_to   | str                                                             | ✅       | The end of the time window by 'creationTime' .                                                                          |
| name_fragment      | str                                                             | ❌       | Filter to return only webinar recordings containing particular substring within their names                             |
| status             | [List[RecordingStatusModel]](../models/RecordingStatusModel.md) | ❌       | The status of the recording.                                                                                            |
| host_user_id       | List[str]                                                       | ❌       | Identifier of the user who hosts a webinar (if omitted, webinars hosted by all company users will be returned)          |
| per_page           | int                                                             | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token         | str                                                             | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`RecordingAdminListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
status=[
    "Processing"
]
host_user_id=[
    "laborum nostrud "
]

result = sdk.historical_recordings.rcw_history_admin_list_recordings(
    creation_time_from="creationTimeFrom",
    creation_time_to="creationTimeTo",
    name_fragment="nameFragment",
    status=status,
    host_user_id=host_user_id,
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_history_admin_get_recording

Returns the webinar recording by ID (Administrator's interface). The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/company/recordings/{recordingId}`

**Parameters**

| Name         | Type | Required | Description                          |
| :----------- | :--- | :------- | :----------------------------------- |
| recording_id | str  | ✅       | Identifier of the Webinar recording. |

**Return Type**

`RecordingAdminExtendedItemModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.historical_recordings.rcw_history_admin_get_recording(recording_id="recordingId")

print(result)
```

## rcw_history_list_recordings

Returns the list of webinar recordings for a given webinar host user

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/recordings`

**Parameters**

| Name               | Type                                                            | Required | Description                                                                                                             |
| :----------------- | :-------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| creation_time_from | str                                                             | ✅       | The beginning of the time window by 'creationTime' .                                                                    |
| creation_time_to   | str                                                             | ✅       | The end of the time window by 'creationTime' .                                                                          |
| status             | [List[RecordingStatusModel]](../models/RecordingStatusModel.md) | ❌       | The status of the recording.                                                                                            |
| per_page           | int                                                             | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token         | str                                                             | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`RecordingListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
status=[
    "Processing"
]

result = sdk.historical_recordings.rcw_history_list_recordings(
    creation_time_from="creationTimeFrom",
    creation_time_to="creationTimeTo",
    status=status,
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_history_get_recording

Returns the webinar recording by ID (Webinar host's interface). This API also returns sharing link if sharing is enabled.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/recordings/{recordingId}`

**Parameters**

| Name         | Type | Required | Description                          |
| :----------- | :--- | :------- | :----------------------------------- |
| recording_id | str  | ✅       | Identifier of the Webinar recording. |

**Return Type**

`RecordingItemExtendedModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.historical_recordings.rcw_history_get_recording(recording_id="recordingId")

print(result)
```

## rcw_history_get_recording_download

Returns the webinar recording download link (both Webinar host's and admin interface). If called by a webinar host, the API returns error (403) if recording downloading is prohibited by company settings. The admin user who has "WebinarSettings" permission should be able to download recording regardless of current company settings.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/recordings/{recordingId}/download`

**Parameters**

| Name                 | Type                                                  | Required | Description                                                                                                                                                                                                                                         |
| :------------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| recording_id         | str                                                   | ✅       | Identifier of the Webinar recording.                                                                                                                                                                                                                |
| recording_media_type | [RecordingMediaType](../models/RecordingMediaType.md) | ❌       | Download file media type. - Type 'Video' refers to a multiplexed audio and video file. - Type 'Audio' refers to an audio only file. - Unless specified by this query parameter, a video file is returned by default when a recording is downloaded. |

**Return Type**

`RecordingDownloadModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import RecordingMediaType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.historical_recordings.rcw_history_get_recording_download(
    recording_id="recordingId",
    recording_media_type="Video"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
