# TimeSettings

Date-time range for the calls. The call is considered to be within time range if it started within time range. Both borders are inclusive

**Properties**

| Name                   | Type                 | Required | Description                                                                                                                                                                                                                                                                                                                                   |
| :--------------------- | :------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| time_zone              | str                  | ✅       | Name of the timezone that will be used for `includeDays` and `includeHours` filters and aggregation intervals. For example 'America/Los_Angeles', 'Europe/Zurich'. See also _[Time Zones](https://www.iana.org/time-zones)_. Value in this field doesn't affect interpretation of time in `timeRange`, as it already includes offset from UTC |
| time_range             | TimeRange            | ✅       | Time range for the request                                                                                                                                                                                                                                                                                                                    |
| advanced_time_settings | AdvancedTimeSettings | ❌       | Allows more granular control over time included in the report                                                                                                                                                                                                                                                                                 |

<!-- This file was generated by liblab | https://liblab.com/ -->
