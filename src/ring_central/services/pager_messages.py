# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.get_internal_text_message_info_response import (
    GetInternalTextMessageInfoResponse,
)
from ..models.create_internal_text_message_request import (
    CreateInternalTextMessageRequest,
)


class PagerMessagesService(BaseService):

    @cast_models
    def create_internal_text_message(
        self,
        request_body: CreateInternalTextMessageRequest,
        account_id: str,
        extension_id: str,
    ) -> GetInternalTextMessageInfoResponse:
        """Creates and sends an internal text message (company pager message).

        :param request_body: The request body.
        :type request_body: CreateInternalTextMessageRequest
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param extension_id: Internal identifier of the RingCentral extension/user
        (can be set to "~" to indicate that the extension associated with current authorization session should be used)
        :type extension_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created text message
        :rtype: GetInternalTextMessageInfoResponse
        """

        Validator(CreateInternalTextMessageRequest).validate(request_body)
        Validator(str).validate(account_id)
        Validator(str).validate(extension_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/extension/{{extensionId}}/company-pager",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("extensionId", extension_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetInternalTextMessageInfoResponse._unmap(response)
