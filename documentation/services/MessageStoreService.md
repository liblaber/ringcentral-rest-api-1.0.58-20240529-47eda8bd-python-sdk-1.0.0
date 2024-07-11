# MessageStoreService

A list of all methods in the `MessageStoreService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_message_content](#read_message_content)                             | Returns media content of a message attachment. The content is typically an audio file (`audio/mpeg` or `audio/wav`) for voicemails, TIFF or PDF for faxes and image/audio/video for MMS. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**                                                                                                                                                                                                                                                                                                                                 |
| [read_message_store_configuration](#read_message_store_configuration)     | Returns message store settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [update_message_store_configuration](#update_message_store_configuration) | Updates message store settings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [sync_messages](#sync_messages)                                           | Synchronizes messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [list_messages](#list_messages)                                           | Returns a list of messages from an extension mailbox.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [delete_message_by_filter](#delete_message_by_filter)                     | Deletes conversation(s) by conversation ID(s). Batch request is supported, max number of IDs passed as query/path parameters is 50. Alternative syntax is supported - user conversations can be deleted by passing multiple IDs in request body as an array of string, max number of conversation IDs passed in request body is 100. In this case asterisk is used in the path instead of IDs                                                                                                                                                                                                                      |
| [read_message](#read_message)                                             | Returns an individual message record or multiple records by the given message ID(s). The length of inbound messages is unlimited. Bulk syntax is supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [update_message](#update_message)                                         | Updates message(s) by their ID(s). Currently, only the `readStatus` can be updated using this method. Bulk syntax is supported, max number of IDs passed as query/path parameters is 50. Alternative bulk syntax is also supported - user messages can be updated by passing multiple IDs in request body as an array of string, max number of IDs passed in the body is 1000. In this case asterisk is used in the path instead of IDs.                                                                                                                                                                           |
| [patch_message](#patch_message)                                           | Patches message(s) by ID(s). Currently, only updating the `readStatus` and restoring deleted messages are supported through this method. For changing status of a message send `readStatus` set to either 'Read' or 'Unread' in request. It is possible to restore a message and its attachments (if message status is 'Deleted') by sending `availability` attribute set to 'Alive' in request body. If a message is already in 'Purged' state then its attachments cannot be restored and the message itself is about to be physically deleted. Bulk syntax (both traditional and alternative one) is supported. |
| [delete_message](#delete_message)                                         | Deletes message(s) by the given message ID(s). The first call of this method transfers the message to the 'Delete' status. The second call transfers the deleted message to the 'Purged' status. If it is required to make the message 'Purged' immediately (from the first call), then set the query parameter purge to `true`.                                                                                                                                                                                                                                                                                   |

## read_message_content

Returns media content of a message attachment. The content is typically an audio file (`audio/mpeg` or `audio/wav`) for voicemails, TIFF or PDF for faxes and image/audio/video for MMS. **This API must be called via media API entry point, e.g. https://media.ringcentral.com**

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}/content/{attachmentId}`

**Parameters**

| Name                         | Type                                                  | Required | Description                                                                                                                                                           |
| :--------------------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id                   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id                 | str                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| message_id                   | str                                                   | ✅       |                                                                                                                                                                       |
| attachment_id                | str                                                   | ✅       |                                                                                                                                                                       |
| content_disposition          | [ContentDisposition](../models/ContentDisposition.md) | ❌       | Whether the content is expected to be displayed in the browser, or downloaded and saved locally                                                                       |
| content_disposition_filename | str                                                   | ❌       | The default filename of the file to be downloaded                                                                                                                     |

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

result = sdk.message_store.read_message_content(
    account_id="~",
    extension_id="~",
    message_id="messageId",
    attachment_id="attachmentId",
    content_disposition="Inline",
    content_disposition_filename="contentDispositionFilename"
)

print(result)
```

## read_message_store_configuration

Returns message store settings.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-configuration`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`MessageStoreConfiguration`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.message_store.read_message_store_configuration(account_id="~")

print(result)
```

## update_message_store_configuration

Updates message store settings.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/message-store-configuration`

**Parameters**

