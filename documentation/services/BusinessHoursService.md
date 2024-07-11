# BusinessHoursService

A list of all methods in the `BusinessHoursService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_company_business_hours](#read_company_business_hours)     | Returns the company business hours schedule. Business hours (and After hours - all the remaining time) schedules are commonly used for setting call handling rules - `business-hours-rule` and `after-hours-rule` correspondingly.                                                                                                                                                                                   |
| [update_company_business_hours](#update_company_business_hours) | Updates the company business hours schedule.                                                                                                                                                                                                                                                                                                                                                                         |
| [read_user_business_hours](#read_user_business_hours)           | Returns the user business hours schedule. Business hours (and After hours - all the remaining time) schedules are commonly used for setting call handling rules - `business-hours-rule` and `after-hours-rule` correspondingly. **Please note:** If the user business hours are set to 'Custom hours' then a particular schedule is returned; however if set to '24 hours/7 days a week' the schedule will be empty. |
| [update_user_business_hours](#update_user_business_hours)       | Updates the user business hours schedule.                                                                                                                                                                                                                                                                                                                                                                            |

## read_company_business_hours

Returns the company business hours schedule. Business hours (and After hours - all the remaining time) schedules are commonly used for setting call handling rules - `business-hours-rule` and `after-hours-rule` correspondingly.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/business-hours`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CompanyBusinessHours`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.business_hours.read_company_business_hours(account_id="~")

print(result)
```

## update_company_business_hours

Updates the company business hours schedule.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/business-hours`

**Parameters**

| Name         | Type                                                                                | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CompanyBusinessHoursUpdateRequest](../models/CompanyBusinessHoursUpdateRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CompanyBusinessHours`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CompanyBusinessHoursUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CompanyBusinessHoursUpdateRequest(
    schedule={
        "weekly_ranges": {
            "monday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "tuesday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "wednesday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "thursday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "friday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "saturday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "sunday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ]
        }
    }
)

result = sdk.business_hours.update_company_business_hours(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_user_business_hours

Returns the user business hours schedule. Business hours (and After hours - all the remaining time) schedules are commonly used for setting call handling rules - `business-hours-rule` and `after-hours-rule` correspondingly. **Please note:** If the user business hours are set to 'Custom hours' then a particular schedule is returned; however if set to '24 hours/7 days a week' the schedule will be empty.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/business-hours`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`GetUserBusinessHoursResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.business_hours.read_user_business_hours(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_user_business_hours

Updates the user business hours schedule.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/business-hours`

**Parameters**

| Name         | Type                                                                          | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UserBusinessHoursUpdateRequest](../models/UserBusinessHoursUpdateRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`UserBusinessHoursUpdateResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UserBusinessHoursUpdateRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UserBusinessHoursUpdateRequest(
    schedule={
        "weekly_ranges": {
            "monday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "tuesday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "wednesday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "thursday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "friday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "saturday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ],
            "sunday": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ]
        }
    }
)

result = sdk.business_hours.update_user_business_hours(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
