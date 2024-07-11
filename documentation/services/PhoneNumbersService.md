# PhoneNumbersService

A list of all methods in the `PhoneNumbersService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_account_phone_numbers_v2](#list_account_phone_numbers_v2)       | Returns the list of phone numbers assigned to RingCentral customer account. Both company-level and extension-level numbers are returned. Conferencing numbers, hot desk and ELIN numbers are not returned.                                                                                                                                                                                                                                                                                                                                          |
| [delete_numbers_from_inventory_v2](#delete_numbers_from_inventory_v2) | This method can only delete numbers that meet one of the following requirements: - numbers that have `"usageType": "Inventory"` - `"Forwarded"` numbers - `"Forwarded Company"` numbers In other words, this method will not delete numbers which are in use on the account - extension direct numbers, main number, etc. It is possible to indicate phone numbers to be deleted using their IDs or exact string values in e.164 format. However, the same lookup method (by ID or by value) must be used for all numbers within the same API call. |
| [assign_phone_number_v2](#assign_phone_number_v2)                     | Assigns or reassigns a phone number as a company or extension number. Assign scenarios supported: - from Inventory to a company number; - from Inventory to an extension number. Reassign scenarios supported: - from an extension to another extension; - from an extension to a company number; - from a company number to an extension.                                                                                                                                                                                                          |
| [replace_phone_number_v2](#replace_phone_number_v2)                   | Replaces (swaps) phone numbers from Inventory with the main, company, direct or company fax numbers. This method is used to replace temporary numbers when the porting process is complete.                                                                                                                                                                                                                                                                                                                                                         |
| [add_numbers_to_inventory_v2](#add_numbers_to_inventory_v2)           | Adds phone numbers to the account Inventory as unassigned. Currently, we support the following values: `Inventory`, `InventoryPartnerBusinessMobileNumber` and `PartnerBusinessMobileNumber`. Later we may support some other values like `ForwardedNumber`, etc.                                                                                                                                                                                                                                                                                   |
| [get_bulk_add_task_results_v2](#get_bulk_add_task_results_v2)         | Returns the result of asynchronous operation which adds phone numbers to the account Inventory.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [list_extension_phone_numbers](#list_extension_phone_numbers)         | Returns the list of phone numbers that are used by a particular extension, can be filtered by the phone number type. The returned list contains all numbers which are directly mapped to the given extension. Plus the features and company-level numbers that may be used when performing different operations on behalf of this extension.                                                                                                                                                                                                        |
| [list_account_phone_numbers](#list_account_phone_numbers)             | Returns the list of phone numbers assigned to RingCentral customer account. Both company-level and extension-level numbers are returned.                                                                                                                                                                                                                                                                                                                                                                                                            |
| [read_account_phone_number](#read_account_phone_number)               | Returns phone number(s) belonging to a certain account or extension by phoneNumberId(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.                                                                                                                                                                                                                                                                                                                                                      |
| [parse_phone_number](#parse_phone_number)                             | Returns one or more parsed and/or formatted phone numbers that are passed as strings.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## list_account_phone_numbers_v2

Returns the list of phone numbers assigned to RingCentral customer account. Both company-level and extension-level numbers are returned. Conferencing numbers, hot desk and ELIN numbers are not returned.

- HTTP Method: `GET`
- Endpoint: `/restapi/v2/accounts/{accountId}/phone-numbers`

**Parameters**

| Name             | Type                                                            | Required | Description                                                                                                                                                                                                                                    |
| :--------------- | :-------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id       | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                   |
| page             | int                                                             | ❌       | The result set page number (1-indexed) to return                                                                                                                                                                                               |
| per_page         | int                                                             | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                                                                                                         |
| type\_           | [List[PhoneNumberType]](../models/PhoneNumberType.md)           | ❌       | Types of phone numbers to be returned                                                                                                                                                                                                          |
| usage_type       | [List[PhoneNumberUsageType]](../models/PhoneNumberUsageType.md) | ❌       | Usage type(s) of phone numbers to be returned                                                                                                                                                                                                  |
| status           | [PhoneNumberStatus](../models/PhoneNumberStatus.md)             | ❌       | Status of the phone number(s) to be returned                                                                                                                                                                                                   |
| toll_type        | [PhoneNumberTollType](../models/PhoneNumberTollType.md)         | ❌       | Toll type of phone numbers to return                                                                                                                                                                                                           |
| extension_status | [ExtensionStatus](../models/ExtensionStatus.md)                 | ❌       | Statuses of extensions to return phone numbers for                                                                                                                                                                                             |
| byoc_number      | bool                                                            | ❌       | The parameter reflects whether this number is BYOC or not                                                                                                                                                                                      |
| phone_number     | str                                                             | ❌       | Phone number in e.164 format to be searched for. Parameter value can include wildcards (e.g. "+165012345\*\*") or be an exact number "+16501234500" - single number is searched in that case. Make sure you escape the "+" in the URL as "%2B" |

**Return Type**

`AccountPhoneNumberList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PhoneNumberStatus, PhoneNumberTollType, ExtensionStatus

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
type_=[
    "VoiceFax"
]
usage_type=[
    "MainCompanyNumber"
]

