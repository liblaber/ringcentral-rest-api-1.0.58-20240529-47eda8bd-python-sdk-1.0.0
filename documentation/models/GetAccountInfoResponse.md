# GetAccountInfoResponse

**Properties**

| Name                 | Type                         | Required | Description                                                                                                                                                                                         |
| :------------------- | :--------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                 | int                          | ❌       | Internal identifier of an account                                                                                                                                                                   |
| uri                  | str                          | ❌       | Canonical URI of an account                                                                                                                                                                         |
| bsid                 | str                          | ❌       | Internal identifier of an account in the billing system                                                                                                                                             |
| main_number          | str                          | ❌       | Main phone number of the current account                                                                                                                                                            |
| operator             | AccountOperatorInfo          | ❌       | Operator extension information. This extension will receive all calls and messages addressed to an operator.                                                                                        |
| partner_id           | str                          | ❌       | Additional account identifier, created by partner application and applied on client side                                                                                                            |
| service_info         | ServiceInfo                  | ❌       | Account service information, including brand, sub-brand, service plan and billing plan                                                                                                              |
| setup_wizard_state   | SetupWizardStateEnum         | ❌       | Initial configuration wizard state                                                                                                                                                                  |
| signup_info          | SignupInfoResource           | ❌       | Account sign up data                                                                                                                                                                                |
| status               | GetAccountInfoResponseStatus | ❌       | Status of the current account                                                                                                                                                                       |
| status_info          | AccountStatusInfo            | ❌       | Optional information to be used when account is moved to "Disabled" status                                                                                                                          |
| regional_settings    | AccountRegionalSettings      | ❌       | Account level region data (web service Auto-Receptionist settings)                                                                                                                                  |
| federated            | bool                         | ❌       | Specifies whether an account is included into any federation of accounts or not                                                                                                                     |
| outbound_call_prefix | int                          | ❌       | If outbound call prefix is not specified, or set to null (0), then the parameter is not returned; the supported value range is 2-9                                                                  |
| cfid                 | str                          | ❌       | Customer facing identifier. Returned for accounts with the turned off PBX features. Equals to main company number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) (without "+" sign)format |
| limits               | AccountLimits                | ❌       | Limits which are effective for the account                                                                                                                                                          |

# GetAccountInfoResponseStatus

Status of the current account

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| INITIAL     | str  | ✅       | "Initial"     |
| CONFIRMED   | str  | ✅       | "Confirmed"   |
| UNCONFIRMED | str  | ✅       | "Unconfirmed" |
| DISABLED    | str  | ✅       | "Disabled"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
