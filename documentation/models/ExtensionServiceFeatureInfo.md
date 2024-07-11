# ExtensionServiceFeatureInfo

**Properties**

| Name         | Type                                   | Required | Description                                                                                                                                                                                                                                                                   |
| :----------- | :------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enabled      | bool                                   | ❌       | Feature status; shows feature availability for an extension                                                                                                                                                                                                                   |
| feature_name | ExtensionServiceFeatureInfoFeatureName | ❌       | Feature name                                                                                                                                                                                                                                                                  |
| reason       | str                                    | ❌       | Reason for limitation of a particular service feature. Returned only if the enabled parameter value is `false`, see Service Feature Limitations and Reasons. When retrieving service features for an extension, the reasons for limitations, if any, are returned in response |

# ExtensionServiceFeatureInfoFeatureName

Feature name

**Properties**

| Name                           | Type | Required | Description                      |
| :----------------------------- | :--- | :------- | :------------------------------- |
| ACCOUNTFEDERATION              | str  | ✅       | "AccountFederation"              |
| ARCHIVER                       | str  | ✅       | "Archiver"                       |
| AUTOMATICCALLRECORDINGMUTE     | str  | ✅       | "AutomaticCallRecordingMute"     |
| AUTOMATICINBOUNDCALLRECORDING  | str  | ✅       | "AutomaticInboundCallRecording"  |
| AUTOMATICOUTBOUNDCALLRECORDING | str  | ✅       | "AutomaticOutboundCallRecording" |
| BLOCKEDMESSAGEFORWARDING       | str  | ✅       | "BlockedMessageForwarding"       |
| CALENDAR                       | str  | ✅       | "Calendar"                       |
| CALLERIDCONTROL                | str  | ✅       | "CallerIdControl"                |
| CALLFORWARDING                 | str  | ✅       | "CallForwarding"                 |
| CALLPARK                       | str  | ✅       | "CallPark"                       |
| CALLPARKLOCATIONS              | str  | ✅       | "CallParkLocations"              |
| CALLSUPERVISION                | str  | ✅       | "CallSupervision"                |
| CALLSWITCH                     | str  | ✅       | "CallSwitch"                     |
| CALLQUALITYSURVEY              | str  | ✅       | "CallQualitySurvey"              |
| CONFERENCING                   | str  | ✅       | "Conferencing"                   |
| CONFERENCINGNUMBER             | str  | ✅       | "ConferencingNumber"             |
| CONFIGUREDELEGATES             | str  | ✅       | "ConfigureDelegates"             |
| DEVELOPERPORTAL                | str  | ✅       | "DeveloperPortal"                |
| DND                            | str  | ✅       | "DND"                            |
| DYNAMICCONFERENCE              | str  | ✅       | "DynamicConference"              |
| EMERGENCYADDRESSAUTOUPDATE     | str  | ✅       | "EmergencyAddressAutoUpdate"     |
| EMERGENCYCALLING               | str  | ✅       | "EmergencyCalling"               |
| ENCRYPTIONATREST               | str  | ✅       | "EncryptionAtRest"               |
| EXTERNALDIRECTORYINTEGRATION   | str  | ✅       | "ExternalDirectoryIntegration"   |
| FAX                            | str  | ✅       | "Fax"                            |
| FAXRECEIVING                   | str  | ✅       | "FaxReceiving"                   |
| FREESOFTPHONELINES             | str  | ✅       | "FreeSoftPhoneLines"             |
| HDVOICE                        | str  | ✅       | "HDVoice"                        |
| HIPAACOMPLIANCE                | str  | ✅       | "HipaaCompliance"                |
| INTERCOM                       | str  | ✅       | "Intercom"                       |
| INTERNATIONALCALLING           | str  | ✅       | "InternationalCalling"           |
| INTERNATIONALSMS               | str  | ✅       | "InternationalSMS"               |
| LINKEDSOFTPHONELINES           | str  | ✅       | "LinkedSoftphoneLines"           |
| MMS                            | str  | ✅       | "MMS"                            |
| MOBILEVOIPEMERGENCYCALLING     | str  | ✅       | "MobileVoipEmergencyCalling"     |
| ONDEMANDCALLRECORDING          | str  | ✅       | "OnDemandCallRecording"          |
| PAGER                          | str  | ✅       | "Pager"                          |
| PAGERRECEIVING                 | str  | ✅       | "PagerReceiving"                 |
| PAGING                         | str  | ✅       | "Paging"                         |
| PASSWORDAUTH                   | str  | ✅       | "PasswordAuth"                   |
| PROMOMESSAGE                   | str  | ✅       | "PromoMessage"                   |
| REPORTS                        | str  | ✅       | "Reports"                        |
| PRESENCE                       | str  | ✅       | "Presence"                       |
| RCTEAMS                        | str  | ✅       | "RCTeams"                        |
| RINGOUT                        | str  | ✅       | "RingOut"                        |
| SALESFORCE                     | str  | ✅       | "SalesForce"                     |
| SHAREDLINES                    | str  | ✅       | "SharedLines"                    |
| SINGLEEXTENSIONUI              | str  | ✅       | "SingleExtensionUI"              |
| SITECODES                      | str  | ✅       | "SiteCodes"                      |
| SMS                            | str  | ✅       | "SMS"                            |
| SMSRECEIVING                   | str  | ✅       | "SMSReceiving"                   |
| SOFTPHONEUPDATE                | str  | ✅       | "SoftPhoneUpdate"                |
| TELEPHONYSESSIONS              | str  | ✅       | "TelephonySessions"              |
| USERMANAGEMENT                 | str  | ✅       | "UserManagement"                 |
| VIDEOCONFERENCING              | str  | ✅       | "VideoConferencing"              |
| VOIPCALLING                    | str  | ✅       | "VoipCalling"                    |
| VOIPCALLINGONMOBILE            | str  | ✅       | "VoipCallingOnMobile"            |
| VOICEMAIL                      | str  | ✅       | "Voicemail"                      |
| VOICEMAILTOTEXT                | str  | ✅       | "VoicemailToText"                |
| WEBPHONE                       | str  | ✅       | "WebPhone"                       |

<!-- This file was generated by liblab | https://liblab.com/ -->
