# CallParty

Information on a party of a call session

**Properties**

| Name            | Type                    | Required | Description                                                                                                                                                                                                                                                                                                            |
| :-------------- | :---------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_            | str                     | ❌       | Internal identifier of a party                                                                                                                                                                                                                                                                                         |
| status          | CallStatusInfo          | ❌       | Status data of a call session                                                                                                                                                                                                                                                                                          |
| muted           | bool                    | ❌       | Specifies if a call participant is muted or not. **Note:** If a call is also controlled via Hard phone or RingCentral App (not only through the API by calling call control methods) then it cannot be fully muted/unmuted via API only, in this case the action should be duplicated via Hard phone/RC App interfaces |
| stand_alone     | bool                    | ❌       | If `true` then the party is not connected to a session voice conference, `false` means the party is connected to other parties in a session                                                                                                                                                                            |
| park            | ParkInfo                | ❌       | Call park information                                                                                                                                                                                                                                                                                                  |
| from\_          | PartyInfo               | ❌       |                                                                                                                                                                                                                                                                                                                        |
| to              | PartyInfo               | ❌       |                                                                                                                                                                                                                                                                                                                        |
| owner           | OwnerInfo               | ❌       | Deprecated. Information on a call owner                                                                                                                                                                                                                                                                                |
| direction       | CallPartyDirection      | ❌       | Direction of a call                                                                                                                                                                                                                                                                                                    |
| conference_role | CallPartyConferenceRole | ❌       | A party's role in the conference scenarios. For calls of 'Conference' type only                                                                                                                                                                                                                                        |
| ring_out_role   | CallPartyRingOutRole    | ❌       | A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only                                                                                                                                                                                                                                      |
| ring_me_role    | CallPartyRingMeRole     | ❌       | A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only                                                                                                                                                                                                                                       |
| recordings      | List[RecordingInfo]     | ❌       | Active recordings list                                                                                                                                                                                                                                                                                                 |

# CallPartyDirection

Direction of a call

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| INBOUND  | str  | ✅       | "Inbound"   |
| OUTBOUND | str  | ✅       | "Outbound"  |

# CallPartyConferenceRole

A party's role in the conference scenarios. For calls of 'Conference' type only

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| HOST        | str  | ✅       | "Host"        |
| PARTICIPANT | str  | ✅       | "Participant" |

# CallPartyRingOutRole

A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringout' type only

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| INITIATOR | str  | ✅       | "Initiator" |
| TARGET    | str  | ✅       | "Target"    |

# CallPartyRingMeRole

A party's role in 'Ring Me'/'RingOut' scenarios. For calls of 'Ringme' type only

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| INITIATOR | str  | ✅       | "Initiator" |
| TARGET    | str  | ✅       | "Target"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
