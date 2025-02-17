# OptOutResponse

Opt-out record

**Properties**

| Name   | Type                 | Required | Description                                                                                                         |
| :----- | :------------------- | :------- | :------------------------------------------------------------------------------------------------------------------ |
| from\_ | str                  | ❌       | Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format from which the recipient has opted out |
| to     | str                  | ❌       | Phone number in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I) format which is opted out                     |
| status | OptOutResponseStatus | ❌       | Status of a phone number                                                                                            |
| source | Source               | ❌       |                                                                                                                     |

# OptOutResponseStatus

Status of a phone number

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| OPTIN  | str  | ✅       | "OptIn"     |
| OPTOUT | str  | ✅       | "OptOut"    |

# Source

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| RECIPIENT | str  | ✅       | "Recipient" |
| ACCOUNT   | str  | ✅       | "Account"   |
| UPSTREAM  | str  | ✅       | "Upstream"  |
| CARRIER   | str  | ✅       | "Carrier"   |

<!-- This file was generated by liblab | https://liblab.com/ -->
