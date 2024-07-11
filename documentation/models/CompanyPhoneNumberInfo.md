# CompanyPhoneNumberInfo

**Properties**

| Name                    | Type                            | Required | Description                                                                                                                                                                 |
| :---------------------- | :------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uri                     | str                             | ❌       | Link to a company phone number resource                                                                                                                                     |
| id\_                    | int                             | ❌       | Internal identifier of a phone number                                                                                                                                       |
| country                 | CountryInfoBasicModel           | ❌       |                                                                                                                                                                             |
| extension               | ExtensionInfo                   | ❌       | Information on the extension, to which the phone number is assigned. Returned only for the request of Account phone number list                                             |
| label                   | str                             | ❌       | Custom user-defined name of a phone number, if any                                                                                                                          |
| location                | str                             | ❌       | Location (City, State). Filled for local US numbers                                                                                                                         |
| payment_type            | PlatformPaymentType             | ❌       | Payment type. 'External' is returned for forwarded numbers which are not terminated in the RingCentral phone system                                                         |
| phone_number            | str                             | ❌       | Phone number                                                                                                                                                                |
| status                  | CompanyPhoneNumberInfoStatus    | ❌       | Status of a phone number. If the value is 'Normal', the phone number is ready to be used. If the value is 'Pending' it is an external number not yet ported to RingCentral. |
| type\_                  | CompanyPhoneNumberInfoType      | ❌       | Phone number type                                                                                                                                                           |
| usage_type              | CompanyPhoneNumberInfoUsageType | ❌       | Usage type of phone number. Usage type of phone number. Numbers of 'NumberPool' type are not returned in phone number list requests                                         |
| temporary_number        | TemporaryNumberInfo             | ❌       | Temporary phone number, if any. Returned for phone numbers in `Pending` porting status only                                                                                 |
| contact_center_provider | ContactCenterProvider           | ❌       | CCRN (Contact Center Routing Number) provider. If not specified then the default value 'InContact/North America' is used, its ID is '1'                                     |
| vanity_pattern          | str                             | ❌       | Vanity pattern for this number. Returned only when vanity search option is requested. Vanity pattern corresponds to request parameters `nxx` plus `line` or `numberPattern` |
| primary                 | bool                            | ❌       | Specifies if a phone number is primary, i.e. displayed as 'main number' and called by default                                                                               |

# CompanyPhoneNumberInfoStatus

Status of a phone number. If the value is 'Normal', the phone number is ready to be used. If the value is 'Pending' it is an external number not yet ported to RingCentral.

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| NORMAL    | str  | ✅       | "Normal"    |
| PENDING   | str  | ✅       | "Pending"   |
| PORTEDIN  | str  | ✅       | "PortedIn"  |
| TEMPORARY | str  | ✅       | "Temporary" |

# CompanyPhoneNumberInfoType

Phone number type

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| VOICEFAX  | str  | ✅       | "VoiceFax"  |
| FAXONLY   | str  | ✅       | "FaxOnly"   |
| VOICEONLY | str  | ✅       | "VoiceOnly" |

# CompanyPhoneNumberInfoUsageType

Usage type of phone number. Usage type of phone number. Numbers of 'NumberPool' type are not returned in phone number list requests

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
| MEETINGSNUMBER              | str  | ✅       | "MeetingsNumber"              |
| NUMBERPOOL                  | str  | ✅       | "NumberPool"                  |
| BUSINESSMOBILENUMBER        | str  | ✅       | "BusinessMobileNumber"        |
| PARTNERBUSINESSMOBILENUMBER | str  | ✅       | "PartnerBusinessMobileNumber" |
| INTEGRATIONNUMBER           | str  | ✅       | "IntegrationNumber"           |

<!-- This file was generated by liblab | https://liblab.com/ -->
