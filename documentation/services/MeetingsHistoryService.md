# MeetingsHistoryService

A list of all methods in the `MeetingsHistoryService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                        |
| :------------------------------------------ | :--------------------------------- |
| [list_video_meetings](#list_video_meetings) | Returns the list of user meetings. |
| [get_video_meeting](#get_video_meeting)     | Returns a user meeting by ID.      |

## list_video_meetings

Returns the list of user meetings.

- HTTP Method: `GET`
- Endpoint: `/rcvideo/v1/history/meetings`

**Parameters**

| Name       | Type                                                        | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :--------- | :---------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| text       | str                                                         | ❌       | Search text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| page_token | str                                                         | ❌       | Token to get the next page                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| per_page   | int                                                         | ❌       | Number of records returned                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| type\_     | [ListVideoMeetingsType](../models/ListVideoMeetingsType.md) | ❌       | Specify what kind of meeting should be returned. Possible values: All, My, Deleted, Shared Request type meaning in meeting search: `None` (not passed) - take meetings only where requested acc/ext is participant OR host OR deputy OR watcher. `ALL`- access rights of meeting is equal to Alive AND requested acc/ext is in watchers list OR host OR deputy `My`- access rights of meeting is equal to Alive AND requested acc/ext is host OR deputy `Shared` - access rights of meeting is equal to Alive AND requested acc/ext is in watcher list AND not HOST `Deleted` - access rights of meeting is equal to Delete and requested acc/ext is host OR deputy |
| start_time | int                                                         | ❌       | Unix timestamp in milliseconds (inclusive) indicates the start time of meetings which should be included in response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| end_time   | int                                                         | ❌       | Unix timestamp in milliseconds (inclusive) indicates the end time of meetings which should be included in response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

**Return Type**

`MeetingPage`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListVideoMeetingsType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.meetings_history.list_video_meetings(
    text="text",
    page_token="pageToken",
    per_page=4,
    type_="All",
    start_time=7,
    end_time=1
)

print(result)
```

## get_video_meeting

Returns a user meeting by ID.

- HTTP Method: `GET`
- Endpoint: `/rcvideo/v1/history/meetings/{meetingId}`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| meeting_id | str  | ✅       | Meeting id  |

**Return Type**

`Meeting`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.meetings_history.get_video_meeting(meeting_id="meetingId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
