# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .model_info import ModelInfo
from .extension_info_int_id import ExtensionInfoIntId
from .device_emergency_info import DeviceEmergencyInfo
from .emergency_service_address_resource import EmergencyServiceAddressResource
from .phone_lines_info import PhoneLinesInfo
from .shipping_info import ShippingInfo
from .device_site_info import DeviceSiteInfo
from .line_pooling_enum import LinePoolingEnum
from .billing_statement_info import BillingStatementInfo


class DeviceResourceType(Enum):
    """An enumeration representing different categories.

    :cvar BLA: "BLA"
    :vartype BLA: str
    :cvar SOFTPHONE: "SoftPhone"
    :vartype SOFTPHONE: str
    :cvar OTHERPHONE: "OtherPhone"
    :vartype OTHERPHONE: str
    :cvar HARDPHONE: "HardPhone"
    :vartype HARDPHONE: str
    :cvar WEBPHONE: "WebPhone"
    :vartype WEBPHONE: str
    :cvar PAGING: "Paging"
    :vartype PAGING: str
    :cvar ROOM: "Room"
    :vartype ROOM: str
    :cvar WEBRTC: "WebRTC"
    :vartype WEBRTC: str
    """

    BLA = "BLA"
    SOFTPHONE = "SoftPhone"
    OTHERPHONE = "OtherPhone"
    HARDPHONE = "HardPhone"
    WEBPHONE = "WebPhone"
    PAGING = "Paging"
    ROOM = "Room"
    WEBRTC = "WebRTC"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DeviceResourceType._member_map_.values()))


