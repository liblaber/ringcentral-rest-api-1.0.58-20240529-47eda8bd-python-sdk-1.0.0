# MissedCallInfo

Specifies behavior for the missed call scenario. Returned only if `enabled` parameter of a voicemail is set to 'false'

**Properties**

| Name        | Type                    | Required | Description                                                                                                                                                                                                                                      |
| :---------- | :---------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action_type | ActionType              | ❌       | Specifies the action that should be executed on a missed call. It can either be playing greeting message and disconnection, or sending call to a calling group. If 'ConnectToExtension' is set, then calling group extension should be specified |
| extension   | MissedCallExtensionInfo | ❌       | Specifies an extension (a calling group) which should be used for the missed call transfer. Returned only if the `actionType` is set to 'ConnectToExtension'                                                                                     |

# ActionType

Specifies the action that should be executed on a missed call. It can either be playing greeting message and disconnection, or sending call to a calling group. If 'ConnectToExtension' is set, then calling group extension should be specified

**Properties**

| Name                      | Type | Required | Description                 |
| :------------------------ | :--- | :------- | :-------------------------- |
| PLAYGREETINGANDDISCONNECT | str  | ✅       | "PlayGreetingAndDisconnect" |
| CONNECTTOEXTENSION        | str  | ✅       | "ConnectToExtension"        |
| CONNECTTOEXTERNALNUMBER   | str  | ✅       | "ConnectToExternalNumber"   |

<!-- This file was generated by liblab | https://liblab.com/ -->
