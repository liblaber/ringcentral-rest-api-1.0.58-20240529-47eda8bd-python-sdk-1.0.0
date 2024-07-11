# WebinarSettingsModel

Various settings which define behavior of this Webinar's Sessions

**Properties**

| Name                            | Type                                              | Required | Description                                                                                                                                                 |
| :------------------------------ | :------------------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| recording_enabled               | bool                                              | ❌       | Indicates if recording is enabled (if false all other recording settings cannot be enabled)                                                                 |
| auto_record                     | bool                                              | ❌       | Indicates if recording should start automatically when a Webinar goes live                                                                                  |
| recording_sharing_enabled       | bool                                              | ❌       | Indicates if recording can be shared                                                                                                                        |
| recording_download_enabled      | bool                                              | ❌       | Indicates if recording can be downloaded                                                                                                                    |
| recording_deletion_enabled      | bool                                              | ❌       | DEPRECATED AND REPLACED BY 'pastSessionDeletionEnabled' setting. Indicates if recording can be deleted (this setting is read-only at webinar/session level) |
| past_session_deletion_enabled   | bool                                              | ❌       | Indicates if deletion of past session along with its artifacts is enabled for host. This setting is read-only at webinar level                              |
| panelist_waiting_room           | bool                                              | ❌       | Indicates if Panelists should be places to waiting room after joining                                                                                       |
| panelist_video_enabled          | bool                                              | ❌       | Indicates if Panelists' video should be 'on' by default                                                                                                     |
| panelist_screen_sharing_enabled | bool                                              | ❌       | Indicates if Panelists' screen sharing should be 'on' by default                                                                                            |
| panelist_mute_control_enabled   | bool                                              | ❌       | Indicates if Panelists can mute/unmute themselves by default                                                                                                |
| panelist_authentication         | WebinarSettingsModelPanelistAuthentication        | ❌       | Indicates if Panelists have to be authenticated users                                                                                                       |
| attendee_authentication         | WebinarSettingsModelAttendeeAuthentication        | ❌       | Indicates if attendees have to be authenticated users                                                                                                       |
| artifacts_access_authentication | WebinarSettingsModelArtifactsAccessAuthentication | ❌       | Indicates who can access webinar artifacts. Applies to recordings at present. Applicable to other artifacts such as Q&A, Polls in the future.               |
| pstn_enabled                    | bool                                              | ❌       | Indicates if dial-in PSTN audio option is enabled by default                                                                                                |
| password                        | str                                               | ❌       | Webinar password                                                                                                                                            |
| qna_enabled                     | bool                                              | ❌       | Indicates if Q&A is enabled for the webinar (if false all other Q&A settings cannot be enabled)                                                             |
| qna_anonymous_enabled           | bool                                              | ❌       | Indicates if anonymous Q&A is enabled for the webinar                                                                                                       |
| moderated_qna_enabled           | bool                                              | ❌       | Indicate if the moderated Q&A enabled for webinar                                                                                                           |
| polls_enabled                   | bool                                              | ❌       | Indicates if polls are enabled for the webinar (if false all other polls settings cannot be enabled)                                                        |
| polls_anonymous_enabled         | bool                                              | ❌       | Indicates if anonymous poll answers are enabled for the webinar                                                                                             |
| registration_enabled            | bool                                              | ❌       | Indicates if a registration is enabled for the webinar (if false all other registration settings are ignored)                                               |
| post_webinar_redirect_uri       | str                                               | ❌       | URI to redirect users after the webinar                                                                                                                     |
| external_livestream_enabled     | bool                                              | ❌       | Indicates if livestreaming to external streaming provider is enabled                                                                                        |

# WebinarSettingsModelPanelistAuthentication

Indicates if Panelists have to be authenticated users

**Properties**

| Name                  | Type | Required | Description             |
| :-------------------- | :--- | :------- | :---------------------- |
| GUEST                 | str  | ✅       | "Guest"                 |
| AUTHENTICATEDUSER     | str  | ✅       | "AuthenticatedUser"     |
| AUTHENTICATEDCOWORKER | str  | ✅       | "AuthenticatedCoworker" |

# WebinarSettingsModelAttendeeAuthentication

Indicates if attendees have to be authenticated users

**Properties**

| Name                  | Type | Required | Description             |
| :-------------------- | :--- | :------- | :---------------------- |
| GUEST                 | str  | ✅       | "Guest"                 |
| AUTHENTICATEDUSER     | str  | ✅       | "AuthenticatedUser"     |
| AUTHENTICATEDCOWORKER | str  | ✅       | "AuthenticatedCoworker" |

# WebinarSettingsModelArtifactsAccessAuthentication

Indicates who can access webinar artifacts. Applies to recordings at present. Applicable to other artifacts such as Q&A, Polls in the future.

**Properties**

| Name                  | Type | Required | Description             |
| :-------------------- | :--- | :------- | :---------------------- |
| GUEST                 | str  | ✅       | "Guest"                 |
| AUTHENTICATEDUSER     | str  | ✅       | "AuthenticatedUser"     |
| AUTHENTICATEDCOWORKER | str  | ✅       | "AuthenticatedCoworker" |

<!-- This file was generated by liblab | https://liblab.com/ -->
