# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .meeting_schedule_resource import MeetingScheduleResource
from .host_info_request import HostInfoRequest
from .recurrence_info import RecurrenceInfo


class MeetingRequestResourceMeetingType(Enum):
    """An enumeration representing different categories.

    :cvar INSTANT: "Instant"
    :vartype INSTANT: str
    :cvar SCHEDULED: "Scheduled"
    :vartype SCHEDULED: str
    :cvar SCHEDULEDRECURRING: "ScheduledRecurring"
    :vartype SCHEDULEDRECURRING: str
    :cvar RECURRING: "Recurring"
    :vartype RECURRING: str
    """

    INSTANT = "Instant"
    SCHEDULED = "Scheduled"
    SCHEDULEDRECURRING = "ScheduledRecurring"
    RECURRING = "Recurring"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                MeetingRequestResourceMeetingType._member_map_.values(),
            )
        )


class MeetingRequestResourceAudioOptions(Enum):
    """An enumeration representing different categories.

    :cvar PHONE: "Phone"
    :vartype PHONE: str
    :cvar COMPUTERAUDIO: "ComputerAudio"
    :vartype COMPUTERAUDIO: str
    """

    PHONE = "Phone"
    COMPUTERAUDIO = "ComputerAudio"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                MeetingRequestResourceAudioOptions._member_map_.values(),
            )
        )


class MeetingRequestResourceAutoRecordType(Enum):
    """An enumeration representing different categories.

    :cvar LOCAL: "local"
    :vartype LOCAL: str
    :cvar CLOUD: "cloud"
    :vartype CLOUD: str
    :cvar NONE: "none"
    :vartype NONE: str
    """

    LOCAL = "local"
    CLOUD = "cloud"
    NONE = "none"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                MeetingRequestResourceAutoRecordType._member_map_.values(),
            )
        )


@JsonMap(
    {
        "meeting_type": "meetingType",
        "allow_join_before_host": "allowJoinBeforeHost",
        "start_host_video": "startHostVideo",
        "start_participants_video": "startParticipantsVideo",
        "use_personal_meeting_id": "usePersonalMeetingId",
        "audio_options": "audioOptions",
        "auto_record_type": "autoRecordType",
        "enforce_login": "enforceLogin",
        "mute_participants_on_entry": "muteParticipantsOnEntry",
        "enable_waiting_room": "enableWaitingRoom",
        "global_dial_in_countries": "globalDialInCountries",
        "alternative_hosts": "alternativeHosts",
    }
)
class MeetingRequestResource(BaseModel):
    """MeetingRequestResource

    :param topic: Custom topic of a meeting, defaults to None
    :type topic: str, optional
    :param meeting_type: meeting_type, defaults to None
    :type meeting_type: MeetingRequestResourceMeetingType, optional
    :param schedule: Timing of a meeting, defaults to None
    :type schedule: MeetingScheduleResource, optional
    :param password: Meeting password, defaults to None
    :type password: str, optional
    :param host: Meeting host information, defaults to None
    :type host: HostInfoRequest, optional
    :param allow_join_before_host: allow_join_before_host, defaults to None
    :type allow_join_before_host: bool, optional
    :param start_host_video: start_host_video, defaults to None
    :type start_host_video: bool, optional
    :param start_participants_video: Starting meetings with participant video on/off (true/false), defaults to None
    :type start_participants_video: bool, optional
    :param use_personal_meeting_id: If true, then personal user's meeting ID is applied for creation of this meeting, defaults to None
    :type use_personal_meeting_id: bool, optional
    :param audio_options: audio_options, defaults to None
    :type audio_options: List[MeetingRequestResourceAudioOptions], optional
    :param recurrence: recurrence, defaults to None
    :type recurrence: RecurrenceInfo, optional
    :param auto_record_type: Automatic record type, defaults to None
    :type auto_record_type: MeetingRequestResourceAutoRecordType, optional
    :param enforce_login: If true, then only signed-in users can join this meeting, defaults to None
    :type enforce_login: bool, optional
    :param mute_participants_on_entry: If true, then participants are muted on entry, defaults to None
    :type mute_participants_on_entry: bool, optional
    :param enable_waiting_room: If true, then the waiting room for participants is enabled, defaults to None
    :type enable_waiting_room: bool, optional
    :param global_dial_in_countries: List of global dial-in countries (eg. US, UK, AU, etc.), defaults to None
    :type global_dial_in_countries: List[str], optional
    :param alternative_hosts: alternative_hosts, defaults to None
    :type alternative_hosts: str, optional
    """

    def __init__(
        self,
        topic: str = None,
        meeting_type: MeetingRequestResourceMeetingType = None,
        schedule: MeetingScheduleResource = None,
        password: str = None,
        host: HostInfoRequest = None,
        allow_join_before_host: bool = None,
        start_host_video: bool = None,
        start_participants_video: bool = None,
        use_personal_meeting_id: bool = None,
        audio_options: List[MeetingRequestResourceAudioOptions] = None,
        recurrence: RecurrenceInfo = None,
        auto_record_type: MeetingRequestResourceAutoRecordType = None,
        enforce_login: bool = None,
        mute_participants_on_entry: bool = None,
        enable_waiting_room: bool = None,
        global_dial_in_countries: List[str] = None,
        alternative_hosts: str = None,
    ):
        if topic is not None:
            self.topic = topic
        if meeting_type is not None:
            self.meeting_type = self._enum_matching(
                meeting_type, MeetingRequestResourceMeetingType.list(), "meeting_type"
            )
        if schedule is not None:
            self.schedule = self._define_object(schedule, MeetingScheduleResource)
        if password is not None:
            self.password = password
        if host is not None:
            self.host = self._define_object(host, HostInfoRequest)
        if allow_join_before_host is not None:
            self.allow_join_before_host = allow_join_before_host
        if start_host_video is not None:
            self.start_host_video = start_host_video
        if start_participants_video is not None:
            self.start_participants_video = start_participants_video
        if use_personal_meeting_id is not None:
            self.use_personal_meeting_id = use_personal_meeting_id
        if audio_options is not None:
            self.audio_options = self._define_list(
                audio_options, MeetingRequestResourceAudioOptions
            )
        if recurrence is not None:
            self.recurrence = self._define_object(recurrence, RecurrenceInfo)
        if auto_record_type is not None:
            self.auto_record_type = self._enum_matching(
                auto_record_type,
                MeetingRequestResourceAutoRecordType.list(),
                "auto_record_type",
            )
        if enforce_login is not None:
            self.enforce_login = enforce_login
        if mute_participants_on_entry is not None:
            self.mute_participants_on_entry = mute_participants_on_entry
        if enable_waiting_room is not None:
            self.enable_waiting_room = enable_waiting_room
        if global_dial_in_countries is not None:
            self.global_dial_in_countries = global_dial_in_countries
        if alternative_hosts is not None:
            self.alternative_hosts = alternative_hosts
