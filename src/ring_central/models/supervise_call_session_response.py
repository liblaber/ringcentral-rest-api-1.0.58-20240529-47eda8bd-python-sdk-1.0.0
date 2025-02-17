# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .party_info import PartyInfo
from .owner_info import OwnerInfo
from .call_status_info import CallStatusInfo


class SuperviseCallSessionResponseDirection(Enum):
    """An enumeration representing different categories.

    :cvar OUTBOUND: "Outbound"
    :vartype OUTBOUND: str
    :cvar INBOUND: "Inbound"
    :vartype INBOUND: str
    """

    OUTBOUND = "Outbound"
    INBOUND = "Inbound"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                SuperviseCallSessionResponseDirection._member_map_.values(),
            )
        )


@JsonMap(
    {
        "from_": "from",
        "id_": "id",
        "account_id": "accountId",
        "extension_id": "extensionId",
        "stand_alone": "standAlone",
    }
)
class SuperviseCallSessionResponse(BaseModel):
    """SuperviseCallSessionResponse

    :param from_: from_, defaults to None
    :type from_: PartyInfo, optional
    :param to: to, defaults to None
    :type to: PartyInfo, optional
    :param direction: Direction of a call, defaults to None
    :type direction: SuperviseCallSessionResponseDirection, optional
    :param id_: Internal identifier of a party that monitors a call, defaults to None
    :type id_: str, optional
    :param account_id: Internal identifier of an account that monitors a call, defaults to None
    :type account_id: str, optional
    :param extension_id: Internal identifier of an extension that monitors a call, defaults to None
    :type extension_id: str, optional
    :param muted: Specifies if a call participant is muted or not. **Note:** If a call is also controlled via Hard phone or RingCentral App (not only through the API by calling call control methods) then it cannot be fully muted/unmuted via API only, in this case the action should be duplicated via Hard phone/RC App interfaces, defaults to None
    :type muted: bool, optional
    :param owner: Deprecated. Information on a call owner, defaults to None
    :type owner: OwnerInfo, optional
    :param stand_alone: If `true` then the party is not connected to a session voice conference, `false` means the party is connected to other parties in a session, defaults to None
    :type stand_alone: bool, optional
    :param status: Status data of a call session, defaults to None
    :type status: CallStatusInfo, optional
    """

    def __init__(
        self,
        from_: PartyInfo = None,
        to: PartyInfo = None,
        direction: SuperviseCallSessionResponseDirection = None,
        id_: str = None,
        account_id: str = None,
        extension_id: str = None,
        muted: bool = None,
        owner: OwnerInfo = None,
        stand_alone: bool = None,
        status: CallStatusInfo = None,
    ):
        if from_ is not None:
            self.from_ = self._define_object(from_, PartyInfo)
        if to is not None:
            self.to = self._define_object(to, PartyInfo)
        if direction is not None:
            self.direction = self._enum_matching(
                direction, SuperviseCallSessionResponseDirection.list(), "direction"
            )
        if id_ is not None:
            self.id_ = id_
        if account_id is not None:
            self.account_id = account_id
        if extension_id is not None:
            self.extension_id = extension_id
        if muted is not None:
            self.muted = muted
        if owner is not None:
            self.owner = self._define_object(owner, OwnerInfo)
        if stand_alone is not None:
            self.stand_alone = stand_alone
        if status is not None:
            self.status = self._define_object(status, CallStatusInfo)
