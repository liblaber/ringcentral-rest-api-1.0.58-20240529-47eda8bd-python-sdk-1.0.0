# InviteesService

A list of all methods in the `InviteesService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rcw_config_list_invitees](#rcw_config_list_invitees)     | Returns the list of Invitees (co-hosts and panelists in phase 1 and also invited attendees in subsequent phases) of a given Webinar Session. An implicit record created for a Webinar 'Host' is always returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [rcw_config_update_invitees](#rcw_config_update_invitees) | Adds, updates and deletes Webinar Session invitees in bulk (co-hosts and panelists in phase 1 and also invited attendees in subsequent phases). The payload may contain multiple added, updated or deleted invitees. For each added record 'role' and either 'firstName'/'lastName'/'email' (for non-authenticated users) or 'linkedUser.\*' (for authenticated users) must be specified, but not both. For updated invitees 'id' and 'role' must be specified, 'linkedUser' change is not supported. For deleted invitees only there ids should be specified. The response contains added/updated records (full) and deleted records (ids only). Deleting an invitee for a Session in 'Active' or 'Finished' status is prohibited. |
| [rcw_config_get_invitee](#rcw_config_get_invitee)         | Returns a Session Invitee information by ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [rcw_config_update_invitee](#rcw_config_update_invitee)   | Updates a Session Invitee. 'role' is required (it can be changed from 'Panelist' to 'CoHost' or vise versa). It is disallowed to update 'linkedUser': it should be done by deleting then adding an invitee. For non-authenticated users 'firstName'/'lastName'/'email' can be specified, but not both. Implicit record created for a Webinar 'Host' cannot be modified. Also it is disallowed to change any other role to 'Host'.                                                                                                                                                                                                                                                                                                   |
| [rcw_config_delete_invitee](#rcw_config_delete_invitee)   | Deletes a Session Invitee. Implicit record created for a Webinar 'Host' cannot be deleted. Deleting an invitee for a Session in 'Active' or 'Finished' status is prohibited (HTTP 403).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## rcw_config_list_invitees

Returns the list of Invitees (co-hosts and panelists in phase 1 and also invited attendees in subsequent phases) of a given Webinar Session. An implicit record created for a Webinar 'Host' is always returned.

- HTTP Method: `GET`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}/invitees`

**Parameters**

| Name       | Type | Required | Description                                                                                                             |
| :--------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar.                                                                                              |
| session_id | str  | ✅       | Identifier of the Session.                                                                                              |
| per_page   | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |
| page_token | str  | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |

**Return Type**

`WcsInviteeListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invitees.rcw_config_list_invitees(
    webinar_id="veniam labore adipi",
    session_id="Ut",
    per_page=100,
    page_token="pageToken"
)

print(result)
```

## rcw_config_update_invitees

Adds, updates and deletes Webinar Session invitees in bulk (co-hosts and panelists in phase 1 and also invited attendees in subsequent phases). The payload may contain multiple added, updated or deleted invitees. For each added record 'role' and either 'firstName'/'lastName'/'email' (for non-authenticated users) or 'linkedUser.\*' (for authenticated users) must be specified, but not both. For updated invitees 'id' and 'role' must be specified, 'linkedUser' change is not supported. For deleted invitees only there ids should be specified. The response contains added/updated records (full) and deleted records (ids only). Deleting an invitee for a Session in 'Active' or 'Finished' status is prohibited.

- HTTP Method: `PATCH`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}/invitees`

**Parameters**

| Name         | Type                                                                | Required | Description                |
| :----------- | :------------------------------------------------------------------ | :------- | :------------------------- |
| request_body | [BulkUpdateInviteesRequest](../models/BulkUpdateInviteesRequest.md) | ✅       | The request body.          |
| webinar_id   | str                                                                 | ✅       | Identifier of the Webinar. |
| session_id   | str                                                                 | ✅       | Identifier of the Session. |

**Return Type**

`BulkUpdateInviteesResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BulkUpdateInviteesRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BulkUpdateInviteesRequest(
    added_invitees=[
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "job_title": "Product Manager",
            "linked_user": {
                "user_id": "irure ullamco ut nulla officia",
                "account_id": "labore aute ipsum",
                "domain": "pbx"
            },
            "role": "Panelist",
            "type_": "User",
            "send_invite": True
        }
    ],
    updated_invitees=[
        {
            "id_": "78654321",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "job_title": "Product Manager",
            "role": "Panelist",
            "type_": "User",
            "send_invite": True
        }
    ],
    deleted_invitees=[
        {
            "id_": "78654321"
        }
    ]
)

result = sdk.invitees.rcw_config_update_invitees(
    request_body=request_body,
    webinar_id="veniam labore adipi",
    session_id="Ut"
)

print(result)
```

## rcw_config_get_invitee

Returns a Session Invitee information by ID

- HTTP Method: `GET`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}/invitees/{inviteeId}`

**Parameters**

| Name       | Type | Required | Description                        |
| :--------- | :--- | :------- | :--------------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar.         |
| session_id | str  | ✅       | Identifier of the Session.         |
| invitee_id | str  | ✅       | Identifier of the Session Invitee. |

**Return Type**

`InviteeResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invitees.rcw_config_get_invitee(
    webinar_id="sed",
    session_id="irure e",
    invitee_id="ut ut cillu"
)

print(result)
```

## rcw_config_update_invitee

Updates a Session Invitee. 'role' is required (it can be changed from 'Panelist' to 'CoHost' or vise versa). It is disallowed to update 'linkedUser': it should be done by deleting then adding an invitee. For non-authenticated users 'firstName'/'lastName'/'email' can be specified, but not both. Implicit record created for a Webinar 'Host' cannot be modified. Also it is disallowed to change any other role to 'Host'.

- HTTP Method: `PUT`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}/invitees/{inviteeId}`

**Parameters**

| Name         | Type                                                      | Required | Description                        |
| :----------- | :-------------------------------------------------------- | :------- | :--------------------------------- |
| request_body | [UpdateInviteeRequest](../models/UpdateInviteeRequest.md) | ✅       | The request body.                  |
| webinar_id   | str                                                       | ✅       | Identifier of the Webinar.         |
| session_id   | str                                                       | ✅       | Identifier of the Session.         |
| invitee_id   | str                                                       | ✅       | Identifier of the Session Invitee. |

**Return Type**

`InviteeResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateInviteeRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateInviteeRequest(
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com",
    job_title="Product Manager",
    role="Panelist",
    type_="User",
    send_invite=True
)

result = sdk.invitees.rcw_config_update_invitee(
    request_body=request_body,
    webinar_id="sed",
    session_id="irure e",
    invitee_id="ut ut cillu"
)

print(result)
```

## rcw_config_delete_invitee

Deletes a Session Invitee. Implicit record created for a Webinar 'Host' cannot be deleted. Deleting an invitee for a Session in 'Active' or 'Finished' status is prohibited (HTTP 403).

- HTTP Method: `DELETE`
- Endpoint: `/webinar/configuration/v1/webinars/{webinarId}/sessions/{sessionId}/invitees/{inviteeId}`

**Parameters**

| Name       | Type | Required | Description                        |
| :--------- | :--- | :------- | :--------------------------------- |
| webinar_id | str  | ✅       | Identifier of the Webinar.         |
| session_id | str  | ✅       | Identifier of the Session.         |
| invitee_id | str  | ✅       | Identifier of the Session Invitee. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invitees.rcw_config_delete_invitee(
    webinar_id="sed",
    session_id="irure e",
    invitee_id="ut ut cillu"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
