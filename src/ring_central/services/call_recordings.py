# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.get_call_recording_response import GetCallRecordingResponse
from ..models.content_disposition import ContentDisposition
from ..models.call_recording_ids import CallRecordingIds


class CallRecordingsService(BaseService):

    @cast_models
    def read_call_recording_content(
        self,
        account_id: str,
        recording_id: str,
        content_disposition: ContentDisposition = None,
        content_disposition_filename: str = None,
    ) -> any:
        """Returns media content of a call recording (`audio/mpeg` or `audio/wav`)

        **This API must be called via media API entry point, e.g. https://media.ringcentral.com**

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param recording_id: Internal identifier of a call recording (returned in Call Log)
        :type recording_id: str
        :param content_disposition: Whether the content is expected to be displayed in the browser, or downloaded and saved locally, defaults to None
        :type content_disposition: ContentDisposition, optional
        :param content_disposition_filename: The default filename of the file to be downloaded, defaults to None
        :type content_disposition_filename: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: any
        """

        Validator(str).validate(account_id)
        Validator(str).validate(recording_id)
        Validator(ContentDisposition).is_optional().validate(content_disposition)
        Validator(str).is_optional().validate(content_disposition_filename)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/recording/{{recordingId}}/content",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("recordingId", recording_id)
            .add_query("contentDisposition", content_disposition)
            .add_query("contentDispositionFilename", content_disposition_filename)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def delete_company_call_recordings(
        self, request_body: CallRecordingIds, account_id: str
    ):
        """Deletes company call recordings by their IDs. *Please note:* This method deletes the recording file itself,
        not the record of it in the call log.

        :param request_body: The request body.
        :type request_body: CallRecordingIds
        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(CallRecordingIds).validate(request_body)
        Validator(str).validate(account_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/call-recordings",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .serialize()
            .set_method("DELETE")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def read_call_recording(
        self, account_id: str, recording_id: str
    ) -> GetCallRecordingResponse:
        """Returns call recordings by ID(s).

        :param account_id: Internal identifier of the RingCentral account
        (can be set to "~" to indicate that the account associated with current authorization session should be used)
        :type account_id: str
        :param recording_id: Internal identifier of a call recording (returned in Call Log)
        :type recording_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success
        :rtype: GetCallRecordingResponse
        """

        Validator(str).validate(account_id)
        Validator(str).validate(recording_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/restapi/v1.0/account/{{accountId}}/recording/{{recordingId}}",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_path("recordingId", recording_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCallRecordingResponse._unmap(response)
