# AutomaticLocationUpdatesTaskInfo

**Properties**

| Name               | Type                                   | Required | Description                                                   |
| :----------------- | :------------------------------------- | :------- | :------------------------------------------------------------ |
| id\_               | str                                    | ❌       | Internal identifier of a task                                 |
| status             | AutomaticLocationUpdatesTaskInfoStatus | ❌       | Status of a task                                              |
| creation_time      | str                                    | ❌       | Task creation time                                            |
| last_modified_time | str                                    | ❌       | Time of the task latest modification                          |
| type\_             | AutomaticLocationUpdatesTaskInfoType   | ❌       | Type of task                                                  |
| result             | TaskResultInfo                         | ❌       | Task detailed result. Returned for failed and completed tasks |

# AutomaticLocationUpdatesTaskInfoStatus

Status of a task

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| ACCEPTED   | str  | ✅       | "Accepted"   |
| INPROGRESS | str  | ✅       | "InProgress" |
| COMPLETED  | str  | ✅       | "Completed"  |
| FAILED     | str  | ✅       | "Failed"     |

# AutomaticLocationUpdatesTaskInfoType

Type of task

**Properties**

| Name                     | Type | Required | Description                |
| :----------------------- | :--- | :------- | :------------------------- |
| WIRELESSPOINTSBULKCREATE | str  | ✅       | "WirelessPointsBulkCreate" |
| WIRELESSPOINTSBULKUPDATE | str  | ✅       | "WirelessPointsBulkUpdate" |
| SWITCHESBULKCREATE       | str  | ✅       | "SwitchesBulkCreate"       |
| SWITCHESBULKUPDATE       | str  | ✅       | "SwitchesBulkUpdate"       |

<!-- This file was generated by liblab | https://liblab.com/ -->
