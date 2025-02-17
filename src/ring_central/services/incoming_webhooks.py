# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.tm_webhook_list import TmWebhookList
from ..models.tm_webhook_info import TmWebhookInfo


class IncomingWebhooksService(BaseService):

    @cast_models
    def list_glip_webhooks_new(self) -> TmWebhookList:
        """Returns the list of all webhooks associated with the current account.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: TmWebhookList
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/webhooks",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return TmWebhookList._unmap(response)

    @cast_models
    def read_glip_webhook_new(self, webhook_id: List[str]) -> TmWebhookList:
        """Returns webhooks(s) with the specified id(s).

        :param webhook_id: Internal identifier of a webhook or comma separated list of webhooks IDs
        :type webhook_id: List[str]
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: TmWebhookList
        """

        Validator(str).is_array().validate(webhook_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/webhooks/{{webhookId}}",
                self.get_default_headers(),
            )
            .add_path("webhookId", webhook_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return TmWebhookList._unmap(response)

    @cast_models
    def delete_glip_webhook_new(self, webhook_id: str):
        """Deletes a webhook by ID.

        :param webhook_id: Internal identifier of a webhook
        :type webhook_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(webhook_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/webhooks/{{webhookId}}",
                self.get_default_headers(),
            )
            .add_path("webhookId", webhook_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def activate_glip_webhook_new(self, webhook_id: str):
        """Activates a webhook by ID.

        :param webhook_id: Internal identifier of a webhook
        :type webhook_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(webhook_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/webhooks/{{webhookId}}/activate",
                self.get_default_headers(),
            )
            .add_path("webhookId", webhook_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def suspend_glip_webhook_new(self, webhook_id: str):
        """Suspends a webhook by ID.

        :param webhook_id: Internal identifier of a webhook
        :type webhook_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(webhook_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/webhooks/{{webhookId}}/suspend",
                self.get_default_headers(),
            )
            .add_path("webhookId", webhook_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def list_glip_group_webhooks_new(self, group_id: str) -> TmWebhookList:
        """Returns webhooks which are available for the current user by group ID.

        :param group_id: Internal identifier of a group
        :type group_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: TmWebhookList
        """

        Validator(str).validate(group_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/groups/{{groupId}}/webhooks",
                self.get_default_headers(),
            )
            .add_path("groupId", group_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return TmWebhookList._unmap(response)

    @cast_models
    def create_glip_group_webhook_new(self, group_id: str) -> TmWebhookInfo:
        """Creates a new webhook.

        :param group_id: Internal identifier of a group
        :type group_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: TmWebhookInfo
        """

        Validator(str).validate(group_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/groups/{{groupId}}/webhooks",
                self.get_default_headers(),
            )
            .add_path("groupId", group_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)

        return TmWebhookInfo._unmap(response)
