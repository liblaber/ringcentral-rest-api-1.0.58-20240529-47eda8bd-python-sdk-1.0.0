# CompanyAnsweringRuleRequest

**Properties**

| Name                 | Type                                          | Required | Description                                                                                                                                                                                                                                                                                        |
| :------------------- | :-------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                 | str                                           | ❌       | Name of an answering rule specified by user. Max number of symbols is 30. The default value is 'My Rule N' where 'N' is the first free number                                                                                                                                                      |
| enabled              | bool                                          | ❌       | Specifies if the rule is active or inactive. The default value is `true`                                                                                                                                                                                                                           |
| type\_               | CompanyAnsweringRuleRequestType               | ❌       | Type of an answering rule, the default value is 'Custom' = ['BusinessHours', 'AfterHours', 'Custom']                                                                                                                                                                                               |
| callers              | List[CompanyAnsweringRuleCallersInfoRequest]  | ❌       | Answering rule will be applied when calls are received from the specified caller(s)                                                                                                                                                                                                                |
| called_numbers       | List[CompanyAnsweringRuleCalledNumberInfo]    | ❌       | Answering rule will be applied when calling the specified number(s)                                                                                                                                                                                                                                |
| schedule             | CompanyAnsweringRuleScheduleInfoRequest       | ❌       | Schedule when an answering rule should be applied                                                                                                                                                                                                                                                  |
| call_handling_action | CompanyAnsweringRuleRequestCallHandlingAction | ❌       | Specifies how incoming calls are forwarded. The default value is 'Operator' 'Operator' - play company greeting and forward to operator extension 'Disconnect' - play company greeting and disconnect 'Bypass' - bypass greeting to go to selected extension = ['Operator', 'Disconnect', 'Bypass'] |
| extension            | CompanyAnsweringRuleExtensionInfoRequest      | ❌       | Extension to which the call is forwarded in 'Bypass' mode                                                                                                                                                                                                                                          |
| greetings            | List[GreetingInfo]                            | ❌       | Greetings applied for an answering rule; only predefined greetings can be applied, see Dictionary Greeting List                                                                                                                                                                                    |

# CompanyAnsweringRuleRequestType

Type of an answering rule, the default value is 'Custom' = ['BusinessHours', 'AfterHours', 'Custom']

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| BUSINESSHOURS | str  | ✅       | "BusinessHours" |
| AFTERHOURS    | str  | ✅       | "AfterHours"    |
| CUSTOM        | str  | ✅       | "Custom"        |

# CompanyAnsweringRuleRequestCallHandlingAction

Specifies how incoming calls are forwarded. The default value is 'Operator' 'Operator' - play company greeting and forward to operator extension 'Disconnect' - play company greeting and disconnect 'Bypass' - bypass greeting to go to selected extension = ['Operator', 'Disconnect', 'Bypass']

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| OPERATOR   | str  | ✅       | "Operator"   |
| DISCONNECT | str  | ✅       | "Disconnect" |
| BYPASS     | str  | ✅       | "Bypass"     |

<!-- This file was generated by liblab | https://liblab.com/ -->
