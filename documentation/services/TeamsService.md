# TeamsService

A list of all methods in the `TeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_glip_everyone_new](#read_glip_everyone_new)             | Returns information about "Everyone" chat (a company level chat which includes all employees).                                                                                                                                                                                                                                                  |
| [patch_glip_everyone_new](#patch_glip_everyone_new)           | Updates "Everyone" chat information.                                                                                                                                                                                                                                                                                                            |
| [list_glip_teams_new](#list_glip_teams_new)                   | Returns the list of teams where the user is a member (both archived and active) combined with a list of public teams that can be joined by the current user. All records in response are sorted by creation time of a chat in ascending order. A team is a chat between 2 and more (unlimited number) participants assigned with specific name. |
| [create_glip_team_new](#create_glip_team_new)                 | Creates a team, and adds a list of people to the team.                                                                                                                                                                                                                                                                                          |
| [read_glip_team_new](#read_glip_team_new)                     | Returns information about the specified team.                                                                                                                                                                                                                                                                                                   |
| [patch_glip_team_new](#patch_glip_team_new)                   | Updates the name and description of the specified team.                                                                                                                                                                                                                                                                                         |
| [delete_glip_team_new](#delete_glip_team_new)                 | Deletes the specified team.                                                                                                                                                                                                                                                                                                                     |
| [remove_glip_team_members_new](#remove_glip_team_members_new) | Removes members from the specified team.                                                                                                                                                                                                                                                                                                        |
| [join_glip_team_new](#join_glip_team_new)                     | Adds the current user to the specified team.                                                                                                                                                                                                                                                                                                    |
| [archive_glip_team_new](#archive_glip_team_new)               | Changes the status of the specified team to 'Archived'.                                                                                                                                                                                                                                                                                         |
| [unarchive_glip_team_new](#unarchive_glip_team_new)           | Changes the status of the specified team to 'Active'.                                                                                                                                                                                                                                                                                           |
| [leave_glip_team_new](#leave_glip_team_new)                   | Removes the current user from the specified team.                                                                                                                                                                                                                                                                                               |
| [add_glip_team_members_new](#add_glip_team_members_new)       | Adds members to the specified team.                                                                                                                                                                                                                                                                                                             |

## read_glip_everyone_new

Returns information about "Everyone" chat (a company level chat which includes all employees).

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/everyone`

**Return Type**

`EveryoneTeamInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.read_glip_everyone_new()

print(result)
```

## patch_glip_everyone_new

Updates "Everyone" chat information.

- HTTP Method: `PATCH`
- Endpoint: `/team-messaging/v1/everyone`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [UpdateEveryoneTeamRequest](../models/UpdateEveryoneTeamRequest.md) | ❌       | The request body. |

**Return Type**

`EveryoneTeamInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateEveryoneTeamRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateEveryoneTeamRequest(
    name="name",
    description="description"
)

result = sdk.teams.patch_glip_everyone_new(request_body=request_body)

print(result)
```

## list_glip_teams_new

Returns the list of teams where the user is a member (both archived and active) combined with a list of public teams that can be joined by the current user. All records in response are sorted by creation time of a chat in ascending order. A team is a chat between 2 and more (unlimited number) participants assigned with specific name.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/teams`

**Parameters**

| Name         | Type | Required | Description                                                                             |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------- |
| record_count | int  | ❌       | Number of teams to be fetched by one request. The maximum value is 250, by default - 30 |
| page_token   | str  | ❌       | Pagination token.                                                                       |

**Return Type**

`TmTeamList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.list_glip_teams_new(
    record_count=30,
    page_token="pageToken"
)

print(result)
```

## create_glip_team_new

Creates a team, and adds a list of people to the team.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/teams`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [TmCreateTeamRequest](../models/TmCreateTeamRequest.md) | ✅       | The request body. |

**Return Type**

`TmTeamInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreateTeamRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreateTeamRequest(
    public=False,
    name="name",
    description="description",
    members=[
        {
            "id_": "id",
            "email": "email"
        }
    ]
)

result = sdk.teams.create_glip_team_new(request_body=request_body)

print(result)
```

## read_glip_team_new

