# ForwardingInfo

Forwarding parameters. Returned if 'ForwardCalls' is specified in 'callHandlingAction'. These settings determine the forwarding numbers to which the call will be forwarded

**Properties**

| Name                     | Type                      | Required | Description                                                                                                                                                                                                                                 |
| :----------------------- | :------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| notify_my_soft_phones    | bool                      | ❌       | Specifies if the user's softphone(s) are notified before forwarding the incoming call to desk phones and forwarding numbers                                                                                                                 |
| notify_admin_soft_phones | bool                      | ❌       | Deprecated parameter. Specifies if the administrator's softphone is notified before forwarding the incoming call to desk phones and forwarding numbers. The default value is `false`                                                        |
| soft_phones_ring_count   | int                       | ❌       | Number of rings before forwarding starts                                                                                                                                                                                                    |
| soft_phones_always_ring  | bool                      | ❌       | Specifies that desktop and mobile applications of the user will ring till the end of their forwarding list. If set to `true` then `softPhonesRingCount` is ignored                                                                          |
| ringing_mode             | ForwardingInfoRingingMode | ❌       | Specifies the order in which the forwarding numbers ring. 'Sequentially' means that forwarding numbers are ringing one at a time, in order of priority. 'Simultaneously' means that forwarding numbers are ring all at the same time        |
| rules                    | List[ForwardingRuleInfo]  | ❌       | Information on a call forwarding rule                                                                                                                                                                                                       |
| soft_phones_position_top | bool                      | ❌       | Specifies if desktop and mobile applications of the user are notified before (true) or after (false) forwarding the incoming call to desk phones and forwarding numbers. Applicable only if `notifyMySoftPhones` parameter is set to `true` |
| mobile_timeout           | bool                      | ❌       | Deprecated parameter. Specifies if mobile timeout is activated for the rule                                                                                                                                                                 |

# ForwardingInfoRingingMode

Specifies the order in which the forwarding numbers ring. 'Sequentially' means that forwarding numbers are ringing one at a time, in order of priority. 'Simultaneously' means that forwarding numbers are ring all at the same time

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| SEQUENTIALLY   | str  | ✅       | "Sequentially"   |
| SIMULTANEOUSLY | str  | ✅       | "Simultaneously" |

<!-- This file was generated by liblab | https://liblab.com/ -->
