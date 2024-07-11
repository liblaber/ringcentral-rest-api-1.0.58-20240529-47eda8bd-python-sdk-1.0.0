# AggregationResponseOptionsTimers

The formula is defined by `aggregationType` and `aggregationInterval` for every timer individually. If `aggregationType` is `Sum` or `Percent`, `aggregationInterval` is not supported. If `aggregationType` is `Min`, `Max` or `Average`, `aggregationInterval` is supported, but not required. If left empty, aggregation will be performed on per-call basis

**Properties**

| Name                            | Type                        | Required | Description                                                                                                                  |
| :------------------------------ | :-------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| all_calls_duration              | AllCallsDuration            | ❌       | Aggregation of all calls duration                                                                                            |
| calls_duration_by_direction     | CallsDurationByDirection    | ❌       | Aggregation of calls duration by direction (Inbound, Outbound)                                                               |
| calls_duration_by_origin        | CallsDurationByOrigin       | ❌       | Aggregation of calls duration by origin (Internal, External)                                                                 |
| calls_duration_by_response      | CallsDurationByResponse     | ❌       | Aggregation of calls duration by response (Answered, NotAnswered, Connected, NotConnected)                                   |
| calls_segments_duration         | CallsSegmentsDuration       | ❌       | Aggregation of calls duration by segments (Ringing, LiveTalk, Hold, Park, Transfer, IvrPrompt, Voicemail, VmGreeting, Setup) |
| calls_duration_by_result        | CallsDurationByResult       | ❌       | Aggregation of calls duration by result (Completed, Abandoned, Voicemail, Unknown, Missed, Accepted)                         |
| calls_duration_by_company_hours | CallsDurationByCompanyHours | ❌       | Aggregation of calls duration by company hours (BusinessHours, AfterHours)                                                   |
| calls_duration_by_queue_sla     | CallsDurationByQueueSla     | ❌       | Aggregation of calls duration by queue SLA (InSLA, OutSLA). This timer is only applicable to Queues grouping                 |
| calls_duration_by_type          | CallsDurationByType         | ❌       | Aggregation of calls duration by type (Direct, FromQueue, ParkRetrieval, Transferred, Outbound)                              |

# AllCallsDuration

Aggregation of all calls duration

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsDurationByDirection

Aggregation of calls duration by direction (Inbound, Outbound)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsDurationByOrigin

Aggregation of calls duration by origin (Internal, External)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsDurationByResponse

Aggregation of calls duration by response (Answered, NotAnswered, Connected, NotConnected)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsSegmentsDuration

Aggregation of calls duration by segments (Ringing, LiveTalk, Hold, Park, Transfer, IvrPrompt, Voicemail, VmGreeting, Setup)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsDurationByResult

Aggregation of calls duration by result (Completed, Abandoned, Voicemail, Unknown, Missed, Accepted)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsDurationByCompanyHours

Aggregation of calls duration by company hours (BusinessHours, AfterHours)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsDurationByQueueSla

Aggregation of calls duration by queue SLA (InSLA, OutSLA). This timer is only applicable to Queues grouping

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsDurationByType

Aggregation of calls duration by type (Direct, FromQueue, ParkRetrieval, Transferred, Outbound)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

<!-- This file was generated by liblab | https://liblab.com/ -->
