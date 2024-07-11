# CallHandlingRulesService

A list of all methods in the `CallHandlingRulesService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                            |
| :-------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| [list_company_answering_rules](#list_company_answering_rules)         | Returns a list of company call handling rules.                         |
| [create_company_answering_rule](#create_company_answering_rule)       | Creates call handling rule on account level.                           |
| [read_company_answering_rule](#read_company_answering_rule)           | Returns a company call handling rule by ID.                            |
| [update_company_answering_rule](#update_company_answering_rule)       | Updates a company call handling rule.                                  |
| [delete_company_answering_rule](#delete_company_answering_rule)       | Deletes a company custom call handling rule by a particular ID.        |
| [get_forward_all_company_calls](#get_forward_all_company_calls)       | Returns information about _Forward All Company Calls_ feature setting. |
| [update_forward_all_company_calls](#update_forward_all_company_calls) | Updates _Forward All Company Calls_ feature setting.                   |
| [list_answering_rules](#list_answering_rules)                         | Returns call handling rules of an extension.                           |
| [create_answering_rule](#create_answering_rule)                       | Creates a custom call handling rule for a particular caller ID.        |
| [read_answering_rule](#read_answering_rule)                           | Returns a call handling rule by ID.                                    |
| [update_answering_rule](#update_answering_rule)                       | Updates a custom call handling rule for a particular caller ID.        |
| [delete_answering_rule](#delete_answering_rule)                       | Deletes a custom call handling rule by a particular ID.                |

## list_company_answering_rules

Returns a list of company call handling rules.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/answering-rule`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| page       | int  | ❌       | The result set page number (1-indexed) to return                                                                                                             |
| per_page   | int  | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                       |

**Return Type**

`CompanyAnsweringRuleList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_handling_rules.list_company_answering_rules(
    account_id="~",
    page=1,
    per_page=100
)

print(result)
```

## create_company_answering_rule

Creates call handling rule on account level.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/answering-rule`

**Parameters**

| Name         | Type                                                                    | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CompanyAnsweringRuleRequest](../models/CompanyAnsweringRuleRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`CompanyAnsweringRuleInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CompanyAnsweringRuleRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CompanyAnsweringRuleRequest(
    name="name",
    enabled=True,
    type_="BusinessHours",
    callers=[
        {
            "caller_id": "callerId",
            "name": "name"
        }
    ],
    called_numbers=[
        {
            "id_": "id",
            "phone_number": "phoneNumber"
        }
    ],
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
        },
        "ranges": [
            {
                "from_": "from",
                "to": "to"
            }
        ],
        "ref": "BusinessHours"
    },
    call_handling_action="Operator",
    extension={
        "id_": "id"
    },
    greetings=[
        {
            "type_": "Introductory",
            "preset": {
                "uri": "uri",
                "id_": "id",
                "name": "name"
            },
            "custom": {
                "id_": "id"
            }
        }
    ]
)

result = sdk.call_handling_rules.create_company_answering_rule(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## read_company_answering_rule

Returns a company call handling rule by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/answering-rule/{ruleId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| rule_id    | str  | ✅       | Internal identifier of a call handling rule                                                                                                                  |

**Return Type**

`CompanyAnsweringRuleInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_handling_rules.read_company_answering_rule(
    account_id="~",
    rule_id="ruleId"
)

print(result)
```

## update_company_answering_rule

Updates a company call handling rule.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/answering-rule/{ruleId}`

**Parameters**

| Name         | Type                                                                  | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CompanyAnsweringRuleUpdate](../models/CompanyAnsweringRuleUpdate.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| rule_id      | str                                                                   | ✅       | Internal identifier of a call handling rule                                                                                                                  |

**Return Type**

`CompanyAnsweringRuleInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CompanyAnsweringRuleUpdate

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CompanyAnsweringRuleUpdate(
    enabled=True,
    name="name",
    callers=[
        {
            "caller_id": "callerId",
            "name": "name"
        }
    ],
    called_numbers=[
        {
            "id_": "id",
            "phone_number": "phoneNumber"
        }
    ],
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
        },
        "ranges": [
            {
                "from_": "from",
                "to": "to"
            }
        ],
        "ref": "BusinessHours"
    },
    call_handling_action="Operator",
    type_="BusinessHours",
    extension={
        "caller_id": "callerId",
        "name": "name"
    },
    greetings=[
        {
            "type_": "Introductory",
            "preset": {
                "uri": "uri",
                "id_": "id",
                "name": "name"
            },
            "custom": {
                "id_": "id"
            }
        }
    ]
)

result = sdk.call_handling_rules.update_company_answering_rule(
    request_body=request_body,
    account_id="~",
    rule_id="ruleId"
)

