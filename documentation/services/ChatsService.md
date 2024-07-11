# ChatsService

A list of all methods in the `ChatsService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [list_recent_chats_new](#list_recent_chats_new)       | Returns recent chats where the user is a member. All records in response are sorted by the `lastModifiedTime` in descending order (the latest changed chat is displayed first on page)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [list_glip_chats_new](#list_glip_chats_new)           | Returns the list of chats where the user is a member and also public teams that can be joined. All records in response are sorted by creation time of a chat in ascending order. **Chat types** There are multiple types of chats, including: _ **Personal** - each user is given a dedicated "personal chat" in which they are the only member. _ **Direct** - a chat between two individuals. _ **Group** - a chat between three or more named individuals. A "group" chat has no name. _ **Team** - a chat related to a specific topic. Members can come and go freely from this chat type. \* **Everyone** - a special chat containing every individual in a company. |
| [read_glip_chat_new](#read_glip_chat_new)             | Returns information about a chat by ID. **Note** 'Chat' is a general name for all types of threads including _Personal_ (user's own me-chat), _Direct_ (one on one chat), _Group_ (chat of 3-15 participants without specific name), _Team_ (chat of 2 and more participants, with a specific name), _Everyone_ (company chat including all employees, with a specific name)."                                                                                                                                                                                                                                                                                            |
| [unfavorite_glip_chat_new](#unfavorite_glip_chat_new) | Removes the specified chat from the users's list of favorite chats.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [favorite_glip_chat_new](#favorite_glip_chat_new)     | Adds the specified chat to the users's list of favorite chats.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [list_favorite_chats_new](#list_favorite_chats_new)   | Returns a list of the current user's favorite chats.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## list_recent_chats_new

Returns recent chats where the user is a member. All records in response are sorted by the `lastModifiedTime` in descending order (the latest changed chat is displayed first on page)

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/recent/chats`

**Parameters**

| Name         | Type                                                                | Required | Description                                                           |
| :----------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------- |
| type\_       | [List[ListRecentChatsNewType]](../models/ListRecentChatsNewType.md) | ❌       | Type of chats to be fetched. By default, all chat types are returned  |
| record_count | int                                                                 | ❌       | Max number of chats to be fetched by one request (Not more than 250). |

**Return Type**

`TmChatListWithoutNavigation`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
type_=[
    "Everyone"
]

result = sdk.chats.list_recent_chats_new(
    type_=type_,
    record_count=30
)

print(result)
```

## list_glip_chats_new

Returns the list of chats where the user is a member and also public teams that can be joined. All records in response are sorted by creation time of a chat in ascending order. **Chat types** There are multiple types of chats, including: _ **Personal** - each user is given a dedicated "personal chat" in which they are the only member. _ **Direct** - a chat between two individuals. _ **Group** - a chat between three or more named individuals. A "group" chat has no name. _ **Team** - a chat related to a specific topic. Members can come and go freely from this chat type. \* **Everyone** - a special chat containing every individual in a company.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/chats`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                              |
| :----------- | :-------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------- |
| type\_       | [List[ListGlipChatsNewType]](../models/ListGlipChatsNewType.md) | ❌       | Type of chats to be fetched. By default, all type of chats will be fetched               |
| record_count | int                                                             | ❌       | Number of chats to be fetched by one request. The maximum value is 250, by default - 30. |
| page_token   | str                                                             | ❌       | Pagination token.                                                                        |

**Return Type**

`TmChatList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
type_=[
    "Personal"
]

result = sdk.chats.list_glip_chats_new(
    type_=type_,
    record_count=30,
    page_token="pageToken"
)

print(result)
```

## read_glip_chat_new

Returns information about a chat by ID. **Note** 'Chat' is a general name for all types of threads including _Personal_ (user's own me-chat), _Direct_ (one on one chat), _Group_ (chat of 3-15 participants without specific name), _Team_ (chat of 2 and more participants, with a specific name), _Everyone_ (company chat including all employees, with a specific name)."

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/chats/{chatId}`

**Parameters**

| Name    | Type | Required | Description                                                                                           |
| :------ | :--- | :------- | :---------------------------------------------------------------------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a chat. If tilde (~) is specified, then `/me` (Personal) chat will be returned |

**Return Type**

`TmChatInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.chats.read_glip_chat_new(chat_id="chatId")

print(result)
```

## unfavorite_glip_chat_new

Removes the specified chat from the users's list of favorite chats.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/chats/{chatId}/unfavorite`

**Parameters**

| Name    | Type | Required | Description                                                 |
| :------ | :--- | :------- | :---------------------------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a chat to remove from favorite list. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.chats.unfavorite_glip_chat_new(chat_id="chatId")

print(result)
```

## favorite_glip_chat_new

Adds the specified chat to the users's list of favorite chats.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/chats/{chatId}/favorite`

**Parameters**

| Name    | Type | Required | Description                                            |
| :------ | :--- | :------- | :----------------------------------------------------- |
| chat_id | str  | ✅       | Internal identifier of a chat to add to favorite list. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.chats.favorite_glip_chat_new(chat_id="chatId")

print(result)
```

## list_favorite_chats_new

Returns a list of the current user's favorite chats.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/favorites`

**Parameters**

| Name         | Type | Required | Description                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------- |
| record_count | int  | ❌       | Max number of chats to be fetched by one request (Not more than 250). |

**Return Type**

`TmChatListWithoutNavigation`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.chats.list_favorite_chats_new(record_count=30)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