result = sdk.phone_numbers.list_account_phone_numbers_v2(
    account_id="~",
    page=1,
    per_page=100,
    type_=type_,
    usage_type=usage_type,
    status="Normal",
    toll_type="Toll",
    extension_status="Enabled",
    byoc_number=True,
    phone_number="consectetur "
)

print(result)
```

## delete_numbers_from_inventory_v2

This method can only delete numbers that meet one of the following requirements: - numbers that have `"usageType": "Inventory"` - `"Forwarded"` numbers - `"Forwarded Company"` numbers In other words, this method will not delete numbers which are in use on the account - extension direct numbers, main number, etc. It is possible to indicate phone numbers to be deleted using their IDs or exact string values in e.164 format. However, the same lookup method (by ID or by value) must be used for all numbers within the same API call.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v2/accounts/{accountId}/phone-numbers`

**Parameters**

| Name         | Type                                                                | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [DeletePhoneNumbersRequest](../models/DeletePhoneNumbersRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`DeletePhoneNumbersResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import DeletePhoneNumbersRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = DeletePhoneNumbersRequest(
    records=[
        {
            "id_": "1162820004",
            "phone_number": "+16501234567"
        }
    ]
)

result = sdk.phone_numbers.delete_numbers_from_inventory_v2(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## assign_phone_number_v2

Assigns or reassigns a phone number as a company or extension number. Assign scenarios supported: - from Inventory to a company number; - from Inventory to an extension number. Reassign scenarios supported: - from an extension to another extension; - from an extension to a company number; - from a company number to an extension.

- HTTP Method: `PATCH`
- Endpoint: `/restapi/v2/accounts/{accountId}/phone-numbers/{phoneNumberId}`

**Parameters**

| Name            | Type                                                              | Required | Description                                                                                                                                                  |
| :-------------- | :---------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body    | [AssignPhoneNumberRequest](../models/AssignPhoneNumberRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id      | str                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| phone_number_id | str                                                               | ✅       | Internal identifier of a phone number                                                                                                                        |

**Return Type**

`AccountPhoneNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AssignPhoneNumberRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AssignPhoneNumberRequest(
    type_="VoiceFax",
    usage_type="MainCompanyNumber",
    extension={
        "id_": "id"
    },
    cost_center_id="costCenterId"
)

result = sdk.phone_numbers.assign_phone_number_v2(
    request_body=request_body,
    account_id="~",
    phone_number_id="1162820004"
)

print(result)
```

## replace_phone_number_v2

Replaces (swaps) phone numbers from Inventory with the main, company, direct or company fax numbers. This method is used to replace temporary numbers when the porting process is complete.

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/phone-numbers/{phoneNumberId}/replace`

**Parameters**

| Name            | Type                                                                | Required | Description                                                                                                                                                  |
| :-------------- | :------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body    | [ReplacePhoneNumberRequest](../models/ReplacePhoneNumberRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id      | str                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| phone_number_id | str                                                                 | ✅       | Internal identifier of a phone number                                                                                                                        |

**Return Type**

`AccountPhoneNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ReplacePhoneNumberRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ReplacePhoneNumberRequest(
    target_phone_number_id="1162820004"
)

result = sdk.phone_numbers.replace_phone_number_v2(
    request_body=request_body,
    account_id="~",
    phone_number_id="1162820004"
)

print(result)
```

## add_numbers_to_inventory_v2

Adds phone numbers to the account Inventory as unassigned. Currently, we support the following values: `Inventory`, `InventoryPartnerBusinessMobileNumber` and `PartnerBusinessMobileNumber`. Later we may support some other values like `ForwardedNumber`, etc.

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/phone-numbers/bulk-add`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AddPhoneNumbersRequest](../models/AddPhoneNumbersRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`AddPhoneNumbersResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AddPhoneNumbersRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddPhoneNumbersRequest(
    records=[
        {
            "phone_number": "phoneNumber",
            "usage_type": "Inventory"
        }
    ]
)

result = sdk.phone_numbers.add_numbers_to_inventory_v2(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## get_bulk_add_task_results_v2

Returns the result of asynchronous operation which adds phone numbers to the account Inventory.

- HTTP Method: `GET`
- Endpoint: `/restapi/v2/accounts/{accountId}/phone-numbers/bulk-add/{taskId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| task_id    | str  | ✅       | Identifier of a task returned by asynchronous bulk add operation                                                                                             |

**Return Type**

`GetBulkAddTaskResultsV2OkResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.phone_numbers.get_bulk_add_task_results_v2(
    account_id="~",
    task_id="taskId"
)

print(result)
```

## list_extension_phone_numbers

Returns the list of phone numbers that are used by a particular extension, can be filtered by the phone number type. The returned list contains all numbers which are directly mapped to the given extension. Plus the features and company-level numbers that may be used when performing different operations on behalf of this extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/phone-number`

**Parameters**

| Name         | Type                                                                                        | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                                         | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| status       | [ListExtensionPhoneNumbersStatus](../models/ListExtensionPhoneNumbersStatus.md)             | ❌       | Status of a phone number                                                                                                                                              |
| usage_type   | [List[ListExtensionPhoneNumbersUsageType]](../models/ListExtensionPhoneNumbersUsageType.md) | ❌       | Usage type of phone number                                                                                                                                            |
| page         | int                                                                                         | ❌       | Indicates a page number to retrieve. Only positive number values are allowed. Default value is '1'                                                                    |
| per_page     | int                                                                                         | ❌       | Indicates a page size (number of items). If not specified, the value is '100' by default                                                                              |

**Return Type**

`GetExtensionPhoneNumbersResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListExtensionPhoneNumbersStatus

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
usage_type=[
    "MainCompanyNumber"
]

result = sdk.phone_numbers.list_extension_phone_numbers(
    account_id="~",
    extension_id="~",
    status="Normal",
    usage_type=usage_type,
    page=1,
    per_page=100
)

print(result)
```

## list_account_phone_numbers

Returns the list of phone numbers assigned to RingCentral customer account. Both company-level and extension-level numbers are returned.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/phone-number`

**Parameters**

| Name         | Type                                                                                    | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| page         | int                                                                                     | ❌       | Indicates a page number to retrieve. Only positive number values are accepted                                                                                |
| per_page     | int                                                                                     | ❌       | Indicates a page size (number of items)                                                                                                                      |
| usage_type   | [List[ListAccountPhoneNumbersUsageType]](../models/ListAccountPhoneNumbersUsageType.md) | ❌       | Usage type of phone number                                                                                                                                   |
| payment_type | [PlatformPaymentType](../models/PlatformPaymentType.md)                                 | ❌       | Payment Type of the number                                                                                                                                   |
| status       | [ListAccountPhoneNumbersStatus](../models/ListAccountPhoneNumbersStatus.md)             | ❌       | Status of a phone number                                                                                                                                     |

**Return Type**

`AccountPhoneNumbers`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PlatformPaymentType, ListAccountPhoneNumbersStatus

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
usage_type=[
    "MainCompanyNumber"
]

result = sdk.phone_numbers.list_account_phone_numbers(
    account_id="~",
    page=1,
    per_page=100,
    usage_type=usage_type,
    payment_type="External",
    status="Normal"
)

print(result)
```

## read_account_phone_number

Returns phone number(s) belonging to a certain account or extension by phoneNumberId(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/phone-number/{phoneNumberId}`

**Parameters**

| Name            | Type | Required | Description                                                                                                                                                  |
| :-------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id      | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| phone_number_id | int  | ✅       | Internal identifier of a phone number                                                                                                                        |

**Return Type**

`CompanyPhoneNumberInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.phone_numbers.read_account_phone_number(
    account_id="~",
    phone_number_id=0
)

print(result)
```

## parse_phone_number

Returns one or more parsed and/or formatted phone numbers that are passed as strings.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/number-parser/parse`

**Parameters**

| Name                 | Type                                                            | Required | Description                                                                                                                                                                                                                            |
| :------------------- | :-------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body         | [ParsePhoneNumberRequest](../models/ParsePhoneNumberRequest.md) | ✅       | The request body.                                                                                                                                                                                                                      |
| home_country         | str                                                             | ❌       | ISO 3166 alpha2 code of the home country to be used if it is impossible to determine country from the number itself. By default, this parameter is preset to the current user's home country or brand country if the user is undefined |
| national_as_priority | bool                                                            | ❌       | The default value is `false`. If `true`, the numbers that are closer to the home country are given higher priority                                                                                                                     |

**Return Type**

`ParsePhoneNumberResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ParsePhoneNumberRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ParsePhoneNumberRequest(
    original_strings=[
        "(650) 722-1621"
    ]
)

result = sdk.phone_numbers.parse_phone_number(
    request_body=request_body,
    home_country="US",
    national_as_priority=True
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