class DeviceResourceStatus(Enum):
    """An enumeration representing different categories.

    :cvar OFFLINE: "Offline"
    :vartype OFFLINE: str
    :cvar ONLINE: "Online"
    :vartype ONLINE: str
    """

    OFFLINE = "Offline"
    ONLINE = "Online"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DeviceResourceStatus._member_map_.values()))


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "computer_name": "computerName",
        "emergency_service_address": "emergencyServiceAddress",
        "phone_lines": "phoneLines",
        "box_billing_id": "boxBillingId",
        "use_as_common_phone": "useAsCommonPhone",
        "hot_desk_device": "hotDeskDevice",
        "in_company_net": "inCompanyNet",
        "last_location_report_time": "lastLocationReportTime",
        "line_pooling": "linePooling",
        "billing_statement": "billingStatement",
    }
)
class DeviceResource(BaseModel):
    """DeviceResource

    :param id_: Internal identifier of a device, defaults to None
    :type id_: str, optional
    :param uri: Canonical URI of a device, defaults to None
    :type uri: str, optional
    :param sku: Device identification number (SKU, Stock Keeping Unit) in the format TP-ID [-AT-AC], where TP is device type (HP for RC desk phones, DV for all other devices including soft phones); ID - device model ID; AT - add-on type ID; AC - add-on count (if any). For example 'HP-56-2-2' , defaults to None
    :type sku: str, optional
    :param type_: Device type, defaults to None
    :type type_: DeviceResourceType, optional
    :param name: Device name. Mandatory if ordering SoftPhone or OtherPhone. Optional for HardPhone. If not specified for HardPhone, then a device model is used as a device name , defaults to None
    :type name: str, optional
    :param serial: Serial number for HardPhone (is returned only when the phone is shipped and provisioned); endpoint ID for SoftPhone and mobile applications , defaults to None
    :type serial: str, optional
    :param status: Device status, defaults to None
    :type status: DeviceResourceStatus, optional
    :param computer_name: Computer name (for devices of `SoftPhone` type only), defaults to None
    :type computer_name: str, optional
    :param model: HardPhone model information, defaults to None
    :type model: ModelInfo, optional
    :param extension: This attribute can be omitted for unassigned devices, defaults to None
    :type extension: ExtensionInfoIntId, optional
    :param emergency: Device emergency settings, defaults to None
    :type emergency: DeviceEmergencyInfo, optional
    :param emergency_service_address: Address for emergency cases. The same emergency address is assigned to all the numbers of one device , defaults to None
    :type emergency_service_address: EmergencyServiceAddressResource, optional
    :param phone_lines: Phone lines information, defaults to None
    :type phone_lines: List[PhoneLinesInfo], optional
    :param shipping: Shipping information, according to which devices (in case of HardPhone) or e911 stickers (in case of SoftPhone and OtherPhone) will be delivered to the customer , defaults to None
    :type shipping: ShippingInfo, optional
    :param box_billing_id: Box billing identifier of a device. Applicable only for devices of `HardPhone` type. It is an alternative way to identify the device to be ordered. Either `model` structure, or `boxBillingId` must be specified , defaults to None
    :type box_billing_id: int, optional
    :param use_as_common_phone: Supported only for devices assigned to Limited extensions. If true, enables users to log in to this phone as a common phone. , defaults to None
    :type use_as_common_phone: bool, optional
    :param hot_desk_device: This flag indicates whether this device is used for hot desking or not, defaults to None
    :type hot_desk_device: bool, optional
    :param in_company_net: Network location status. `true` if the device is located in the configured corporate network (On-Net); `false` for Off-Net location. Parameter is not returned if `EmergencyAddressAutoUpdate` feature is not enabled for the account/user, or if device network location is not determined , defaults to None
    :type in_company_net: bool, optional
    :param site: Site data, defaults to None
    :type site: DeviceSiteInfo, optional
    :param last_location_report_time: Date/time of receiving last location report in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format including timezone, for example *2016-03-10T18:07:52.534Z , defaults to None
    :type last_location_report_time: str, optional
    :param line_pooling: Pooling type of device: - `Host` - device with a standalone paid phone line which can be linked to soft phone client instance; - `Guest` - device with a linked phone line; - `None` - device without a phone line or with a specific line (free, BLA, etc.) , defaults to None
    :type line_pooling: LinePoolingEnum, optional
    :param billing_statement: Billing information. Returned for device update request if `prestatement` query parameter is set to 'true' , defaults to None
    :type billing_statement: BillingStatementInfo, optional
    """

    def __init__(
        self,
        id_: str = None,
        uri: str = None,
        sku: str = None,
        type_: DeviceResourceType = None,
        name: str = None,
        serial: str = None,
        status: DeviceResourceStatus = None,
        computer_name: str = None,
        model: ModelInfo = None,
        extension: ExtensionInfoIntId = None,
        emergency: DeviceEmergencyInfo = None,
        emergency_service_address: EmergencyServiceAddressResource = None,
        phone_lines: List[PhoneLinesInfo] = None,
        shipping: ShippingInfo = None,
        box_billing_id: int = None,
        use_as_common_phone: bool = None,
        hot_desk_device: bool = None,
        in_company_net: bool = None,
        site: DeviceSiteInfo = None,
        last_location_report_time: str = None,
        line_pooling: LinePoolingEnum = None,
        billing_statement: BillingStatementInfo = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if uri is not None:
            self.uri = uri
        if sku is not None:
            self.sku = sku
        if type_ is not None:
            self.type_ = self._enum_matching(type_, DeviceResourceType.list(), "type_")
        if name is not None:
            self.name = name
        if serial is not None:
            self.serial = serial
        if status is not None:
            self.status = self._enum_matching(
                status, DeviceResourceStatus.list(), "status"
            )
        if computer_name is not None:
            self.computer_name = computer_name
        if model is not None:
            self.model = self._define_object(model, ModelInfo)
        if extension is not None:
            self.extension = self._define_object(extension, ExtensionInfoIntId)
        if emergency is not None:
            self.emergency = self._define_object(emergency, DeviceEmergencyInfo)
        if emergency_service_address is not None:
            self.emergency_service_address = self._define_object(
                emergency_service_address, EmergencyServiceAddressResource
            )
        if phone_lines is not None:
            self.phone_lines = self._define_list(phone_lines, PhoneLinesInfo)
        if shipping is not None:
            self.shipping = self._define_object(shipping, ShippingInfo)
        if box_billing_id is not None:
            self.box_billing_id = box_billing_id
        if use_as_common_phone is not None:
            self.use_as_common_phone = use_as_common_phone
        if hot_desk_device is not None:
            self.hot_desk_device = hot_desk_device
        if in_company_net is not None:
            self.in_company_net = in_company_net
        if site is not None:
            self.site = self._define_object(site, DeviceSiteInfo)
        if last_location_report_time is not None:
            self.last_location_report_time = last_location_report_time
        if line_pooling is not None:
            self.line_pooling = self._enum_matching(
                line_pooling, LinePoolingEnum.list(), "line_pooling"
            )
        if billing_statement is not None:
            self.billing_statement = self._define_object(
                billing_statement, BillingStatementInfo
            )
