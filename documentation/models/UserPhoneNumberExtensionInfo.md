# UserPhoneNumberExtensionInfo

Information on the extension, to which the phone number is assigned. Returned only for the request of Account phone number list

**Properties**

| Name                    | Type                             | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :---------------------- | :------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                    | int                              | ❌       | Internal identifier of an extension                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| uri                     | str                              | ❌       | Canonical URI of an extension                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| extension_number        | str                              | ❌       | Extension short number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| partner_id              | str                              | ❌       | For Partner Applications Internal identifier of an extension created by partner. The RingCentral supports the mapping of accounts and stores the corresponding account ID/extension ID for each partner ID of a client application. In request URIs partner IDs are accepted instead of regular RingCentral native IDs as path parameters using `pid=XXX` clause. Though in response URIs contain the corresponding account IDs and extension IDs. In all request and response bodies these values are reflected via partnerId attributes of account and extension |
| type\_                  | UserPhoneNumberExtensionInfoType | ❌       | Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology                                                                                                                                                                                                                                                                                                                                                                                                               |
| contact_center_provider | ContactCenterProvider            | ❌       | CCRN (Contact Center Routing Number) provider. If not specified then the default value 'InContact/North America' is used, its ID is '1'                                                                                                                                                                                                                                                                                                                                                                                                                            |
| name                    | str                              | ❌       | Extension name. For user extension types the value is a combination of the specified first name and last name                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

# UserPhoneNumberExtensionInfoType

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
| SITE                 | str  | ✅       | "Site"                 |

<!-- This file was generated by liblab | https://liblab.com/ -->
