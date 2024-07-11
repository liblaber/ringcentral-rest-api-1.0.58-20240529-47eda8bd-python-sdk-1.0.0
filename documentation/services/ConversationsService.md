# ConversationsService

A list of all methods in the `ConversationsService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_glip_conversations_new](#list_glip_conversations_new)   | Returns the list of conversations where the user is a member. All records in response are sorted by creation time of a conversation in ascending order. Conversation is a chat of the _Group_ type.                                                                                                                                                                                       |
| [create_glip_conversation_new](#create_glip_conversation_new) | Creates a new conversation or opens the existing one. If the conversation already exists, then its ID will be returned in response. A conversation is an adhoc discussion between a particular set of users, not featuring any specific name or description; it is a chat of 'Group' type. If you add a person to the existing conversation (group), it creates a whole new conversation. |
| [read_glip_conversation_new](#read_glip_conversation_new)     | Returns information about the specified conversation, including the list of conversation participants. A conversation is an adhoc discussion between a particular set of users, not featuring any specific name or description; it is a chat of 'Group' type. If you add a person to the existing conversation, it creates a whole new conversation.                                      |

## list_glip_conversations_new

Returns the list of conversations where the user is a member. All records in response are sorted by creation time of a conversation in ascending order. Conversation is a chat of the _Group_ type.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/conversations`

**Parameters**

| Name         | Type | Required | Description                                                                                     |
| :----------- | :--- | :------- | :---------------------------------------------------------------------------------------------- |
| record_count | int  | ❌       | Number of conversations to be fetched by one request. The maximum value is 250, by default - 30 |
| page_token   | str  | ❌       | Pagination token.                                                                               |

**Return Type**

`TmConversationList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.conversations.list_glip_conversations_new(
    record_count=30,
    page_token="pageToken"
)

print(result)
```

## create_glip_conversation_new

Creates a new conversation or opens the existing one. If the conversation already exists, then its ID will be returned in response. A conversation is an adhoc discussion between a particular set of users, not featuring any specific name or description; it is a chat of 'Group' type. If you add a person to the existing conversation (group), it creates a whole new conversation.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/conversations`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [CreateConversationRequest](../models/CreateConversationRequest.md) | ✅       | The request body. |

**Return Type**

`TmConversationInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateConversationRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateConversationRequest(
    members=[
        {
            "id_": "id",
            "email": "email"
        }
    ]
)

result = sdk.conversations.create_glip_conversation_new(request_body=request_body)

print(result)
```

## read_glip_conversation_new

Returns information about the specified conversation, including the list of conversation participants. A conversation is an adhoc discussion between a particular set of users, not featuring any specific name or description; it is a chat of 'Group' type. If you add a person to the existing conversation, it creates a whole new conversation.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/conversations/{chatId}`

**Parameters**

| Name    | Type | Required | Description                                           |
| :------ | :--- | :------- | :---------------------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a conversation to be returned. |

**Return Type**

`TmConversationInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.conversations.read_glip_conversation_new(chat_id="chatId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
