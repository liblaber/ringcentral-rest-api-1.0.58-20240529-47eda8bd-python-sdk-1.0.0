# PersonalContactResource

**Properties**

| Name             | Type                                | Required | Description                                                                                                                                                                |
| :--------------- | :---------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uri              | str                                 | ❌       | Canonical URI of a contact                                                                                                                                                 |
| availability     | PersonalContactResourceAvailability | ❌       | This property has a special meaning only on Address Book Sync (e.g. a contact can be `Deleted`). For simple contact list reading it has always the default value - `Alive` |
| email            | str                                 | ❌       | Email of a contact                                                                                                                                                         |
| id\_             | int                                 | ❌       | Internal identifier of availability contact                                                                                                                                |
| notes            | str                                 | ❌       | Notes for a contact                                                                                                                                                        |
| company          | str                                 | ❌       | Company name of a contact                                                                                                                                                  |
| first_name       | str                                 | ❌       | First name of a contact                                                                                                                                                    |
| last_name        | str                                 | ❌       | Last name of a contact                                                                                                                                                     |
| job_title        | str                                 | ❌       | Job title of a contact                                                                                                                                                     |
| birthday         | str                                 | ❌       | Date of birth of a contact                                                                                                                                                 |
| web_page         | str                                 | ❌       | The contact home page URL                                                                                                                                                  |
| middle_name      | str                                 | ❌       | Middle name of a contact                                                                                                                                                   |
| nick_name        | str                                 | ❌       | Nick name of a contact                                                                                                                                                     |
| email2           | str                                 | ❌       | Second email of a contact                                                                                                                                                  |
| email3           | str                                 | ❌       | Third email of a contact                                                                                                                                                   |
| home_phone       | str                                 | ❌       | Home phone number of a contact in e.164 (with "+") format                                                                                                                  |
| home_phone2      | str                                 | ❌       | Second home phone number of a contact in e.164 (with "+") format                                                                                                           |
| business_phone   | str                                 | ❌       | Business phone of the contact in e.164 (with "+") format                                                                                                                   |
| business_phone2  | str                                 | ❌       | Second business phone of a contact in e.164 (with "+") format                                                                                                              |
| mobile_phone     | str                                 | ❌       | Mobile phone of a contact in e.164 (with "+") format                                                                                                                       |
| business_fax     | str                                 | ❌       | Business fax number of a contact in e.164 (with "+") format                                                                                                                |
| company_phone    | str                                 | ❌       | Company number of a contact in e.164 (with "+") format                                                                                                                     |
| assistant_phone  | str                                 | ❌       | Phone number of a contact assistant in e.164 (with "+") format                                                                                                             |
| car_phone        | str                                 | ❌       | Car phone number of a contact in e.164 (with "+") format                                                                                                                   |
| other_phone      | str                                 | ❌       | Other phone number of a contact in e.164 (with "+") format                                                                                                                 |
| other_fax        | str                                 | ❌       | Other fax number of a contact in e.164 (with "+") format                                                                                                                   |
| callback_phone   | str                                 | ❌       | Callback phone number of a contact in e.164 (with "+") format                                                                                                              |
| business_address | ContactAddressInfo                  | ❌       |                                                                                                                                                                            |
| home_address     | ContactAddressInfo                  | ❌       |                                                                                                                                                                            |
| other_address    | ContactAddressInfo                  | ❌       |                                                                                                                                                                            |
| ringtone_index   | str                                 | ❌       | Contact ringtone. Max number of symbols is 64                                                                                                                              |

# PersonalContactResourceAvailability

This property has a special meaning only on Address Book Sync (e.g. a contact can be `Deleted`). For simple contact list reading it has always the default value - `Alive`

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| ALIVE   | str  | ✅       | "Alive"     |
| DELETED | str  | ✅       | "Deleted"   |
| PURGED  | str  | ✅       | "Purged"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
