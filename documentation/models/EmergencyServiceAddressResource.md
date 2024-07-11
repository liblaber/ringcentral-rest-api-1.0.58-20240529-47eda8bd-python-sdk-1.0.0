# EmergencyServiceAddressResource

Address for emergency cases. The same emergency address is assigned to all the numbers of one device

**Properties**

| Name                      | Type                                                  | Required | Description                                                                                                                        |
| :------------------------ | :---------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| street                    | str                                                   | ❌       |                                                                                                                                    |
| street2                   | str                                                   | ❌       |                                                                                                                                    |
| city                      | str                                                   | ❌       |                                                                                                                                    |
| zip                       | str                                                   | ❌       |                                                                                                                                    |
| customer_name             | str                                                   | ❌       |                                                                                                                                    |
| state                     | str                                                   | ❌       | State/province name                                                                                                                |
| state_id                  | str                                                   | ❌       | Internal identifier of a state                                                                                                     |
| state_iso_code            | str                                                   | ❌       | ISO code of a state                                                                                                                |
| state_name                | str                                                   | ❌       | Full name of a state                                                                                                               |
| country_id                | str                                                   | ❌       | Internal identifier of a country                                                                                                   |
| country_iso_code          | str                                                   | ❌       | ISO code of a country                                                                                                              |
| country                   | str                                                   | ❌       | Country name                                                                                                                       |
| country_name              | str                                                   | ❌       | Full name of a country                                                                                                             |
| out_of_country            | bool                                                  | ❌       | Specifies if emergency address is out of country                                                                                   |
| sync_status               | EmergencyServiceAddressResourceSyncStatus             | ❌       | Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress` parameter is set to `true`               |
| additional_customer_name  | str                                                   | ❌       | Name of an additional contact person. Should be specified for countries except the US, Canada, the UK and Australia.               |
| customer_email            | str                                                   | ❌       | Email of a primary contact person (receiver). Should be specified for countries except the US, Canada, the UK and Australia.       |
| additional_customer_email | str                                                   | ❌       | Email of an additional contact person. Should be specified for countries except the US, Canada, the UK and Australia.              |
| customer_phone            | str                                                   | ❌       | Phone number of a primary contact person (receiver). Should be specified for countries except the US, Canada, the UK and Australia |
| additional_customer_phone | str                                                   | ❌       | Phone number of an additional contact person. Should be specified for countries except the US, Canada, the UK & Australia.         |
| line_provisioning_status  | EmergencyServiceAddressResourceLineProvisioningStatus | ❌       | Status of digital line provisioning                                                                                                |
| tax_id                    | str                                                   | ❌       | Internal identifier of a tax                                                                                                       |

# EmergencyServiceAddressResourceSyncStatus

Resulting status of emergency address synchronization. Returned if `syncEmergencyAddress` parameter is set to `true`

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| VERIFIED    | str  | ✅       | "Verified"    |
| UPDATED     | str  | ✅       | "Updated"     |
| DELETED     | str  | ✅       | "Deleted"     |
| NOTREQUIRED | str  | ✅       | "NotRequired" |
| UNSUPPORTED | str  | ✅       | "Unsupported" |
| FAILED      | str  | ✅       | "Failed"      |

# EmergencyServiceAddressResourceLineProvisioningStatus

Status of digital line provisioning

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| PROVISIONING | str  | ✅       | "Provisioning" |
| VALID        | str  | ✅       | "Valid"        |
| INVALID      | str  | ✅       | "Invalid"      |

<!-- This file was generated by liblab | https://liblab.com/ -->
