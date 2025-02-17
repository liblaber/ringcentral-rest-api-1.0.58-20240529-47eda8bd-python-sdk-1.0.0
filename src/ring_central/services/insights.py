# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.interaction_input import InteractionInput
from ..models.cai_async_api_response import CaiAsyncApiResponse


class InsightsService(BaseService):

    @cast_models
    def cai_analyze_interaction(
        self, request_body: InteractionInput, webhook: str
    ) -> CaiAsyncApiResponse:
        """Returns multiple insights including summaries, emotion, key phrases, questions asked, and more in a single API call.

        :param request_body: The request body.
        :type request_body: InteractionInput
        :param webhook: The webhook URI to which the job response will be returned
        :type webhook: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Task accepted for processing.
        :rtype: CaiAsyncApiResponse
        """

        Validator(InteractionInput).validate(request_body)
        Validator(str).validate(webhook)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ai/insights/v1/async/analyze-interaction",
                self.get_default_headers(),
            )
            .add_query("webhook", webhook)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CaiAsyncApiResponse._unmap(response)
