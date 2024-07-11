# AdaptiveCardInfo

**Properties**

| Name                       | Type                            | Required | Description                                                                                                                                            |
| :------------------------- | :------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                       | str                             | ❌       | Internal identifier of an adaptive card                                                                                                                |
| creation_time              | str                             | ❌       | Adaptive Card creation datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format                                                           |
| last_modified_time         | str                             | ❌       | Post last modification datetime in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format                                                           |
| schema                     | str                             | ❌       | Schema of an adaptive card                                                                                                                             |
| type\_                     | AdaptiveCardInfoType            | ❌       |                                                                                                                                                        |
| version                    | str                             | ❌       | Version of an adaptive card                                                                                                                            |
| creator                    | AdaptiveCardCreator             | ❌       |                                                                                                                                                        |
| chat_ids                   | List[str]                       | ❌       | Chat IDs where an adaptive card is posted or shared.                                                                                                   |
| body                       | List[AdaptiveCardInfoRequest]   | ❌       | List of card elements to show in the primary card region                                                                                               |
| actions                    | List[AdaptiveCardAction]        | ❌       |                                                                                                                                                        |
| select_action              | AdaptiveCardSelectAction        | ❌       | An action that will be invoked when the card is tapped or selected. `Action.ShowCard` is not supported                                                 |
| fallback_text              | str                             | ❌       | Text shown when the client doesn't support the version specified (may contain markdown)                                                                |
| background_image           | AdaptiveCardInfoBackgroundImage | ❌       | Specifies the background image of a card                                                                                                               |
| min_height                 | str                             | ❌       | Specifies the minimum height of the card in pixels                                                                                                     |
| speak                      | str                             | ❌       | Specifies what should be spoken for this entire card. This is simple text or SSML fragment                                                             |
| lang                       | AdaptiveCardInfoLang            | ❌       | The 2-letter ISO-639-1 language used in the card. Used to localize any date/time functions                                                             |
| vertical_content_alignment | VerticalContentAlignment        | ❌       | Defines how the content should be aligned vertically within the container. Only relevant for fixed-height cards, or cards with a `minHeight` specified |

# AdaptiveCardInfoType

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| ADAPTIVECARD | str  | ✅       | "AdaptiveCard" |

# AdaptiveCardInfoBackgroundImage

Specifies the background image of a card

# AdaptiveCardInfoLang

The 2-letter ISO-639-1 language used in the card. Used to localize any date/time functions

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| EN   | str  | ✅       | "en"        |
| FR   | str  | ✅       | "fr"        |
| ES   | str  | ✅       | "es"        |

<!-- This file was generated by liblab | https://liblab.com/ -->
