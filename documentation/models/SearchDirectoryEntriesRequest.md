# SearchDirectoryEntriesRequest

**Properties**

| Name                     | Type                               | Required | Description                                                                                                                                                                                                                                     |
| :----------------------- | :--------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| search_string            | str                                | ❌       | String value to filter the contacts. The value specified is searched through the following fields: `firstName`, `lastName`, `extensionNumber`, `phoneNumber`, `email`, `jobTitle`, `department`, `customFieldValue`                             |
| search_fields            | List[SearchFields]                 | ❌       | The list of field to be searched for                                                                                                                                                                                                            |
| show_federated           | bool                               | ❌       | If `true` then contacts of all accounts in federation are returned, if it is in federation, account section will be returned. If `false` then only contacts of the current account are returned, and account section is eliminated in this case |
| show_admin_only_contacts | bool                               | ❌       | Should show AdminOnly Contacts                                                                                                                                                                                                                  |
| extension_type           | SearchDirectoryContactType         | ❌       | Type of directory contact to filter                                                                                                                                                                                                             |
| site_id                  | str                                | ❌       | Internal identifier of the business site to which extensions belong                                                                                                                                                                             |
| show_external_contacts   | bool                               | ❌       | Allows to control whether External (Hybrid) contacts should be returned in the response or not                                                                                                                                                  |
| account_ids              | List[str]                          | ❌       | The list of Internal identifiers of an accounts                                                                                                                                                                                                 |
| department               | str                                | ❌       | Department                                                                                                                                                                                                                                      |
| site_ids                 | List[str]                          | ❌       | The list of Internal identifiers of the business sites to which extensions belong                                                                                                                                                               |
| extension_statuses       | List[ExtensionStatuses]            | ❌       | Extension current state.                                                                                                                                                                                                                        |
| extension_types          | List[SearchDirectoryExtensionType] | ❌       | Types of extension to filter the contacts                                                                                                                                                                                                       |
| order_by                 | List[OrderBy]                      | ❌       | Sorting settings                                                                                                                                                                                                                                |
| page                     | int                                | ❌       |                                                                                                                                                                                                                                                 |
| per_page                 | int                                | ❌       |                                                                                                                                                                                                                                                 |

# SearchFields

**Properties**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| FIRSTNAME        | str  | ✅       | "firstName"        |
| LASTNAME         | str  | ✅       | "lastName"         |
| EXTENSIONNUMBER  | str  | ✅       | "extensionNumber"  |
| PHONENUMBER      | str  | ✅       | "phoneNumber"      |
| EMAIL            | str  | ✅       | "email"            |
| JOBTITLE         | str  | ✅       | "jobTitle"         |
| DEPARTMENT       | str  | ✅       | "department"       |
| CUSTOMFIELDVALUE | str  | ✅       | "customFieldValue" |

# ExtensionStatuses

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| ENABLED      | str  | ✅       | "Enabled"      |
| DISABLED     | str  | ✅       | "Disabled"     |
| NOTACTIVATED | str  | ✅       | "NotActivated" |

<!-- This file was generated by liblab | https://liblab.com/ -->
