# EmergencyAddressInfo

# EmergencyAddressInfo_1

**Properties**

| Name             | Type                            | Required | Description                                                                                                                                        |
| :--------------- | :------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| country          | str                             | ❌       | Country name                                                                                                                                       |
| country_id       | str                             | ❌       | Internal identifier of a country                                                                                                                   |
| country_iso_code | str                             | ❌       | ISO code of a country                                                                                                                              |
| country_name     | str                             | ❌       | Full name of a country                                                                                                                             |
| state            | str                             | ❌       | State/Province name. Mandatory for the USA, the UK and Canada                                                                                      |
| state_id         | str                             | ❌       | Internal identifier of a state                                                                                                                     |
| state_iso_code   | str                             | ❌       | ISO code of a state                                                                                                                                |
| state_name       | str                             | ❌       | Full name of a state                                                                                                                               |
| city             | str                             | ❌       | City name                                                                                                                                          |
| street           | str                             | ❌       | First line address                                                                                                                                 |
| street2          | str                             | ❌       | Second line address (apartment, suite, unit, building, floor, etc.)                                                                                |
| zip              | str                             | ❌       | Postal (Zip) code                                                                                                                                  |
| customer_name    | str                             | ❌       | Customer name                                                                                                                                      |
| sync_status      | EmergencyAddressInfo1SyncStatus | ❌       | Resulting status of emergency address synchronization. Returned for 'Get Device Info' request if `syncEmergencyAddress` parameter is set to `true` |

# EmergencyAddressInfo_1SyncStatus

Resulting status of emergency address synchronization. Returned for 'Get Device Info' request if `syncEmergencyAddress` parameter is set to `true`

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| VERIFIED    | str  | ✅       | "Verified"    |
| UPDATED     | str  | ✅       | "Updated"     |
| DELETED     | str  | ✅       | "Deleted"     |
| NOTREQUIRED | str  | ✅       | "NotRequired" |
| UNSUPPORTED | str  | ✅       | "Unsupported" |
| FAILED      | str  | ✅       | "Failed"      |

# EmergencyAddressInfo_2

**Properties**

| Name             | Type                            | Required | Description                                                                                                                                        |
| :--------------- | :------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| country          | str                             | ❌       | Country name                                                                                                                                       |
| country_id       | str                             | ❌       | Internal identifier of a country                                                                                                                   |
| country_iso_code | str                             | ❌       | ISO code of a country                                                                                                                              |
| country_name     | str                             | ❌       | Full name of a country                                                                                                                             |
| state            | str                             | ❌       | State/Province name. Mandatory for the USA, the UK and Canada                                                                                      |
| state_id         | str                             | ❌       | Internal identifier of a state                                                                                                                     |
| state_iso_code   | str                             | ❌       | ISO code of a state                                                                                                                                |
| state_name       | str                             | ❌       | Full name of a state                                                                                                                               |
| city             | str                             | ❌       | City name                                                                                                                                          |
| street           | str                             | ❌       | The name of the street (the field is utilized as 'streetName' field for AU addresses)                                                              |
| company_name     | str                             | ❌       | Company name                                                                                                                                       |
| building_name    | str                             | ❌       | (Optional) Building name                                                                                                                           |
| street_type      | str                             | ❌       | Street type                                                                                                                                        |
| building_number  | str                             | ❌       | Building/street number                                                                                                                             |
| street2          | str                             | ❌       | Second line address (apartment, suite, unit, building, floor, etc.)                                                                                |
| zip              | str                             | ❌       | Postal (Zip) code                                                                                                                                  |
| customer_name    | str                             | ❌       | Customer name                                                                                                                                      |
| sync_status      | EmergencyAddressInfo2SyncStatus | ❌       | Resulting status of emergency address synchronization. Returned for 'Get Device Info' request if `syncEmergencyAddress` parameter is set to `true` |

# EmergencyAddressInfo_2SyncStatus

Resulting status of emergency address synchronization. Returned for 'Get Device Info' request if `syncEmergencyAddress` parameter is set to `true`

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| VERIFIED    | str  | ✅       | "Verified"    |
| UPDATED     | str  | ✅       | "Updated"     |
| DELETED     | str  | ✅       | "Deleted"     |
| NOTREQUIRED | str  | ✅       | "NotRequired" |
| UNSUPPORTED | str  | ✅       | "Unsupported" |
| FAILED      | str  | ✅       | "Failed"      |

# EmergencyAddressInfo_3

**Properties**

| Name             | Type                            | Required | Description                                                                                                                                        |
| :--------------- | :------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| country          | str                             | ❌       | Country name                                                                                                                                       |
| country_id       | str                             | ❌       | Internal identifier of a country                                                                                                                   |
| country_iso_code | str                             | ❌       | ISO code of a country                                                                                                                              |
| country_name     | str                             | ❌       | Full name of a country                                                                                                                             |
| state            | str                             | ❌       | State/Province name. Mandatory for the USA, the UK and Canada                                                                                      |
| state_id         | str                             | ❌       | Internal identifier of a state                                                                                                                     |
| state_iso_code   | str                             | ❌       | ISO code of a state                                                                                                                                |
| state_name       | str                             | ❌       | Full name of a state                                                                                                                               |
| city             | str                             | ❌       | City name                                                                                                                                          |
| street           | str                             | ❌       | The name of the street (The field is utilized as 'streetName' field for FR addresses)                                                              |
| company_name     | str                             | ❌       | Company name                                                                                                                                       |
| building_name    | str                             | ❌       | (Optional) Building name                                                                                                                           |
| building_number  | str                             | ❌       | Building/street number                                                                                                                             |
| street2          | str                             | ❌       | Second line address (apartment, suite, unit, building, floor, etc.)                                                                                |
| zip              | str                             | ❌       | Postal (Zip) code                                                                                                                                  |
| customer_name    | str                             | ❌       | Customer name                                                                                                                                      |
| sync_status      | EmergencyAddressInfo3SyncStatus | ❌       | Resulting status of emergency address synchronization. Returned for 'Get Device Info' request if `syncEmergencyAddress` parameter is set to `true` |

# EmergencyAddressInfo_3SyncStatus

Resulting status of emergency address synchronization. Returned for 'Get Device Info' request if `syncEmergencyAddress` parameter is set to `true`

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| VERIFIED    | str  | ✅       | "Verified"    |
| UPDATED     | str  | ✅       | "Updated"     |
| DELETED     | str  | ✅       | "Deleted"     |
| NOTREQUIRED | str  | ✅       | "NotRequired" |
| UNSUPPORTED | str  | ✅       | "Unsupported" |
| FAILED      | str  | ✅       | "Failed"      |

<!-- This file was generated by liblab | https://liblab.com/ -->
