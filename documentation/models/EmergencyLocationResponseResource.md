# EmergencyLocationResponseResource

**Properties**

| Name              | Type                               | Required | Description                                                                                                                                                      |
| :---------------- | :--------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_              | str                                | ❌       | Internal identifier of an emergency response location                                                                                                            |
| address           | CommonEmergencyLocationAddressInfo | ❌       |                                                                                                                                                                  |
| name              | str                                | ❌       | Emergency response location name                                                                                                                                 |
| site              | ShortSiteInfo                      | ❌       |                                                                                                                                                                  |
| address_status    | AddressStatus                      | ❌       | Emergency address status                                                                                                                                         |
| usage_status      | UsageStatus                        | ❌       | Status of emergency response location usage.                                                                                                                     |
| sync_status       | SyncStatus                         | ❌       | Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress` parameter is set to `true`                                             |
| address_type      | EmergencyAddressType               | ❌       |                                                                                                                                                                  |
| visibility        | Visibility                         | ❌       | Visibility of an emergency response location. If `Private` is set, then location is visible only for the restricted number of users, specified in `owners` array |
| owners            | List[LocationOwnerInfo]            | ❌       | List of private location owners                                                                                                                                  |
| address_format_id | str                                | ❌       | Address format ID                                                                                                                                                |
| trusted           | bool                               | ❌       | If 'true' address validation for non-us addresses is skipped                                                                                                     |

<!-- This file was generated by liblab | https://liblab.com/ -->
