# ScheduleUserMeetingInfo

Scheduling meeting settings locked on account level \|\| Settings defining how to schedule user meetings

**Properties**

| Name                                         | Type                                      | Required | Description                                                                                                                                                              |
| :------------------------------------------- | :---------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enforce_login                                | bool                                      | ❌       | If true, then only signed-in users can join this meeting                                                                                                                 |
| start_host_video                             | bool                                      | ❌       | Starting meetings with host video on/off (true/false)                                                                                                                    |
| start_participants_video                     | bool                                      | ❌       | Starting meetings with participant video on/off (true/false)                                                                                                             |
| audio_options                                | List[ScheduleUserMeetingInfoAudioOptions] | ❌       | Determines how participants can join the audio channel of a meeting                                                                                                      |
| allow_join_before_host                       | bool                                      | ❌       | Allows participants to join the meeting before the host arrives                                                                                                          |
| use_pmi_for_scheduled_meetings               | bool                                      | ❌       | Determines whether to use Personal Meeting ID (PMI) when scheduling a meeting                                                                                            |
| use_pmi_for_instant_meetings                 | bool                                      | ❌       | Determines whether to use Personal Meeting ID (PMI) when starting an instant meeting                                                                                     |
| require_password_for_scheduling_new_meetings | bool                                      | ❌       | A password will be generated when scheduling a meeting and participants will require password to join a meeting. The Personal Meeting ID (PMI) meetings are not included |
| require_password_for_scheduled_meetings      | bool                                      | ❌       | Specifies whether to require a password for meetings which have already been scheduled                                                                                   |
| default_password_for_scheduled_meetings      | str                                       | ❌       | Password for already scheduled meetings. Users can set it individually                                                                                                   |
| require_password_for_instant_meetings        | bool                                      | ❌       | A random password will be generated for an instant meeting, if set to `true`. If you use PMI for your instant meetings, this option will be disabled                     |
| require_password_for_pmi_meetings            | RequirePasswordForPmiMeetings             | ❌       | Specifies whether to require a password for meetings using Personal Meeting ID (PMI). The supported values are: 'none', 'all' and 'jbhOnly' (joined before host only)    |
| pmi_password                                 | str                                       | ❌       | The default password for Personal Meeting ID (PMI) meetings                                                                                                              |
| pstn_password_protected                      | bool                                      | ❌       | Specifies whether to generate and require a password for participants joining by phone                                                                                   |
| mute_participants_on_entry                   | bool                                      | ❌       |                                                                                                                                                                          |

# ScheduleUserMeetingInfoAudioOptions

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| PHONE         | str  | ✅       | "Phone"         |
| COMPUTERAUDIO | str  | ✅       | "ComputerAudio" |
| THIRDPARTY    | str  | ✅       | "ThirdParty"    |

# RequirePasswordForPmiMeetings

Specifies whether to require a password for meetings using Personal Meeting ID (PMI). The supported values are: 'none', 'all' and 'jbhOnly' (joined before host only)

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| ALL     | str  | ✅       | "all"       |
| NONE    | str  | ✅       | "none"      |
| JBHONLY | str  | ✅       | "jbhOnly"   |

<!-- This file was generated by liblab | https://liblab.com/ -->
