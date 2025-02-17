# PartySuperviseRequest

**Properties**

| Name                 | Type                          | Required | Description                                                                                                                                                                                                                                  |
| :------------------- | :---------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mode                 | PartySuperviseRequestMode     | ✅       | Supervising mode                                                                                                                                                                                                                             |
| supervisor_device_id | str                           | ✅       | Internal identifier of a supervisor's device                                                                                                                                                                                                 |
| agent_extension_id   | str                           | ✅       | Mailbox ID of a user that will be monitored                                                                                                                                                                                                  |
| auto_answer          | bool                          | ❌       | Specifies if auto-answer SIP header should be sent. If auto-answer is set to `true`, the call is automatically answered by the supervising party, if set to `false` - then the supervising party has to accept or decline the monitored call |
| media_sdp            | PartySuperviseRequestMediaSdp | ❌       | Specifies session description protocol (SDP) setting. The possible values are 'sendOnly' (only sending) meaning one-way audio streaming; and 'sendRecv' (sending/receiving) meaning two-way audio streaming                                  |

# PartySuperviseRequestMode

Supervising mode

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| LISTEN | str  | ✅       | "Listen"    |

# PartySuperviseRequestMediaSdp

Specifies session description protocol (SDP) setting. The possible values are 'sendOnly' (only sending) meaning one-way audio streaming; and 'sendRecv' (sending/receiving) meaning two-way audio streaming

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| SENDONLY | str  | ✅       | "sendOnly"  |
| SENDRECV | str  | ✅       | "sendRecv"  |

<!-- This file was generated by liblab | https://liblab.com/ -->
