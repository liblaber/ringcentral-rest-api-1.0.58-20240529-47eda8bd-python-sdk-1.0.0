# CalendarEventsService

A list of all methods in the `CalendarEventsService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                            |
| :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_glip_events_new](#read_glip_events_new)                 | Returns all calendar events created by the current user.                                                                                               |
| [create_event_new](#create_event_new)                         | Creates a new calendar event.                                                                                                                          |
| [read_event_new](#read_event_new)                             | Returns the specified calendar event(s) by ID(s).                                                                                                      |
| [update_event_new](#update_event_new)                         | Updates the specified calendar event.                                                                                                                  |
| [delete_event_new](#delete_event_new)                         | Deletes the specified calendar event.                                                                                                                  |
| [list_group_events_new](#list_group_events_new)               | Returns a list of calendar events available for the current user within the specified group. Users can only see their personal tasks and public tasks. |
| [create_event_by_group_id_new](#create_event_by_group_id_new) | Creates a new calendar event within the specified group.                                                                                               |

## read_glip_events_new

Returns all calendar events created by the current user.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/events`

**Parameters**

| Name         | Type | Required | Description                                                                               |
| :----------- | :--- | :------- | :---------------------------------------------------------------------------------------- |
| record_count | int  | ❌       | Number of groups to be fetched by one request. The maximum value is 250, by default - 30. |
| page_token   | str  | ❌       | Token of a page to be returned                                                            |

**Return Type**

`TmEventList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.calendar_events.read_glip_events_new(
    record_count=30,
    page_token="pageToken"
)

print(result)
```

## create_event_new

Creates a new calendar event.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/events`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [TmCreateEventRequest](../models/TmCreateEventRequest.md) | ✅       | The request body. |

**Return Type**

`TmEventInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreateEventRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreateEventRequest(
    id_="id",
    creator_id="creatorId",
    title="title",
    start_time="startTime",
    end_time="endTime",
    all_day=True,
    recurrence={
        "schedule": "None",
        "ending_condition": "None",
        "ending_after": 6,
        "ending_on": "endingOn"
    },
    color="Black",
    location="location",
    description="description"
)

result = sdk.calendar_events.create_event_new(request_body=request_body)

print(result)
```

## read_event_new

Returns the specified calendar event(s) by ID(s).

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/events/{eventId}`

**Parameters**

| Name     | Type      | Required | Description                                    |
| :------- | :-------- | :------- | :--------------------------------------------- |
| event_id | List[str] | ✅       | Event id or comma separated list of event ids. |

**Return Type**

`TmEventInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
event_id=[
    "eventId"
]

result = sdk.calendar_events.read_event_new(event_id=event_id)

print(result)
```

## update_event_new

Updates the specified calendar event.

- HTTP Method: `PUT`
- Endpoint: `/team-messaging/v1/events/{eventId}`

**Parameters**

| Name         | Type                                                      | Required | Description                     |
| :----------- | :-------------------------------------------------------- | :------- | :------------------------------ |
| request_body | [TmCreateEventRequest](../models/TmCreateEventRequest.md) | ✅       | The request body.               |
| event_id     | str                                                       | ✅       | Internal identifier of an event |

**Return Type**

`TmEventInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreateEventRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreateEventRequest(
    id_="id",
    creator_id="creatorId",
    title="title",
    start_time="startTime",
    end_time="endTime",
    all_day=True,
    recurrence={
        "schedule": "None",
        "ending_condition": "None",
        "ending_after": 6,
        "ending_on": "endingOn"
    },
    color="Black",
    location="location",
    description="description"
)

result = sdk.calendar_events.update_event_new(
    request_body=request_body,
    event_id="eventId"
)

print(result)
```

## delete_event_new

Deletes the specified calendar event.

- HTTP Method: `DELETE`
- Endpoint: `/team-messaging/v1/events/{eventId}`

**Parameters**

| Name     | Type | Required | Description                                   |
| :------- | :--- | :------- | :-------------------------------------------- |
| event_id | str  | ✅       | Internal identifier of an event to be deleted |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.calendar_events.delete_event_new(event_id="eventId")

print(result)
```

## list_group_events_new

Returns a list of calendar events available for the current user within the specified group. Users can only see their personal tasks and public tasks.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/groups/{groupId}/events`

**Parameters**

| Name     | Type | Required | Description                    |
| :------- | :--- | :------- | :----------------------------- |
| group_id | str  | ✅       | Internal identifier of a group |

**Return Type**

`TmEventInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.calendar_events.list_group_events_new(group_id="groupId")

print(result)
```

## create_event_by_group_id_new

Creates a new calendar event within the specified group.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/groups/{groupId}/events`

**Parameters**

| Name         | Type                                                      | Required | Description                    |
| :----------- | :-------------------------------------------------------- | :------- | :----------------------------- |
| request_body | [TmCreateEventRequest](../models/TmCreateEventRequest.md) | ✅       | The request body.              |
| group_id     | str                                                       | ✅       | Internal identifier of a group |

**Return Type**

`TmEventInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreateEventRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreateEventRequest(
    id_="id",
    creator_id="creatorId",
    title="title",
    start_time="startTime",
    end_time="endTime",
    all_day=True,
    recurrence={
        "schedule": "None",
        "ending_condition": "None",
        "ending_after": 6,
        "ending_on": "endingOn"
    },
    color="Black",
    location="location",
    description="description"
)

result = sdk.calendar_events.create_event_by_group_id_new(
    request_body=request_body,
    group_id="groupId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
