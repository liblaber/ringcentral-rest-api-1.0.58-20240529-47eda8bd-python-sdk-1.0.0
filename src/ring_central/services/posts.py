# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.tm_update_post_request import TmUpdatePostRequest
from ..models.tm_posts_list import TmPostsList
from ..models.tm_post_info import TmPostInfo
from ..models.tm_create_post_request import TmCreatePostRequest
from ..models.tm_add_file_request import TmAddFileRequest
from ..models.create_glip_file_new_request import CreateGlipFileNewRequest


class PostsService(BaseService):

    @cast_models
    def create_glip_file_new(
        self, request_body: dict, group_id: int = None, name: str = None
    ) -> TmAddFileRequest:
        """Posts a file.

        :param request_body: The request body.
        :type request_body: dict
        :param group_id: Internal identifier of a group to which the post with attachment will be added to, defaults to None
        :type group_id: int, optional
        :param name: Name of a file attached, defaults to None
        :type name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success
        :rtype: TmAddFileRequest
        """

        Validator(dict).validate(request_body)
        Validator(int).is_optional().validate(group_id)
        Validator(str).is_optional().validate(name)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/files", self.get_default_headers()
            )
            .add_query("groupId", group_id)
            .add_query("name", name)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response = self.send_request(serialized_request)

        return TmAddFileRequest._unmap(response)

    @cast_models
    def read_glip_posts_new(
        self, chat_id: str, record_count: int = None, page_token: str = None
    ) -> TmPostsList:
        """Returns a list of posts from the specified chat.

        :param chat_id: Internal identifier of a chat
        :type chat_id: str
        :param record_count: Max number of posts to be fetched by one request (not more than 250), defaults to None
        :type record_count: int, optional
        :param page_token: Pagination token., defaults to None
        :type page_token: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: OK
        :rtype: TmPostsList
        """

        Validator(str).validate(chat_id)
        Validator(int).is_optional().max(250).validate(record_count)
        Validator(str).is_optional().validate(page_token)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/chats/{{chatId}}/posts",
                self.get_default_headers(),
            )
            .add_path("chatId", chat_id)
            .add_query("recordCount", record_count)
            .add_query("pageToken", page_token)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return TmPostsList._unmap(response)

    @cast_models
    def create_glip_post_new(
        self, request_body: TmCreatePostRequest, chat_id: str
    ) -> TmPostInfo:
        """Creates a post in the chat specified in path. Any mention can be added within the `text` attribute of the request body in .md format - `![:Type](id)`, where `type` is one of (Person, Team, File, Note, Task, Event, Link, Card) and `id` is a unique identifier of the mentioned object of the specified type. Attachments of the following types (File, Card, Event, Note) can also be added to a post by passing type and ID of attachment(s) in request body.

        :param request_body: The request body.
        :type request_body: TmCreatePostRequest
        :param chat_id: Internal identifier of a chat.
        :type chat_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success
        :rtype: TmPostInfo
        """

        Validator(TmCreatePostRequest).validate(request_body)
        Validator(str).validate(chat_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/chats/{{chatId}}/posts",
                self.get_default_headers(),
            )
            .add_path("chatId", chat_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return TmPostInfo._unmap(response)

    @cast_models
    def read_glip_post_new(self, chat_id: str, post_id: str) -> TmPostInfo:
        """Returns information about the specified post.

        :param chat_id: Internal identifier of a chat
        :type chat_id: str
        :param post_id: Internal identifier of a post
        :type post_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success
        :rtype: TmPostInfo
        """

        Validator(str).validate(chat_id)
        Validator(str).validate(post_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/chats/{{chatId}}/posts/{{postId}}",
                self.get_default_headers(),
            )
            .add_path("chatId", chat_id)
            .add_path("postId", post_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return TmPostInfo._unmap(response)

    @cast_models
    def patch_glip_post_new(
        self, request_body: TmUpdatePostRequest, chat_id: str, post_id: str
    ) -> TmPostInfo:
        """Updates a specific post within a chat.

        :param request_body: The request body.
        :type request_body: TmUpdatePostRequest
        :param chat_id: Internal identifier of a chat
        :type chat_id: str
        :param post_id: Internal identifier of a post to be updated
        :type post_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success
        :rtype: TmPostInfo
        """

        Validator(TmUpdatePostRequest).validate(request_body)
        Validator(str).validate(chat_id)
        Validator(str).validate(post_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/chats/{{chatId}}/posts/{{postId}}",
                self.get_default_headers(),
            )
            .add_path("chatId", chat_id)
            .add_path("postId", post_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return TmPostInfo._unmap(response)

    @cast_models
    def delete_glip_post_new(self, chat_id: str, post_id: str):
        """Deletes the specified post from the chat.

        :param chat_id: Internal identifier of a chat
        :type chat_id: str
        :param post_id: Internal identifier of a post to be deleted
        :type post_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(chat_id)
        Validator(str).validate(post_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/team-messaging/v1/chats/{{chatId}}/posts/{{postId}}",
                self.get_default_headers(),
            )
            .add_path("chatId", chat_id)
            .add_path("postId", post_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response
