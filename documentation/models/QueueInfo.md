# QueueInfo

Queue settings applied for department (call queue) extension type, with the 'AgentQueue' value specified as a call handling action

**Properties**

| Name                           | Type                              | Required | Description                                                                                                                                                                                                                                                                              |
| :----------------------------- | :-------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| transfer_mode                  | TransferMode                      | ❌       | Specifies how calls are transferred to group members                                                                                                                                                                                                                                     |
| transfer                       | List[TransferInfo]                | ❌       | Call transfer information                                                                                                                                                                                                                                                                |
| no_answer_action               | NoAnswerAction                    | ❌       | Specifies the type of action to be taken if: members are available but no one answers, or all members are busy/unavailable. This option is available for Business hours only. For simultaneous transfer mode only 'WaitPrimaryMembers' and 'WaitPrimaryAndOverflowMembers' are supported |
| fixed_order_agents             | List[FixedOrderAgents]            | ❌       | Information on a call forwarding rule                                                                                                                                                                                                                                                    |
| hold_audio_interruption_mode   | HoldAudioInterruptionMode         | ❌       | Connecting audio interruption mode                                                                                                                                                                                                                                                       |
| hold_audio_interruption_period | int                               | ❌       | Connecting audio interruption message period in seconds                                                                                                                                                                                                                                  |
| hold_time_expiration_action    | HoldTimeExpirationAction          | ❌       | Specifies the type of action to be taken after the hold time (waiting for an available call queue member) expires. If 'TransferToExtension' option is selected, the extension specified in `transfer` field is used. The default value is `Voicemail`                                    |
| agent_timeout                  | int                               | ❌       | Maximum time in seconds to wait for a call queue member before trying the next member                                                                                                                                                                                                    |
| wrap_up_time                   | int                               | ❌       | Minimum post-call wrap up time in seconds before agent status is automatically set; the value range is from 0 to 300 sec.                                                                                                                                                                |
| hold_time                      | int                               | ❌       | Maximum hold time in seconds to wait for an available call queue member                                                                                                                                                                                                                  |
| max_callers                    | int                               | ❌       | Maximum count of callers on hold; the limitation is 25 callers                                                                                                                                                                                                                           |
| max_callers_action             | MaxCallersAction                  | ❌       | Specifies the type of action to be taken if count of callers on hold exceeds the supported maximum                                                                                                                                                                                       |
| unconditional_forwarding       | List[UnconditionalForwardingInfo] | ❌       |                                                                                                                                                                                                                                                                                          |

# TransferMode

Specifies how calls are transferred to group members

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| ROTATING     | str  | ✅       | "Rotating"     |
| SIMULTANEOUS | str  | ✅       | "Simultaneous" |
| FIXEDORDER   | str  | ✅       | "FixedOrder"   |

# NoAnswerAction

Specifies the type of action to be taken if: members are available but no one answers, or all members are busy/unavailable. This option is available for Business hours only. For simultaneous transfer mode only 'WaitPrimaryMembers' and 'WaitPrimaryAndOverflowMembers' are supported

**Properties**

| Name                          | Type | Required | Description                     |
| :---------------------------- | :--- | :------- | :------------------------------ |
| WAITPRIMARYMEMBERS            | str  | ✅       | "WaitPrimaryMembers"            |
| WAITPRIMARYANDOVERFLOWMEMBERS | str  | ✅       | "WaitPrimaryAndOverflowMembers" |
| VOICEMAIL                     | str  | ✅       | "Voicemail"                     |
| TRANSFERTOEXTENSION           | str  | ✅       | "TransferToExtension"           |
| UNCONDITIONALFORWARDING       | str  | ✅       | "UnconditionalForwarding"       |

# HoldAudioInterruptionMode

Connecting audio interruption mode

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| NEVER         | str  | ✅       | "Never"         |
| WHENMUSICENDS | str  | ✅       | "WhenMusicEnds" |
| PERIODICALLY  | str  | ✅       | "Periodically"  |

# HoldTimeExpirationAction

Specifies the type of action to be taken after the hold time (waiting for an available call queue member) expires. If 'TransferToExtension' option is selected, the extension specified in `transfer` field is used. The default value is `Voicemail`

**Properties**

| Name                    | Type | Required | Description               |
| :---------------------- | :--- | :------- | :------------------------ |
| TRANSFERTOEXTENSION     | str  | ✅       | "TransferToExtension"     |
| UNCONDITIONALFORWARDING | str  | ✅       | "UnconditionalForwarding" |
| VOICEMAIL               | str  | ✅       | "Voicemail"               |

# MaxCallersAction

Specifies the type of action to be taken if count of callers on hold exceeds the supported maximum

**Properties**

| Name                    | Type | Required | Description               |
| :---------------------- | :--- | :------- | :------------------------ |
| VOICEMAIL               | str  | ✅       | "Voicemail"               |
| ANNOUNCEMENT            | str  | ✅       | "Announcement"            |
| TRANSFERTOEXTENSION     | str  | ✅       | "TransferToExtension"     |
| UNCONDITIONALFORWARDING | str  | ✅       | "UnconditionalForwarding" |

<!-- This file was generated by liblab | https://liblab.com/ -->
