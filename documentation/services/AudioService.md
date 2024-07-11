# AudioService

A list of all methods in the `AudioService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                                                            |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [cai_enrollments_list](#cai_enrollments_list)     | Returns the List of Enrolled Speakers                                                                                                                  |
| [cai_enrollments_create](#cai_enrollments_create) | Creates Enrollment for the provided Speaker.                                                                                                           |
| [cai_enrollments_get](#cai_enrollments_get)       | Get The Status of Enrollment for the provided Speaker.                                                                                                 |
| [cai_enrollments_update](#cai_enrollments_update) | Add newer audio data to improve an existing speaker enrollment                                                                                         |
| [cai_enrollments_delete](#cai_enrollments_delete) | Delete The Enrollment for the provided Speaker.                                                                                                        |
| [cai_speech_to_text](#cai_speech_to_text)         | Returns Speech to Text Conversion to the provided webhook URI.                                                                                         |
| [cai_speaker_diarize](#cai_speaker_diarize)       | Identifies who said what. Speaker diarization will identify the speaker for each segment so you can tell who spoke the sentence, paragraph, or phrase. |
| [cai_speaker_identify](#cai_speaker_identify)     | Returns Speaker Identification to the provided webhook URI.                                                                                            |

## cai_enrollments_list

Returns the List of Enrolled Speakers

- HTTP Method: `GET`
- Endpoint: `/ai/audio/v1/enrollments`

**Parameters**

| Name     | Type | Required | Description                                                 |
| :------- | :--- | :------- | :---------------------------------------------------------- |
| partial  | bool | ✅       | Indicates if partially enrolled speakers should be returned |
| per_page | int  | ✅       | Number of enrollments to be returned per page               |
| page     | int  | ✅       | Page number to be returned                                  |

**Return Type**

`ListEnrolledSpeakers`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.audio.cai_enrollments_list(
    partial=True,
    per_page=6,
    page=7
)

print(result)
```

## cai_enrollments_create

Creates Enrollment for the provided Speaker.

- HTTP Method: `POST`
- Endpoint: `/ai/audio/v1/enrollments`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [EnrollmentInput](../models/EnrollmentInput.md) | ✅       | The request body. |

**Return Type**

`EnrollmentStatus`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EnrollmentInput

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EnrollmentInput(
    encoding="Mpeg",
    language_code="en-US",
    content="base64EncodedAudioInput",
    speaker_id="JohnDoe"
)

result = sdk.audio.cai_enrollments_create(request_body=request_body)

print(result)
```

## cai_enrollments_get

Get The Status of Enrollment for the provided Speaker.

- HTTP Method: `GET`
- Endpoint: `/ai/audio/v1/enrollments/{speakerId}`

**Parameters**

| Name       | Type | Required | Description                            |
| :--------- | :--- | :------- | :------------------------------------- |
| speaker_id | str  | ✅       | Speaker identifier of enrolled speaker |

**Return Type**

`EnrollmentStatus`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.audio.cai_enrollments_get(speaker_id="speakerId")

print(result)
```

## cai_enrollments_update

Add newer audio data to improve an existing speaker enrollment

- HTTP Method: `PATCH`
- Endpoint: `/ai/audio/v1/enrollments/{speakerId}`

**Parameters**

| Name         | Type                                                      | Required | Description                            |
| :----------- | :-------------------------------------------------------- | :------- | :------------------------------------- |
| request_body | [EnrollmentPatchInput](../models/EnrollmentPatchInput.md) | ✅       | The request body.                      |
| speaker_id   | str                                                       | ✅       | Speaker identifier of enrolled speaker |

**Return Type**

`EnrollmentStatus`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import EnrollmentPatchInput

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = EnrollmentPatchInput(
    encoding="Mpeg",
    language_code="en-US",
    content="base64EncodedAudioInput"
)

result = sdk.audio.cai_enrollments_update(
    request_body=request_body,
    speaker_id="speakerId"
)

