# BusinessAnalyticsService

A list of all methods in the `BusinessAnalyticsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                           |
| :---------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| [analytics_calls_aggregation_fetch](#analytics_calls_aggregation_fetch) | Returns call aggregations filtered by parameters specified            |
| [analytics_calls_timeline_fetch](#analytics_calls_timeline_fetch)       | Returns time-value data aggregations filtered by parameters specified |

## analytics_calls_aggregation_fetch

Returns call aggregations filtered by parameters specified

- HTTP Method: `POST`
- Endpoint: `/analytics/calls/v1/accounts/{accountId}/aggregation/fetch`

**Parameters**

| Name         | Type                                                  | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AggregationRequest](../models/AggregationRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                   | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| page         | int                                                   | ❌       | The current page number (positive numbers only)                                                                                                              |
| per_page     | int                                                   | ❌       | Number of records displayed on a page (positive numbers only, max value of 200)                                                                              |

**Return Type**

`AggregationResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AggregationRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AggregationRequest(
    grouping={
        "group_by": "Company",
        "keys": [
            "keys"
        ]
    },
    time_settings={
        "time_zone": "timeZone",
        "time_range": {
            "time_from": "timeFrom",
            "time_to": "timeTo"
        },
        "advanced_time_settings": {
            "include_days": [
                "Sunday"
            ],
            "include_hours": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ]
        }
    },
    call_filters={
        "extension_filters": {
            "from_ids": [
                "fromIds"
            ],
            "to_ids": [
                "toIds"
            ]
        },
        "queues": [
            "queues"
        ],
        "called_numbers": [
            "calledNumbers"
        ],
        "directions": [
            "Inbound"
        ],
        "origins": [
            "Internal"
        ],
        "call_responses": [
            "Answered"
        ],
        "call_results": [
            "Completed"
        ],
        "call_segments": [
            {
                "segment": "Ringing",
                "length": {
                    "min_seconds": 4,
                    "max_seconds": 2
                }
            }
        ],
        "call_actions": [
            "HoldOff"
        ],
        "company_hours": [
            "BusinessHours"
        ],
        "call_duration": {
            "min_seconds": 9,
            "max_seconds": 8
        },
        "time_spent": {
            "min_seconds": 6,
            "max_seconds": 4
        },
        "queue_sla": [
            "InSla"
        ],
        "call_types": [
            "Direct"
        ]
    },
    response_options={
        "counters": {
            "all_calls": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_direction": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_origin": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_response": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_segments": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_result": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_company_hours": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_queue_sla": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_actions": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_by_type": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "queue_opportunities": {
                "aggregation_type": "Sum"
            }
        },
        "timers": {
            "all_calls_duration": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_duration_by_direction": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_duration_by_origin": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_duration_by_response": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_segments_duration": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_duration_by_result": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_duration_by_company_hours": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_duration_by_queue_sla": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            },
            "calls_duration_by_type": {
                "aggregation_type": "Sum",
                "aggregation_interval": "Hour"
            }
        }
    }
)

result = sdk.business_analytics.analytics_calls_aggregation_fetch(
    request_body=request_body,
    account_id="~",
    page=8,
    per_page=175
)

print(result)
```

## analytics_calls_timeline_fetch

Returns time-value data aggregations filtered by parameters specified

- HTTP Method: `POST`
- Endpoint: `/analytics/calls/v1/accounts/{accountId}/timeline/fetch`

**Parameters**

| Name         | Type                                            | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [TimelineRequest](../models/TimelineRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                             | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| interval     | [Interval](../models/Interval.md)               | ✅       | Aggregation interval                                                                                                                                         |
| page         | int                                             | ❌       | The current page number (positive numbers only)                                                                                                              |
| per_page     | int                                             | ❌       | Number of records displayed on a page (positive numbers only, max value of 20)                                                                               |

**Return Type**

`TimelineResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import TimelineRequest, Interval

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TimelineRequest(
    grouping={
        "group_by": "Company",
        "keys": [
            "keys"
        ]
    },
    time_settings={
        "time_zone": "timeZone",
        "time_range": {
            "time_from": "timeFrom",
            "time_to": "timeTo"
        },
        "advanced_time_settings": {
            "include_days": [
                "Sunday"
            ],
            "include_hours": [
                {
                    "from_": "from",
                    "to": "to"
                }
            ]
        }
    },
    call_filters={
        "extension_filters": {
            "from_ids": [
                "fromIds"
            ],
            "to_ids": [
                "toIds"
            ]
        },
        "queues": [
            "queues"
        ],
        "called_numbers": [
            "calledNumbers"
        ],
        "directions": [
            "Inbound"
        ],
        "origins": [
            "Internal"
        ],
        "call_responses": [
            "Answered"
        ],
        "call_results": [
            "Completed"
        ],
        "call_segments": [
            {
                "segment": "Ringing",
                "length": {
                    "min_seconds": 4,
                    "max_seconds": 2
                }
            }
        ],
        "call_actions": [
            "HoldOff"
        ],
        "company_hours": [
            "BusinessHours"
        ],
        "call_duration": {
            "min_seconds": 9,
            "max_seconds": 8
        },
        "time_spent": {
            "min_seconds": 6,
            "max_seconds": 4
        },
        "queue_sla": [
            "InSla"
        ],
        "call_types": [
            "Direct"
        ]
    },
    response_options={
        "counters": {
            "all_calls": False,
            "calls_by_direction": False,
            "calls_by_origin": True,
            "calls_by_response": False,
            "calls_segments": False,
            "calls_by_result": True,
            "calls_by_company_hours": True,
            "calls_by_queue_sla": True,
            "calls_by_actions": False,
            "calls_by_type": True,
            "queue_opportunities": False
        },
        "timers": {
            "all_calls_duration": False,
            "calls_duration_by_direction": True,
            "calls_duration_by_origin": True,
            "calls_duration_by_response": True,
            "calls_segments_duration": False,
            "calls_duration_by_result": False,
            "calls_duration_by_company_hours": False,
            "calls_duration_by_queue_sla": False,
            "calls_duration_by_type": False
        }
    }
)

result = sdk.business_analytics.analytics_calls_timeline_fetch(
    request_body=request_body,
    account_id="~",
    interval="Hour",
    page=4,
    per_page=16
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
