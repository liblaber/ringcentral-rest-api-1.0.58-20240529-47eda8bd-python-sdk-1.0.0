# UserPhoneNumberInfo

**Properties**

| Name                    | Type                              | Required | Description                                                                                                                                                 |
| :---------------------- | :-------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uri                     | str                               | ❌       | Link to the user phone number resource                                                                                                                      |
| id\_                    | int                               | ❌       | Internal identifier of a phone number                                                                                                                       |
| country                 | CountryInfoBasicModel             | ❌       |                                                                                                                                                             |
| contact_center_provider | ContactCenterProvider             | ❌       | CCRN (Contact Center Routing Number) provider. If not specified then the default value 'InContact/North America' is used, its ID is '1'                     |
| extension               | UserPhoneNumberExtensionInfo      | ❌       | Information on the extension, to which the phone number is assigned. Returned only for the request of Account phone number list                             |
| label                   | str                               | ❌       | Custom user-defined name of a phone number, if any                                                                                                          |
| location                | str                               | ❌       | Location (City, State). Filled for local US numbers                                                                                                         |
| payment_type            | PlatformPaymentType               | ❌       | Payment type. 'External' is returned for forwarded numbers which are not terminated in the RingCentral phone system                                         |
| phone_number            | str                               | ❌       | Phone number                                                                                                                                                |
| primary                 | bool                              | ❌       | Indicates if a phone number is primary, i.e. displayed as 'main number' and called by default                                                               |
| status                  | UserPhoneNumberInfoStatus         | ❌       | Status of a phone number. If the value is 'Normal', the phone number is ready to be used. Otherwise, it is an external number not yet ported to RingCentral |
| type\_                  | UserPhoneNumberInfoType           | ❌       | Phone number type                                                                                                                                           |
| sub_type                | UserPhoneNumberInfoSubType        | ❌       | Extension subtype, if applicable. For any unsupported subtypes the 'Unknown' value will be returned                                                         |
| usage_type              | UserPhoneNumberInfoUsageType      | ❌       | Usage type of phone number. Numbers of 'NumberPool' type will not be returned for phone number list requests                                                |
| features                | List[UserPhoneNumberInfoFeatures] | ❌       | List of features of a phone number                                                                                                                          |

# UserPhoneNumberInfoStatus

Status of a phone number. If the value is 'Normal', the phone number is ready to be used. Otherwise, it is an external number not yet ported to RingCentral

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| NORMAL    | str  | ✅       | "Normal"    |
| PENDING   | str  | ✅       | "Pending"   |
| PORTEDIN  | str  | ✅       | "PortedIn"  |
| TEMPORARY | str  | ✅       | "Temporary" |

# UserPhoneNumberInfoType

Phone number type

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| VOICEFAX  | str  | ✅       | "VoiceFax"  |
| FAXONLY   | str  | ✅       | "FaxOnly"   |
| VOICEONLY | str  | ✅       | "VoiceOnly" |

# UserPhoneNumberInfoSubType

Extension subtype, if applicable. For any unsupported subtypes the 'Unknown' value will be returned

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| VIDEOPRO       | str  | ✅       | "VideoPro"       |
| VIDEOPROPLUS   | str  | ✅       | "VideoProPlus"   |
| DIGITALSIGNAGE | str  | ✅       | "DigitalSignage" |
| UNKNOWN        | str  | ✅       | "Unknown"        |
| EMERGENCY      | str  | ✅       | "Emergency"      |

# UserPhoneNumberInfoUsageType

Usage type of phone number. Numbers of 'NumberPool' type will not be returned for phone number list requests

**Properties**

| Name                        | Type | Required | Description                   |
| :-------------------------- | :--- | :------- | :---------------------------- |
| MAINCOMPANYNUMBER           | str  | ✅       | "MainCompanyNumber"           |
| ADDITIONALCOMPANYNUMBER     | str  | ✅       | "AdditionalCompanyNumber"     |
| COMPANYNUMBER               | str  | ✅       | "CompanyNumber"               |
| DIRECTNUMBER                | str  | ✅       | "DirectNumber"                |
| COMPANYFAXNUMBER            | str  | ✅       | "CompanyFaxNumber"            |
| FORWARDEDNUMBER             | str  | ✅       | "ForwardedNumber"             |
| FORWARDEDCOMPANYNUMBER      | str  | ✅       | "ForwardedCompanyNumber"      |
| CONTACTCENTERNUMBER         | str  | ✅       | "ContactCenterNumber"         |
| CONFERENCINGNUMBER          | str  | ✅       | "ConferencingNumber"          |
| NUMBERPOOL                  | str  | ✅       | "NumberPool"                  |
| BUSINESSMOBILENUMBER        | str  | ✅       | "BusinessMobileNumber"        |
| PARTNERBUSINESSMOBILENUMBER | str  | ✅       | "PartnerBusinessMobileNumber" |
| INTEGRATIONNUMBER           | str  | ✅       | "IntegrationNumber"           |

# UserPhoneNumberInfoFeatures

**Properties**

| Name                   | Type | Required | Description              |
| :--------------------- | :--- | :------- | :----------------------- |
| CALLERID               | str  | ✅       | "CallerId"               |
| SMSSENDER              | str  | ✅       | "SmsSender"              |
| A2PSMSSENDER           | str  | ✅       | "A2PSmsSender"           |
| MMSSENDER              | str  | ✅       | "MmsSender"              |
| INTERNATIONALSMSSENDER | str  | ✅       | "InternationalSmsSender" |
| DELEGATED              | str  | ✅       | "Delegated"              |

<!-- This file was generated by liblab | https://liblab.com/ -->
