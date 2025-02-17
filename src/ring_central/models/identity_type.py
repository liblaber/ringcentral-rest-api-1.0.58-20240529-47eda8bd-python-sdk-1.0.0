# This file was generated by liblab | https://liblab.com/

from enum import Enum


class IdentityType(Enum):
    """An enumeration representing different categories.

    :cvar APPLEMESSAGESFORBUSINESS: "AppleMessagesForBusiness"
    :vartype APPLEMESSAGESFORBUSINESS: str
    :cvar EMAIL: "Email"
    :vartype EMAIL: str
    :cvar ENGAGEMESSAGING: "EngageMessaging"
    :vartype ENGAGEMESSAGING: str
    :cvar FACEBOOK: "Facebook"
    :vartype FACEBOOK: str
    :cvar GOOGLEBUSINESSMESSAGES: "GoogleBusinessMessages"
    :vartype GOOGLEBUSINESSMESSAGES: str
    :cvar GOOGLEMYBUSINESS: "GoogleMyBusiness"
    :vartype GOOGLEMYBUSINESS: str
    :cvar INSTAGRAM: "Instagram"
    :vartype INSTAGRAM: str
    :cvar LINKEDIN: "Linkedin"
    :vartype LINKEDIN: str
    :cvar TWITTER: "Twitter"
    :vartype TWITTER: str
    :cvar VIBER: "Viber"
    :vartype VIBER: str
    :cvar WHATSAPP: "WhatsApp"
    :vartype WHATSAPP: str
    :cvar YOUTUBE: "Youtube"
    :vartype YOUTUBE: str
    """

    APPLEMESSAGESFORBUSINESS = "AppleMessagesForBusiness"
    EMAIL = "Email"
    ENGAGEMESSAGING = "EngageMessaging"
    FACEBOOK = "Facebook"
    GOOGLEBUSINESSMESSAGES = "GoogleBusinessMessages"
    GOOGLEMYBUSINESS = "GoogleMyBusiness"
    INSTAGRAM = "Instagram"
    LINKEDIN = "Linkedin"
    TWITTER = "Twitter"
    VIBER = "Viber"
    WHATSAPP = "WhatsApp"
    YOUTUBE = "Youtube"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, IdentityType._member_map_.values()))
