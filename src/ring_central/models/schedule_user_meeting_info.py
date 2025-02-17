# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class ScheduleUserMeetingInfoAudioOptions(Enum):
    """An enumeration representing different categories.

    :cvar PHONE: "Phone"
    :vartype PHONE: str
    :cvar COMPUTERAUDIO: "ComputerAudio"
    :vartype COMPUTERAUDIO: str
    :cvar THIRDPARTY: "ThirdParty"
    :vartype THIRDPARTY: str
    """

    PHONE = "Phone"
    COMPUTERAUDIO = "ComputerAudio"
    THIRDPARTY = "ThirdParty"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                ScheduleUserMeetingInfoAudioOptions._member_map_.values(),
            )
        )


class RequirePasswordForPmiMeetings(Enum):
    """An enumeration representing different categories.

    :cvar ALL: "all"
    :vartype ALL: str
    :cvar NONE: "none"
    :vartype NONE: str
    :cvar JBHONLY: "jbhOnly"
    :vartype JBHONLY: str
    """

    ALL = "all"
    NONE = "none"
    JBHONLY = "jbhOnly"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, RequirePasswordForPmiMeetings._member_map_.values())
        )


@JsonMap(
    {
        "enforce_login": "enforceLogin",
        "start_host_video": "startHostVideo",
        "start_participants_video": "startParticipantsVideo",
        "audio_options": "audioOptions",
        "allow_join_before_host": "allowJoinBeforeHost",
        "use_pmi_for_scheduled_meetings": "usePmiForScheduledMeetings",
        "use_pmi_for_instant_meetings": "usePmiForInstantMeetings",
        "require_password_for_scheduling_new_meetings": "requirePasswordForSchedulingNewMeetings",
        "require_password_for_scheduled_meetings": "requirePasswordForScheduledMeetings",
        "default_password_for_scheduled_meetings": "defaultPasswordForScheduledMeetings",
        "require_password_for_instant_meetings": "requirePasswordForInstantMeetings",
        "require_password_for_pmi_meetings": "requirePasswordForPmiMeetings",
        "pmi_password": "pmiPassword",
        "pstn_password_protected": "pstnPasswordProtected",
        "mute_participants_on_entry": "muteParticipantsOnEntry",
    }
)
class ScheduleUserMeetingInfo(BaseModel):
    """Scheduling meeting settings locked on account level || Settings defining how to schedule user meetings

    :param enforce_login: If true, then only signed-in users can join this meeting, defaults to None
    :type enforce_login: bool, optional
    :param start_host_video: Starting meetings with host video on/off (true/false), defaults to None
    :type start_host_video: bool, optional
    :param start_participants_video: Starting meetings with participant video on/off (true/false), defaults to None
    :type start_participants_video: bool, optional
    :param audio_options: Determines how participants can join the audio channel of a meeting, defaults to None
    :type audio_options: List[ScheduleUserMeetingInfoAudioOptions], optional
    :param allow_join_before_host: Allows participants to join the meeting before the host arrives, defaults to None
    :type allow_join_before_host: bool, optional
    :param use_pmi_for_scheduled_meetings: Determines whether to use Personal Meeting ID (PMI) when scheduling a meeting, defaults to None
    :type use_pmi_for_scheduled_meetings: bool, optional
    :param use_pmi_for_instant_meetings: Determines whether to use Personal Meeting ID (PMI) when starting an instant meeting, defaults to None
    :type use_pmi_for_instant_meetings: bool, optional
    :param require_password_for_scheduling_new_meetings: A password will be generated when scheduling a meeting and participants will require password to join a meeting. The Personal Meeting ID (PMI) meetings are not included, defaults to None
    :type require_password_for_scheduling_new_meetings: bool, optional
    :param require_password_for_scheduled_meetings: Specifies whether to require a password for meetings which have already been scheduled, defaults to None
    :type require_password_for_scheduled_meetings: bool, optional
    :param default_password_for_scheduled_meetings: Password for already scheduled meetings. Users can set it individually, defaults to None
    :type default_password_for_scheduled_meetings: str, optional
    :param require_password_for_instant_meetings: A random password will be generated for an instant meeting, if set to `true`. If you use PMI for your instant meetings, this option will be disabled, defaults to None
    :type require_password_for_instant_meetings: bool, optional
    :param require_password_for_pmi_meetings: Specifies whether to require a password for meetings using Personal Meeting ID (PMI). The supported values are: 'none', 'all' and 'jbhOnly' (joined before host only), defaults to None
    :type require_password_for_pmi_meetings: RequirePasswordForPmiMeetings, optional
    :param pmi_password: The default password for Personal Meeting ID (PMI) meetings, defaults to None
    :type pmi_password: str, optional
    :param pstn_password_protected: Specifies whether to generate and require a password for participants joining by phone, defaults to None
    :type pstn_password_protected: bool, optional
    :param mute_participants_on_entry: mute_participants_on_entry, defaults to None
    :type mute_participants_on_entry: bool, optional
    """

    def __init__(
        self,
        enforce_login: bool = None,
        start_host_video: bool = None,
        start_participants_video: bool = None,
        audio_options: List[ScheduleUserMeetingInfoAudioOptions] = None,
        allow_join_before_host: bool = None,
        use_pmi_for_scheduled_meetings: bool = None,
        use_pmi_for_instant_meetings: bool = None,
        require_password_for_scheduling_new_meetings: bool = None,
        require_password_for_scheduled_meetings: bool = None,
        default_password_for_scheduled_meetings: str = None,
        require_password_for_instant_meetings: bool = None,
        require_password_for_pmi_meetings: RequirePasswordForPmiMeetings = None,
        pmi_password: str = None,
        pstn_password_protected: bool = None,
        mute_participants_on_entry: bool = None,
    ):
        if enforce_login is not None:
            self.enforce_login = enforce_login
        if start_host_video is not None:
            self.start_host_video = start_host_video
        if start_participants_video is not None:
            self.start_participants_video = start_participants_video
        if audio_options is not None:
            self.audio_options = self._define_list(
                audio_options, ScheduleUserMeetingInfoAudioOptions
            )
        if allow_join_before_host is not None:
            self.allow_join_before_host = allow_join_before_host
        if use_pmi_for_scheduled_meetings is not None:
            self.use_pmi_for_scheduled_meetings = use_pmi_for_scheduled_meetings
        if use_pmi_for_instant_meetings is not None:
            self.use_pmi_for_instant_meetings = use_pmi_for_instant_meetings
        if require_password_for_scheduling_new_meetings is not None:
            self.require_password_for_scheduling_new_meetings = (
                require_password_for_scheduling_new_meetings
            )
        if require_password_for_scheduled_meetings is not None:
            self.require_password_for_scheduled_meetings = (
                require_password_for_scheduled_meetings
            )
        if default_password_for_scheduled_meetings is not None:
            self.default_password_for_scheduled_meetings = (
                default_password_for_scheduled_meetings
            )
        if require_password_for_instant_meetings is not None:
            self.require_password_for_instant_meetings = (
                require_password_for_instant_meetings
            )
        if require_password_for_pmi_meetings is not None:
            self.require_password_for_pmi_meetings = self._enum_matching(
                require_password_for_pmi_meetings,
                RequirePasswordForPmiMeetings.list(),
                "require_password_for_pmi_meetings",
            )
        if pmi_password is not None:
            self.pmi_password = pmi_password
        if pstn_password_protected is not None:
            self.pstn_password_protected = pstn_password_protected
        if mute_participants_on_entry is not None:
            self.mute_participants_on_entry = mute_participants_on_entry
