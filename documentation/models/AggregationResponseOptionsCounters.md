# AggregationResponseOptionsCounters

The formula is defined by `aggregationType` and `aggregationInterval` for every counter individually. If `aggregationType` is `Sum` or `Percent`, `aggregationInterval` is not supported. If `aggregationType` is `Min`, `Max` or `Average`, `aggregationInterval` is required

**Properties**

| Name                   | Type                                                  | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :--------------------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| all_calls              | AggregationResponseOptionsCountersAllCalls            | ❌       | Aggregation of all calls count                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| calls_by_direction     | AggregationResponseOptionsCountersCallsByDirection    | ❌       | Aggregation of calls count by direction (Inbound, Outbound)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| calls_by_origin        | AggregationResponseOptionsCountersCallsByOrigin       | ❌       | Aggregation of calls count by origin (Internal, External)                                                                                                                                                                                                                                                                                                                                                                                                                      |
| calls_by_response      | AggregationResponseOptionsCountersCallsByResponse     | ❌       | Aggregation of calls count by response (Answered, NotAnswered, Connected, NotConnected)                                                                                                                                                                                                                                                                                                                                                                                        |
| calls_segments         | CallsSegments                                         | ❌       | Aggregation of calls count by segments (Ringing, LiveTalk, Hold, Park, Transfer, IvrPrompt, Voicemail, VmGreeting, Setup)                                                                                                                                                                                                                                                                                                                                                      |
| calls_by_result        | AggregationResponseOptionsCountersCallsByResult       | ❌       | Aggregation of calls count by result (Completed, Abandoned, Voicemail, Unknown, Missed, Accepted)                                                                                                                                                                                                                                                                                                                                                                              |
| calls_by_company_hours | AggregationResponseOptionsCountersCallsByCompanyHours | ❌       | Aggregation of calls count by company hours (BusinessHours, AfterHours)                                                                                                                                                                                                                                                                                                                                                                                                        |
| calls_by_queue_sla     | AggregationResponseOptionsCountersCallsByQueueSla     | ❌       | Aggregation of calls count by queue SLA (InSLA, OutSLA). This counter is only applicable to Queues grouping                                                                                                                                                                                                                                                                                                                                                                    |
| calls_by_actions       | AggregationResponseOptionsCountersCallsByActions      | ❌       | Aggregation of calls count by action (HoldOff, HoldOn, ParkOn, ParkOff, BlindTransfer, WarmTransfer, DTMFTransfer)                                                                                                                                                                                                                                                                                                                                                             |
| calls_by_type          | AggregationResponseOptionsCountersCallsByType         | ❌       | Aggregation of calls count by type (Direct, FromQueue, ParkRetrieval, Transferred, Outbound)                                                                                                                                                                                                                                                                                                                                                                                   |
| queue_opportunities    | AggregationResponseOptionsCountersQueueOpportunities  | ❌       | Aggregation of calls count by the total number of times a Queue call was presented to the user. It is limited to `groupBy` Users and `groupByMembers` (Department, Queue, Site, UserGroup) grouping. Only the listed below options for call filters are applicable to `queueOpportunities` and provide meaningful results: `queues` (selected queue extension ids), `callResults` (Missed, Abandoned), `callResponses` (Answered, NotAnswered), `origins` (Internal, External) |

# AggregationResponseOptionsCountersAllCalls

Aggregation of all calls count

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByDirection

Aggregation of calls count by direction (Inbound, Outbound)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByOrigin

Aggregation of calls count by origin (Internal, External)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByResponse

Aggregation of calls count by response (Answered, NotAnswered, Connected, NotConnected)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# CallsSegments

Aggregation of calls count by segments (Ringing, LiveTalk, Hold, Park, Transfer, IvrPrompt, Voicemail, VmGreeting, Setup)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByResult

Aggregation of calls count by result (Completed, Abandoned, Voicemail, Unknown, Missed, Accepted)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByCompanyHours

Aggregation of calls count by company hours (BusinessHours, AfterHours)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByQueueSla

Aggregation of calls count by queue SLA (InSLA, OutSLA). This counter is only applicable to Queues grouping

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByActions

Aggregation of calls count by action (HoldOff, HoldOn, ParkOn, ParkOff, BlindTransfer, WarmTransfer, DTMFTransfer)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersCallsByType

Aggregation of calls count by type (Direct, FromQueue, ParkRetrieval, Transferred, Outbound)

**Properties**

| Name                 | Type                | Required | Description                                                                               |
| :------------------- | :------------------ | :------- | :---------------------------------------------------------------------------------------- |
| aggregation_type     | AggregationType     | ✅       | Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`              |
| aggregation_interval | AggregationInterval | ❌       | Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month` |

# AggregationResponseOptionsCountersQueueOpportunities

Aggregation of calls count by the total number of times a Queue call was presented to the user. It is limited to `groupBy` Users and `groupByMembers` (Department, Queue, Site, UserGroup) grouping. Only the listed below options for call filters are applicable to `queueOpportunities` and provide meaningful results: `queues` (selected queue extension ids), `callResults` (Missed, Abandoned), `callResponses` (Answered, NotAnswered), `origins` (Internal, External)

**Properties**

| Name             | Type                              | Required | Description                                                              |
| :--------------- | :-------------------------------- | :------- | :----------------------------------------------------------------------- |
| aggregation_type | QueueOpportunitiesAggregationType | ✅       | Counter aggregation type for queue opportunities, limited to `Sum` only. |

<!-- This file was generated by liblab | https://liblab.com/ -->
