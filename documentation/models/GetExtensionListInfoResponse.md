# GetExtensionListInfoResponse

**Properties**

| Name             | Type                                | Required | Description                                                                                                                                                                                                |
| :--------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_             | int                                 | ❌       | Internal identifier of an extension                                                                                                                                                                        |
| uri              | str                                 | ❌       | Canonical URI of an extension                                                                                                                                                                              |
| contact          | ContactInfo                         | ❌       | Detailed contact information                                                                                                                                                                               |
| extension_number | str                                 | ❌       | Extension short number                                                                                                                                                                                     |
| name             | str                                 | ❌       | Extension name. For user extension types the value is a combination of the specified first name and last name                                                                                              |
| permissions      | ExtensionPermissions                | ❌       | Extension permissions, corresponding to the Service Web permissions 'Admin' and 'InternationalCalling'                                                                                                     |
| profile_image    | ProfileImageInfo                    | ❌       | Information on profile image                                                                                                                                                                               |
| status           | GetExtensionListInfoResponseStatus  | ❌       | Extension current state. If 'Unassigned' is specified, then extensions without `extensionNumber` are returned. If not specified, then all extensions are returned                                          |
| type\_           | GetExtensionListInfoResponseType    | ❌       | Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                                                       |
| sub_type         | GetExtensionListInfoResponseSubType | ❌       | Extension subtype, if applicable. For any unsupported subtypes the `Unknown` value will be returned                                                                                                        |
| call_queue_info  | CallQueueExtensionInfo              | ❌       | For Call Queue extension type only. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                                   |
| hidden           | bool                                | ❌       | Hides extension from showing in company directory. Supported for extensions of User type only                                                                                                              |
| site             | ProvisioningSiteInfo                | ❌       | Site data. If multi-site feature is turned on for an account, then ID of a site must be specified. In order to assign a wireless point to the main site (company) the site ID should be set to `main-site` |
| assigned_country | AssignedCountryInfo                 | ❌       | Information on a country assigned to an extension user. Returned for the User extension type only                                                                                                          |
| cost_center      | CostCenterInfo                      | ❌       | Cost center information. Applicable if Cost Center feature is enabled. The default is `root` cost center value                                                                                             |

# GetExtensionListInfoResponseStatus

Extension current state. If 'Unassigned' is specified, then extensions without `extensionNumber` are returned. If not specified, then all extensions are returned

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| ENABLED      | str  | ✅       | "Enabled"      |
| DISABLED     | str  | ✅       | "Disabled"     |
| FROZEN       | str  | ✅       | "Frozen"       |
| NOTACTIVATED | str  | ✅       | "NotActivated" |
| UNASSIGNED   | str  | ✅       | "Unassigned"   |

# GetExtensionListInfoResponseType

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
| BOT                  | str  | ✅       | "Bot"                  |
| ROOM                 | str  | ✅       | "Room"                 |
| LIMITED              | str  | ✅       | "Limited"              |
| SITE                 | str  | ✅       | "Site"                 |
| PROXYADMIN           | str  | ✅       | "ProxyAdmin"           |
| DELEGATEDLINESGROUP  | str  | ✅       | "DelegatedLinesGroup"  |
| GROUPCALLPICKUP      | str  | ✅       | "GroupCallPickup"      |

# GetExtensionListInfoResponseSubType

Extension subtype, if applicable. For any unsupported subtypes the `Unknown` value will be returned

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| VIDEOPRO       | str  | ✅       | "VideoPro"       |
| VIDEOPROPLUS   | str  | ✅       | "VideoProPlus"   |
| DIGITALSIGNAGE | str  | ✅       | "DigitalSignage" |
| UNKNOWN        | str  | ✅       | "Unknown"        |
| EMERGENCY      | str  | ✅       | "Emergency"      |

<!-- This file was generated by liblab | https://liblab.com/ -->
