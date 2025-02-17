# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "password_protected": "passwordProtected",
        "no_guests": "noGuests",
        "same_account": "sameAccount",
    }
)
class BridgeRequestSecurity(BaseModel):
    """BridgeRequestSecurity

    :param password_protected: Specifies if a meeting is password protected. By default, Instant and Scheduled bridges are not password protected. For default (PMI) bridge, password protection will be turned on and the password will be generated if it is not specified while creation. While creation to set password protection you should set this field to true and specify a password in the **password** field. If you want to change password or set password protection for an unprotected bridge, you should set this field to true and specify a password in the **password** field in the update operation. To make protected bridge as unprotected you should set this field to false in the update operation. , defaults to None
    :type password_protected: bool, optional
    :param password: Specifies a password if bridge meetings should be password protected (passwordProtected field is true). Besides that, if the field is specified in the request but **passwordProtected** field is missing then it means that **passwordProtected** field is set to true. , defaults to None
    :type password: str, optional
    :param no_guests: If true, only authenticated users can join to a meeting., defaults to None
    :type no_guests: bool, optional
    :param same_account: If true, only users have the same account can join to a meeting., defaults to None
    :type same_account: bool, optional
    :param e2ee: If true, end to end encryption will be enabled for a meeting., defaults to None
    :type e2ee: bool, optional
    """

    def __init__(
        self,
        password_protected: bool = None,
        password: str = None,
        no_guests: bool = None,
        same_account: bool = None,
        e2ee: bool = None,
    ):
        if password_protected is not None:
            self.password_protected = password_protected
        if password is not None:
            self.password = password
        if no_guests is not None:
            self.no_guests = no_guests
        if same_account is not None:
            self.same_account = same_account
        if e2ee is not None:
            self.e2ee = e2ee
