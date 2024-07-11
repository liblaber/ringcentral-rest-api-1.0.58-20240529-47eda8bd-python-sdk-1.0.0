# DeviceResource

**Properties**

| Name                      | Type                            | Required | Description                                                                                                                                                                                                                                                                                 |
| :------------------------ | :------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id\_                      | str                             | ❌       | Internal identifier of a device                                                                                                                                                                                                                                                             |
| uri                       | str                             | ❌       | Canonical URI of a device                                                                                                                                                                                                                                                                   |
| sku                       | str                             | ❌       | Device identification number (SKU, Stock Keeping Unit) in the format TP-ID [-AT-AC], where TP is device type (HP for RC desk phones, DV for all other devices including soft phones); ID - device model ID; AT - add-on type ID; AC - add-on count (if any). For example 'HP-56-2-2'        |
| type\_                    | DeviceResourceType              | ❌       | Device type                                                                                                                                                                                                                                                                                 |
| name                      | str                             | ❌       | Device name. Mandatory if ordering SoftPhone or OtherPhone. Optional for HardPhone. If not specified for HardPhone, then a device model is used as a device name                                                                                                                            |
| serial                    | str                             | ❌       | Serial number for HardPhone (is returned only when the phone is shipped and provisioned); endpoint ID for SoftPhone and mobile applications                                                                                                                                                 |
| status                    | DeviceResourceStatus            | ❌       | Device status                                                                                                                                                                                                                                                                               |
| computer_name             | str                             | ❌       | Computer name (for devices of `SoftPhone` type only)                                                                                                                                                                                                                                        |
| model                     | ModelInfo                       | ❌       | HardPhone model information                                                                                                                                                                                                                                                                 |
| extension                 | ExtensionInfoIntId              | ❌       | This attribute can be omitted for unassigned devices                                                                                                                                                                                                                                        |
| emergency                 | DeviceEmergencyInfo             | ❌       | Device emergency settings                                                                                                                                                                                                                                                                   |
| emergency_service_address | EmergencyServiceAddressResource | ❌       | Address for emergency cases. The same emergency address is assigned to all the numbers of one device                                                                                                                                                                                        |
| phone_lines               | List[PhoneLinesInfo]            | ❌       | Phone lines information                                                                                                                                                                                                                                                                     |
| shipping                  | ShippingInfo                    | ❌       | Shipping information, according to which devices (in case of HardPhone) or e911 stickers (in case of SoftPhone and OtherPhone) will be delivered to the customer                                                                                                                            |
| box_billing_id            | int                             | ❌       | Box billing identifier of a device. Applicable only for devices of `HardPhone` type. It is an alternative way to identify the device to be ordered. Either `model` structure, or `boxBillingId` must be specified                                                                           |
| use_as_common_phone       | bool                            | ❌       | Supported only for devices assigned to Limited extensions. If true, enables users to log in to this phone as a common phone.                                                                                                                                                                |
| hot_desk_device           | bool                            | ❌       | This flag indicates whether this device is used for hot desking or not                                                                                                                                                                                                                      |
| in_company_net            | bool                            | ❌       | Network location status. `true` if the device is located in the configured corporate network (On-Net); `false` for Off-Net location. Parameter is not returned if `EmergencyAddressAutoUpdate` feature is not enabled for the account/user, or if device network location is not determined |
| site                      | DeviceSiteInfo                  | ❌       | Site data                                                                                                                                                                                                                                                                                   |
| last_location_report_time | str                             | ❌       | Date/time of receiving last location report in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, for example \*2016-03-10T18:07:52.534Z                                                                                                                         |
| line_pooling              | LinePoolingEnum                 | ❌       | Pooling type of device: - `Host` - device with a standalone paid phone line which can be linked to soft phone client instance; - `Guest` - device with a linked phone line; - `None` - device without a phone line or with a specific line (free, BLA, etc.)                                |
| billing_statement         | BillingStatementInfo            | ❌       | Billing information. Returned for device update request if `prestatement` query parameter is set to 'true'                                                                                                                                                                                  |

# DeviceResourceType

Device type

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| BLA        | str  | ✅       | "BLA"        |
| SOFTPHONE  | str  | ✅       | "SoftPhone"  |
| OTHERPHONE | str  | ✅       | "OtherPhone" |
| HARDPHONE  | str  | ✅       | "HardPhone"  |
| WEBPHONE   | str  | ✅       | "WebPhone"   |
| PAGING     | str  | ✅       | "Paging"     |
| ROOM       | str  | ✅       | "Room"       |
| WEBRTC     | str  | ✅       | "WebRTC"     |

# DeviceResourceStatus

Device status

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| OFFLINE | str  | ✅       | "Offline"   |
| ONLINE  | str  | ✅       | "Online"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
