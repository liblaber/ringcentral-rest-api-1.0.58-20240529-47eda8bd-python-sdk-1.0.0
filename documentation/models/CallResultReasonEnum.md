# CallResultReasonEnum

The reason of the call result: - `Accepted` - The call was connected to and accepted by this number - `Connected` - The call was answered, but there was no response on how to handle the call (for example, a voice mail system answered the call and did not push "1" to accept) - `Line Busy` - The phone number you dialed was busy - `Not Answered` - The phone number you dialed was not answered - `No Answer` - You did not answer the call - `Hang Up` - The caller hung up before the call was answered - `Stopped` - This attempt was stopped because the call was answered by another phone - `Internal Error` - An internal error occurred when making the call. Please try again - `No Credit` - There was not enough Calling Credit on your account to make this call - `Restricted Number` - The number you dialed is restricted by RingCentral - `Wrong Number` - The number you dialed has either been disconnected or is not a valid phone number. Please check the number and try again - `International Disabled` - International calling is not enabled on your account. Contact customer service to activate International Calling - `International Restricted` - The country and/or area you attempted to call has been prohibited by your administrator - `Bad Number` - An error occurred when making the call. Please check the number before trying again - `Info 411 Restricted` - Calling to 411 Information Services is restricted - `Customer 611 Restricted` - 611 customer service is not supported. Please contact customer service at ```(888) 555-1212````   - `No Digital Line`- This DigitalLine was either not plugged in or did not have an internet connection   -`Failed Try Again`- Call failed. Please try again   -`Max Call Limit`- The number of simultaneous calls to your account has reached its limit   -`Too Many Calls`- The number of simultaneous calls for per DigitalLine associated with Other Phone has reached its limit. Please contact customer service   -`Calls Not Accepted`- Your account was not accepting calls at this time   -`Number Not Allowed`- The number that was dialed to access your account is not allowed   -`Number Blocked`- This number is in your Blocked Numbers list   -`Number Disabled`- The phone number and/or area you attempted to call has been prohibited by your administrator   -`Resource Error`- An error occurred when making the call. Please try again   -`Call Loop`- A call loop occurred due to an incorrect call forwarding configuration. Please check that you are not forwarding calls back to your own account   -`Fax Not Received`- An incoming fax could not be received because a proper connection with the sender's fax machine could not be established   -`Fax Partially Sent`- The fax was only partially sent. Possible explanations include phone line quality to poor to maintain the connection or the call was dropped   -`Fax Not Sent`- An attempt to send the fax was made, but could not connect with the receiving fax machine   -`Fax Poor Line`- An attempt to send the fax was made, but the phone line quality was too poor to send the fax   -`Fax Prepare Error`- An internal error occurred when preparing the fax. Please try again   -`Fax Save Error`- An internal error occurred when saving the fax. Please try again   -`Fax Send Error`- An error occurred when sending the fax. Please try again   -`Emergency Address not defined`- The call was rejected due to no E911 address   -`Carrier is not active`- The call was rejected due to carrier inactivity   -`EDGE trunk misconfigured`- The call was rejected due to error in EDGE trunk configuration   -`Internal Call Error`- An internal error occurred when making the call. Please try again   -`Receive Error` - Fax receive error

**Properties**

| Name                          | Type | Required | Description                     |
| :---------------------------- | :--- | :------- | :------------------------------ |
| ACCEPTED                      | str  | ✅       | "Accepted"                      |
| BAD_NUMBER                    | str  | ✅       | "Bad Number"                    |
| CALL_LOOP                     | str  | ✅       | "Call Loop"                     |
| CALLS_NOT_ACCEPTED            | str  | ✅       | "Calls Not Accepted"            |
| CARRIER_IS_NOT_ACTIVE         | str  | ✅       | "Carrier is not active"         |
| CONNECTED                     | str  | ✅       | "Connected"                     |
| CUSTOMER_611_RESTRICTED       | str  | ✅       | "Customer 611 Restricted"       |
| EDGE_TRUNK_MISCONFIGURED      | str  | ✅       | "EDGE trunk misconfigured"      |
| EMERGENCY_ADDRESS_NOT_DEFINED | str  | ✅       | "Emergency Address not defined" |
| FAILED_TRY_AGAIN              | str  | ✅       | "Failed Try Again"              |
| FAX_NOT_RECEIVED              | str  | ✅       | "Fax Not Received"              |
| FAX_NOT_SENT                  | str  | ✅       | "Fax Not Sent"                  |
| FAX_PARTIALLY_SENT            | str  | ✅       | "Fax Partially Sent"            |
| FAX_POOR_LINE                 | str  | ✅       | "Fax Poor Line"                 |
| FAX_PREPARE_ERROR             | str  | ✅       | "Fax Prepare Error"             |
| FAX_SAVE_ERROR                | str  | ✅       | "Fax Save Error"                |
| FAX_SEND_ERROR                | str  | ✅       | "Fax Send Error"                |
| HANG_UP                       | str  | ✅       | "Hang Up"                       |
| INFO_411_RESTRICTED           | str  | ✅       | "Info 411 Restricted"           |
| INTERNAL_CALL_ERROR           | str  | ✅       | "Internal Call Error"           |
| INTERNAL_ERROR                | str  | ✅       | "Internal Error"                |
| INTERNATIONAL_DISABLED        | str  | ✅       | "International Disabled"        |
| INTERNATIONAL_RESTRICTED      | str  | ✅       | "International Restricted"      |
| LINE_BUSY                     | str  | ✅       | "Line Busy"                     |
| MAX_CALL_LIMIT                | str  | ✅       | "Max Call Limit"                |
| NO_ANSWER                     | str  | ✅       | "No Answer"                     |
| NO_CREDIT                     | str  | ✅       | "No Credit"                     |
| NO_DIGITAL_LINE               | str  | ✅       | "No Digital Line"               |
| NOT_ANSWERED                  | str  | ✅       | "Not Answered"                  |
| NUMBER_BLOCKED                | str  | ✅       | "Number Blocked"                |
| NUMBER_DISABLED               | str  | ✅       | "Number Disabled"               |
| NUMBER_NOT_ALLOWED            | str  | ✅       | "Number Not Allowed"            |
| RECEIVE_ERROR                 | str  | ✅       | "Receive Error"                 |
| RESOURCE_ERROR                | str  | ✅       | "Resource Error"                |
| RESTRICTED_NUMBER             | str  | ✅       | "Restricted Number"             |
| STOPPED                       | str  | ✅       | "Stopped"                       |
| TOO_MANY_CALLS                | str  | ✅       | "Too Many Calls"                |
| UNKNOWN                       | str  | ✅       | "Unknown"                       |
| WRONG_NUMBER                  | str  | ✅       | "Wrong Number"                  |

<!-- This file was generated by liblab | https://liblab.com/ -->
