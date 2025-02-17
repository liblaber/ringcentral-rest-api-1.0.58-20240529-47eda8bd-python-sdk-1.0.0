# MobileDeliveryMode

**Properties**

| Name             | Type                            | Required | Description                                                                                             |
| :--------------- | :------------------------------ | :------- | :------------------------------------------------------------------------------------------------------ |
| transport_type   | MobileDeliveryModeTransportType | ✅       | The transport type for this subscription, or the channel by which an app should be notified of an event |
| certificate_name | str                             | ✅       | Certificate name for mobile notification transports                                                     |
| registration_id  | str                             | ✅       | Device instance ID for mobile notification transports                                                   |
| encryption       | MobileDeliveryModeEncryption    | ✅       | Specifies if notification messages will be encrypted or not.                                            |

# MobileDeliveryModeTransportType

The transport type for this subscription, or the channel by which an app should be notified of an event

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| RC_APNS | str  | ✅       | "RC/APNS"   |
| RC_GCM  | str  | ✅       | "RC/GCM"    |

# MobileDeliveryModeEncryption

Specifies if notification messages will be encrypted or not.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| FALSE | str  | ✅       | "false"     |

<!-- This file was generated by liblab | https://liblab.com/ -->