Returns information about the specified team.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/teams/{chatId}`

**Parameters**

| Name    | Type | Required | Description                                   |
| :------ | :--- | :------- | :-------------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a team to be returned. |

**Return Type**

`TmTeamInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.read_glip_team_new(chat_id="chatId")

print(result)
```

## patch_glip_team_new

Updates the name and description of the specified team.

- HTTP Method: `PATCH`
- Endpoint: `/team-messaging/v1/teams/{chatId}`

**Parameters**

| Name         | Type                                                    | Required | Description                                  |
| :----------- | :------------------------------------------------------ | :------- | :------------------------------------------- |
| request_body | [TmUpdateTeamRequest](../models/TmUpdateTeamRequest.md) | ✅       | The request body.                            |
| chat_id      | str                                                     | ✅       | Internal identifier of a team to be updated. |

**Return Type**

`TmTeamInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmUpdateTeamRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmUpdateTeamRequest(
    public=False,
    name="name",
    description="description"
)

result = sdk.teams.patch_glip_team_new(
    request_body=request_body,
    chat_id="chatId"
)

print(result)
```

## delete_glip_team_new

Deletes the specified team.

- HTTP Method: `DELETE`
- Endpoint: `/team-messaging/v1/teams/{chatId}`

**Parameters**

| Name    | Type | Required | Description                    |
| :------ | :--- | :------- | :----------------------------- |
| chat_id | str  | ✅       | Internal identifier of a team. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.delete_glip_team_new(chat_id="chatId")

print(result)
```

## remove_glip_team_members_new

Removes members from the specified team.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/teams/{chatId}/remove`

**Parameters**

| Name         | Type                                                                  | Required | Description                                           |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------------------------------------------- |
| request_body | [TmRemoveTeamMembersRequest](../models/TmRemoveTeamMembersRequest.md) | ✅       | The request body.                                     |
| chat_id      | str                                                                   | ✅       | Internal identifier of a team to remove members from. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmRemoveTeamMembersRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmRemoveTeamMembersRequest(
    members=[
        {
            "id_": "id"
        }
    ]
)

result = sdk.teams.remove_glip_team_members_new(
    request_body=request_body,
    chat_id="chatId"
)

print(result)
```

## join_glip_team_new

Adds the current user to the specified team.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/teams/{chatId}/join`

**Parameters**

| Name    | Type | Required | Description                                 |
| :------ | :--- | :------- | :------------------------------------------ |
| chat_id | str  | ✅       | Internal identifier of a team to be joined. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.join_glip_team_new(chat_id="chatId")

print(result)
```

## archive_glip_team_new

Changes the status of the specified team to 'Archived'.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/teams/{chatId}/archive`

**Parameters**

| Name    | Type | Required | Description                                   |
| :------ | :--- | :------- | :-------------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a team to be archived. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.archive_glip_team_new(chat_id="chatId")

print(result)
```

## unarchive_glip_team_new

Changes the status of the specified team to 'Active'.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/teams/{chatId}/unarchive`

**Parameters**

| Name    | Type | Required | Description                                      |
| :------ | :--- | :------- | :----------------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a team to be made active. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.unarchive_glip_team_new(chat_id="chatId")

print(result)
```

## leave_glip_team_new

Removes the current user from the specified team.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/teams/{chatId}/leave`

**Parameters**

| Name    | Type | Required | Description                               |
| :------ | :--- | :------- | :---------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a team to be left. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.leave_glip_team_new(chat_id="chatId")

print(result)
```

## add_glip_team_members_new

Adds members to the specified team.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/teams/{chatId}/add`

**Parameters**

| Name         | Type                                                            | Required | Description                                      |
| :----------- | :-------------------------------------------------------------- | :------- | :----------------------------------------------- |
| request_body | [TmAddTeamMembersRequest](../models/TmAddTeamMembersRequest.md) | ✅       | The request body.                                |
| chat_id      | str                                                             | ✅       | Internal identifier of a team to add members to. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmAddTeamMembersRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmAddTeamMembersRequest(
    members=[
        {
            "id_": "id",
            "email": "email"
        }
    ]
)

result = sdk.teams.add_glip_team_members_new(
    request_body=request_body,
    chat_id="chatId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
