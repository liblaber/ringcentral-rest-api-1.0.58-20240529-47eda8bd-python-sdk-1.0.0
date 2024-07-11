# ExtensionBulkUpdateInfo

**Properties**

| Name               | Type                            | Required | Description                                                                                                                                                                                                |
| :----------------- | :------------------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_               | str                             | ❌       | Internal identifier of an extension                                                                                                                                                                        |
| status             | ExtensionBulkUpdateInfoStatus   | ❌       |                                                                                                                                                                                                            |
| status_info        | ExtensionStatusInfo             | ❌       | Status information (reason, comment). Returned for 'Disabled' status only                                                                                                                                  |
| reason             | str                             | ❌       | Type of suspension                                                                                                                                                                                         |
| comment            | str                             | ❌       | Free form user comment                                                                                                                                                                                     |
| extension_number   | str                             | ❌       | Extension number available                                                                                                                                                                                 |
| contact            | ContactInfoUpdateRequest        | ❌       |                                                                                                                                                                                                            |
| regional_settings  | ExtensionRegionalSettingRequest | ❌       |                                                                                                                                                                                                            |
| setup_wizard_state | SetupWizardStateForUpdateEnum   | ❌       | Initial configuration wizard state                                                                                                                                                                         |
| partner_id         | str                             | ❌       | Additional extension identifier created by partner application and applied on client side                                                                                                                  |
| ivr_pin            | str                             | ❌       | IVR PIN                                                                                                                                                                                                    |
| password           | str                             | ❌       | Password for extension                                                                                                                                                                                     |
| call_queue_info    | CallQueueInfoRequest            | ❌       | For Call Queue extension type only. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                                   |
| transition         | UserTransitionInfo              | ❌       | For NotActivated extensions only. Welcome email settings                                                                                                                                                   |
| cost_center        | CostCenterInfo                  | ❌       | Cost center information. Applicable if Cost Center feature is enabled. The default is `root` cost center value                                                                                             |
| custom_fields      | List[CustomFieldInfo]           | ❌       |                                                                                                                                                                                                            |
| hidden             | bool                            | ❌       | Hides extension from showing in company directory. Supported for extensions of User type only                                                                                                              |
| site               | ProvisioningSiteInfo            | ❌       | Site data. If multi-site feature is turned on for an account, then ID of a site must be specified. In order to assign a wireless point to the main site (company) the site ID should be set to `main-site` |
| type\_             | ExtensionBulkUpdateInfoType     | ❌       | Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                                                       |
| references         | List[ReferenceInfo]             | ❌       | List of non-RC internal identifiers assigned to an extension                                                                                                                                               |

# ExtensionBulkUpdateInfoStatus

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| DISABLED     | str  | ✅       | "Disabled"     |
| ENABLED      | str  | ✅       | "Enabled"      |
| NOTACTIVATED | str  | ✅       | "NotActivated" |
| FROZEN       | str  | ✅       | "Frozen"       |

# ExtensionBulkUpdateInfoType

Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology

**Properties**

| Name                 | Type | Required | Description            |
| :------------------- | :--- | :------- | :--------------------- |
| USER                 | str  | ✅       | "User"                 |
| FAXUSER              | str  | ✅       | "FaxUser"              |
| VIRTUALUSER          | str  | ✅       | "VirtualUser"          |
| DIGITALUSER          | str  | ✅       | "DigitalUser"          |
| DEPARTMENT           | str  | ✅       | "Department"           |
| ANNOUNCEMENT         | str  | ✅       | "Announcement"         |
| VOICEMAIL            | str  | ✅       | "Voicemail"            |
| SHAREDLINESGROUP     | str  | ✅       | "SharedLinesGroup"     |
| PAGINGONLY           | str  | ✅       | "PagingOnly"           |
| IVRMENU              | str  | ✅       | "IvrMenu"              |
| APPLICATIONEXTENSION | str  | ✅       | "ApplicationExtension" |
| PARKLOCATION         | str  | ✅       | "ParkLocation"         |
| DELEGATEDLINESGROUP  | str  | ✅       | "DelegatedLinesGroup"  |

<!-- This file was generated by liblab | https://liblab.com/ -->
