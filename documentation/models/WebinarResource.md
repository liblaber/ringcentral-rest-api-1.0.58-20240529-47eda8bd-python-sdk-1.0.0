# WebinarResource

**Properties**

| Name               | Type                 | Required | Description                                                       |
| :----------------- | :------------------- | :------- | :---------------------------------------------------------------- |
| creation_time      | str                  | ✅       | Object creation time                                              |
| last_modified_time | str                  | ✅       | Object last modification time                                     |
| title              | str                  | ✅       | Webinar title                                                     |
| host               | HostModel            | ✅       |                                                                   |
| id\_               | str                  | ❌       | Internal object ID                                                |
| description        | str                  | ❌       | User-friendly description of the Webinar                          |
| settings           | WebinarSettingsModel | ❌       | Various settings which define behavior of this Webinar's Sessions |

<!-- This file was generated by liblab | https://liblab.com/ -->
