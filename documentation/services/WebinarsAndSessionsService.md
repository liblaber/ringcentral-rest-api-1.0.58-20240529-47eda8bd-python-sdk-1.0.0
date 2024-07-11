# WebinarsAndSessionsService

A list of all methods in the `WebinarsAndSessionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rcw_config_list_webinars](#rcw_config_list_webinars)                         | Returns the list of Webinars hosted by a current authorized user sorted by 'scheduledStartTime' or 'creationTime' in the ascending order.                                                                                                                                                                                                                                                                                                                                     |
| [rcw_config_create_webinar](#rcw_config_create_webinar)                       | Creates a new webinar. If "host" parameter is NOT passed then the current authorized user will become a Host. If "host" parameter is passed then the caller must be a company administrator and have "WebinarSettings" permission. "host.linkedUser.accountId" must be the same as authorized user's account ID. The webinar settings which are not mandated at account level or are unlocked can be specified. All other settings are defaulted according to account policy. |
| [rcw_config_get_webinar](#rcw_config_get_webinar)                             | Returns a Webinar information by ID. Some webinar settings are returned basing on webinar-level overrides, other - from default settings defined at account level.                                                                                                                                                                                                                                                                                                            |
| [rcw_config_update_webinar](#rcw_config_update_webinar)                       | Updates a Webinar. The payload may contain just changed fields of a Webinar resource (it is a partial update): - host cannot be changed, and host user information cannot be updated; - only the settings which are not mandated at account level or are unlocked can be changed; - in order to reset a webinar password it should be passed as an empty string; - "registrationStatus" cannot be changed.                                                                    |
| [rcw_config_delete_webinar](#rcw_config_delete_webinar)                       | Deletes a Webinar by ID. All child objects (Sessions, Invitees) will be also deleted. It is disallowed to delete a Webinar which has at least one Session in 'Active' or 'Finished' state.                                                                                                                                                                                                                                                                                    |
| [rcw_config_create_session](#rcw_config_create_session)                       | Creates a new Session for a given Webinar                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [rcw_config_get_session](#rcw_config_get_session)                             | Returns a Webinar Session by ID.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [rcw_config_update_session](#rcw_config_update_session)                       | Updates a Webinar Session. The payload may contain certain attributes from the Session resource (it is a partial update). Changing the 'status' field usually invokes certain workflow actions. Updating a Session in 'Active' or 'Finished' status is prohibited. Some status transitions (for example, to 'Active" or 'Finished') may be prohibited.                                                                                                                        |
| [rcw_config_delete_session](#rcw_config_delete_session)                       | Deletes a Webinar Session. All child objects (Invitees) will be also deleted. It is disallowed to delete a Session which is in 'Active' or 'Finished' state                                                                                                                                                                                                                                                                                                                   |
| [rcw_config_list_all_company_sessions](#rcw_config_list_all_company_sessions) | Returns the list of Webinar Sessions hosted by all company users or particular user(s) sorted by 'scheduledStartTime' or 'creationTime' (if 'scheduledStartTime' is not set) in the ascending ordered. The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403.                                                                                                                                                                            |
| [rcw_config_list_all_sessions](#rcw_config_list_all_sessions)                 | Returns the list of Webinar Sessions hosted by a current authorized user sorted by 'scheduledStartTime' or 'creationTime' (if 'scheduledStartTime' is not set) in the ascending order                                                                                                                                                                                                                                                                                         |

## rcw_config_list_webinars

Returns the list of Webinars hosted by a current authorized user sorted by 'scheduledStartTime' or 'creationTime' in the ascending order.

- HTTP Method: `GET`
- Endpoint: `/webinar/configuration/v1/webinars`

**Parameters**

| Name               | Type | Required | Description                                                                                                             |
| :----------------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| creation_time_from | str  | ✅       | The beginning of the time window by 'creationTime' .                                                                    |
| per_page           | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token         | str  | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`WebinarListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webinars_and_sessions.rcw_config_list_webinars(
    creation_time_from="creationTimeFrom",
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_config_create_webinar

Creates a new webinar. If "host" parameter is NOT passed then the current authorized user will become a Host. If "host" parameter is passed then the caller must be a company administrator and have "WebinarSettings" permission. "host.linkedUser.accountId" must be the same as authorized user's account ID. The webinar settings which are not mandated at account level or are unlocked can be specified. All other settings are defaulted according to account policy.

- HTTP Method: `POST`
- Endpoint: `/webinar/configuration/v1/webinars`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [WebinarCreationRequest](../models/WebinarCreationRequest.md) | ✅       | The request body. |

**Return Type**

`WcsWebinarResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import WebinarCreationRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = WebinarCreationRequest(
    title="All-Hands Webinar",
    description="Quarterly All-hands event to present recent news about our company to employees",
    settings={
        "recording_enabled": True,
        "auto_record": True,
        "recording_sharing_enabled": True,
        "recording_download_enabled": True,
        "past_session_deletion_enabled": False,
        "panelist_waiting_room": False,
        "panelist_video_enabled": True,
        "panelist_screen_sharing_enabled": True,
        "panelist_mute_control_enabled": True,
        "panelist_authentication": "Guest",
        "attendee_authentication": "Guest",
        "artifacts_access_authentication": "Guest",
        "pstn_enabled": False,
        "password": "tempo",
        "qna_enabled": True,
        "qna_anonymous_enabled": True,
        "polls_enabled": True,
        "polls_anonymous_enabled": True,
        "registration_enabled": True,
        "post_webinar_redirect_uri": "https://www.acme.com/thankyou",
        "external_livestream_enabled": True,
        "moderated_qna_enabled": True
    },
    host={
        "linked_user": {
            "user_id": "irure ullamco ut nulla officia",
            "account_id": "labore aute ipsum",
            "domain": "pbx"
        }
    }
)

result = sdk.webinars_and_sessions.rcw_config_create_webinar(request_body=request_body)

print(result)
```

## rcw_config_get_webinar

Returns a Webinar information by ID. Some webinar settings are returned basing on webinar-level overrides, other - from default settings defined at account level.

- HTTP Method: `GET`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar. |

**Return Type**

`WcsWebinarResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webinars_and_sessions.rcw_config_get_webinar(webinar_id="a")

print(result)
```

## rcw_config_update_webinar

Updates a Webinar. The payload may contain just changed fields of a Webinar resource (it is a partial update): - host cannot be changed, and host user information cannot be updated; - only the settings which are not mandated at account level or are unlocked can be changed; - in order to reset a webinar password it should be passed as an empty string; - "registrationStatus" cannot be changed.

- HTTP Method: `PATCH`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}`

**Parameters**

| Name         | Type                                              | Required | Description                |
| :----------- | :------------------------------------------------ | :------- | :------------------------- |
| request_body | [WebinarBaseModel](../models/WebinarBaseModel.md) | ✅       | The request body.          |
| webinar_id   | str                                               | ✅       | Identifier of the Webinar. |

**Return Type**

`WcsWebinarResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import WebinarBaseModel

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = WebinarBaseModel(
    title="All-Hands Webinar",
    description="Quarterly All-hands event to present recent news about our company to employees",
    settings={
        "recording_enabled": True,
        "auto_record": True,
        "recording_sharing_enabled": True,
        "recording_download_enabled": True,
        "past_session_deletion_enabled": False,
        "panelist_waiting_room": False,
        "panelist_video_enabled": True,
        "panelist_screen_sharing_enabled": True,
        "panelist_mute_control_enabled": True,
        "panelist_authentication": "Guest",
        "attendee_authentication": "Guest",
        "artifacts_access_authentication": "Guest",
        "pstn_enabled": False,
        "password": "tempo",
        "qna_enabled": True,
        "qna_anonymous_enabled": True,
        "polls_enabled": True,
        "polls_anonymous_enabled": True,
        "registration_enabled": True,
        "post_webinar_redirect_uri": "https://www.acme.com/thankyou",
        "external_livestream_enabled": True,
        "moderated_qna_enabled": True
    }
)

