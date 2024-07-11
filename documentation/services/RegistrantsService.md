# RegistrantsService

A list of all methods in the `RegistrantsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rcw_reg_list_registrants](#rcw_reg_list_registrants)   | Returns the list of Registrants ordered by "id" ascending. A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission.                                                                                              |
| [rcw_reg_create_registrant](#rcw_reg_create_registrant) | Creates a new Registrant for a given session. Registration MUST be open for the session for this call to succeed (otherwise it should return HTTP 403). A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission. |
| [rcw_reg_get_registrant](#rcw_reg_get_registrant)       | Returns a Registrant by ID. A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission.                                                                                                                             |
| [rcw_reg_delete_registrant](#rcw_reg_delete_registrant) | Deletes a Registrant by ID. Session must not be in finished state (otherwise it should return HTTP 403). A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission.                                                |

## rcw_reg_list_registrants

Returns the list of Registrants ordered by "id" ascending. A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission.

- HTTP Method: `GET`
- Endpoint: `/webinar/registration/v1/sessions/{sessionId}/registrants`

**Parameters**

| Name                  | Type | Required | Description                                                                                                             |
| :-------------------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| session_id            | str  | ✅       | Identifier of the Session.                                                                                              |
| per_page              | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token            | str  | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |
| include_questionnaire | bool | ❌       | Indicates if registrant's "questionnaire" should be returned                                                            |

**Return Type**

`RegistrantListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.registrants.rcw_reg_list_registrants(
    session_id="minim ea fu",
    per_page=100,
    page_token="pageToken",
    include_questionnaire=False
)

print(result)
```

## rcw_reg_create_registrant

Creates a new Registrant for a given session. Registration MUST be open for the session for this call to succeed (otherwise it should return HTTP 403). A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission.

- HTTP Method: `POST`
- Endpoint: `/webinar/registration/v1/sessions/{sessionId}/registrants`

**Parameters**

| Name         | Type                                                                                      | Required | Description                |
| :----------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------- |
| request_body | [RegistrantBaseModelWithQuestionnaire](../models/RegistrantBaseModelWithQuestionnaire.md) | ✅       | The request body.          |
| session_id   | str                                                                                       | ✅       | Identifier of the Session. |

**Return Type**

`RegistrantModelResponsePostWithQuestionnaire`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import RegistrantBaseModelWithQuestionnaire

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RegistrantBaseModelWithQuestionnaire(
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com",
    join_uri="https://v.ringcentral.com/w/a/join/iuyef77fsj473wn10ashjfk34",
    cancellation_uri="https://abcde12345.webinar.ringcentral.com/register?jlt=iuyef77fsj473wn10ashjfk34&action=cancel",
    registered_post_webinar=True,
    visitor_id="visitorId",
    external_id="externalId",
    registration_time="registrationTime",
    ip_address="ipAddress",
    source="source",
    participant_id="participantId",
    questionnaire=[
        {
            "question_id": "123456789",
            "answer_ids": [
                "answerIds"
            ]
        }
    ]
)

result = sdk.registrants.rcw_reg_create_registrant(
    request_body=request_body,
    session_id="sit"
)

print(result)
```

## rcw_reg_get_registrant

Returns a Registrant by ID. A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission.

- HTTP Method: `GET`
- Endpoint: `/webinar/registration/v1/sessions/{sessionId}/registrants/{registrantId}`

**Parameters**

| Name                  | Type | Required | Description                                                  |
| :-------------------- | :--- | :------- | :----------------------------------------------------------- |
| session_id            | str  | ✅       | Identifier of the Session.                                   |
| registrant_id         | str  | ✅       | Identifier of the Session Registrant                         |
| include_questionnaire | bool | ❌       | Indicates if registrant's "questionnaire" should be returned |

**Return Type**

`RegistrantModelWithQuestionnaire`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.registrants.rcw_reg_get_registrant(
    session_id="laborum sunt",
    registrant_id="su",
    include_questionnaire=False
)

print(result)
```

## rcw_reg_delete_registrant

Deletes a Registrant by ID. Session must not be in finished state (otherwise it should return HTTP 403). A caller must be an authorized user: either a host of the webinar or an IT Admin: a user from host's account with "WebinarSettings" permission.

- HTTP Method: `DELETE`
- Endpoint: `/webinar/registration/v1/sessions/{sessionId}/registrants/{registrantId}`

**Parameters**

| Name          | Type | Required | Description                          |
| :------------ | :--- | :------- | :----------------------------------- |
| session_id    | str  | ✅       | Identifier of the Session.           |
| registrant_id | str  | ✅       | Identifier of the Session Registrant |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.registrants.rcw_reg_delete_registrant(
    session_id="dolore reprehend",
    registrant_id="in sunt consectet"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