print(result)
```

## cai_enrollments_delete

Delete The Enrollment for the provided Speaker.

- HTTP Method: `DELETE`
- Endpoint: `/ai/audio/v1/enrollments/{speakerId}`

**Parameters**

| Name       | Type | Required | Description                            |
| :--------- | :--- | :------- | :------------------------------------- |
| speaker_id | str  | ✅       | Speaker identifier of enrolled speaker |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.audio.cai_enrollments_delete(speaker_id="speakerId")

print(result)
```

## cai_speech_to_text

Returns Speech to Text Conversion to the provided webhook URI.

- HTTP Method: `POST`
- Endpoint: `/ai/audio/v1/async/speech-to-text`

**Parameters**

| Name         | Type                              | Required | Description                                                |
| :----------- | :-------------------------------- | :------- | :--------------------------------------------------------- |
| request_body | [AsrInput](../models/AsrInput.md) | ✅       | The request body.                                          |
| webhook      | str                               | ✅       | The webhook URI to which the job response will be returned |

**Return Type**

`CaiAsyncApiResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AsrInput

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AsrInput(
    content_uri="contentUri",
    encoding="Mpeg",
    language_code="en-US",
    source="RingCentral",
    audio_type="CallCenter",
    separate_speaker_per_channel=True,
    speaker_count=2,
    speaker_ids=[
        "speakerIds"
    ],
    enable_voice_activity_detection=True,
    enable_punctuation=True,
    enable_speaker_diarization=True,
    speech_contexts=[
        {
            "phrases": [
                "phrases"
            ]
        }
    ]
)

result = sdk.audio.cai_speech_to_text(
    request_body=request_body,
    webhook="webhook"
)

print(result)
```

## cai_speaker_diarize

Identifies who said what. Speaker diarization will identify the speaker for each segment so you can tell who spoke the sentence, paragraph, or phrase.

- HTTP Method: `POST`
- Endpoint: `/ai/audio/v1/async/speaker-diarize`

**Parameters**

| Name         | Type                                      | Required | Description                                                |
| :----------- | :---------------------------------------- | :------- | :--------------------------------------------------------- |
| request_body | [DiarizeInput](../models/DiarizeInput.md) | ✅       | The request body.                                          |
| webhook      | str                                       | ✅       | The webhook URI to which the job response will be returned |

**Return Type**

`CaiAsyncApiResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import DiarizeInput

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = DiarizeInput(
    content_uri="contentUri",
    encoding="Mpeg",
    language_code="en-US",
    source="RingCentral",
    audio_type="CallCenter",
    separate_speaker_per_channel=True,
    speaker_count=2,
    speaker_ids=[
        "speakerIds"
    ],
    enable_voice_activity_detection=False
)

result = sdk.audio.cai_speaker_diarize(
    request_body=request_body,
    webhook="webhook"
)

print(result)
```

## cai_speaker_identify

Returns Speaker Identification to the provided webhook URI.

- HTTP Method: `POST`
- Endpoint: `/ai/audio/v1/async/speaker-identify`

**Parameters**

| Name         | Type                                        | Required | Description                                                |
| :----------- | :------------------------------------------ | :------- | :--------------------------------------------------------- |
| request_body | [IdentifyInput](../models/IdentifyInput.md) | ✅       | The request body.                                          |
| webhook      | str                                         | ✅       | The webhook URI to which the job response will be returned |

**Return Type**

`CaiAsyncApiResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import IdentifyInput

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = IdentifyInput(
    content_uri="contentUri",
    encoding="Mpeg",
    language_code="en-US",
    source="RingCentral",
    audio_type="CallCenter",
    speaker_ids=[
        "speakerIds"
    ],
    enable_voice_activity_detection=False
)

result = sdk.audio.cai_speaker_identify(
    request_body=request_body,
    webhook="webhook"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
