# HistoricalWebinarsService

A list of all methods in the `HistoricalWebinarsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rcw_history_get_webinar](#rcw_history_get_webinar)                             | Returns a historical webinar information by ID (host interface)                                                                                                                                                                                                                                                                         |
| [rcw_history_get_session](#rcw_history_get_session)                             | Returns a historical webinar Session by ID. Access allowed to participants with original role as Host or CoHost.                                                                                                                                                                                                                        |
| [rcw_history_list_participants](#rcw_history_list_participants)                 | Returns the list of participants of a given Webinar Session (host interface).                                                                                                                                                                                                                                                           |
| [rcw_history_get_participant_info](#rcw_history_get_participant_info)           | Returns the participant information specific to a webinar session. Accessible by any authenticated participant. For a non-authenticated participant, API returns error.                                                                                                                                                                 |
| [rcw_history_list_invitees](#rcw_history_list_invitees)                         | Returns the list of Invitees (co-hosts and panelists) of a given Webinar Session (host interface). An implicit record created for a Webinar 'Host' is always returned.                                                                                                                                                                  |
| [rcw_history_get_invitee](#rcw_history_get_invitee)                             | Returns a historical session invitee information by ID (host interface).                                                                                                                                                                                                                                                                |
| [rcw_history_list_all_company_sessions](#rcw_history_list_all_company_sessions) | Returns the list of historical Webinar Sessions hosted by particular user(s) or all company users sorted by 'endTime' in the descending order. Depending on a session status 'endTime' can represent actual end time or scheduled end time. The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403. |
| [rcw_history_list_all_sessions](#rcw_history_list_all_sessions)                 | Returns the list of historical Webinar Sessions hosted by a current authorized user sorted by 'endTime' in the descending order. Depending on a session status 'endTime' can represent actual end time or scheduled end time.                                                                                                           |

## rcw_history_get_webinar

Returns a historical webinar information by ID (host interface)

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/webinars/{webinarId}`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar. |

**Return Type**

`WebinarResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.historical_webinars.rcw_history_get_webinar(webinar_id="consequat")

print(result)
```

## rcw_history_get_session

Returns a historical webinar Session by ID. Access allowed to participants with original role as Host or CoHost.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/webinars/{webinarId}/sessions/{sessionId}`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar. |
| session_id | str  | ✅       | Identifier of the Session. |

**Return Type**

`SessionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.historical_webinars.rcw_history_get_session(
    webinar_id="eu ",
    session_id="consectetur "
)

print(result)
```

## rcw_history_list_participants

Returns the list of participants of a given Webinar Session (host interface).

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/webinars/{webinarId}/sessions/{sessionId}/participants`

**Parameters**

| Name          | Type                                          | Required | Description                                                                                                             |
| :------------ | :-------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| webinar_id    | str                                           | ✅       | Identifier of the Webinar.                                                                                              |
| session_id    | str                                           | ✅       | Identifier of the Session.                                                                                              |
| role          | [List[RcwRoleEnum]](../models/RcwRoleEnum.md) | ❌       | The role of the invitee/participant.                                                                                    |
| original_role | [List[RcwRoleEnum]](../models/RcwRoleEnum.md) | ❌       | The original role of the invitee/participant.                                                                           |
| per_page      | int                                           | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token    | str                                           | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`ParticipantListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
role=[
    "Panelist"
]
original_role=[
    "Panelist"
]

result = sdk.historical_webinars.rcw_history_list_participants(
    webinar_id="consectetur aute d",
    session_id="qui magna ",
    role=role,
    original_role=original_role,
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_history_get_participant_info

Returns the participant information specific to a webinar session. Accessible by any authenticated participant. For a non-authenticated participant, API returns error.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/webinars/{webinarId}/sessions/{sessionId}/participants/self`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar. |
| session_id | str  | ✅       | Identifier of the Session. |

**Return Type**

`ParticipantReducedModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.historical_webinars.rcw_history_get_participant_info(
    webinar_id="laboris occaecat ",
    session_id="culpa"
)

print(result)
```

## rcw_history_list_invitees

