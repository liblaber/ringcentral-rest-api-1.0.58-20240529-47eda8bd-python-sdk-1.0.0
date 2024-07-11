# RegionalSettingsService

A list of all methods in the `RegionalSettingsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                          |
| :-------------------------------- | :--------------------------------------------------- |
| [list_states](#list_states)       | Returns all states of a certain country.             |
| [read_state](#read_state)         | Returns information on a specific state by ID.       |
| [list_locations](#list_locations) | Returns all available locations for a certain state. |
| [list_languages](#list_languages) | Returns information about the supported languages.   |
| [read_language](#read_language)   | Returns a language by ID.                            |
| [list_timezones](#list_timezones) | Returns all available timezones.                     |
| [read_timezone](#read_timezone)   | Returns information on a certain timezone.           |
| [list_countries](#list_countries) | Returns all countries available for calling.         |
| [read_country](#read_country)     | Returns information on a specific country.           |

## list_states

Returns all states of a certain country.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/state`

**Parameters**

| Name               | Type | Required | Description                                                                                                                                                   |
| :----------------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| all_countries      | bool | ❌       | If set to `true` then states of all countries are returned and `countryId` is ignored, even if specified. If the value is empty then the parameter is ignored |
| country_id         | int  | ❌       | Internal identifier of a country                                                                                                                              |
| page               | int  | ❌       | Indicates a page number to retrieve. Only positive number values are accepted                                                                                 |
| per_page           | int  | ❌       | Indicates a page size (number of items)                                                                                                                       |
| with_phone_numbers | bool | ❌       | If `true` the list of states with phone numbers available for buying is returned                                                                              |

**Return Type**

`GetStateListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.list_states(
    all_countries=True,
    country_id=0,
    page=1,
    per_page=100,
    with_phone_numbers=False
)

print(result)
```

## read_state

Returns information on a specific state by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/state/{stateId}`

**Parameters**

| Name     | Type | Required | Description                    |
| :------- | :--- | :------- | :----------------------------- |
| state_id | int  | ✅       | Internal identifier of a state |

**Return Type**

`GetStateInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.read_state(state_id=10)

print(result)
```

## list_locations

Returns all available locations for a certain state.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/location`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                   |
| :------- | :-------------------------------------------------------- | :------- | :---------------------------------------------------------------------------- |
| order_by | [ListLocationsOrderBy](../models/ListLocationsOrderBy.md) | ❌       | Sorts results by the property specified                                       |
| page     | int                                                       | ❌       | Indicates a page number to retrieve. Only positive number values are accepted |
| per_page | int                                                       | ❌       | Indicates a page size (number of items)                                       |
| state_id | str                                                       | ❌       | Internal identifier of a state                                                |
| with_nxx | bool                                                      | ❌       | Specifies if `nxx` codes are returned                                         |

**Return Type**

`GetLocationListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListLocationsOrderBy

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.list_locations(
    order_by="Npa",
    page=1,
    per_page=100,
    state_id="stateId",
    with_nxx=False
)

print(result)
```

## list_languages

Returns information about the supported languages.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/language`

**Return Type**

`LanguageList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.list_languages()

print(result)
```

## read_language

Returns a language by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/language/{languageId}`

**Parameters**

| Name        | Type | Required | Description                       |
| :---------- | :--- | :------- | :-------------------------------- |
| language_id | int  | ✅       | Internal identifier of a language |

**Return Type**

`LanguageInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.read_language(language_id=4)

print(result)
```

## list_timezones

Returns all available timezones.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/timezone`

**Parameters**

| Name     | Type | Required | Description                                                                                        |
| :------- | :--- | :------- | :------------------------------------------------------------------------------------------------- |
| page     | int  | ❌       | Indicates a page number to retrieve. Only positive number values are allowed. Default value is '1' |
| per_page | int  | ❌       | Indicates a page size (number of items). If not specified, the value is '100' by default           |

**Return Type**

`GetTimezoneListResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.list_timezones(
    page=1,
    per_page=100
)

print(result)
```

## read_timezone

Returns information on a certain timezone.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/timezone/{timezoneId}`

**Parameters**

| Name        | Type | Required | Description                       |
| :---------- | :--- | :------- | :-------------------------------- |
| timezone_id | int  | ✅       | Internal identifier of a timezone |

**Return Type**

`GetTimezoneInfoResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.read_timezone(timezone_id=9)

print(result)
```

## list_countries

Returns all countries available for calling.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/country`

**Parameters**

| Name                | Type | Required | Description                                                                                                                                            |
| :------------------ | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| login_allowed       | bool | ❌       | Specifies whether the logging-in with the phone numbers of this country is enabled or not                                                              |
| signup_allowed      | bool | ❌       | Indicates whether a signup/billing is allowed for a country. If not specified all countries are returned (according to other specified filters if any) |
| number_selling      | bool | ❌       | Specifies if RingCentral sells phone numbers of this country                                                                                           |
| page                | int  | ❌       | Indicates a page number to retrieve. Only positive number values are accepted                                                                          |
| per_page            | int  | ❌       | Indicates a page size (number of items)                                                                                                                |
| free_softphone_line | bool | ❌       | Specifies if free phone line for softphone is available for a country or not                                                                           |

**Return Type**

`CountryListDictionaryModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.list_countries(
    login_allowed=True,
    signup_allowed=False,
    number_selling=True,
    page=1,
    per_page=100,
    free_softphone_line=False
)

print(result)
```

## read_country

Returns information on a specific country.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/dictionary/country/{countryId}`

**Parameters**

| Name       | Type | Required | Description                      |
| :--------- | :--- | :------- | :------------------------------- |
| country_id | int  | ✅       | Internal identifier of a country |

**Return Type**

`CountryInfoDictionaryModel`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.regional_settings.read_country(country_id=0)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
