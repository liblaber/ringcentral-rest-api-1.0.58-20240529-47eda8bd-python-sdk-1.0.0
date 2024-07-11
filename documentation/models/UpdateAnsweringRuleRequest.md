# UpdateAnsweringRuleRequest

**Properties**

| Name                     | Type                                         | Required | Description                                                                                                                                                                                                                                                                                                                                                                        |
| :----------------------- | :------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                     | str                                          | ❌       | Identifier of an answering rule                                                                                                                                                                                                                                                                                                                                                    |
| forwarding               | ForwardingInfoCreateRuleRequest              | ❌       | Forwarding parameters. Returned if 'ForwardCalls' is specified in 'callHandlingAction'. These settings determine the forwarding numbers to which the call will be forwarded                                                                                                                                                                                                        |
| enabled                  | bool                                         | ❌       | Specifies if the rule is active or inactive. The default value is `true`                                                                                                                                                                                                                                                                                                           |
| name                     | str                                          | ❌       | Name of an answering rule specified by user                                                                                                                                                                                                                                                                                                                                        |
| callers                  | List[CallersInfoRequest]                     | ❌       | Answering rule will be applied when calls are received from the specified caller(s)                                                                                                                                                                                                                                                                                                |
| called_numbers           | List[CalledNumberInfo]                       | ❌       | Answering rules are applied when calling to selected number(s)                                                                                                                                                                                                                                                                                                                     |
| schedule                 | ScheduleInfo                                 | ❌       | Schedule when an answering rule should be applied                                                                                                                                                                                                                                                                                                                                  |
| call_handling_action     | UpdateAnsweringRuleRequestCallHandlingAction | ❌       | Specifies how incoming calls are forwarded                                                                                                                                                                                                                                                                                                                                         |
| type\_                   | UpdateAnsweringRuleRequestType               | ❌       | Type of an answering rule                                                                                                                                                                                                                                                                                                                                                          |
| unconditional_forwarding | UnconditionalForwardingInfo                  | ❌       | Unconditional forwarding parameters. Returned if 'UnconditionalForwarding' value is specified for the `callHandlingAction` parameter                                                                                                                                                                                                                                               |
| queue                    | QueueInfo                                    | ❌       | Queue settings applied for department (call queue) extension type, with the 'AgentQueue' value specified as a call handling action                                                                                                                                                                                                                                                 |
| voicemail                | VoicemailInfo                                | ❌       | Specifies whether to take a voicemail and who should do it                                                                                                                                                                                                                                                                                                                         |
| missed_call              | MissedCallInfo                               | ❌       | Specifies behavior for the missed call scenario. Returned only if `enabled` parameter of a voicemail is set to 'false'                                                                                                                                                                                                                                                             |
| greetings                | List[GreetingInfo]                           | ❌       | Greetings applied for an answering rule; only predefined greetings can be applied, see Dictionary Greeting List                                                                                                                                                                                                                                                                    |
| screening                | UpdateAnsweringRuleRequestScreening          | ❌       | Call screening status. 'Off' - no call screening; 'NoCallerId' - if caller ID is missing, then callers are asked to say their name before connecting; 'UnknownCallerId' - if caller ID is not in contact list, then callers are asked to say their name before connecting; 'Always' - the callers are always asked to say their name before connecting. The default value is 'Off' |
| show_inactive_numbers    | bool                                         | ❌       | Indicates whether inactive numbers should be returned or not                                                                                                                                                                                                                                                                                                                       |
| transfer                 | TransferredExtensionInfo                     | ❌       |                                                                                                                                                                                                                                                                                                                                                                                    |

# UpdateAnsweringRuleRequestCallHandlingAction

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

# UpdateAnsweringRuleRequestType

Type of an answering rule

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| BUSINESSHOURS | str  | ✅       | "BusinessHours" |
| AFTERHOURS    | str  | ✅       | "AfterHours"    |
| CUSTOM        | str  | ✅       | "Custom"        |

# UpdateAnsweringRuleRequestScreening

Call screening status. 'Off' - no call screening; 'NoCallerId' - if caller ID is missing, then callers are asked to say their name before connecting; 'UnknownCallerId' - if caller ID is not in contact list, then callers are asked to say their name before connecting; 'Always' - the callers are always asked to say their name before connecting. The default value is 'Off'

**Properties**

| Name            | Type | Required | Description       |
| :-------------- | :--- | :------- | :---------------- |
| OFF             | str  | ✅       | "Off"             |
| NOCALLERID      | str  | ✅       | "NoCallerId"      |
| UNKNOWNCALLERID | str  | ✅       | "UnknownCallerId" |
| ALWAYS          | str  | ✅       | "Always"          |

<!-- This file was generated by liblab | https://liblab.com/ -->
