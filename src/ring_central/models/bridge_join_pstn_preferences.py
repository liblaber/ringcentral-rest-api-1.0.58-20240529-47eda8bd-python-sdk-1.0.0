# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "bridge_id": "bridgeId",
        "prompt_announcement": "promptAnnouncement",
        "prompt_participants": "promptParticipants",
    }
)
class BridgeJoinPstnPreferences(BaseModel):
    """BridgeJoinPstnPreferences

    :param bridge_id: Bridge identifier, defaults to None
    :type bridge_id: str, optional
    :param prompt_announcement: Specifies whether to play 'Announce yourself' prompt, defaults to None
    :type prompt_announcement: bool, optional
    :param prompt_participants: Specifies whether to play 'There are X participants' prompt, defaults to None
    :type prompt_participants: bool, optional
    """

    def __init__(
        self,
        bridge_id: str = None,
        prompt_announcement: bool = None,
        prompt_participants: bool = None,
    ):
        if bridge_id is not None:
            self.bridge_id = bridge_id
        if prompt_announcement is not None:
            self.prompt_announcement = prompt_announcement
        if prompt_participants is not None:
            self.prompt_participants = prompt_participants
