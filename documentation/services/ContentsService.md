# ContentsService

A list of all methods in the `ContentsService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [soc_msg_list_contents](#soc_msg_list_contents)   | List contents by creation date. The default creation order is descending. The account context of this request is determined by the RC Account Id associated with the access token provided in the Authorization header. The query parameters provided shall be considered an AND operation to filter the list. A query parameter not specified or a query parameter provided with no value is treated as not required for filtering the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [soc_msg_create_content](#soc_msg_create_content) | Creates new content for use in discussions. This request is used to reply to already-posted content or to initiate a discussion. If authorized, the authenticated user will be used as the content author. Content will be created and pushed asynchronously to the channel. When the content is successfully pushed to the channel, the Content.Exported event will be reported. The account context of this request is determined by the RC Account Id associated with the access token provided in the Authorization header. Replying to customer content is usually possible unless the channel or conversation is read only. Composing content, on the contrary, depends on the channel itself. _ The channel may not support it (and be purely reactive like Instagram, Messenger, etc.). _ Some channels (usually public accounts like Twitter or Facebook pages) allow for the publishing of content without targeting specific individuals. \* Some channels (usually non-public media) require specific targeting (phone number for SMS, email address for email, customer_id, etc.) to be able to create content. This is channel-specific and detailed under the generic parameters. |
| [soc_msg_get_content](#soc_msg_get_content)       | Retrieves the content from the given id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## soc_msg_list_contents

List contents by creation date. The default creation order is descending. The account context of this request is determined by the RC Account Id associated with the access token provided in the Authorization header. The query parameters provided shall be considered an AND operation to filter the list. A query parameter not specified or a query parameter provided with no value is treated as not required for filtering the list.

- HTTP Method: `GET`
- Endpoint: `/cx/social-messaging/v1/contents`

**Parameters**

| Name           | Type                                                            | Required | Description                                                                                                             |
| :------------- | :-------------------------------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| intervention   | List[str]                                                       | ❌       | Filter based on the specified intervention identifiers.                                                                 |
| identity       | List[str]                                                       | ❌       | Filter based on the specified identity identifiers.                                                                     |
| identity_group | List[str]                                                       | ❌       | Filter based on the specified identity group identifiers.                                                               |
| source         | List[str]                                                       | ❌       | Filter based on the specified channel identifiers.                                                                      |
| thread         | List[str]                                                       | ❌       | Filter based on the specified thread identifiers.                                                                       |
| text           | List[str]                                                       | ❌       | Filter based on the specified text(s). Provided multiple times, the values are ANDed.                                   |
| status         | [List[ContentStatus]](../models/ContentStatus.md)               | ❌       | Filter for specified status.                                                                                            |
| order_by       | [SocMsgCreationTimeOrder](../models/SocMsgCreationTimeOrder.md) | ❌       | Order results by specified field.                                                                                       |
| page_token     | str                                                             | ❌       | The token indicating the particular page of the result set to be retrieved. If omitted the first page will be returned. |
| per_page       | int                                                             | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied  |

**Return Type**

`ContentList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SocMsgCreationTimeOrder

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
intervention=[
    "intervention"
]
identity=[
    "identity"
]
identity_group=[
    "identityGroup"
]
source=[
    "source"
]
thread=[
    "thread"
]
text=[
    "text"
]
status=[
    "New"
]

result = sdk.contents.soc_msg_list_contents(
    intervention=intervention,
    identity=identity,
    identity_group=identity_group,
    source=source,
    thread=thread,
    text=text,
    status=status,
    order_by="-creationTime",
    page_token="pageToken",
    per_page=100
)

print(result)
```

## soc_msg_create_content

Creates new content for use in discussions. This request is used to reply to already-posted content or to initiate a discussion. If authorized, the authenticated user will be used as the content author. Content will be created and pushed asynchronously to the channel. When the content is successfully pushed to the channel, the Content.Exported event will be reported. The account context of this request is determined by the RC Account Id associated with the access token provided in the Authorization header. Replying to customer content is usually possible unless the channel or conversation is read only. Composing content, on the contrary, depends on the channel itself. _ The channel may not support it (and be purely reactive like Instagram, Messenger, etc.). _ Some channels (usually public accounts like Twitter or Facebook pages) allow for the publishing of content without targeting specific individuals. \* Some channels (usually non-public media) require specific targeting (phone number for SMS, email address for email, customer_id, etc.) to be able to create content. This is channel-specific and detailed under the generic parameters.

- HTTP Method: `POST`
- Endpoint: `/cx/social-messaging/v1/contents`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateContentRequest](../models/CreateContentRequest.md) | ✅       | The request body. |

**Return Type**

`ContentModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateContentRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateContentRequest(
    author_identity_id="541014e17aa58d8ccf000023",
    body="Body of the content",
    in_reply_to_content_id="123414e17asdd8ccf000023",
    public=True,
    source_id="fff415437asdd8ccf000023",
    attachment_ids=[
        "506d9e817aa58d1259000f12"
    ],
    title="An email title",
    to=[
        "+33634231224"
    ],
    cc=[
        "user@example.com"
    ],
    bcc=[
        "user@example.com"
    ],
    template_name="customer_order_shipment_template",
    template_language="fr",
    components=[
        {
            "type_": "type",
            "parameters": [
                {
                    "type_": "type",
                    "text": "text"
                }
            ]
        }
    ],
    context_data={},
    auto_submitted=False
)

result = sdk.contents.soc_msg_create_content(request_body=request_body)

print(result)
```

## soc_msg_get_content

Retrieves the content from the given id.

- HTTP Method: `GET`
- Endpoint: `/cx/social-messaging/v1/contents/{contentId}`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| content_id | str  | ✅       |             |

**Return Type**

`ContentModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contents.soc_msg_get_content(content_id="contentId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