print(result)
```

## delete_company_answering_rule

Deletes a company custom call handling rule by a particular ID.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/answering-rule/{ruleId}`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| rule_id    | str  | ✅       | Internal identifier of a call handling rule                                                                                                                  |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_handling_rules.delete_company_answering_rule(
    account_id="~",
    rule_id="ruleId"
)

print(result)
```

## get_forward_all_company_calls

Returns information about _Forward All Company Calls_ feature setting.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/forward-all-calls`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`ForwardAllCompanyCallsInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_handling_rules.get_forward_all_company_calls(account_id="~")

print(result)
```

## update_forward_all_company_calls

Updates _Forward All Company Calls_ feature setting.

- HTTP Method: `PATCH`
- Endpoint: `/restapi/v1.0/account/{accountId}/forward-all-calls`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [ForwardAllCompanyCallsRequest](../models/ForwardAllCompanyCallsRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`ForwardAllCompanyCallsInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ForwardAllCompanyCallsRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ForwardAllCompanyCallsRequest(
    enabled=False
)

result = sdk.call_handling_rules.update_forward_all_company_calls(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## list_answering_rules

Returns call handling rules of an extension.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                                                                                                           |
| :----------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str                                                           | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                           | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| type\_       | [ListAnsweringRulesType](../models/ListAnsweringRulesType.md) | ❌       | Filters custom call handling rules of the extension                                                                                                                   |
| view         | [ListAnsweringRulesView](../models/ListAnsweringRulesView.md) | ❌       |                                                                                                                                                                       |
| enabled_only | bool                                                          | ❌       | If true, then only active call handling rules are returned                                                                                                            |
| page         | int                                                           | ❌       | The result set page number (1-indexed) to return                                                                                                                      |
| per_page     | int                                                           | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                                |

**Return Type**

`UserAnsweringRuleList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import ListAnsweringRulesType, ListAnsweringRulesView

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_handling_rules.list_answering_rules(
    account_id="~",
    extension_id="~",
    type_="Custom",
    view="Detailed",
    enabled_only=False,
    page=1,
    per_page=100
)

print(result)
```

## create_answering_rule

Creates a custom call handling rule for a particular caller ID.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule`

**Parameters**

| Name         | Type                                                                  | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [CreateAnsweringRuleRequest](../models/CreateAnsweringRuleRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |

**Return Type**

`CustomAnsweringRuleInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateAnsweringRuleRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateAnsweringRuleRequest(
    enabled=True,
    type_="type",
    name="name",
    callers=[
        {
            "caller_id": "callerId",
            "name": "name"
        }
    ],
    called_numbers=[
        {
            "phone_number": "phoneNumber"
        }
    ],
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
        },
        "ranges": [
            {
                "from_": "from",
                "to": "to"
            }
        ],
        "ref": "BusinessHours"
    },
    call_handling_action="ForwardCalls",
    forwarding={
        "notify_my_soft_phones": False,
        "soft_phones_ring_count": 2,
        "soft_phones_always_ring": True,
        "ringing_mode": "Sequentially",
        "rules": [
            {
                "index": 4,
                "ring_count": 6,
                "enabled": True,
                "forwarding_numbers": [
                    {
                        "id_": "id",
                        "uri": "uri",
                        "phone_number": "phoneNumber",
                        "label": "label",
                        "type_": "Home"
                    }
                ]
            }
        ],
        "soft_phones_position_top": False
    },
    unconditional_forwarding={
        "phone_number": "phoneNumber",
        "action": "HoldTimeExpiration"
    },
    queue={
        "transfer_mode": "Rotating",
        "transfer": [
            {
                "extension": {
                    "id_": "id",
                    "uri": "uri",
                    "name": "name",
                    "extension_number": "extensionNumber"
                },
                "action": "HoldTimeExpiration"
            }
        ],
        "no_answer_action": "WaitPrimaryMembers",
        "fixed_order_agents": [
            {
                "extension": {
                    "id_": "id",
                    "uri": "uri",
                    "extension_number": "extensionNumber",
                    "name": "name"
                },
                "index": 0
            }
        ],
        "hold_audio_interruption_mode": "Never",
        "hold_audio_interruption_period": 10,
        "hold_time_expiration_action": "TransferToExtension",
        "agent_timeout": 8,
        "wrap_up_time": 15,
        "hold_time": 5,
        "max_callers": 14,
        "max_callers_action": "Voicemail",
        "unconditional_forwarding": [
            {
                "phone_number": "phoneNumber",
                "action": "HoldTimeExpiration"
            }
        ]
    },
    transfer={
        "extension": {
            "id_": "id",
            "uri": "uri"
        }
    },
    voicemail={
        "enabled": False,
        "recipient": {
            "uri": "uri",
            "id_": "id"
        }
    },
    missed_call={
        "action_type": "PlayGreetingAndDisconnect",
        "extension": {
            "id_": "id",
            "external_number": {
                "phone_number": "phoneNumber"
            }
        }
    },
    greetings=[
        {
            "type_": "Introductory",
            "preset": {
                "uri": "uri",
                "id_": "id",
                "name": "name"
            },
            "custom": {
                "id_": "id"
            }
        }
    ],
    screening="Off"
)

result = sdk.call_handling_rules.create_answering_rule(
    request_body=request_body,
    account_id="~",
    extension_id="~"
)

print(result)
```

## read_answering_rule

Returns a call handling rule by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule/{ruleId}`

**Parameters**

| Name                  | Type | Required | Description                                                                                                                                                           |
| :-------------------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id            | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id          | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| rule_id               | str  | ✅       | Internal identifier of a call handling rule                                                                                                                           |
| show_inactive_numbers | bool | ❌       | Indicates whether inactive numbers should be returned or not                                                                                                          |

**Return Type**

`AnsweringRuleInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_handling_rules.read_answering_rule(
    account_id="~",
    extension_id="~",
    rule_id="ruleId",
    show_inactive_numbers=True
)

print(result)
```

## update_answering_rule

Updates a custom call handling rule for a particular caller ID.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule/{ruleId}`

**Parameters**

| Name         | Type                                                                  | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdateAnsweringRuleRequest](../models/UpdateAnsweringRuleRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                                   | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| rule_id      | str                                                                   | ✅       | Internal identifier of a call handling rule                                                                                                                           |

**Return Type**

`AnsweringRuleInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateAnsweringRuleRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateAnsweringRuleRequest(
    id_="id",
    forwarding={
        "notify_my_soft_phones": True,
        "soft_phones_ring_count": 2,
        "soft_phones_always_ring": True,
        "ringing_mode": "Sequentially",
        "rules": [
            {
                "index": 9,
                "ring_count": 4,
                "enabled": True,
                "forwarding_numbers": [
                    {
                        "id_": "id",
                        "type_": "Home",
                        "phone_number": "phoneNumber",
                        "label": "label"
                    }
                ]
            }
        ]
    },
    enabled=True,
    name="name",
    callers=[
        {
            "caller_id": "callerId",
            "name": "name"
        }
    ],
    called_numbers=[
        {
            "phone_number": "phoneNumber"
        }
    ],
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
        },
        "ranges": [
            {
                "from_": "from",
                "to": "to"
            }
        ],
        "ref": "BusinessHours"
    },
    call_handling_action="ForwardCalls",
    type_="BusinessHours",
    unconditional_forwarding={
        "phone_number": "phoneNumber",
        "action": "HoldTimeExpiration"
    },
    queue={
        "transfer_mode": "Rotating",
        "transfer": [
            {
                "extension": {
                    "id_": "id",
                    "uri": "uri",
                    "name": "name",
                    "extension_number": "extensionNumber"
                },
                "action": "HoldTimeExpiration"
            }
        ],
        "no_answer_action": "WaitPrimaryMembers",
        "fixed_order_agents": [
            {
                "extension": {
                    "id_": "id",
                    "uri": "uri",
                    "extension_number": "extensionNumber",
                    "name": "name"
                },
                "index": 0
            }
        ],
        "hold_audio_interruption_mode": "Never",
        "hold_audio_interruption_period": 10,
        "hold_time_expiration_action": "TransferToExtension",
        "agent_timeout": 8,
        "wrap_up_time": 15,
        "hold_time": 5,
        "max_callers": 14,
        "max_callers_action": "Voicemail",
        "unconditional_forwarding": [
            {
                "phone_number": "phoneNumber",
                "action": "HoldTimeExpiration"
            }
        ]
    },
    voicemail={
        "enabled": False,
        "recipient": {
            "uri": "uri",
            "id_": "id"
        }
    },
    missed_call={
        "action_type": "PlayGreetingAndDisconnect",
        "extension": {
            "id_": "id",
            "external_number": {
                "phone_number": "phoneNumber"
            }
        }
    },
    greetings=[
        {
            "type_": "Introductory",
            "preset": {
                "uri": "uri",
                "id_": "id",
                "name": "name"
            },
            "custom": {
                "id_": "id"
            }
        }
    ],
    screening="Off",
    show_inactive_numbers=True,
    transfer={
        "extension": {
            "id_": "id",
            "uri": "uri"
        }
    }
)

result = sdk.call_handling_rules.update_answering_rule(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    rule_id="ruleId"
)

print(result)
```

## delete_answering_rule

Deletes a custom call handling rule by a particular ID.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule/{ruleId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                           |
| :----------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id   | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str  | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| rule_id      | str  | ✅       | Internal identifier of a call handling rule                                                                                                                           |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.call_handling_rules.delete_answering_rule(
    account_id="~",
    extension_id="~",
    rule_id="ruleId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
