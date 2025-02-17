# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .extension_status_info import ExtensionStatusInfo
from .contact_info_update_request import ContactInfoUpdateRequest
from .extension_regional_setting_request import ExtensionRegionalSettingRequest
from .setup_wizard_state_for_update_enum import SetupWizardStateForUpdateEnum
from .call_queue_info_request import CallQueueInfoRequest
from .user_transition_info import UserTransitionInfo
from .cost_center_info import CostCenterInfo
from .custom_field_info import CustomFieldInfo
from .provisioning_site_info import ProvisioningSiteInfo
from .reference_info import ReferenceInfo


class ExtensionBulkUpdateInfoStatus(Enum):
    """An enumeration representing different categories.

    :cvar DISABLED: "Disabled"
    :vartype DISABLED: str
    :cvar ENABLED: "Enabled"
    :vartype ENABLED: str
    :cvar NOTACTIVATED: "NotActivated"
    :vartype NOTACTIVATED: str
    :cvar FROZEN: "Frozen"
    :vartype FROZEN: str
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"
    NOTACTIVATED = "NotActivated"
    FROZEN = "Frozen"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ExtensionBulkUpdateInfoStatus._member_map_.values())
        )


class ExtensionBulkUpdateInfoType(Enum):
    """An enumeration representing different categories.

    :cvar USER: "User"
    :vartype USER: str
    :cvar FAXUSER: "FaxUser"
    :vartype FAXUSER: str
    :cvar VIRTUALUSER: "VirtualUser"
    :vartype VIRTUALUSER: str
    :cvar DIGITALUSER: "DigitalUser"
    :vartype DIGITALUSER: str
    :cvar DEPARTMENT: "Department"
    :vartype DEPARTMENT: str
    :cvar ANNOUNCEMENT: "Announcement"
    :vartype ANNOUNCEMENT: str
    :cvar VOICEMAIL: "Voicemail"
    :vartype VOICEMAIL: str
    :cvar SHAREDLINESGROUP: "SharedLinesGroup"
    :vartype SHAREDLINESGROUP: str
    :cvar PAGINGONLY: "PagingOnly"
    :vartype PAGINGONLY: str
    :cvar IVRMENU: "IvrMenu"
    :vartype IVRMENU: str
    :cvar APPLICATIONEXTENSION: "ApplicationExtension"
    :vartype APPLICATIONEXTENSION: str
    :cvar PARKLOCATION: "ParkLocation"
    :vartype PARKLOCATION: str
    :cvar DELEGATEDLINESGROUP: "DelegatedLinesGroup"
    :vartype DELEGATEDLINESGROUP: str
    """

    USER = "User"
    FAXUSER = "FaxUser"
    VIRTUALUSER = "VirtualUser"
    DIGITALUSER = "DigitalUser"
    DEPARTMENT = "Department"
    ANNOUNCEMENT = "Announcement"
    VOICEMAIL = "Voicemail"
    SHAREDLINESGROUP = "SharedLinesGroup"
    PAGINGONLY = "PagingOnly"
    IVRMENU = "IvrMenu"
    APPLICATIONEXTENSION = "ApplicationExtension"
    PARKLOCATION = "ParkLocation"
    DELEGATEDLINESGROUP = "DelegatedLinesGroup"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ExtensionBulkUpdateInfoType._member_map_.values())
        )


@JsonMap(
    {
        "id_": "id",
        "status_info": "statusInfo",
        "extension_number": "extensionNumber",
        "regional_settings": "regionalSettings",
        "setup_wizard_state": "setupWizardState",
        "partner_id": "partnerId",
        "ivr_pin": "ivrPin",
        "call_queue_info": "callQueueInfo",
        "cost_center": "costCenter",
        "custom_fields": "customFields",
        "type_": "type",
    }
)
class ExtensionBulkUpdateInfo(BaseModel):
    """ExtensionBulkUpdateInfo

    :param id_: Internal identifier of an extension, defaults to None
    :type id_: str, optional
    :param status: status, defaults to None
    :type status: ExtensionBulkUpdateInfoStatus, optional
    :param status_info: Status information (reason, comment). Returned for 'Disabled' status only , defaults to None
    :type status_info: ExtensionStatusInfo, optional
    :param reason: Type of suspension, defaults to None
    :type reason: str, optional
    :param comment: Free form user comment, defaults to None
    :type comment: str, optional
    :param extension_number: Extension number available, defaults to None
    :type extension_number: str, optional
    :param contact: contact, defaults to None
    :type contact: ContactInfoUpdateRequest, optional
    :param regional_settings: regional_settings, defaults to None
    :type regional_settings: ExtensionRegionalSettingRequest, optional
    :param setup_wizard_state: Initial configuration wizard state, defaults to None
    :type setup_wizard_state: SetupWizardStateForUpdateEnum, optional
    :param partner_id: Additional extension identifier created by partner application and applied on client side , defaults to None
    :type partner_id: str, optional
    :param ivr_pin: IVR PIN, defaults to None
    :type ivr_pin: str, optional
    :param password: Password for extension, defaults to None
    :type password: str, optional
    :param call_queue_info: For Call Queue extension type only. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology , defaults to None
    :type call_queue_info: CallQueueInfoRequest, optional
    :param transition: For NotActivated extensions only. Welcome email settings , defaults to None
    :type transition: UserTransitionInfo, optional
    :param cost_center: Cost center information. Applicable if Cost Center feature is enabled. The default is `root` cost center value, defaults to None
    :type cost_center: CostCenterInfo, optional
    :param custom_fields: custom_fields, defaults to None
    :type custom_fields: List[CustomFieldInfo], optional
    :param hidden: Hides extension from showing in company directory. Supported for extensions of User type only, defaults to None
    :type hidden: bool, optional
    :param site: Site data. If multi-site feature is turned on for an account, then ID of a site must be specified. In order to assign a wireless point to the main site (company) the site ID should be set to `main-site` , defaults to None
    :type site: ProvisioningSiteInfo, optional
    :param type_: Extension type. Please note that legacy 'Department' extension type corresponds to 'Call Queue' extensions in modern RingCentral product terminology , defaults to None
    :type type_: ExtensionBulkUpdateInfoType, optional
    :param references: List of non-RC internal identifiers assigned to an extension , defaults to None
    :type references: List[ReferenceInfo], optional
    """

    def __init__(
        self,
        id_: str = None,
        status: ExtensionBulkUpdateInfoStatus = None,
        status_info: ExtensionStatusInfo = None,
        reason: str = None,
        comment: str = None,
        extension_number: str = None,
        contact: ContactInfoUpdateRequest = None,
        regional_settings: ExtensionRegionalSettingRequest = None,
        setup_wizard_state: SetupWizardStateForUpdateEnum = None,
        partner_id: str = None,
        ivr_pin: str = None,
        password: str = None,
        call_queue_info: CallQueueInfoRequest = None,
        transition: UserTransitionInfo = None,
        cost_center: CostCenterInfo = None,
        custom_fields: List[CustomFieldInfo] = None,
        hidden: bool = None,
        site: ProvisioningSiteInfo = None,
        type_: ExtensionBulkUpdateInfoType = None,
        references: List[ReferenceInfo] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if status is not None:
            self.status = self._enum_matching(
                status, ExtensionBulkUpdateInfoStatus.list(), "status"
            )
        if status_info is not None:
            self.status_info = self._define_object(status_info, ExtensionStatusInfo)
        if reason is not None:
            self.reason = reason
        if comment is not None:
            self.comment = comment
        if extension_number is not None:
            self.extension_number = extension_number
        if contact is not None:
            self.contact = self._define_object(contact, ContactInfoUpdateRequest)
        if regional_settings is not None:
            self.regional_settings = self._define_object(
                regional_settings, ExtensionRegionalSettingRequest
            )
        if setup_wizard_state is not None:
            self.setup_wizard_state = self._enum_matching(
                setup_wizard_state,
                SetupWizardStateForUpdateEnum.list(),
                "setup_wizard_state",
            )
        if partner_id is not None:
            self.partner_id = partner_id
        if ivr_pin is not None:
            self.ivr_pin = ivr_pin
        if password is not None:
            self.password = password
        if call_queue_info is not None:
            self.call_queue_info = self._define_object(
                call_queue_info, CallQueueInfoRequest
            )
        if transition is not None:
            self.transition = self._define_object(transition, UserTransitionInfo)
        if cost_center is not None:
            self.cost_center = self._define_object(cost_center, CostCenterInfo)
        if custom_fields is not None:
            self.custom_fields = self._define_list(custom_fields, CustomFieldInfo)
        if hidden is not None:
            self.hidden = hidden
        if site is not None:
            self.site = self._define_object(site, ProvisioningSiteInfo)
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, ExtensionBulkUpdateInfoType.list(), "type_"
            )
        if references is not None:
            self.references = self._define_list(references, ReferenceInfo)
