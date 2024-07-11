# ExtensionCreationRequest

**Properties**

| Name               | Type                           | Required | Description                                                                                                                                                                                                                      |
| :----------------- | :----------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| contact            | ContactInfoCreationRequest     | ❌       | Contact Information                                                                                                                                                                                                              |
| extension_number   | str                            | ❌       | Extension short number                                                                                                                                                                                                           |
| cost_center        | CostCenterInfo                 | ❌       | Cost center information. Applicable if Cost Center feature is enabled. The default is `root` cost center value                                                                                                                   |
| custom_fields      | List[CustomFieldInfo]          | ❌       |                                                                                                                                                                                                                                  |
| password           | str                            | ❌       | Password for extension. If not specified, the password is auto-generated                                                                                                                                                         |
| references         | List[ReferenceInfo]            | ❌       | List of non-RC internal identifiers assigned to an extension                                                                                                                                                                     |
| regional_settings  | RegionalSettings               | ❌       | Regional data (timezone, home country, language) of an extension/account. The default is Company (Auto-Receptionist) settings                                                                                                    |
| partner_id         | str                            | ❌       | Additional extension identifier, created by partner application and applied on client side                                                                                                                                       |
| ivr_pin            | str                            | ❌       | IVR PIN                                                                                                                                                                                                                          |
| setup_wizard_state | SetupWizardStateForUpdateEnum  | ❌       | Initial configuration wizard state                                                                                                                                                                                               |
| site               | SiteInfo                       | ❌       |                                                                                                                                                                                                                                  |
| status             | ExtensionCreationRequestStatus | ❌       | Extension current state                                                                                                                                                                                                          |
| status_info        | ExtensionStatusInfo            | ❌       | Status information (reason, comment). Returned for 'Disabled' status only                                                                                                                                                        |
| type\_             | ExtensionCreationRequestType   | ❌       | Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                                                                             |
| hidden             | bool                           | ❌       | Hides extension from showing in company directory. Supported for extensions of 'User' type only. For unassigned extensions the value is set to `true` by default. For assigned extensions the value is set to `false` by default |

# ExtensionCreationRequestStatus

Extension current state

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| ENABLED      | str  | ✅       | "Enabled"      |
| DISABLED     | str  | ✅       | "Disabled"     |
| NOTACTIVATED | str  | ✅       | "NotActivated" |
| UNASSIGNED   | str  | ✅       | "Unassigned"   |
| FROZEN       | str  | ✅       | "Frozen"       |

# ExtensionCreationRequestType

Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology

**Properties**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| USER             | str  | ✅       | "User"             |
| VIRTUALUSER      | str  | ✅       | "VirtualUser"      |
| DIGITALUSER      | str  | ✅       | "DigitalUser"      |
| FLEXIBLEUSER     | str  | ✅       | "FlexibleUser"     |
| DEPARTMENT       | str  | ✅       | "Department"       |
| ANNOUNCEMENT     | str  | ✅       | "Announcement"     |
| VOICEMAIL        | str  | ✅       | "Voicemail"        |
| SHAREDLINESGROUP | str  | ✅       | "SharedLinesGroup" |
| PAGINGONLY       | str  | ✅       | "PagingOnly"       |
| PARKLOCATION     | str  | ✅       | "ParkLocation"     |
| LIMITED          | str  | ✅       | "Limited"          |

<!-- This file was generated by liblab | https://liblab.com/ -->