Returns the list of Invitees (co-hosts and panelists) of a given Webinar Session (host interface). An implicit record created for a Webinar 'Host' is always returned.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/webinars/{webinarId}/sessions/{sessionId}/invitees`

**Parameters**

| Name          | Type                                          | Required | Description                                                                                                             |
| :------------ | :-------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| webinar_id    | str                                           | ✅       | Identifier of the Webinar.                                                                                              |
| session_id    | str                                           | ✅       | Identifier of the Session.                                                                                              |
| role          | [List[RcwRoleEnum]](../models/RcwRoleEnum.md) | ❌       | The role of the invitee/participant.                                                                                    |
| original_role | [List[RcwRoleEnum]](../models/RcwRoleEnum.md) | ❌       | The original role of the invitee/participant.                                                                           |
| per_page      | int                                           | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token    | str                                           | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`InviteeListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
role=[
    "Panelist"
]
original_role=[
    "Panelist"
]

result = sdk.historical_webinars.rcw_history_list_invitees(
    webinar_id="irure",
    session_id="Duis",
    role=role,
    original_role=original_role,
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_history_get_invitee

Returns a historical session invitee information by ID (host interface).

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/webinars/{webinarId}/sessions/{sessionId}/invitees/{inviteeId}`

**Parameters**

| Name       | Type | Required | Description                        |
| :--------- | :--- | :------- | :--------------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar.         |
| session_id | str  | ✅       | Identifier of the Session.         |
| invitee_id | str  | ✅       | Identifier of the Session Invitee. |

**Return Type**

`InviteeModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.historical_webinars.rcw_history_get_invitee(
    webinar_id="commodo",
    session_id="dolore",
    invitee_id="culpa Ut"
)

print(result)
```

## rcw_history_list_all_company_sessions

Returns the list of historical Webinar Sessions hosted by particular user(s) or all company users sorted by 'endTime' in the descending order. Depending on a session status 'endTime' can represent actual end time or scheduled end time. The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/company/sessions`

**Parameters**

| Name          | Type                                                              | Required | Description                                                                                                             |
| :------------ | :---------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| end_time_from | str                                                               | ✅       | The beginning of the time window by 'endTime' .                                                                         |
| end_time_to   | str                                                               | ✅       | The end of the time window by 'endTime' .                                                                               |
| host_user_id  | List[str]                                                         | ❌       | Identifier of the user who hosts a webinar (if omitted, webinars hosted by all company users will be returned)          |
| status        | [List[RcwSessionStatusModel]](../models/RcwSessionStatusModel.md) | ❌       | Filter to return only webinar sessions in certain status. Multiple values are supported.                                |
| per_page      | int                                                               | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token    | str                                                               | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`SessionGlobalListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
host_user_id=[
    "eu consequa"
]
status=[
    "Scheduled"
]

result = sdk.historical_webinars.rcw_history_list_all_company_sessions(
    end_time_from="endTimeFrom",
    end_time_to="endTimeTo",
    host_user_id=host_user_id,
    status=status,
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_history_list_all_sessions

Returns the list of historical Webinar Sessions hosted by a current authorized user sorted by 'endTime' in the descending order. Depending on a session status 'endTime' can represent actual end time or scheduled end time.

- HTTP Method: `GET`
- Endpoint: `/webinar/history/v1/sessions`

**Parameters**

| Name          | Type                                                              | Required | Description                                                                                                             |
| :------------ | :---------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| end_time_from | str                                                               | ✅       | The beginning of the time window by 'endTime' .                                                                         |
| end_time_to   | str                                                               | ✅       | The end of the time window by 'endTime' .                                                                               |
| name_fragment | str                                                               | ❌       | Filter to return only webinar sessions containing particular substring within their names                               |
| status        | [List[RcwSessionStatusModel]](../models/RcwSessionStatusModel.md) | ❌       | Filter to return only webinar sessions in certain status. Multiple values are supported.                                |
| per_page      | int                                                               | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token    | str                                                               | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`SessionGlobalListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
status=[
    "Scheduled"
]

result = sdk.historical_webinars.rcw_history_list_all_sessions(
    end_time_from="endTimeFrom",
    end_time_to="endTimeTo",
    name_fragment="nameFragment",
    status=status,
    per_page=100,
    page_token="pageToken"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
