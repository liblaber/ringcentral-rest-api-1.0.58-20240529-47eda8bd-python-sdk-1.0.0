# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


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
class TimelineResponseOptionsTimers(BaseModel):
    """Options for selecting breakdown for calls duration

    :param all_calls_duration: Include data for all calls duration, defaults to None
    :type all_calls_duration: bool, optional
    :param calls_duration_by_direction: Include breakdown of calls duration by direction (Inbound, Outbound), defaults to None
    :type calls_duration_by_direction: bool, optional
    :param calls_duration_by_origin: Include breakdown of calls duration by origin (Internal, External), defaults to None
    :type calls_duration_by_origin: bool, optional
    :param calls_duration_by_response: Include breakdown of calls duration by response (Answered, NotAnswered, Connected, NotConnected), defaults to None
    :type calls_duration_by_response: bool, optional
    :param calls_segments_duration: Include breakdown of calls duration by segments (Ringing, LiveTalk, Hold, Park, Transfer, IvrPrompt, Voicemail, VmGreeting, Setup), defaults to None
    :type calls_segments_duration: bool, optional
    :param calls_duration_by_result: Include breakdown of calls duration by result (Completed, Abandoned, Voicemail, Unknown, Missed, Accepted), defaults to None
    :type calls_duration_by_result: bool, optional
    :param calls_duration_by_company_hours: Include breakdown of calls duration by company hours (BusinessHours, AfterHours), defaults to None
    :type calls_duration_by_company_hours: bool, optional
    :param calls_duration_by_queue_sla: Include breakdown of calls duration by queue SLA (InSLA, OutSLA). This timer is only applicable to Queues grouping, defaults to None
    :type calls_duration_by_queue_sla: bool, optional
    :param calls_duration_by_type: Include breakdown of calls duration by type (Direct, FromQueue, ParkRetrieval, Transferred, Outbound), defaults to None
    :type calls_duration_by_type: bool, optional
    """

    def __init__(
        self,
        all_calls_duration: bool = None,
        calls_duration_by_direction: bool = None,
        calls_duration_by_origin: bool = None,
        calls_duration_by_response: bool = None,
        calls_segments_duration: bool = None,
        calls_duration_by_result: bool = None,
        calls_duration_by_company_hours: bool = None,
        calls_duration_by_queue_sla: bool = None,
        calls_duration_by_type: bool = None,
    ):
        if all_calls_duration is not None:
            self.all_calls_duration = all_calls_duration
        if calls_duration_by_direction is not None:
            self.calls_duration_by_direction = calls_duration_by_direction
        if calls_duration_by_origin is not None:
            self.calls_duration_by_origin = calls_duration_by_origin
        if calls_duration_by_response is not None:
            self.calls_duration_by_response = calls_duration_by_response
        if calls_segments_duration is not None:
            self.calls_segments_duration = calls_segments_duration
        if calls_duration_by_result is not None:
            self.calls_duration_by_result = calls_duration_by_result
        if calls_duration_by_company_hours is not None:
            self.calls_duration_by_company_hours = calls_duration_by_company_hours
        if calls_duration_by_queue_sla is not None:
            self.calls_duration_by_queue_sla = calls_duration_by_queue_sla
        if calls_duration_by_type is not None:
            self.calls_duration_by_type = calls_duration_by_type
