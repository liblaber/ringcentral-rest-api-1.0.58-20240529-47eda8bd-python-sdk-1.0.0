# ScheduleInfo

Schedule when an answering rule should be applied

**Properties**

| Name          | Type               | Required | Description                                                                                                                    |
| :------------ | :----------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------- |
| weekly_ranges | WeeklyScheduleInfo | ❌       | Weekly schedule                                                                                                                |
| ranges        | List[RangesInfo]   | ❌       | Specific data ranges                                                                                                           |
| ref           | ScheduleInfoRef    | ❌       | The user's schedule specified for business hours or after hours; it can also be set/retrieved calling the corresponding method |

# ScheduleInfoRef

The user's schedule specified for business hours or after hours; it can also be set/retrieved calling the corresponding method

**Properties**

| Name          | Type | Required | Description     |
| :------------ | :--- | :------- | :-------------- |
| BUSINESSHOURS | str  | ✅       | "BusinessHours" |
| AFTERHOURS    | str  | ✅       | "AfterHours"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
