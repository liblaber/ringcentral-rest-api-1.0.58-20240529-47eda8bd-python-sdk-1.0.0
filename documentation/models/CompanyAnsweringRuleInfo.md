# CompanyAnsweringRuleInfo

**Properties**

| Name                 | Type                                              | Required | Description                                                                                                                                                                                                                                                                                        |
| :------------------- | :------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                 | str                                               | ❌       | Internal identifier of an answering rule                                                                                                                                                                                                                                                           |
| uri                  | str                                               | ❌       | Canonical URI of an answering rule                                                                                                                                                                                                                                                                 |
| enabled              | bool                                              | ❌       | Specifies if the rule is active or inactive                                                                                                                                                                                                                                                        |
| type\_               | CompanyAnsweringRuleInfoType                      | ❌       | Type of an answering rule                                                                                                                                                                                                                                                                          |
| name                 | str                                               | ❌       | Name of an answering rule specified by user. Max number of symbols is 30. The default value is 'My Rule N' where 'N' is the first free number                                                                                                                                                      |
| callers              | List[CompanyAnsweringRuleCallersInfoRequest]      | ❌       | Answering rule will be applied when calls are received from the specified caller(s)                                                                                                                                                                                                                |
| called_numbers       | List[CompanyAnsweringRuleCalledNumberInfoRequest] | ❌       | Answering rule will be applied when calling the specified number(s)                                                                                                                                                                                                                                |
| schedule             | CompanyAnsweringRuleScheduleInfo                  | ❌       | Schedule when an answering rule should be applied                                                                                                                                                                                                                                                  |
| call_handling_action | CompanyAnsweringRuleInfoCallHandlingAction        | ❌       | Specifies how incoming calls are forwarded. The default value is 'Operator' 'Operator' - play company greeting and forward to operator extension 'Disconnect' - play company greeting and disconnect 'Bypass' - bypass greeting to go to selected extension = ['Operator', 'Disconnect', 'Bypass'] |
| extension            | CompanyAnsweringRuleExtensionInfoRequest          | ❌       | Extension to which the call is forwarded in 'Bypass' mode                                                                                                                                                                                                                                          |
| greetings            | List[GreetingInfo]                                | ❌       | Greetings applied for an answering rule; only predefined greetings can be applied, see Dictionary Greeting List                                                                                                                                                                                    |

# CompanyAnsweringRuleInfoType

Type of an answering rule

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| BUSINESSHOURS | str  | ✅       | "BusinessHours" |
| AFTERHOURS    | str  | ✅       | "AfterHours"    |
| CUSTOM        | str  | ✅       | "Custom"        |

# CompanyAnsweringRuleInfoCallHandlingAction

Specifies how incoming calls are forwarded. The default value is 'Operator' 'Operator' - play company greeting and forward to operator extension 'Disconnect' - play company greeting and disconnect 'Bypass' - bypass greeting to go to selected extension = ['Operator', 'Disconnect', 'Bypass']

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| OPERATOR   | str  | ✅       | "Operator"   |
| DISCONNECT | str  | ✅       | "Disconnect" |
| BYPASS     | str  | ✅       | "Bypass"     |

<!-- This file was generated by liblab | https://liblab.com/ -->
