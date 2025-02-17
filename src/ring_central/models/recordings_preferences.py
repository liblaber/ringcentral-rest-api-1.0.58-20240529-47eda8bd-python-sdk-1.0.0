# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .everyone_can_control import EveryoneCanControl
from .auto_shared import AutoShared


@JsonMap({"everyone_can_control": "everyoneCanControl", "auto_shared": "autoShared"})
class RecordingsPreferences(BaseModel):
    """Recordings preferences

    :param everyone_can_control: Controls whether participants can start and pause recording, defaults to None
    :type everyone_can_control: EveryoneCanControl, optional
    :param auto_shared: Controls whether recording can be auto shared, defaults to None
    :type auto_shared: AutoShared, optional
    """

    def __init__(
        self,
        everyone_can_control: EveryoneCanControl = None,
        auto_shared: AutoShared = None,
    ):
        if everyone_can_control is not None:
            self.everyone_can_control = self._define_object(
                everyone_can_control, EveryoneCanControl
            )
        if auto_shared is not None:
            self.auto_shared = self._define_object(auto_shared, AutoShared)
