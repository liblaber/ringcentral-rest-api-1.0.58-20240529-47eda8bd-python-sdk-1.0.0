# EmailRecipientInfo

**Properties**

| Name             | Type                     | Required | Description                                                                                                                            |
| :--------------- | :----------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| extension_id     | str                      | ❌       | Internal identifier of an extension                                                                                                    |
| full_name        | str                      | ❌       | User full name                                                                                                                         |
| extension_number | str                      | ❌       | User extension number                                                                                                                  |
| status           | EmailRecipientInfoStatus | ❌       | Current state of an extension                                                                                                          |
| email_addresses  | List[str]                | ❌       | List of user email addresses from extension notification settings. By default, main email address from contact information is returned |
| permission       | Permission               | ❌       | Call queue manager permission                                                                                                          |

# EmailRecipientInfoStatus

Current state of an extension

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| ENABLED      | str  | ✅       | "Enabled"      |
| DISABLE      | str  | ✅       | "Disable"      |
| NOTACTIVATED | str  | ✅       | "NotActivated" |
| UNASSIGNED   | str  | ✅       | "Unassigned"   |

# Permission

Call queue manager permission

**Properties**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| FULLACCESS       | str  | ✅       | "FullAccess"       |
| MESSAGES         | str  | ✅       | "Messages"         |
| MEMBERMANAGEMENT | str  | ✅       | "MemberManagement" |

<!-- This file was generated by liblab | https://liblab.com/ -->
