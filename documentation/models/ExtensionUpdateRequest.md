# ExtensionUpdateRequest

**Properties**

| Name               | Type                            | Required | Description                                                                                                                                                              |
| :----------------- | :------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status             | ExtensionUpdateRequestStatus    | ❌       |                                                                                                                                                                          |
| status_info        | ExtensionStatusInfo             | ❌       | Status information (reason, comment). Returned for 'Disabled' status only                                                                                                |
| extension_number   | str                             | ❌       | Extension number available                                                                                                                                               |
| contact            | ContactInfoUpdateRequest        | ❌       |                                                                                                                                                                          |
| regional_settings  | ExtensionRegionalSettingRequest | ❌       |                                                                                                                                                                          |
| setup_wizard_state | SetupWizardStateForUpdateEnum   | ❌       | Initial configuration wizard state                                                                                                                                       |
| partner_id         | str                             | ❌       | Additional extension identifier, created by partner application and applied on client side                                                                               |
| ivr_pin            | str                             | ❌       | IVR PIN                                                                                                                                                                  |
| password           | str                             | ❌       | Password for extension                                                                                                                                                   |
| call_queue_info    | CallQueueInfoRequest            | ❌       | For Call Queue extension type only. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology |
| transition         | UserTransitionInfo              | ❌       | For NotActivated extensions only. Welcome email settings                                                                                                                 |
| custom_fields      | List[CustomFieldInfo]           | ❌       |                                                                                                                                                                          |
| site               | SiteReference                   | ❌       |                                                                                                                                                                          |
| type\_             | ExtensionUpdateRequestType      | ❌       | Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                     |
| sub_type           | ExtensionUpdateRequestSubType   | ❌       | Extension subtype, if applicable. For any unsupported subtypes the 'Unknown' value will be returned                                                                      |
| references         | List[ReferenceInfo]             | ❌       | List of non-RC internal identifiers assigned to an extension                                                                                                             |

# ExtensionUpdateRequestStatus

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| DISABLED     | str  | ✅       | "Disabled"     |
| ENABLED      | str  | ✅       | "Enabled"      |
| NOTACTIVATED | str  | ✅       | "NotActivated" |
| FROZEN       | str  | ✅       | "Frozen"       |

# ExtensionUpdateRequestType

Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology

**Properties**

| Name                 | Type | Required | Description            |
| :------------------- | :--- | :------- | :--------------------- |
| USER                 | str  | ✅       | "User"                 |
| FAXUSER              | str  | ✅       | "FaxUser"              |
| FLEXIBLEUSER         | str  | ✅       | "FlexibleUser"         |
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
| GROUPCALLPICKUP      | str  | ✅       | "GroupCallPickup"      |

# ExtensionUpdateRequestSubType

Extension subtype, if applicable. For any unsupported subtypes the 'Unknown' value will be returned

**Properties**

| Name                    | Type | Required | Description               |
| :---------------------- | :--- | :------- | :------------------------ |
| VIDEOPRO                | str  | ✅       | "VideoPro"                |
| VIDEOPROPLUS            | str  | ✅       | "VideoProPlus"            |
| DIGITALSIGNAGEONLYROOMS | str  | ✅       | "DigitalSignageOnlyRooms" |
| UNKNOWN                 | str  | ✅       | "Unknown"                 |
| EMERGENCY               | str  | ✅       | "Emergency"               |

<!-- This file was generated by liblab | https://liblab.com/ -->
