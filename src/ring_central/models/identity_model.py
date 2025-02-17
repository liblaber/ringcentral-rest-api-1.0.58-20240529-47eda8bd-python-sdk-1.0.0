# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .soc_msg_gender import SocMsgGender
from .identity_type import IdentityType


@JsonMap(
    {
        "id_": "id",
        "avatar_uri": "avatarUri",
        "creation_time": "creationTime",
        "display_name": "displayName",
        "email_address": "emailAddress",
        "extra_values": "extraValues",
        "first_name": "firstName",
        "home_phone": "homePhone",
        "identity_group_id": "identityGroupId",
        "last_name": "lastName",
        "mobile_phone": "mobilePhone",
        "screen_name": "screenName",
        "type_": "type",
        "last_modified_time": "lastModifiedTime",
        "user_ids": "userIds",
        "mobile_device_info": "mobileDeviceInfo",
        "fb_bio": "fbBio",
        "fb_category": "fbCategory",
        "fb_locale": "fbLocale",
        "ig_followers_count": "igFollowersCount",
        "tw_description": "twDescription",
        "tw_followers_count": "twFollowersCount",
        "tw_following_count": "twFollowingCount",
        "tw_statuses_count": "twStatusesCount",
        "tw_location": "twLocation",
        "api_version": "apiVersion",
        "device_type": "deviceType",
        "primary_device_os": "primaryDeviceOs",
        "viber_version": "viberVersion",
    }
)
class IdentityModel(BaseModel):
    """IdentityModel

    :param id_: Identity identifier.
    :type id_: str
    :param avatar_uri: Identity's avatar Uri., defaults to None
    :type avatar_uri: str, optional
    :param company: Company., defaults to None
    :type company: str, optional
    :param creation_time: Creation time of the resource.
    :type creation_time: str
    :param display_name: Display name of the identity., defaults to None
    :type display_name: str, optional
    :param email_address: Email address., defaults to None
    :type email_address: str, optional
    :param extra_values: Additional data to store along the identity., defaults to None
    :type extra_values: dict, optional
    :param first_name: FirstName., defaults to None
    :type first_name: str, optional
    :param gender: Gender., defaults to None
    :type gender: SocMsgGender, optional
    :param home_phone: Phone number., defaults to None
    :type home_phone: str, optional
    :param identity_group_id: The identity group id references the identity group that contains all information (phone, notes, etc.). Many identities may belong to this group. If the identity group id is null, it means that identity does not have a group and any extra information. , defaults to None
    :type identity_group_id: str, optional
    :param last_name: LastName., defaults to None
    :type last_name: str, optional
    :param mobile_phone: Phone number., defaults to None
    :type mobile_phone: str, optional
    :param screen_name: Screen name of the identity., defaults to None
    :type screen_name: str, optional
    :param type_: Type of the identity.
    :type type_: IdentityType
    :param last_modified_time: The time when the last modification was completed.
    :type last_modified_time: str
    :param user_ids: List of the associated user identifiers who can use the identity., defaults to None
    :type user_ids: List[str], optional
    :param uuid: UUID of the identity., defaults to None
    :type uuid: str, optional
    :param mobile_device_info: Device info of the identity. Applicable to RingCX Digital Messaging channels only. , defaults to None
    :type mobile_device_info: str, optional
    :param fb_bio: Facebook biography of the identity. Applicable to Facebook and Messenger channels only. , defaults to None
    :type fb_bio: str, optional
    :param fb_category: Facebook category of the identity. Applicable to Facebook and Messenger channels only. , defaults to None
    :type fb_category: str, optional
    :param fb_locale: Facebook locale of the identity. Applicable to Facebook and Messenger channels only. , defaults to None
    :type fb_locale: str, optional
    :param ig_followers_count: Instagram followers count of the identity. Applicable to Instagram and InstagramMessaging channels only. , defaults to None
    :type ig_followers_count: int, optional
    :param tw_description: Twitter description of the identity. Applicable to Twitter channels only. , defaults to None
    :type tw_description: str, optional
    :param tw_followers_count: Twitter followers count of the identity. Applicable to Twitter channels only. , defaults to None
    :type tw_followers_count: int, optional
    :param tw_following_count: Count of Twitter accounts followed by the identity. Applicable to Twitter channels only. , defaults to None
    :type tw_following_count: int, optional
    :param tw_statuses_count: Count of tweets of the identity. Applicable to Twitter channels only. , defaults to None
    :type tw_statuses_count: int, optional
    :param tw_location: Twitter location of the identity. Applicable to Twitter channels only. , defaults to None
    :type tw_location: str, optional
    :param api_version: Viber API version of the identity. Applicable to Viber channels only. , defaults to None
    :type api_version: str, optional
    :param country: Viber country of the identity. Applicable to Viber channels only. , defaults to None
    :type country: str, optional
    :param device_type: Viber device type of the identity. Applicable to Viber channels only. , defaults to None
    :type device_type: str, optional
    :param language: Viber language of the identity. Applicable to Viber channels only. , defaults to None
    :type language: str, optional
    :param mcc: Viber mobile country code of the identity. Applicable to Viber channels only. , defaults to None
    :type mcc: str, optional
    :param mnc: Viber mobile network code of the identity. Applicable to Viber channels only. , defaults to None
    :type mnc: str, optional
    :param primary_device_os: Viber primary device OS of the identity. Applicable to Viber channels only. , defaults to None
    :type primary_device_os: str, optional
    :param viber_version: Viber application version of the identity. Applicable to Viber channels only. , defaults to None
    :type viber_version: str, optional
    """

    def __init__(
        self,
        id_: str,
        creation_time: str,
        type_: IdentityType,
        last_modified_time: str,
        avatar_uri: str = None,
        company: str = None,
        display_name: str = None,
        email_address: str = None,
        extra_values: dict = None,
        first_name: str = None,
        gender: SocMsgGender = None,
        home_phone: str = None,
        identity_group_id: str = None,
        last_name: str = None,
        mobile_phone: str = None,
        screen_name: str = None,
        user_ids: List[str] = None,
        uuid: str = None,
        mobile_device_info: str = None,
        fb_bio: str = None,
        fb_category: str = None,
        fb_locale: str = None,
        ig_followers_count: int = None,
        tw_description: str = None,
        tw_followers_count: int = None,
        tw_following_count: int = None,
        tw_statuses_count: int = None,
        tw_location: str = None,
        api_version: str = None,
        country: str = None,
        device_type: str = None,
        language: str = None,
        mcc: str = None,
        mnc: str = None,
        primary_device_os: str = None,
        viber_version: str = None,
    ):
        self.id_ = id_
        if avatar_uri is not None:
            self.avatar_uri = avatar_uri
        if company is not None:
            self.company = company
        self.creation_time = creation_time
        if display_name is not None:
            self.display_name = display_name
        if email_address is not None:
            self.email_address = email_address
        if extra_values is not None:
            self.extra_values = extra_values
        if first_name is not None:
            self.first_name = first_name
        if gender is not None:
            self.gender = self._enum_matching(gender, SocMsgGender.list(), "gender")
        if home_phone is not None:
            self.home_phone = home_phone
        if identity_group_id is not None:
            self.identity_group_id = identity_group_id
        if last_name is not None:
            self.last_name = last_name
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if screen_name is not None:
            self.screen_name = screen_name
        self.type_ = self._enum_matching(type_, IdentityType.list(), "type_")
        self.last_modified_time = last_modified_time
        if user_ids is not None:
            self.user_ids = user_ids
        if uuid is not None:
            self.uuid = uuid
        if mobile_device_info is not None:
            self.mobile_device_info = mobile_device_info
        if fb_bio is not None:
            self.fb_bio = fb_bio
        if fb_category is not None:
            self.fb_category = fb_category
        if fb_locale is not None:
            self.fb_locale = fb_locale
        if ig_followers_count is not None:
            self.ig_followers_count = ig_followers_count
        if tw_description is not None:
            self.tw_description = tw_description
        if tw_followers_count is not None:
            self.tw_followers_count = tw_followers_count
        if tw_following_count is not None:
            self.tw_following_count = tw_following_count
        if tw_statuses_count is not None:
            self.tw_statuses_count = tw_statuses_count
        if tw_location is not None:
            self.tw_location = tw_location
        if api_version is not None:
            self.api_version = api_version
        if country is not None:
            self.country = country
        if device_type is not None:
            self.device_type = device_type
        if language is not None:
            self.language = language
        if mcc is not None:
            self.mcc = mcc
        if mnc is not None:
            self.mnc = mnc
        if primary_device_os is not None:
            self.primary_device_os = primary_device_os
        if viber_version is not None:
            self.viber_version = viber_version
