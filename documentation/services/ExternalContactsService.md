# ExternalContactsService

A list of all methods in the `ExternalContactsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                                                                                                                                           |
| :---------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [address_book_bulk_upload](#address_book_bulk_upload)                   | Uploads multiple contacts for multiple extensions at once. Maximum 500 extensions can be uploaded per request. Max amount of contacts that can be uploaded per extension is 10,000. Each contact uploaded for a certain extension is not visible to other extensions. |
| [get_address_book_bulk_upload_task](#get_address_book_bulk_upload_task) | Returns the status of a task on adding multiple contacts to multiple extensions.                                                                                                                                                                                      |
| [list_favorite_contacts](#list_favorite_contacts)                       | Returns the list of favorite contacts of the current extension. Favorite contacts include both company contacts (extensions) and personal contacts (address book records).                                                                                            |
| [update_favorite_contact_list](#update_favorite_contact_list)           | Updates the list of favorite contacts of the current extension. Favorite contacts include both company contacts (extensions) and personal contacts (address book records).**Please note**: Currently personal address book size is limited to 10 000 contacts.        |
| [list_contacts](#list_contacts)                                         | Returns the user personal contacts.                                                                                                                                                                                                                                   |
| [create_contact](#create_contact)                                       | Creates the user personal contact.                                                                                                                                                                                                                                    |
| [read_contact](#read_contact)                                           | Returns the user personal contact(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.                                                                                                                           |
| [update_contact](#update_contact)                                       | Updates the user personal contact(s) (full resource update). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.                                                                                                    |
| [patch_contact](#patch_contact)                                         | Updates particular values of a personal contact attributes specified in request (partial resource update). Omitted attributes will remain unchanged. If any attribute is passed in request body with the null value, then this attribute value will be removed.       |
| [delete_contact](#delete_contact)                                       | Deletes the user personal contact(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.                                                                                                                           |
| [sync_address_book](#sync_address_book)                                 | Synchronizes user contacts.                                                                                                                                                                                                                                           |

## address_book_bulk_upload

Uploads multiple contacts for multiple extensions at once. Maximum 500 extensions can be uploaded per request. Max amount of contacts that can be uploaded per extension is 10,000. Each contact uploaded for a certain extension is not visible to other extensions.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/address-book-bulk-upload`

**Parameters**

