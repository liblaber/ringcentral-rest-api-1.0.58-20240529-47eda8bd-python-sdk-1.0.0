# RecordingDownloadModel

**Properties**

| Name                  | Type                | Required | Description                                             |
| :-------------------- | :------------------ | :------- | :------------------------------------------------------ |
| download_uri          | str                 | ✅       | Download URI (available only for webinar host or admin) |
| download_content_type | DownloadContentType | ✅       | MIME type of the file to download.                      |
| download_size         | int                 | ✅       | Download file size in bytes                             |

# DownloadContentType

MIME type of the file to download.

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| VIDEO_MP4 | str  | ✅       | "video/mp4" |
| AUDIO_M4A | str  | ✅       | "audio/m4a" |

<!-- This file was generated by liblab | https://liblab.com/ -->
