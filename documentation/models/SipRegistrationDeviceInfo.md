# SipRegistrationDeviceInfo

**Properties**

| Name                      | Type                                         | Required | Description                                                                                                                                                                                                                                                                                 |
| :------------------------ | :------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| uri                       | str                                          | ❌       | Canonical URI of the resource                                                                                                                                                                                                                                                               |
| id\_                      | str                                          | ❌       | Internal identifier of a device                                                                                                                                                                                                                                                             |
| type\_                    | SipRegistrationDeviceInfoType                | ❌       | Device type                                                                                                                                                                                                                                                                                 |
| sku                       | str                                          | ❌       | Device identification number (SKU, Stock Keeping Unit) in the format TP-ID [-AT-AC], where TP is device type (HP for RC desk phones, DV for all other devices including soft phones); ID - device model ID; AT - add-on type ID; AC - add-on count (if any). For example 'HP-56-2-2'        |
| status                    | SipRegistrationDeviceInfoStatus              | ❌       |                                                                                                                                                                                                                                                                                             |
| name                      | str                                          | ❌       | Device name. Mandatory if ordering SoftPhone or OtherPhone. Optional for HardPhone. If not specified for HardPhone, then device model name is used as device name                                                                                                                           |
| serial                    | str                                          | ❌       | Serial number for HardPhone (is returned only when the phone is shipped and provisioned); endpoint_id for Softphone and mobile applications                                                                                                                                                 |
| computer_name             | str                                          | ❌       | Computer name (for devices of `SoftPhone` type only)                                                                                                                                                                                                                                        |
| model                     | DeviceModelInfo                              | ❌       | HardPhone model information                                                                                                                                                                                                                                                                 |
| extension                 | DeviceExtensionInfo                          | ❌       |                                                                                                                                                                                                                                                                                             |
| emergency_service_address | DeviceEmergencyServiceAddressResourceDefault | ❌       | Address for emergency cases. The same emergency address is assigned to all the numbers of one device                                                                                                                                                                                        |
| emergency                 | SipRegistrationDeviceEmergencyInfo           | ❌       | Emergency response location settings of a device                                                                                                                                                                                                                                            |
| shipping                  | ShippingInfo                                 | ❌       | Shipping information, according to which devices (in case of HardPhone) or e911 stickers (in case of SoftPhone and OtherPhone) will be delivered to the customer                                                                                                                            |
| phone_lines               | List[DevicePhoneLinesInfo]                   | ❌       | Phone lines information                                                                                                                                                                                                                                                                     |
| box_billing_id            | int                                          | ❌       | Box billing identifier of a device. Applicable only for devices of `HardPhone` type.                                                                                                                                                                                                        |
| use_as_common_phone       | bool                                         | ❌       | Supported only for devices assigned to Limited extensions. If true, enables users to log in to this phone as a common phone.                                                                                                                                                                |
| line_pooling              | LinePoolingEnum                              | ❌       | Pooling type of device: - `Host` - device with a standalone paid phone line which can be linked to soft phone client instance; - `Guest` - device with a linked phone line; - `None` - device without a phone line or with a specific line (free, BLA, etc.)                                |
| in_company_net            | bool                                         | ❌       | Network location status. `true` if the device is located in the configured corporate network (On-Net); `false` for Off-Net location. Parameter is not returned if `EmergencyAddressAutoUpdate` feature is not enabled for the account/user, or if device network location is not determined |
| site                      | DeviceSiteInfo                               | ❌       | Site data                                                                                                                                                                                                                                                                                   |
| last_location_report_time | str                                          | ❌       | Timestamp of receiving last location report in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, for example \*2016-03-10T18:07:52.534Z                                                                                                                         |

# SipRegistrationDeviceInfoType

Device type

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| HARDPHONE  | str  | ✅       | "HardPhone"  |
| SOFTPHONE  | str  | ✅       | "SoftPhone"  |
| OTHERPHONE | str  | ✅       | "OtherPhone" |
| PAGING     | str  | ✅       | "Paging"     |
| WEBPHONE   | str  | ✅       | "WebPhone"   |
| ROOM       | str  | ✅       | "Room"       |

# SipRegistrationDeviceInfoStatus

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| ONLINE  | str  | ✅       | "Online"    |
| OFFLINE | str  | ✅       | "Offline"   |

<!-- This file was generated by liblab | https://liblab.com/ -->
