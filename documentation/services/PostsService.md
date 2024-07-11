# PostsService

A list of all methods in the `PostsService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_glip_file_new](#create_glip_file_new) | Posts a file.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [read_glip_posts_new](#read_glip_posts_new)   | Returns a list of posts from the specified chat.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [create_glip_post_new](#create_glip_post_new) | Creates a post in the chat specified in path. Any mention can be added within the `text` attribute of the request body in .md format - `![:Type](id)`, where `type` is one of (Person, Team, File, Note, Task, Event, Link, Card) and `id` is a unique identifier of the mentioned object of the specified type. Attachments of the following types (File, Card, Event, Note) can also be added to a post by passing type and ID of attachment(s) in request body. |
| [read_glip_post_new](#read_glip_post_new)     | Returns information about the specified post.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [patch_glip_post_new](#patch_glip_post_new)   | Updates a specific post within a chat.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [delete_glip_post_new](#delete_glip_post_new) | Deletes the specified post from the chat.                                                                                                                                                                                                                                                                                                                                                                                                                          |

## create_glip_file_new

Posts a file.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/files`

**Parameters**

| Name         | Type                      | Required | Description                                                                       |
| :----------- | :------------------------ | :------- | :-------------------------------------------------------------------------------- |
| request_body | [dict](../models/dict.md) | ✅       | The request body.                                                                 |
| group_id     | int                       | ❌       | Internal identifier of a group to which the post with attachment will be added to |
| name         | str                       | ❌       | Name of a file attached                                                           |

**Return Type**

`TmAddFileRequest`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateGlipFileNewRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {
    "body": "body"
}

result = sdk.posts.create_glip_file_new(
    request_body=request_body,
    group_id=2,
    name="name"
)

print(result)
```

## read_glip_posts_new

Returns a list of posts from the specified chat.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/chats/{chatId}/posts`

**Parameters**

| Name         | Type | Required | Description                                                          |
| :----------- | :--- | :------- | :------------------------------------------------------------------- |
| chat_id      | str  | ✅       | Internal identifier of a chat                                        |
| record_count | int  | ❌       | Max number of posts to be fetched by one request (not more than 250) |
| page_token   | str  | ❌       | Pagination token.                                                    |

**Return Type**

`TmPostsList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posts.read_glip_posts_new(
    chat_id="chatId",
    record_count=30,
    page_token="pageToken"
)

print(result)
```

## create_glip_post_new

Creates a post in the chat specified in path. Any mention can be added within the `text` attribute of the request body in .md format - `![:Type](id)`, where `type` is one of (Person, Team, File, Note, Task, Event, Link, Card) and `id` is a unique identifier of the mentioned object of the specified type. Attachments of the following types (File, Card, Event, Note) can also be added to a post by passing type and ID of attachment(s) in request body.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/chats/{chatId}/posts`

**Parameters**

| Name         | Type                                                    | Required | Description                    |
| :----------- | :------------------------------------------------------ | :------- | :----------------------------- |
| request_body | [TmCreatePostRequest](../models/TmCreatePostRequest.md) | ✅       | The request body.              |
| chat_id      | str                                                     | ✅       | Internal identifier of a chat. |

**Return Type**

`TmPostInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmCreatePostRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmCreatePostRequest(
    text="text",
    attachments=[
        {
            "id_": "id",
            "type_": "File"
        }
    ]
)

result = sdk.posts.create_glip_post_new(
    request_body=request_body,
    chat_id="chatId"
)

print(result)
```

## read_glip_post_new

Returns information about the specified post.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/chats/{chatId}/posts/{postId}`

**Parameters**

| Name    | Type | Required | Description                   |
| :------ | :--- | :------- | :---------------------------- |
| chat_id | str  | ✅       | Internal identifier of a chat |
| post_id | str  | ✅       | Internal identifier of a post |

**Return Type**

`TmPostInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posts.read_glip_post_new(
    chat_id="chatId",
    post_id="postId"
)

print(result)
```

## patch_glip_post_new

Updates a specific post within a chat.

- HTTP Method: `PATCH`
- Endpoint: `/team-messaging/v1/chats/{chatId}/posts/{postId}`

**Parameters**

| Name         | Type                                                    | Required | Description                                 |
| :----------- | :------------------------------------------------------ | :------- | :------------------------------------------ |
| request_body | [TmUpdatePostRequest](../models/TmUpdatePostRequest.md) | ✅       | The request body.                           |
| chat_id      | str                                                     | ✅       | Internal identifier of a chat               |
| post_id      | str                                                     | ✅       | Internal identifier of a post to be updated |

**Return Type**

`TmPostInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TmUpdatePostRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TmUpdatePostRequest(
    text="text"
)

result = sdk.posts.patch_glip_post_new(
    request_body=request_body,
    chat_id="chatId",
    post_id="postId"
)

print(result)
```

## delete_glip_post_new

Deletes the specified post from the chat.

- HTTP Method: `DELETE`
- Endpoint: `/team-messaging/v1/chats/{chatId}/posts/{postId}`

**Parameters**

| Name    | Type | Required | Description                                 |
| :------ | :--- | :------- | :------------------------------------------ |
| chat_id | str  | ✅       | Internal identifier of a chat               |
| post_id | str  | ✅       | Internal identifier of a post to be deleted |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posts.delete_glip_post_new(
    chat_id="chatId",
    post_id="postId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