| Name         | Type                                                                | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [MessageStoreConfiguration](../models/MessageStoreConfiguration.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`MessageStoreConfiguration`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import MessageStoreConfiguration

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MessageStoreConfiguration(
    retention_period=72
)

result = sdk.message_store.update_message_store_configuration(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## sync_messages

Synchronizes messages.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-sync`

**Parameters**

| Name                   | Type                                                            | Required | Description                                                                                                                                                                                                |
| :--------------------- | :-------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id             | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                               |
| extension_id           | str                                                             | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                                      |
| conversation_id        | int                                                             | ❌       | Conversation identifier for the resulting messages. Meaningful for SMS and Pager messages only.                                                                                                            |
| date_from              | str                                                             | ❌       | The start date/time for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is dateTo minus 24 hours                                         |
| date_to                | str                                                             | ❌       | The end date/time for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time                                                    |
| direction              | [List[MessageDirectionEnum]](../models/MessageDirectionEnum.md) | ❌       | Direction for the resulting messages. If not specified, both inbound and outbound messages are returned. Multiple values are accepted                                                                      |
| distinct_conversations | bool                                                            | ❌       | If `true`, then the latest messages per every conversation ID are returned                                                                                                                                 |
| message_type           | [List[MessageTypeEnum]](../models/MessageTypeEnum.md)           | ❌       | Type for the resulting messages. If not specified, all types of messages are returned. Multiple values are accepted                                                                                        |
| record_count           | int                                                             | ❌       | Limits the number of records to be returned (works in combination with dateFrom and dateTo if specified)                                                                                                   |
| sync_token             | str                                                             | ❌       | A `syncToken` value from the previous sync response (for `ISync` mode only, mandatory)                                                                                                                     |
| sync_type              | [SyncTypeEnum](../models/SyncTypeEnum.md)                       | ❌       | Type of message synchronization                                                                                                                                                                            |
| voicemail_owner        | List[str]                                                       | ❌       | This query parameter will filter voicemail messages based on its owner. This parameter should be controlled by the 'SharedVoicemail' feature. If the feature is disabled this filter shouldn't be applied. |

**Return Type**

`GetMessageSyncResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SyncTypeEnum

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
direction=[
    "Inbound"
]
message_type=[
    "Fax"
]
voicemail_owner=[
    "voicemailOwner"
]

result = sdk.message_store.sync_messages(
    account_id="~",
    extension_id="~",
    conversation_id=5,
    date_from="dateFrom",
    date_to="dateTo",
    direction=direction,
    distinct_conversations=False,
    message_type=message_type,
    record_count=2,
    sync_token="syncToken",
    sync_type="FSync",
    voicemail_owner=voicemail_owner
)

print(result)
```

## list_messages

Returns a list of messages from an extension mailbox.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store`

**Parameters**

| Name                   | Type                                                                  | Required | Description                                                                                                                                                           |
| :--------------------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id             | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id           | str                                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| availability           | [List[MessageAvailabilityEnum]](../models/MessageAvailabilityEnum.md) | ❌       | Specifies the availability status for resulting messages. Multiple values are accepted                                                                                |
| conversation_id        | str                                                                   | ❌       | Specifies a conversation identifier for the resulting messages                                                                                                        |
| date_from              | str                                                                   | ❌       | Start date/time for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is dateTo minus 24 hours        |
| date_to                | str                                                                   | ❌       | End date/time for resulting messages in ISO 8601 format including timezone, for example 2016-03-10T18:07:52.534Z. The default value is current time                   |
| direction              | [List[MessageDirectionEnum]](../models/MessageDirectionEnum.md)       | ❌       | Direction for resulting messages. If not specified, both inbound and outbound messages are returned. Multiple values are accepted                                     |
| distinct_conversations | bool                                                                  | ❌       | If `true`, then the latest messages per every conversation ID are returned                                                                                            |
| message_type           | [List[MessageTypeEnum]](../models/MessageTypeEnum.md)                 | ❌       | Type of resulting messages. If not specified, all messages without message type filtering are returned. Multiple values are accepted                                  |
| read_status            | [List[MessageReadStatusEnum]](../models/MessageReadStatusEnum.md)     | ❌       | Read status for resulting messages. Multiple values are accepted                                                                                                      |
| page                   | int                                                                   | ❌       | Indicates a page number to retrieve. Only positive number values are accepted                                                                                         |
| per_page               | int                                                                   | ❌       | Indicates a page size (number of items)                                                                                                                               |
| phone_number           | str                                                                   | ❌       | Phone number. If specified, messages are returned for this particular phone number only                                                                               |

**Return Type**

`GetMessageList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
availability=[
    "Alive"
]
direction=[
    "Inbound"
]
message_type=[
    "Fax"
]
read_status=[
    "Read"
]

result = sdk.message_store.list_messages(
    account_id="~",
    extension_id="~",
    availability=availability,
    conversation_id="conversationId",
    date_from="dateFrom",
    date_to="dateTo",
    direction=direction,
    distinct_conversations=False,
    message_type=message_type,
    read_status=read_status,
    page=1,
    per_page=100,
    phone_number="phoneNumber"
)

print(result)
```

## delete_message_by_filter

Deletes conversation(s) by conversation ID(s). Batch request is supported, max number of IDs passed as query/path parameters is 50. Alternative syntax is supported - user conversations can be deleted by passing multiple IDs in request body as an array of string, max number of conversation IDs passed in request body is 100. In this case asterisk is used in the path instead of IDs

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store`

**Parameters**

| Name            | Type                                                                | Required | Description                                                                                                                                                           |
| :-------------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id    | str                                                                 | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| conversation_id | List[str]                                                           | ❌       |                                                                                                                                                                       |
| date_to         | str                                                                 | ❌       | Messages received earlier then the date specified will be deleted. The default value is current date/time                                                             |
| type\_          | [DeleteMessageByFilterType](../models/DeleteMessageByFilterType.md) | ❌       | Type of messages to be deleted                                                                                                                                        |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import DeleteMessageByFilterType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
conversation_id=[
    "conversationId"
]

result = sdk.message_store.delete_message_by_filter(
    account_id="~",
    extension_id="~",
    conversation_id=conversation_id,
    date_to="dateTo",
    type_="Fax"
)

print(result)
```

## read_message

Returns an individual message record or multiple records by the given message ID(s). The length of inbound messages is unlimited. Bulk syntax is supported.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}`

**Parameters**

| Name         | Type      | Required | Description                                                                                                                                                           |
| :----------- | :-------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| message_id   | List[str] | ✅       | Internal identifier of a message (or multiple messages in case of bulk operation)                                                                                     |

**Return Type**

`GetMessageInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
message_id=[
    "8930983240"
]

result = sdk.message_store.read_message(
    account_id="~",
    extension_id="~",
    message_id=message_id
)

print(result)
```

## update_message

Updates message(s) by their ID(s). Currently, only the `readStatus` can be updated using this method. Bulk syntax is supported, max number of IDs passed as query/path parameters is 50. Alternative bulk syntax is also supported - user messages can be updated by passing multiple IDs in request body as an array of string, max number of IDs passed in the body is 1000. In this case asterisk is used in the path instead of IDs.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}`

**Parameters**

| Name         | Type                                                      | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateMessageRequest](../models/UpdateMessageRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| message_id   | List[str]                                                 | ✅       | Internal identifier of a message (or multiple messages in case of bulk operation)                                                                                     |

**Return Type**

`GetMessageInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateMessageRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateMessageRequest(
    read_status="Read"
)
message_id=[
    "8930983240"
]

result = sdk.message_store.update_message(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    message_id=message_id
)

print(result)
```

## patch_message

Patches message(s) by ID(s). Currently, only updating the `readStatus` and restoring deleted messages are supported through this method. For changing status of a message send `readStatus` set to either 'Read' or 'Unread' in request. It is possible to restore a message and its attachments (if message status is 'Deleted') by sending `availability` attribute set to 'Alive' in request body. If a message is already in 'Purged' state then its attachments cannot be restored and the message itself is about to be physically deleted. Bulk syntax (both traditional and alternative one) is supported.

- HTTP Method: `PATCH`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}`

**Parameters**

| Name         | Type                                                    | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [PatchMessageRequest](../models/PatchMessageRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                     | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| message_id   | List[str]                                               | ✅       | Internal identifier of a message (or multiple messages in case of bulk operation)                                                                                     |

**Return Type**

`GetMessageInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PatchMessageRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PatchMessageRequest(
    read_status="Read",
    availability="Alive"
)
message_id=[
    "8930983240"
]

result = sdk.message_store.patch_message(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    message_id=message_id
)

print(result)
```

## delete_message

Deletes message(s) by the given message ID(s). The first call of this method transfers the message to the 'Delete' status. The second call transfers the deleted message to the 'Purged' status. If it is required to make the message 'Purged' immediately (from the first call), then set the query parameter purge to `true`.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/message-store/{messageId}`

**Parameters**

| Name         | Type      | Required | Description                                                                                                                                                           |
| :----------- | :-------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | List[str] | ❌       | The request body.                                                                                                                                                     |
| account_id   | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| message_id   | List[str] | ✅       | Internal identifier of a message (or multiple messages in case of bulk operation)                                                                                     |
| purge        | bool      | ❌       | If the value is `true`, then the message is purged immediately with all the attachments                                                                               |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    "dolore ven"
]
message_id=[
    "8930983240"
]

result = sdk.message_store.delete_message(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    message_id=message_id,
    purge=True
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
