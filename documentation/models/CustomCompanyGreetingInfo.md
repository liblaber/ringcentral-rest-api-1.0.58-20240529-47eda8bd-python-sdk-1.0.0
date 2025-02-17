# CustomCompanyGreetingInfo

**Properties**

| Name           | Type                                 | Required | Description                                                                                                     |
| :------------- | :----------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------- |
| uri            | str                                  | ❌       | Link to an extension custom greeting                                                                            |
| id\_           | str                                  | ❌       | Internal identifier of an answering rule                                                                        |
| type\_         | CustomCompanyGreetingInfoType        | ❌       | Type of company greeting                                                                                        |
| content_type   | CustomCompanyGreetingInfoContentType | ❌       | Content media type                                                                                              |
| content_uri    | str                                  | ❌       | Link to a greeting content (audio file)                                                                         |
| answering_rule | CustomGreetingAnsweringRuleInfo      | ❌       | Information on an answering rule that the greeting is applied to                                                |
| language       | CustomCompanyGreetingLanguageInfo    | ❌       | Information on a greeting language. Supported for types 'StopRecording', 'StartRecording', 'AutomaticRecording' |

# CustomCompanyGreetingInfoType

Type of company greeting

**Properties**

| Name               | Type | Required | Description          |
| :----------------- | :--- | :------- | :------------------- |
| COMPANY            | str  | ✅       | "Company"            |
| STARTRECORDING     | str  | ✅       | "StartRecording"     |
| STOPRECORDING      | str  | ✅       | "StopRecording"      |
| AUTOMATICRECORDING | str  | ✅       | "AutomaticRecording" |
| TEMPLATEGREETING   | str  | ✅       | "TemplateGreeting"   |

# CustomCompanyGreetingInfoContentType

Content media type

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| AUDIO_MPEG | str  | ✅       | "audio/mpeg" |
| AUDIO_WAV  | str  | ✅       | "audio/wav"  |

<!-- This file was generated by liblab | https://liblab.com/ -->
