# NotesService

A list of all methods in the `NotesService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                |
| :-------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_chat_notes_new](#list_chat_notes_new)   | Returns the list of chat notes.                                                                                                                            |
| [create_chat_note_new](#create_chat_note_new) | Creates a new note in the specified chat.                                                                                                                  |
| [read_user_note_new](#read_user_note_new)     | Returns the specified note(s). It is possible to fetch up to 50 notes per request.                                                                         |
| [patch_note_new](#patch_note_new)             | Edits a note. Notes can be edited by any user if posted to a chat. the user belongs to.                                                                    |
| [delete_note_new](#delete_note_new)           | Deletes the specified note.                                                                                                                                |
| [lock_note_new](#lock_note_new)               | Locks a note providing the user with the unique write access for 5 hours.                                                                                  |
| [publish_note_new](#publish_note_new)         | Publishes a note making it visible to other users.                                                                                                         |
| [unlock_note_new](#unlock_note_new)           | Unlocks a note letting other users edit this note. Once the note is locked (by another user) it cannot be unlocked during 5 hours since the lock datetime. |

## list_chat_notes_new

Returns the list of chat notes.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/chats/{chatId}/notes`

**Parameters**

| Name               | Type                                                          | Required | Description                                                                                                                                                                 |
| :----------------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| chat_id            | str                                                           | ✅       | Internal identifier of a chat to fetch notes from.                                                                                                                          |
| creation_time_to   | str                                                           | ❌       | The end datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, e.g. 2019-03-10T18:23:45. The default value is Now. |
| creation_time_from | str                                                           | ❌       | The start datetime for resulting records in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone                                                    |
| creator_id         | str                                                           | ❌       | Internal identifier of the user that created the note. Multiple values are supported                                                                                        |
| status             | [ListChatNotesNewStatus](../models/ListChatNotesNewStatus.md) | ❌       | Status of notes to be fetched; if not specified all notes are fetched by default.                                                                                           |
| page_token         | str                                                           | ❌       | Pagination token                                                                                                                                                            |
| record_count       | int                                                           | ❌       | Max number of notes to be fetched by one request; the value range is 1-250.                                                                                                 |

**Return Type**

`TmNoteList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListChatNotesNewStatus

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.notes.list_chat_notes_new(
    chat_id="chatId",
    creation_time_to="creationTimeTo",
    creation_time_from="creationTimeFrom",
    creator_id="creatorId",
    status="Active",
    page_token="pageToken",
    record_count=30
)

print(result)
```

## create_chat_note_new

Creates a new note in the specified chat.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/chats/{chatId}/notes`

**Parameters**

| Name         | Type                                                    | Required | Description                                       |
| :----------- | :------------------------------------------------------ | :------- | :------------------------------------------------ |
| request_body | [TmCreateNoteRequest](../models/TmCreateNoteRequest.md) | ✅       | The request body.                                 |
| chat_id      | str                                                     | ✅       | Internal identifier of a chat to create a note in |

**Return Type**

`TmNoteInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreateNoteRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreateNoteRequest(
    title="title",
    body="body"
)

result = sdk.notes.create_chat_note_new(
    request_body=request_body,
    chat_id="chatId"
)

print(result)
```

## read_user_note_new

Returns the specified note(s). It is possible to fetch up to 50 notes per request.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/notes/{noteId}`

**Parameters**

| Name    | Type | Required | Description                                 |
| :------ | :--- | :------- | :------------------------------------------ |
| note_id | str  | ✅       | Internal identifier of a note to be fetched |

**Return Type**

`TmNoteWithBodyInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.notes.read_user_note_new(note_id="noteId")

print(result)
```

## patch_note_new

Edits a note. Notes can be edited by any user if posted to a chat. the user belongs to.

- HTTP Method: `PATCH`
- Endpoint: `/team-messaging/v1/notes/{noteId}`

**Parameters**

| Name         | Type                                                    | Required | Description                                                   |
| :----------- | :------------------------------------------------------ | :------- | :------------------------------------------------------------ |
| request_body | [TmCreateNoteRequest](../models/TmCreateNoteRequest.md) | ✅       | The request body.                                             |
| note_id      | str                                                     | ✅       | Internal identifier of a note to be updated                   |
| release_lock | bool                                                    | ❌       | If true then note lock (if any) will be released upon request |

**Return Type**

`TmNoteInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreateNoteRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreateNoteRequest(
    title="title",
    body="body"
)

result = sdk.notes.patch_note_new(
    request_body=request_body,
    note_id="noteId",
    release_lock=True
)

print(result)
```

## delete_note_new

Deletes the specified note.

- HTTP Method: `DELETE`
- Endpoint: `/team-messaging/v1/notes/{noteId}`

**Parameters**

| Name    | Type | Required | Description                                 |
| :------ | :--- | :------- | :------------------------------------------ |
| note_id | str  | ✅       | Internal identifier of a note to be deleted |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.notes.delete_note_new(note_id="noteId")

print(result)
```

## lock_note_new

Locks a note providing the user with the unique write access for 5 hours.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/notes/{noteId}/lock`

**Parameters**

| Name    | Type | Required | Description                                |
| :------ | :--- | :------- | :----------------------------------------- |
| note_id | str  | ✅       | Internal identifier of a note to be locked |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.notes.lock_note_new(note_id="noteId")

print(result)
```

## publish_note_new

Publishes a note making it visible to other users.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/notes/{noteId}/publish`

**Parameters**

| Name    | Type | Required | Description                                   |
| :------ | :--- | :------- | :-------------------------------------------- |
| note_id | str  | ✅       | Internal identifier of a note to be published |

**Return Type**

`TmNoteInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.notes.publish_note_new(note_id="noteId")

print(result)
```

## unlock_note_new

Unlocks a note letting other users edit this note. Once the note is locked (by another user) it cannot be unlocked during 5 hours since the lock datetime.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/notes/{noteId}/unlock`

**Parameters**

| Name    | Type | Required | Description                                  |
| :------ | :--- | :------- | :------------------------------------------- |
| note_id | str  | ✅       | Internal identifier of a note to be unlocked |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.notes.unlock_note_new(note_id="noteId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
