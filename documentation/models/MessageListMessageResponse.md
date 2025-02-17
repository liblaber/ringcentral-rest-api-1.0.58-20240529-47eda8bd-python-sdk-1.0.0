# MessageListMessageResponse

The short detail of the message in the get batch response

**Properties**

| Name               | Type             | Required | Description                                                                                                 |
| :----------------- | :--------------- | :------- | :---------------------------------------------------------------------------------------------------------- |
| id\_               | int              | ❌       | The Id of the message                                                                                       |
| batch_id           | str              | ❌       | Internal identifier of a batch the message was submitted in                                                 |
| from\_             | str              | ❌       | Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format from which the message is sent |
| to                 | List[str]        | ❌       | Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format to which a message is sent     |
| creation_time      | str              | ❌       | The time at which the message was created                                                                   |
| last_modified_time | str              | ❌       | The time at which the messages was last updated                                                             |
| message_status     | SmsStatusEnum    | ❌       | Current status of a message                                                                                 |
| segment_count      | int              | ❌       | Number of segments of a message                                                                             |
| text               | str              | ❌       | Text of a message. Returned if the `view` parameter is set to 'Detailed'                                    |
| cost               | float            | ❌       | Cost of a message                                                                                           |
| direction          | SmsDirectionEnum | ❌       | Direction of the SMS message                                                                                |
| error_code         | str              | ❌       | The RC error code of the message sending failure reason                                                     |

<!-- This file was generated by liblab | https://liblab.com/ -->
