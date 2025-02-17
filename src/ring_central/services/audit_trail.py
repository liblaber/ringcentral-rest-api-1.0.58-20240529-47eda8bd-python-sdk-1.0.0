# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.account_history_search_public_response import (
    AccountHistorySearchPublicResponse,
)
from ..models.account_history_search_public_request import (
    AccountHistorySearchPublicRequest,
)


class AuditTrailService(BaseService):

    @cast_models
    def audit_trail_search(
        self, account_id: str, request_body: AccountHistorySearchPublicRequest = None
    ) -> AccountHistorySearchPublicResponse:
        """Returns the audit trail data with specific filters applied.
        Audit trail searching is limited to the last 10,000 records or last 180 days, whichever comes first.

        :param request_body: The request body., defaults to None
        :type request_body: AccountHistorySearchPublicRequest, optional
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List of Account History Records
        :rtype: AccountHistorySearchPublicResponse
        """

        Validator(AccountHistorySearchPublicRequest).is_optional().validate(
            request_body
        )
        Validator(str).validate(account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/audit-trail/search",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return AccountHistorySearchPublicResponse._unmap(response)
