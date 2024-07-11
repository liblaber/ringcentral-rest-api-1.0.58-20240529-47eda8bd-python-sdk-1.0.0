# CompanyService

A list of all methods in the `CompanyService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                                                                                   |
| :------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- |
| [get_account_info_v2](#get_account_info_v2)                         | Returns basic information about particular RingCentral account                                                                |
| [send_welcome_email_v2](#send_welcome_email_v2)                     | Sends/resends welcome email to the system user of confirmed account                                                           |
| [send_activation_email_v2](#send_activation_email_v2)               | Sends/resends activation email to the system user of unconfirmed account.                                                     |
| [read_account_info](#read_account_info)                             | Returns basic information about a particular RingCentral customer account.                                                    |
| [read_account_service_info](#read_account_service_info)             | Returns the information about service plan, available features and limitations for a particular RingCentral customer account. |
| [read_account_business_address](#read_account_business_address)     | Returns business address of a company.                                                                                        |
| [update_account_business_address](#update_account_business_address) | Updates the business address of a company that account is linked to.                                                          |
| [list_contracted_countries](#list_contracted_countries)             | Returns the list of contracted countries for the given brand.                                                                 |
| [list_domestic_countries](#list_domestic_countries)                 | Returns the list of domestic countries for account contracted country and brand.                                              |

## get_account_info_v2

Returns basic information about particular RingCentral account

- HTTP Method: `GET`
- Endpoint: `/restapi/v2/accounts/{accountId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`AccountInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.company.get_account_info_v2(account_id="~")

print(result)
```

## send_welcome_email_v2

Sends/resends welcome email to the system user of confirmed account

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/send-welcome-email`

**Parameters**

| Name         | Type                                                                | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [SendWelcomeEmailV2Request](../models/SendWelcomeEmailV2Request.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SendWelcomeEmailV2Request

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SendWelcomeEmailV2Request(
    email="user@email.com"
)

result = sdk.company.send_welcome_email_v2(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## send_activation_email_v2

Sends/resends activation email to the system user of unconfirmed account.

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/send-activation-email`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.company.send_activation_email_v2(account_id="~")

print(result)
```

## read_account_info

Returns basic information about a particular RingCentral customer account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`GetAccountInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.company.read_account_info(account_id="~")

print(result)
```

## read_account_service_info

Returns the information about service plan, available features and limitations for a particular RingCentral customer account.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/service-info`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`AccountServiceInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.company.read_account_service_info(account_id="~")

print(result)
```

## read_account_business_address

Returns business address of a company.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/business-address`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`AccountBusinessAddressResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.company.read_account_business_address(account_id="~")

print(result)
```

## update_account_business_address

Updates the business address of a company that account is linked to.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/business-address`

**Parameters**

| Name         | Type                                                                                    | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ModifyAccountBusinessAddressRequest](../models/ModifyAccountBusinessAddressRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`AccountBusinessAddressResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ModifyAccountBusinessAddressRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ModifyAccountBusinessAddressRequest(
    company="company",
    email="email",
    business_address={
        "country": "country",
        "state": "state",
        "city": "city",
        "street": "street",
        "zip": "zip"
    },
    main_site_name="mainSiteName"
)

result = sdk.company.update_account_business_address(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_contracted_countries

Returns the list of contracted countries for the given brand.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/brand/{brandId}/contracted-country`

**Parameters**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| brand_id | str  | ✅       |             |

**Return Type**

`ContractedCountryListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.company.list_contracted_countries(brand_id="brandId")

print(result)
```

## list_domestic_countries

Returns the list of domestic countries for account contracted country and brand.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/brand/{brandId}/contracted-country/{contractedCountryId}`

**Parameters**

| Name                  | Type | Required | Description                                                                   |
| :-------------------- | :--- | :------- | :---------------------------------------------------------------------------- |
| brand_id              | str  | ✅       | Internal identifier of a brand                                                |
| contracted_country_id | str  | ✅       | Internal identifier of a country                                              |
| page                  | int  | ❌       | Indicates a page number to retrieve. Only positive number values are accepted |
| per_page              | int  | ❌       | Indicates a page size (number of items)                                       |

**Return Type**

`CountryListDictionaryModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.company.list_domestic_countries(
    brand_id="brandId",
    contracted_country_id="contractedCountryId",
    page=1,
    per_page=100
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
