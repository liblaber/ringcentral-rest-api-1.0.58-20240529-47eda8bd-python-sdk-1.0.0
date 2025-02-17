# EmergencyLocationRequestResource

**Properties**

| Name              | Type                                          | Required | Description                                                                                                                                                    |
| :---------------- | :-------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_              | str                                           | ❌       | Internal identifier of an emergency response location                                                                                                          |
| address           | CommonEmergencyLocationAddressInfo            | ❌       |                                                                                                                                                                |
| name              | str                                           | ❌       | Emergency response location name                                                                                                                               |
| site              | ShortSiteInfo                                 | ❌       |                                                                                                                                                                |
| address_status    | EmergencyLocationRequestResourceAddressStatus | ❌       | Emergency address status                                                                                                                                       |
| usage_status      | EmergencyLocationRequestResourceUsageStatus   | ❌       | Status of an emergency response location usage.                                                                                                                |
| address_format_id | str                                           | ❌       | Address format ID                                                                                                                                              |
| visibility        | EmergencyLocationRequestResourceVisibility    | ❌       | Visibility of an emergency response location. If `Private` is set, then a location is visible only for restricted number of users, specified in `owners` array |
| trusted           | bool                                          | ❌       | If 'true' address validation for non-us addresses is skipped                                                                                                   |

# EmergencyLocationRequestResourceAddressStatus

Emergency address status

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| VALID   | str  | ✅       | "Valid"     |
| INVALID | str  | ✅       | "Invalid"   |

# EmergencyLocationRequestResourceUsageStatus

Status of an emergency response location usage.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| ACTIVE   | str  | ✅       | "Active"    |
| INACTIVE | str  | ✅       | "Inactive"  |

# EmergencyLocationRequestResourceVisibility

Visibility of an emergency response location. If `Private` is set, then a location is visible only for restricted number of users, specified in `owners` array

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| PUBLIC | str  | ✅       | "Public"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
