# MessageDetailsResponse

Complete details of the message

**Properties**

| Name               | Type             | Required | Description                                                                                                         |
| :----------------- | :--------------- | :------- | :------------------------------------------------------------------------------------------------------------------ |
| id\_               | str              | ❌       | Internal identifier of a message                                                                                    |
| from\_             | str              | ❌       | Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format from which the message was sent        |
| to                 | List[str]        | ❌       | List of phone numbers in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format to which the message was sent |
| text               | str              | ❌       | Text of a message, maximum number of characters is 1000                                                             |
| creation_time      | str              | ❌       | The time when this is message was created.                                                                          |
| last_modified_time | str              | ❌       | The time when this message was last updated.                                                                        |
| message_status     | SmsStatusEnum    | ❌       | Current status of a message                                                                                         |
| segment_count      | int              | ❌       | Number of segments of a message                                                                                     |
| cost               | float            | ❌       | Cost of a message                                                                                                   |
| batch_id           | str              | ❌       | The batch in which the message was submitted                                                                        |
| direction          | SmsDirectionEnum | ❌       | Direction of the SMS message                                                                                        |
| error_code         | str              | ❌       | The RC error code of the message sending failure reason                                                             |

<!-- This file was generated by liblab | https://liblab.com/ -->