result = sdk.webinars_and_sessions.rcw_config_update_webinar(
    request_body=request_body,
    webinar_id="a"
)

print(result)
```

## rcw_config_delete_webinar

Deletes a Webinar by ID. All child objects (Sessions, Invitees) will be also deleted. It is disallowed to delete a Webinar which has at least one Session in 'Active' or 'Finished' state.

- HTTP Method: `DELETE`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webinars_and_sessions.rcw_config_delete_webinar(webinar_id="a")

print(result)
```

## rcw_config_create_session

Creates a new Session for a given Webinar

- HTTP Method: `POST`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions`

**Parameters**

| Name         | Type                                                                        | Required | Description                |
| :----------- | :-------------------------------------------------------------------------- | :------- | :------------------------- |
| request_body | [WcsSessionWithLocaleCodeModel](../models/WcsSessionWithLocaleCodeModel.md) | ✅       | The request body.          |
| webinar_id   | str                                                                         | ✅       | Identifier of the Webinar. |

**Return Type**

`WcsSessionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import WcsSessionWithLocaleCodeModel

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = WcsSessionWithLocaleCodeModel(
    scheduled_start_time="scheduledStartTime",
    scheduled_duration=1800,
    time_zone="America/New_York",
    localized_time_zone_description="Eastern Time (America/New_York)",
    panel_join_time_offset=900,
    title="Live Broadcasting US",
    description="Live session for US-based participants",
    status="Scheduled",
    host_join_uri="https://v.ringcentral.com/w/join/de7yd8ew7yfsdfjh899843rgj",
    locale_code="en-US"
)

result = sdk.webinars_and_sessions.rcw_config_create_session(
    request_body=request_body,
    webinar_id="minim qui"
)

