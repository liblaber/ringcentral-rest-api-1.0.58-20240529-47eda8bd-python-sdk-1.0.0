# AdaptiveCardsService

A list of all methods in the `AdaptiveCardsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                |
| :-------------------------------------------------------------- | :--------------------------------------------------------- |
| [create_glip_adaptive_card_new](#create_glip_adaptive_card_new) | Creates a new adaptive card in the chat specified in path. |
| [get_glip_adaptive_card_new](#get_glip_adaptive_card_new)       | Returns adaptive card(s) with given id(s).                 |
| [update_glip_adaptive_card_new](#update_glip_adaptive_card_new) | Updates an adaptive card.                                  |
| [delete_glip_adaptive_card_new](#delete_glip_adaptive_card_new) | Deletes an adaptive card by ID.                            |

## create_glip_adaptive_card_new

Creates a new adaptive card in the chat specified in path.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/chats/{chatId}/adaptive-cards`

**Parameters**

| Name         | Type                                                    | Required | Description                   |
| :----------- | :------------------------------------------------------ | :------- | :---------------------------- |
| request_body | [AdaptiveCardRequest](../models/AdaptiveCardRequest.md) | ✅       | The request body.             |
| chat_id      | str                                                     | ✅       | Internal identifier of a chat |

**Return Type**

`AdaptiveCardShortInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AdaptiveCardRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AdaptiveCardRequest(
    type_="AdaptiveCard",
    version="version",
    body=[
        {
            "type_": "Container",
            "items": [
                {
                    "type_": "TextBlock",
                    "text": "text",
                    "weight": "weight",
                    "size": "size",
                    "columns": [
                        {
                            "type_": "type",
                            "width": "width",
                            "items": [
                                {
                                    "type_": "type",
                                    "url": "url",
                                    "size": "size",
                                    "style": "style",
                                    "wrap": True,
                                    "spacing": "spacing",
                                    "text": "text",
                                    "is_subtle": True
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    actions=[
        {
            "type_": "Action.ShowCard",
            "title": "title",
            "card": {
                "type_": "AdaptiveCard",
                "body": [
                    {
                        "type_": "Input.Text",
                        "id_": "id",
                        "is_multiline": False,
                        "placeholder": "placeholder"
                    }
                ]
            },
            "url": "url"
        }
    ],
    select_action={
        "type_": "Action.Submit"
    },
    fallback_text="fallbackText",
    background_image="mollit sint",
    min_height="50px",
    speak="speak",
    lang="en",
    vertical_content_alignment="top"
)

result = sdk.adaptive_cards.create_glip_adaptive_card_new(
    request_body=request_body,
    chat_id="chatId"
)

print(result)
```

## get_glip_adaptive_card_new

Returns adaptive card(s) with given id(s).

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/adaptive-cards/{cardId}`

**Parameters**

| Name    | Type      | Required | Description                                                                             |
| :------ | :-------- | :------- | :-------------------------------------------------------------------------------------- |
| card_id | List[str] | ✅       | Internal identifier of an adaptive card, or comma separated list of adaptive cards IDs. |

**Return Type**

`AdaptiveCardInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
card_id=[
    "cardId"
]

result = sdk.adaptive_cards.get_glip_adaptive_card_new(card_id=card_id)

print(result)
```

## update_glip_adaptive_card_new

Updates an adaptive card.

- HTTP Method: `PUT`
- Endpoint: `/team-messaging/v1/adaptive-cards/{cardId}`

**Parameters**

| Name         | Type                                                    | Required | Description                             |
| :----------- | :------------------------------------------------------ | :------- | :-------------------------------------- |
| request_body | [AdaptiveCardRequest](../models/AdaptiveCardRequest.md) | ✅       | The request body.                       |
| card_id      | str                                                     | ✅       | Internal identifier of an adaptive card |

**Return Type**

`AdaptiveCardShortInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AdaptiveCardRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AdaptiveCardRequest(
    type_="AdaptiveCard",
    version="version",
    body=[
        {
            "type_": "Container",
            "items": [
                {
                    "type_": "TextBlock",
                    "text": "text",
                    "weight": "weight",
                    "size": "size",
                    "columns": [
                        {
                            "type_": "type",
                            "width": "width",
                            "items": [
                                {
                                    "type_": "type",
                                    "url": "url",
                                    "size": "size",
                                    "style": "style",
                                    "wrap": True,
                                    "spacing": "spacing",
                                    "text": "text",
                                    "is_subtle": True
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ],
    actions=[
        {
            "type_": "Action.ShowCard",
            "title": "title",
            "card": {
                "type_": "AdaptiveCard",
                "body": [
                    {
                        "type_": "Input.Text",
                        "id_": "id",
                        "is_multiline": False,
                        "placeholder": "placeholder"
                    }
                ]
            },
            "url": "url"
        }
    ],
    select_action={
        "type_": "Action.Submit"
    },
    fallback_text="fallbackText",
    background_image="mollit sint",
    min_height="50px",
    speak="speak",
    lang="en",
    vertical_content_alignment="top"
)

result = sdk.adaptive_cards.update_glip_adaptive_card_new(
    request_body=request_body,
    card_id="cardId"
)

print(result)
```

## delete_glip_adaptive_card_new

Deletes an adaptive card by ID.

- HTTP Method: `DELETE`
- Endpoint: `/team-messaging/v1/adaptive-cards/{cardId}`

**Parameters**

| Name    | Type | Required | Description                     |
| :------ | :--- | :------- | :------------------------------ |
| card_id | str  | ✅       | Adaptive Card ID to be deleted. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.adaptive_cards.delete_glip_adaptive_card_new(card_id="cardId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
