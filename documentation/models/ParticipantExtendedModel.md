# ParticipantExtendedModel

**Properties**

| Name             | Type                         | Required | Description                                                                                                                                                                                        |
| :--------------- | :--------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| role             | RcwRoleEnum                  | ✅       | The role of the webinar session participant/invitee. See also: [Understanding Webinar Roles](https://support.ringcentral.com/webinar/getting-started/understanding-ringcentral-webinar-roles.html) |
| original_role    | RcwRoleEnum                  | ✅       | The role of the webinar session participant/invitee. See also: [Understanding Webinar Roles](https://support.ringcentral.com/webinar/getting-started/understanding-ringcentral-webinar-roles.html) |
| type\_           | ParticipantExtendedModelType | ✅       | The type of the participant specified in invite or determined at join time                                                                                                                         |
| id\_             | str                          | ❌       | Internal object ID                                                                                                                                                                                 |
| first_name       | str                          | ❌       | First (given) name                                                                                                                                                                                 |
| last_name        | str                          | ❌       | Last (family) name                                                                                                                                                                                 |
| linked_user      | RcwDomainUserModel           | ❌       |                                                                                                                                                                                                    |
| avatar_token     | str                          | ❌       | A token to access avatar image from CDN. Available only for authenticated panelists                                                                                                                |
| email            | str                          | ❌       | User's contact email                                                                                                                                                                               |
| qna_blocked      | bool                         | ❌       | Boolean to indicate if the participant was blocked from Q&A                                                                                                                                        |
| join_time        | str                          | ❌       | The time (earliest) when this participant joined the session                                                                                                                                       |
| leave_time       | str                          | ❌       | The time (latest) when this participant left the session                                                                                                                                           |
| was_ejected      | bool                         | ❌       | Indicates if this participant was ejected from the webinar                                                                                                                                         |
| invitee_id       | str                          | ❌       | For invited participants - Invitee ID (matches Configuration API Invitee IDs)                                                                                                                      |
| registrant_id    | str                          | ❌       | Registrant ID                                                                                                                                                                                      |
| unique_user_hash | str                          | ❌       | The hash string which is unique for each unique user                                                                                                                                               |

# ParticipantExtendedModelType

The type of the participant specified in invite or determined at join time

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| USER | str  | ✅       | "User"      |
| ROOM | str  | ✅       | "Room"      |

<!-- This file was generated by liblab | https://liblab.com/ -->