print(result)
```

## rcw_config_get_session

Returns a Webinar Session by ID.

- HTTP Method: `GET`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar. |
| session_id | str  | ✅       | Identifier of the Session. |

**Return Type**

`WcsSessionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webinars_and_sessions.rcw_config_get_session(
    webinar_id="ci",
    session_id="et in"
)

print(result)
```

## rcw_config_update_session

Updates a Webinar Session. The payload may contain certain attributes from the Session resource (it is a partial update). Changing the 'status' field usually invokes certain workflow actions. Updating a Session in 'Active' or 'Finished' status is prohibited. Some status transitions (for example, to 'Active" or 'Finished') may be prohibited.

- HTTP Method: `PATCH`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}`

**Parameters**

| Name         | Type                                                                        | Required | Description                |
| :----------- | :-------------------------------------------------------------------------- | :------- | :------------------------- |
| request_body | [WcsSessionWithLocaleCodeModel](../models/WcsSessionWithLocaleCodeModel.md) | ✅       | The request body.          |
| webinar_id   | str                                                                         | ✅       | Identifier of the Webinar. |
| session_id   | str                                                                         | ✅       | Identifier of the Session. |

**Return Type**

`WcsSessionResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import WcsSessionWithLocaleCodeModel

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = WcsSessionWithLocaleCodeModel(
    scheduled_start_time="scheduledStartTime",
    scheduled_duration=1800,
    time_zone="America/New_York",
    localized_time_zone_description="Eastern Time (America/New_York)",
    panel_join_time_offset=900,
    title="Live Broadcasting US",
    description="Live session for US-based participants",
    status="Scheduled",
    host_join_uri="https://v.ringcentral.com/w/join/de7yd8ew7yfsdfjh899843rgj",
    locale_code="en-US"
)

result = sdk.webinars_and_sessions.rcw_config_update_session(
    request_body=request_body,
    webinar_id="ci",
    session_id="et in"
)

print(result)
```

## rcw_config_delete_session

Deletes a Webinar Session. All child objects (Invitees) will be also deleted. It is disallowed to delete a Session which is in 'Active' or 'Finished' state

- HTTP Method: `DELETE`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar. |
| session_id | str  | ✅       | Identifier of the Session. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webinars_and_sessions.rcw_config_delete_session(
    webinar_id="ci",
    session_id="et in"
)

print(result)
```

## rcw_config_list_all_company_sessions

Returns the list of Webinar Sessions hosted by all company users or particular user(s) sorted by 'scheduledStartTime' or 'creationTime' (if 'scheduledStartTime' is not set) in the ascending ordered. The user must have "WebinarSettings" permission granted otherwise the API returns HTTP 403.

- HTTP Method: `GET`
- Endpoint: `/webinar/configuration/v1/company/sessions`

**Parameters**

| Name          | Type                                                        | Required | Description                                                                                                             |
| :------------ | :---------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| end_time_from | str                                                         | ✅       | The beginning of the time window by 'endTime' (it is calculated as scheduledStartTime+scheduledDuration)                |
| status        | [WcsSessionStatusModel](../models/WcsSessionStatusModel.md) | ❌       | Filter to return only webinar sessions in certain status. Multiple values are supported.                                |
| host_user_id  | List[str]                                                   | ❌       | Identifier of the user who hosts a webinar (if omitted, webinars hosted by all company users will be returned)          |
| per_page      | int                                                         | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token    | str                                                         | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`WcsSessionGlobalListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import WcsSessionStatusModel

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
host_user_id=[
    "eu"
]

result = sdk.webinars_and_sessions.rcw_config_list_all_company_sessions(
    end_time_from="endTimeFrom",
    status="Scheduled",
    host_user_id=host_user_id,
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_config_list_all_sessions

Returns the list of Webinar Sessions hosted by a current authorized user sorted by 'scheduledStartTime' or 'creationTime' (if 'scheduledStartTime' is not set) in the ascending order

- HTTP Method: `GET`
- Endpoint: `/webinar/configuration/v1/sessions`

**Parameters**

| Name          | Type                                                        | Required | Description                                                                                                             |
| :------------ | :---------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| end_time_from | str                                                         | ✅       | The beginning of the time window by 'endTime' (it is calculated as scheduledStartTime+scheduledDuration)                |
| name_fragment | str                                                         | ❌       | Filter to return only webinar sessions containing particular substring within their names                               |
| status        | [WcsSessionStatusModel](../models/WcsSessionStatusModel.md) | ❌       | Filter to return only webinar sessions in certain status. Multiple values are supported.                                |
| per_page      | int                                                         | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token    | str                                                         | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`WcsSessionGlobalListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import WcsSessionStatusModel

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webinars_and_sessions.rcw_config_list_all_sessions(
    end_time_from="endTimeFrom",
    name_fragment="nameFragment",
    status="Scheduled",
    per_page=100,
    page_token="pageToken"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
