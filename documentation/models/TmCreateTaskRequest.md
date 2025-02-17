# TmCreateTaskRequest

**Properties**

| Name                   | Type                                     | Required | Description                                                              |
| :--------------------- | :--------------------------------------- | :------- | :----------------------------------------------------------------------- |
| subject                | str                                      | ✅       | Task name/subject. Max allowed length is 250 characters                  |
| assignees              | List[TmCreateTaskRequestAssignees]       | ✅       |                                                                          |
| completeness_condition | TmCreateTaskRequestCompletenessCondition | ❌       |                                                                          |
| start_date             | str                                      | ❌       | Task start date in UTC time zone.                                        |
| due_date               | str                                      | ❌       | Task due date/time in UTC time zone.                                     |
| color                  | TmCreateTaskRequestColor                 | ❌       |                                                                          |
| section                | str                                      | ❌       | Task section to group / search by. Max allowed length is 100 characters. |
| description            | str                                      | ❌       | Task details. Max allowed length is 102400 characters (100kB).           |
| recurrence             | TaskRecurrenceInfo                       | ❌       | Task information                                                         |
| attachments            | List[TmAttachmentInfo]                   | ❌       |                                                                          |

# TmCreateTaskRequestAssignees

**Properties**

| Name | Type | Required | Description                        |
| :--- | :--- | :------- | :--------------------------------- |
| id\_ | str  | ❌       | Internal identifier of an assignee |

# TmCreateTaskRequestCompletenessCondition

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| SIMPLE       | str  | ✅       | "Simple"       |
| ALLASSIGNEES | str  | ✅       | "AllAssignees" |
| PERCENTAGE   | str  | ✅       | "Percentage"   |

# TmCreateTaskRequestColor

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| BLACK   | str  | ✅       | "Black"     |
| RED     | str  | ✅       | "Red"       |
| ORANGE  | str  | ✅       | "Orange"    |
| YELLOW  | str  | ✅       | "Yellow"    |
| GREEN   | str  | ✅       | "Green"     |
| BLUE    | str  | ✅       | "Blue"      |
| PURPLE  | str  | ✅       | "Purple"    |
| MAGENTA | str  | ✅       | "Magenta"   |

<!-- This file was generated by liblab | https://liblab.com/ -->
