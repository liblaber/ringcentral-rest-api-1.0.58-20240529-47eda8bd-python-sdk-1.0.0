# UpdateSwitchInfo

**Properties**

| Name              | Type                 | Required | Description                                                                                                                                                          |
| :---------------- | :------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_              | str                  | ❌       | Internal identifier of a switch                                                                                                                                      |
| chassis_id        | str                  | ❌       | Unique identifier of a network switch. The supported formats are: XX:XX:XX:XX:XX:XX (symbols 0-9 and A-F) for MAC address and X.X.X.X for IP address (symbols 0-255) |
| port              | str                  | ❌       | Switch entity extension for better diversity. Should be used together with chassisId.                                                                                |
| name              | str                  | ❌       | Name of a network switch                                                                                                                                             |
| site              | SwitchSiteInfo       | ❌       |                                                                                                                                                                      |
| emergency_address | EmergencyAddressInfo | ❌       |                                                                                                                                                                      |

<!-- This file was generated by liblab | https://liblab.com/ -->
