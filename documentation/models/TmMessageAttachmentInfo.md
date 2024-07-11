# TmMessageAttachmentInfo

**Properties**

| Name          | Type                         | Required | Description                                                                                                                       |
| :------------ | :--------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| id\_          | str                          | ❌       | Internal identifier of an attachment                                                                                              |
| type\_        | TmMessageAttachmentInfoType  | ❌       | Type of an attachment                                                                                                             |
| fallback      | str                          | ❌       | A string of default text that will be rendered in the case that the client does not support Interactive Messages                  |
| intro         | str                          | ❌       | A pretext to the message                                                                                                          |
| author        | TmAttachmentAuthorInfo       | ❌       |                                                                                                                                   |
| title         | str                          | ❌       | Message title                                                                                                                     |
| text          | str                          | ❌       | A large string field (up to 1000 chars) to be displayed as the body of a message (Supports GlipDown)                              |
| image_uri     | str                          | ❌       | Link to an image displayed at the bottom of a message                                                                             |
| thumbnail_uri | str                          | ❌       | Link to an image preview displayed to the right of a message (82x82)                                                              |
| fields        | List[TmAttachmentFieldsInfo] | ❌       | Information on navigation                                                                                                         |
| footnote      | TmAttachmentFootnoteInfo     | ❌       |                                                                                                                                   |
| creator_id    | str                          | ❌       | Internal identifier of a person created an event                                                                                  |
| start_time    | str                          | ❌       | Datetime of starting an event                                                                                                     |
| end_time      | str                          | ❌       | Datetime of ending an event                                                                                                       |
| all_day       | bool                         | ❌       | Indicates whether an event has some specific time slot or lasts for the whole day(s)                                              |
| recurrence    | EventRecurrenceInfo          | ❌       |                                                                                                                                   |
| color         | TmMessageAttachmentInfoColor | ❌       | Color of Event title, including its presentation in Calendar; or the color of the side border of an interactive message of a Card |
| location      | str                          | ❌       | Event location                                                                                                                    |
| description   | str                          | ❌       | Event details                                                                                                                     |

# TmMessageAttachmentInfoType

Type of an attachment

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| CARD  | str  | ✅       | "Card"      |
| EVENT | str  | ✅       | "Event"     |
| FILE  | str  | ✅       | "File"      |
| NOTE  | str  | ✅       | "Note"      |
| TASK  | str  | ✅       | "Task"      |

# TmMessageAttachmentInfoColor

Color of Event title, including its presentation in Calendar; or the color of the side border of an interactive message of a Card

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| BLACK   | str  | ✅       | "Black"     |
| RED     | str  | ✅       | "Red"       |
| ORANGE  | str  | ✅       | "Orange"    |
| YELLOW  | str  | ✅       | "Yellow"    |
| GREEN   | str  | ✅       | "Green"     |
| BLUE    | str  | ✅       | "Blue"      |
| PURPLE  | str  | ✅       | "Purple"    |
| MAGENTA | str  | ✅       | "Magenta"   |

<!-- This file was generated by liblab | https://liblab.com/ -->
