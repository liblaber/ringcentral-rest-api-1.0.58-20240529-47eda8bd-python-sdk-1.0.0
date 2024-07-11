# TmTaskInfo

**Properties**

| Name                    | Type                            | Required | Description                                                                                      |
| :---------------------- | :------------------------------ | :------- | :----------------------------------------------------------------------------------------------- |
| id\_                    | str                             | ❌       | Internal identifier of a task                                                                    |
| creation_time           | str                             | ❌       | Task creation date/time in UTC time zone                                                         |
| last_modified_time      | str                             | ❌       | Task the last modified time in UTC time zone                                                     |
| type\_                  | TmTaskInfoType                  | ❌       | Task type                                                                                        |
| creator                 | Creator                         | ❌       |                                                                                                  |
| chat_ids                | List[str]                       | ❌       | Internal identifiers of the chats where the task is posted or shared                             |
| status                  | TmTaskInfoStatus                | ❌       | Task execution status                                                                            |
| subject                 | str                             | ❌       | Task name/subject                                                                                |
| assignees               | List[TmTaskInfoAssignees]       | ❌       | Task name/subject                                                                                |
| completeness_condition  | TmTaskInfoCompletenessCondition | ❌       | How the task completeness should be determined                                                   |
| completeness_percentage | int                             | ❌       | Current completeness percentage of the task with the specified percentage completeness condition |
| start_date              | str                             | ❌       | Task start date                                                                                  |
| due_date                | str                             | ❌       | Task due date/time                                                                               |
| color                   | TmTaskInfoColor                 | ❌       | Font color of a post with the current task                                                       |
| section                 | str                             | ❌       | Task section to group / search by                                                                |
| description             | str                             | ❌       | Task details                                                                                     |
| recurrence              | TaskRecurrenceInfo              | ❌       | Task information                                                                                 |
| attachments             | List[TaskAttachment]            | ❌       |                                                                                                  |

# TmTaskInfoType

Task type

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| TASK | str  | ✅       | "Task"      |

# Creator

**Properties**

| Name | Type | Required | Description                           |
| :--- | :--- | :------- | :------------------------------------ |
| id\_ | str  | ❌       | Internal identifier of a task creator |

# TmTaskInfoStatus

Task execution status

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| PENDING    | str  | ✅       | "Pending"    |
| INPROGRESS | str  | ✅       | "InProgress" |
| COMPLETED  | str  | ✅       | "Completed"  |

# TmTaskInfoAssignees

**Properties**

| Name   | Type            | Required | Description                        |
| :----- | :-------------- | :------- | :--------------------------------- |
| id\_   | str             | ❌       | Internal identifier of an assignee |
| status | AssigneesStatus | ❌       | Task execution status by assignee  |

# AssigneesStatus

Task execution status by assignee

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| PENDING   | str  | ✅       | "Pending"   |
| COMPLETED | str  | ✅       | "Completed" |

# TmTaskInfoCompletenessCondition

How the task completeness should be determined

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| SIMPLE       | str  | ✅       | "Simple"       |
| ALLASSIGNEES | str  | ✅       | "AllAssignees" |
| PERCENTAGE   | str  | ✅       | "Percentage"   |

# TmTaskInfoColor

Font color of a post with the current task

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
