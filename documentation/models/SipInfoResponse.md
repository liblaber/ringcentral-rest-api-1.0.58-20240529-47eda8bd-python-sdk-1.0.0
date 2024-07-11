# SipInfoResponse

**Properties**

| Name                        | Type                     | Required | Description                                                                                                                                                                                                                                                              |
| :-------------------------- | :----------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username                    | str                      | ❌       | User credentials                                                                                                                                                                                                                                                         |
| password                    | str                      | ❌       | User password. Not returned if SipDigest is not enabled                                                                                                                                                                                                                  |
| authorization_types         | List[AuthorizationType]  | ❌       | Supported authorization types and their priority for clients                                                                                                                                                                                                             |
| authorization_id            | str                      | ❌       | Identifier for SIP authorization                                                                                                                                                                                                                                         |
| domain                      | str                      | ❌       | SIP domain                                                                                                                                                                                                                                                               |
| outbound_proxy              | str                      | ❌       | SIP outbound proxy server address (in the format `<host:port>`                                                                                                                                                                                                           |
| outbound_proxy_i_pv6        | str                      | ❌       | SIP outbound IPv6 proxy server address (in the format `<host:port>`)                                                                                                                                                                                                     |
| outbound_proxy_backup       | str                      | ❌       | SIP outbound proxy server backup address (in the format `<host:port>`)                                                                                                                                                                                                   |
| outbound_proxy_i_pv6_backup | str                      | ❌       | SIP outbound IPv6 proxy server backup address (in the format `<host:port>`)                                                                                                                                                                                              |
| transport                   | SipInfoResponseTransport | ❌       | Preferred transport. SIP info will be returned for this transport if supported                                                                                                                                                                                           |
| certificate                 | str                      | ❌       | For TLS transport only, Base64 encoded certificate                                                                                                                                                                                                                       |
| switch_back_interval        | int                      | ❌       | The interval in seconds after which the app must try to switch back to primary proxy if it was previously switched to backup. If this parameter is not returned, the app must stay on backup proxy and try to switch to primary proxy after the next SIP-provision call. |
| stun_servers                | List[str]                | ❌       | List of stun servers in the format `<host:port>`                                                                                                                                                                                                                         |

# SipInfoResponseTransport

Preferred transport. SIP info will be returned for this transport if supported

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| UDP  | str  | ✅       | "UDP"       |
| TCP  | str  | ✅       | "TCP"       |
| TLS  | str  | ✅       | "TLS"       |
| WSS  | str  | ✅       | "WSS"       |

<!-- This file was generated by liblab | https://liblab.com/ -->
