# PhoneNumberInfoConferencing

**Properties**

| Name         | Type                  | Required | Description                                                                                                                                                                                                                        |
| :----------- | :-------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| country      | CountryInfoShortModel | ❌       |                                                                                                                                                                                                                                    |
| default      | bool                  | ❌       | The value should be `true` if the number is default for the conference. Default conference number is a domestic number that can be set by user (otherwise it is set by the system). Only one default number per country is allowed |
| has_greeting | bool                  | ❌       | The value should be `true` if any greeting message is played on this number                                                                                                                                                        |
| location     | str                   | ❌       | Location (city, region, state) of a conference phone number                                                                                                                                                                        |
| phone_number | str                   | ❌       | Dial-in phone number to connect to a conference                                                                                                                                                                                    |
| premium      | bool                  | ❌       | Indicates if the number is 'premium' (account phone number with the `ConferencingNumber` usageType)                                                                                                                                |

<!-- This file was generated by liblab | https://liblab.com/ -->
