# AddPhoneNumberRequestItem

**Properties**

| Name         | Type                               | Required | Description                                                                                                                                                                                                                        |
| :----------- | :--------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| phone_number | str                                | ✅       | Phone number in e.164 format (with '+' prefix). Wildcards are supported to pass large sets (for example 100 numbers); only one phone number record must be passed in request in that case, for example '+1650123456\*'             |
| usage_type   | AddPhoneNumberRequestItemUsageType | ✅       | Usage type of phone number. Currently, we support the following values: `Inventory`, `InventoryPartnerBusinessMobileNumber` and `PartnerBusinessMobileNumber`. Later we may support some other values like `ForwardedNumber`, etc. |

# AddPhoneNumberRequestItemUsageType

Usage type of phone number. Currently, we support the following values: `Inventory`, `InventoryPartnerBusinessMobileNumber` and `PartnerBusinessMobileNumber`. Later we may support some other values like `ForwardedNumber`, etc.

**Properties**

| Name                                 | Type | Required | Description                            |
| :----------------------------------- | :--- | :------- | :------------------------------------- |
| INVENTORY                            | str  | ✅       | "Inventory"                            |
| INVENTORYPARTNERBUSINESSMOBILENUMBER | str  | ✅       | "InventoryPartnerBusinessMobileNumber" |
| PARTNERBUSINESSMOBILENUMBER          | str  | ✅       | "PartnerBusinessMobileNumber"          |

<!-- This file was generated by liblab | https://liblab.com/ -->
