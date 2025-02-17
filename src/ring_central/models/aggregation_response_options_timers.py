# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .aggregation_type import AggregationType
from .aggregation_interval import AggregationInterval


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class AllCallsDuration(BaseModel):
    """Aggregation of all calls duration

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsDurationByDirection(BaseModel):
    """Aggregation of calls duration by direction (Inbound, Outbound)

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsDurationByOrigin(BaseModel):
    """Aggregation of calls duration by origin (Internal, External)

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsDurationByResponse(BaseModel):
    """Aggregation of calls duration by response (Answered, NotAnswered, Connected, NotConnected)

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsSegmentsDuration(BaseModel):
    """Aggregation of calls duration by segments (Ringing, LiveTalk, Hold, Park, Transfer, IvrPrompt, Voicemail, VmGreeting, Setup)

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsDurationByResult(BaseModel):
    """Aggregation of calls duration by result (Completed, Abandoned, Voicemail, Unknown, Missed, Accepted)

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsDurationByCompanyHours(BaseModel):
    """Aggregation of calls duration by company hours (BusinessHours, AfterHours)

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsDurationByQueueSla(BaseModel):
    """Aggregation of calls duration by queue SLA (InSLA, OutSLA). This timer is only applicable to Queues grouping

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "aggregation_type": "aggregationType",
        "aggregation_interval": "aggregationInterval",
    }
)
class CallsDurationByType(BaseModel):
    """Aggregation of calls duration by type (Direct, FromQueue, ParkRetrieval, Transferred, Outbound)

    :param aggregation_type: Counter aggregation type. Can be `Sum`, `Average`, `Min`, `Max` or `Percent`
    :type aggregation_type: AggregationType
    :param aggregation_interval: Time interval which will be used for aggregation. Can be `Hour`, `Day`, `Week` or `Month`, defaults to None
    :type aggregation_interval: AggregationInterval, optional
    """

    def __init__(
        self,
        aggregation_type: AggregationType,
        aggregation_interval: AggregationInterval = None,
    ):
        self.aggregation_type = self._enum_matching(
            aggregation_type, AggregationType.list(), "aggregation_type"
        )
        if aggregation_interval is not None:
            self.aggregation_interval = self._enum_matching(
                aggregation_interval, AggregationInterval.list(), "aggregation_interval"
            )


@JsonMap(
    {
        "all_calls_duration": "allCallsDuration",
        "calls_duration_by_direction": "callsDurationByDirection",
        "calls_duration_by_origin": "callsDurationByOrigin",
        "calls_duration_by_response": "callsDurationByResponse",
        "calls_segments_duration": "callsSegmentsDuration",
        "calls_duration_by_result": "callsDurationByResult",
        "calls_duration_by_company_hours": "callsDurationByCompanyHours",
        "calls_duration_by_queue_sla": "callsDurationByQueueSla",
        "calls_duration_by_type": "callsDurationByType",
    }
)
class AggregationResponseOptionsTimers(BaseModel):
    """The formula is defined by `aggregationType` and `aggregationInterval` for every timer individually.
    If `aggregationType` is `Sum` or `Percent`, `aggregationInterval` is not supported.
    If `aggregationType` is `Min`, `Max` or `Average`, `aggregationInterval` is supported, but not required.
    If left empty, aggregation will be performed on per-call basis

    :param all_calls_duration: Aggregation of all calls duration, defaults to None
    :type all_calls_duration: AllCallsDuration, optional
    :param calls_duration_by_direction: Aggregation of calls duration by direction (Inbound, Outbound), defaults to None
    :type calls_duration_by_direction: CallsDurationByDirection, optional
    :param calls_duration_by_origin: Aggregation of calls duration by origin (Internal, External), defaults to None
    :type calls_duration_by_origin: CallsDurationByOrigin, optional
    :param calls_duration_by_response: Aggregation of calls duration by response (Answered, NotAnswered, Connected, NotConnected), defaults to None
    :type calls_duration_by_response: CallsDurationByResponse, optional
    :param calls_segments_duration: Aggregation of calls duration by segments (Ringing, LiveTalk, Hold, Park, Transfer, IvrPrompt, Voicemail, VmGreeting, Setup), defaults to None
    :type calls_segments_duration: CallsSegmentsDuration, optional
    :param calls_duration_by_result: Aggregation of calls duration by result (Completed, Abandoned, Voicemail, Unknown, Missed, Accepted), defaults to None
    :type calls_duration_by_result: CallsDurationByResult, optional
    :param calls_duration_by_company_hours: Aggregation of calls duration by company hours (BusinessHours, AfterHours), defaults to None
    :type calls_duration_by_company_hours: CallsDurationByCompanyHours, optional
    :param calls_duration_by_queue_sla: Aggregation of calls duration by queue SLA (InSLA, OutSLA). This timer is only applicable to Queues grouping, defaults to None
    :type calls_duration_by_queue_sla: CallsDurationByQueueSla, optional
    :param calls_duration_by_type: Aggregation of calls duration by type (Direct, FromQueue, ParkRetrieval, Transferred, Outbound), defaults to None
    :type calls_duration_by_type: CallsDurationByType, optional
    """

    def __init__(
        self,
        all_calls_duration: AllCallsDuration = None,
        calls_duration_by_direction: CallsDurationByDirection = None,
        calls_duration_by_origin: CallsDurationByOrigin = None,
        calls_duration_by_response: CallsDurationByResponse = None,
        calls_segments_duration: CallsSegmentsDuration = None,
        calls_duration_by_result: CallsDurationByResult = None,
        calls_duration_by_company_hours: CallsDurationByCompanyHours = None,
        calls_duration_by_queue_sla: CallsDurationByQueueSla = None,
        calls_duration_by_type: CallsDurationByType = None,
    ):
        if all_calls_duration is not None:
            self.all_calls_duration = self._define_object(
                all_calls_duration, AllCallsDuration
            )
        if calls_duration_by_direction is not None:
            self.calls_duration_by_direction = self._define_object(
                calls_duration_by_direction, CallsDurationByDirection
            )
        if calls_duration_by_origin is not None:
            self.calls_duration_by_origin = self._define_object(
                calls_duration_by_origin, CallsDurationByOrigin
            )
        if calls_duration_by_response is not None:
            self.calls_duration_by_response = self._define_object(
                calls_duration_by_response, CallsDurationByResponse
            )
        if calls_segments_duration is not None:
            self.calls_segments_duration = self._define_object(
                calls_segments_duration, CallsSegmentsDuration
            )
        if calls_duration_by_result is not None:
            self.calls_duration_by_result = self._define_object(
                calls_duration_by_result, CallsDurationByResult
            )
        if calls_duration_by_company_hours is not None:
            self.calls_duration_by_company_hours = self._define_object(
                calls_duration_by_company_hours, CallsDurationByCompanyHours
            )
        if calls_duration_by_queue_sla is not None:
            self.calls_duration_by_queue_sla = self._define_object(
                calls_duration_by_queue_sla, CallsDurationByQueueSla
            )
        if calls_duration_by_type is not None:
            self.calls_duration_by_type = self._define_object(
                calls_duration_by_type, CallsDurationByType
            )