| Name         | Type                                                                      | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AddressBookBulkUploadRequest](../models/AddressBookBulkUploadRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`AddressBookBulkUploadResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AddressBookBulkUploadRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddressBookBulkUploadRequest(
    records=[
        {
            "extension_id": "extensionId",
            "contacts": [
                {
                    "email": "charlie.williams@example.com",
                    "notes": "#1 Customer",
                    "company": "Example, Inc.",
                    "first_name": "Charlie",
                    "last_name": "Williams",
                    "job_title": "CEO",
                    "birthday": "birthday",
                    "web_page": "http://www.example.com",
                    "middle_name": "J",
                    "nick_name": "The Boss",
                    "email2": "charlie-example@gmail.com",
                    "email3": "theboss-example@hotmail.com",
                    "home_phone": "+15551234567",
                    "home_phone2": "+15551234567",
                    "business_phone": "+15551234567",
                    "business_phone2": "+15551234567",
                    "mobile_phone": "+15551234567",
                    "business_fax": "+15551234567",
                    "company_phone": "+15551234567",
                    "assistant_phone": "+15551234567",
                    "car_phone": "+15551234567",
                    "other_phone": "+15551234567",
                    "other_fax": "+15551234567",
                    "callback_phone": "+15551234567",
                    "business_address": {
                        "country": "country",
                        "state": "state",
                        "city": "city",
                        "street": "street",
                        "zip": "zip"
                    },
                    "home_address": {
                        "country": "country",
                        "state": "state",
                        "city": "city",
                        "street": "street",
                        "zip": "zip"
                    },
                    "other_address": {
                        "country": "country",
                        "state": "state",
                        "city": "city",
                        "street": "street",
                        "zip": "zip"
                    }
                }
            ]
        }
    ]
)

result = sdk.external_contacts.address_book_bulk_upload(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## get_address_book_bulk_upload_task

Returns the status of a task on adding multiple contacts to multiple extensions.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/address-book-bulk-upload/tasks/{taskId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| task_id    | str  | ✅       | Internal identifier of a task                                                                                                                                |

**Return Type**

`AddressBookBulkUploadResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.external_contacts.get_address_book_bulk_upload_task(
    account_id="~",
    task_id="taskId"
)

print(result)
```

## list_favorite_contacts

Returns the list of favorite contacts of the current extension. Favorite contacts include both company contacts (extensions) and personal contacts (address book records).

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/favorite`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`FavoriteContactList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.external_contacts.list_favorite_contacts(
    account_id="~",
    extension_id="~"
)

print(result)
```

## update_favorite_contact_list

Updates the list of favorite contacts of the current extension. Favorite contacts include both company contacts (extensions) and personal contacts (address book records).**Please note**: Currently personal address book size is limited to 10 000 contacts.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/favorite`

**Parameters**

| Name         | Type                                                  | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [FavoriteCollection](../models/FavoriteCollection.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`FavoriteContactList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import FavoriteCollection

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = FavoriteCollection(
    records=[
        {
            "id_": 10,
            "extension_id": "extensionId",
            "account_id": "accountId",
            "contact_id": "contactId"
        }
    ]
)

result = sdk.external_contacts.update_favorite_contact_list(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## list_contacts

Returns the user personal contacts.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact`

**Parameters**

| Name         | Type                                | Required | Description                                                                                                                                                           |
| :----------- | :---------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                 | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| starts_with  | str                                 | ❌       | If specified, only contacts which 'First name' or 'Last name' start with the mentioned substring will be returned. Case-insensitive                                   |
| sort_by      | [List[SortBy]](../models/SortBy.md) | ❌       | Sorts results by the specified property                                                                                                                               |
| page         | int                                 | ❌       | The result set page number (1-indexed) to return                                                                                                                      |
| per_page     | int                                 | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                                |
| phone_number | List[str]                           | ❌       | Phone number in e.164 format                                                                                                                                          |

**Return Type**

`ContactList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
sort_by=[
    "FirstName"
]
phone_number=[
    "phoneNumber"
]

result = sdk.external_contacts.list_contacts(
    account_id="~",
    extension_id="~",
    starts_with="startsWith",
    sort_by=sort_by,
    page=1,
    per_page=100,
    phone_number=phone_number
)

print(result)
```

## create_contact

Creates the user personal contact.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                                     |
| :----------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| request_body | [PersonalContactRequest](../models/PersonalContactRequest.md) | ✅       | The request body.                                                                                                                                                               |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                    |
| extension_id | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)           |
| dialing_plan | str                                                           | ❌       | Country code value complying with the [ISO 3166-1 alpha-2](https://ru.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. The default value is home country of the current extension |

**Return Type**

`PersonalContactResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PersonalContactRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PersonalContactRequest(
    first_name="Charlie",
    last_name="Williams",
    middle_name="J",
    nick_name="The Boss",
    company="Example, Inc.",
    job_title="CEO",
    email="charlie.williams@example.com",
    email2="charlie-example@gmail.com",
    email3="theboss-example@hotmail.com",
    birthday="birthday",
    web_page="http://www.example.com",
    notes="#1 Customer",
    home_phone="+15551234567",
    home_phone2="+15551234567",
    business_phone="+15551234567",
    business_phone2="+15551234567",
    mobile_phone="+15551234567",
    business_fax="+15551234567",
    company_phone="+15551234567",
    assistant_phone="+15551234567",
    car_phone="+15551234567",
    other_phone="+15551234567",
    other_fax="+15551234567",
    callback_phone="+15551234567",
    home_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    business_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    other_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    ringtone_index="ringtoneIndex"
)

result = sdk.external_contacts.create_contact(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    dialing_plan="dialingPlan"
)

print(result)
```

## read_contact

Returns the user personal contact(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact/{contactId}`

**Parameters**

| Name         | Type      | Required | Description                                                                                                                                                           |
| :----------- | :-------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| contact_id   | List[int] | ✅       | The list of contact identifiers (comma-separated)                                                                                                                     |

**Return Type**

`PersonalContactResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
contact_id=[
    3
]

result = sdk.external_contacts.read_contact(
    account_id="~",
    extension_id="~",
    contact_id=contact_id
)

print(result)
```

## update_contact

Updates the user personal contact(s) (full resource update). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact/{contactId}`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                                     |
| :----------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| request_body | [PersonalContactRequest](../models/PersonalContactRequest.md) | ✅       | The request body.                                                                                                                                                               |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                    |
| extension_id | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)           |
| contact_id   | List[int]                                                     | ✅       | The list of contact identifiers (comma-separated)                                                                                                                               |
| dialing_plan | str                                                           | ❌       | Country code value complying with the [ISO 3166-1 alpha-2](https://ru.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. The default value is home country of the current extension |

**Return Type**

`PersonalContactResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PersonalContactRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PersonalContactRequest(
    first_name="Charlie",
    last_name="Williams",
    middle_name="J",
    nick_name="The Boss",
    company="Example, Inc.",
    job_title="CEO",
    email="charlie.williams@example.com",
    email2="charlie-example@gmail.com",
    email3="theboss-example@hotmail.com",
    birthday="birthday",
    web_page="http://www.example.com",
    notes="#1 Customer",
    home_phone="+15551234567",
    home_phone2="+15551234567",
    business_phone="+15551234567",
    business_phone2="+15551234567",
    mobile_phone="+15551234567",
    business_fax="+15551234567",
    company_phone="+15551234567",
    assistant_phone="+15551234567",
    car_phone="+15551234567",
    other_phone="+15551234567",
    other_fax="+15551234567",
    callback_phone="+15551234567",
    home_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    business_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    other_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    ringtone_index="ringtoneIndex"
)
contact_id=[
    7
]

result = sdk.external_contacts.update_contact(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    contact_id=contact_id,
    dialing_plan="dialingPlan"
)

print(result)
```

## patch_contact

Updates particular values of a personal contact attributes specified in request (partial resource update). Omitted attributes will remain unchanged. If any attribute is passed in request body with the null value, then this attribute value will be removed.

- HTTP Method: `PATCH`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact/{contactId}`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                                     |
| :----------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| request_body | [PersonalContactRequest](../models/PersonalContactRequest.md) | ✅       | The request body.                                                                                                                                                               |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                    |
| extension_id | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)           |
| contact_id   | int                                                           | ✅       | Internal identifier of a contact record in the RingCentral database                                                                                                             |
| dialing_plan | str                                                           | ❌       | Country code value complying with the [ISO 3166-1 alpha-2](https://ru.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. The default value is home country of the current extension |

**Return Type**

`PersonalContactResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import PersonalContactRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PersonalContactRequest(
    first_name="Charlie",
    last_name="Williams",
    middle_name="J",
    nick_name="The Boss",
    company="Example, Inc.",
    job_title="CEO",
    email="charlie.williams@example.com",
    email2="charlie-example@gmail.com",
    email3="theboss-example@hotmail.com",
    birthday="birthday",
    web_page="http://www.example.com",
    notes="#1 Customer",
    home_phone="+15551234567",
    home_phone2="+15551234567",
    business_phone="+15551234567",
    business_phone2="+15551234567",
    mobile_phone="+15551234567",
    business_fax="+15551234567",
    company_phone="+15551234567",
    assistant_phone="+15551234567",
    car_phone="+15551234567",
    other_phone="+15551234567",
    other_fax="+15551234567",
    callback_phone="+15551234567",
    home_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    business_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    other_address={
        "street": "20 Davis Dr.",
        "city": "Belmont",
        "country": "country",
        "state": "CA",
        "zip": "94002"
    },
    ringtone_index="ringtoneIndex"
)

result = sdk.external_contacts.patch_contact(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    contact_id=3,
    dialing_plan="dialingPlan"
)

print(result)
```

## delete_contact

Deletes the user personal contact(s). [Batch request syntax](https://developers.ringcentral.com/api-reference/Batch-Requests) is supported.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book/contact/{contactId}`

**Parameters**

| Name         | Type      | Required | Description                                                                                                                                                           |
| :----------- | :-------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| contact_id   | List[int] | ✅       | The list of contact identifiers (comma-separated)                                                                                                                     |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
contact_id=[
    8
]

result = sdk.external_contacts.delete_contact(
    account_id="~",
    extension_id="~",
    contact_id=contact_id
)

print(result)
```

## sync_address_book

Synchronizes user contacts.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/address-book-sync`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                          |
| :----------- | :-------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                                                                                                                                                         |
| extension_id | str                                                             | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                                                                                                                                                                                                                |
| sync_type    | [SyncAddressBookSyncType](../models/SyncAddressBookSyncType.md) | ❌       | Type of synchronization                                                                                                                                                                                                                                                                                                                                                              |
| sync_token   | str                                                             | ❌       | Value of syncToken property of the last sync request response                                                                                                                                                                                                                                                                                                                        |
| per_page     | int                                                             | ❌       | Number of records per page to be returned. Max number of records is 250, which is also the default. For 'FSync' - if the number of records exceeds the parameter value (either specified or default), all of the pages can be retrieved in several requests. For 'ISync' - if the number of records exceeds page size, then the number of incoming changes to this number is limited |
| page_id      | int                                                             | ❌       | Internal identifier of a page. It can be obtained from the 'nextPageId' parameter passed in response body                                                                                                                                                                                                                                                                            |

**Return Type**

`AddressBookSync`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SyncAddressBookSyncType

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.external_contacts.sync_address_book(
    account_id="~",
    extension_id="~",
    sync_type="FSync",
    sync_token="syncToken",
    per_page=2,
    page_id=4
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
