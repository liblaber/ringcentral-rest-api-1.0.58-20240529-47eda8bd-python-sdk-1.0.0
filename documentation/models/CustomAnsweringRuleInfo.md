# CustomAnsweringRuleInfo

**Properties**

| Name                     | Type                                      | Required | Description                                                                                                                                                                                                                                                                                                                                                                        |
| :----------------------- | :---------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uri                      | str                                       | ❌       | Canonical URI to an answering rule resource                                                                                                                                                                                                                                                                                                                                        |
| id\_                     | str                                       | ❌       | Internal identifier of an answering rule                                                                                                                                                                                                                                                                                                                                           |
| type\_                   | CustomAnsweringRuleInfoType               | ❌       | Type of an answering rule                                                                                                                                                                                                                                                                                                                                                          |
| name                     | str                                       | ❌       | Name of an answering rule specified by user                                                                                                                                                                                                                                                                                                                                        |
| enabled                  | bool                                      | ❌       | Specifies if an answering rule is active or inactive                                                                                                                                                                                                                                                                                                                               |
| schedule                 | ScheduleInfo                              | ❌       | Schedule when an answering rule should be applied                                                                                                                                                                                                                                                                                                                                  |
| called_numbers           | List[CalledNumberInfo]                    | ❌       | Answering rules are applied when calling to selected number(s)                                                                                                                                                                                                                                                                                                                     |
| callers                  | List[CallersInfo]                         | ❌       | Answering rules are applied when calls are received from specified caller(s)                                                                                                                                                                                                                                                                                                       |
| call_handling_action     | CustomAnsweringRuleInfoCallHandlingAction | ❌       | Specifies how incoming calls are forwarded                                                                                                                                                                                                                                                                                                                                         |
| forwarding               | ForwardingInfo                            | ❌       | Forwarding parameters. Returned if 'ForwardCalls' is specified in 'callHandlingAction'. These settings determine the forwarding numbers to which the call will be forwarded                                                                                                                                                                                                        |
| unconditional_forwarding | UnconditionalForwardingInfo               | ❌       | Unconditional forwarding parameters. Returned if 'UnconditionalForwarding' value is specified for the `callHandlingAction` parameter                                                                                                                                                                                                                                               |
| queue                    | QueueInfo                                 | ❌       | Queue settings applied for department (call queue) extension type, with the 'AgentQueue' value specified as a call handling action                                                                                                                                                                                                                                                 |
| transfer                 | TransferredExtensionInfo                  | ❌       |                                                                                                                                                                                                                                                                                                                                                                                    |
| voicemail                | VoicemailInfo                             | ❌       | Specifies whether to take a voicemail and who should do it                                                                                                                                                                                                                                                                                                                         |
| greetings                | List[GreetingInfo]                        | ❌       | Greetings applied for an answering rule; only predefined greetings can be applied, see Dictionary Greeting List                                                                                                                                                                                                                                                                    |
| screening                | CustomAnsweringRuleInfoScreening          | ❌       | Call screening status. 'Off' - no call screening; 'NoCallerId' - if caller ID is missing, then callers are asked to say their name before connecting; 'UnknownCallerId' - if caller ID is not in contact list, then callers are asked to say their name before connecting; 'Always' - the callers are always asked to say their name before connecting. The default value is 'Off' |
| shared_lines             | SharedLinesInfo                           | ❌       | SharedLines call handling action settings                                                                                                                                                                                                                                                                                                                                          |

# CustomAnsweringRuleInfoType

Type of an answering rule

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| BUSINESSHOURS | str  | ✅       | "BusinessHours" |
| AFTERHOURS    | str  | ✅       | "AfterHours"    |
| CUSTOM        | str  | ✅       | "Custom"        |

# CustomAnsweringRuleInfoCallHandlingAction

Specifies how incoming calls are forwarded

**Properties**

| Name                    | Type | Required | Description               |
| :---------------------- | :--- | :------- | :------------------------ |
| FORWARDCALLS            | str  | ✅       | "ForwardCalls"            |
| UNCONDITIONALFORWARDING | str  | ✅       | "UnconditionalForwarding" |
| AGENTQUEUE              | str  | ✅       | "AgentQueue"              |
| TRANSFERTOEXTENSION     | str  | ✅       | "TransferToExtension"     |
| TAKEMESSAGESONLY        | str  | ✅       | "TakeMessagesOnly"        |
| PLAYANNOUNCEMENTONLY    | str  | ✅       | "PlayAnnouncementOnly"    |
| SHAREDLINES             | str  | ✅       | "SharedLines"             |

# CustomAnsweringRuleInfoScreening

Call screening status. 'Off' - no call screening; 'NoCallerId' - if caller ID is missing, then callers are asked to say their name before connecting; 'UnknownCallerId' - if caller ID is not in contact list, then callers are asked to say their name before connecting; 'Always' - the callers are always asked to say their name before connecting. The default value is 'Off'

**Properties**

| Name            | Type | Required | Description       |
| :-------------- | :--- | :------- | :---------------- |
| OFF             | str  | ✅       | "Off"             |
| NOCALLERID      | str  | ✅       | "NoCallerId"      |
| UNKNOWNCALLERID | str  | ✅       | "UnknownCallerId" |
| ALWAYS          | str  | ✅       | "Always"          |

<!-- This file was generated by liblab | https://liblab.com/ -->
