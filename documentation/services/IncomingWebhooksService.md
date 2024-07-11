# IncomingWebhooksService

A list of all methods in the `IncomingWebhooksService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                                            |
| :-------------------------------------------------------------- | :--------------------------------------------------------------------- |
| [list_glip_webhooks_new](#list_glip_webhooks_new)               | Returns the list of all webhooks associated with the current account.  |
| [read_glip_webhook_new](#read_glip_webhook_new)                 | Returns webhooks(s) with the specified id(s).                          |
| [delete_glip_webhook_new](#delete_glip_webhook_new)             | Deletes a webhook by ID.                                               |
| [activate_glip_webhook_new](#activate_glip_webhook_new)         | Activates a webhook by ID.                                             |
| [suspend_glip_webhook_new](#suspend_glip_webhook_new)           | Suspends a webhook by ID.                                              |
| [list_glip_group_webhooks_new](#list_glip_group_webhooks_new)   | Returns webhooks which are available for the current user by group ID. |
| [create_glip_group_webhook_new](#create_glip_group_webhook_new) | Creates a new webhook.                                                 |

## list_glip_webhooks_new

Returns the list of all webhooks associated with the current account.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/webhooks`

**Return Type**

`TmWebhookList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.incoming_webhooks.list_glip_webhooks_new()

print(result)
```

## read_glip_webhook_new

Returns webhooks(s) with the specified id(s).

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/webhooks/{webhookId}`

**Parameters**

| Name       | Type      | Required | Description                                                              |
| :--------- | :-------- | :------- | :----------------------------------------------------------------------- |
| webhook_id | List[str] | ✅       | Internal identifier of a webhook or comma separated list of webhooks IDs |

**Return Type**

`TmWebhookList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
webhook_id=[
    "webhookId"
]

result = sdk.incoming_webhooks.read_glip_webhook_new(webhook_id=webhook_id)

print(result)
```

## delete_glip_webhook_new

Deletes a webhook by ID.

- HTTP Method: `DELETE`
- Endpoint: `/team-messaging/v1/webhooks/{webhookId}`

**Parameters**

| Name       | Type | Required | Description                      |
| :--------- | :--- | :------- | :------------------------------- |
| webhook_id | str  | ✅       | Internal identifier of a webhook |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.incoming_webhooks.delete_glip_webhook_new(webhook_id="webhookId")

print(result)
```

## activate_glip_webhook_new

Activates a webhook by ID.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/webhooks/{webhookId}/activate`

**Parameters**

| Name       | Type | Required | Description                      |
| :--------- | :--- | :------- | :------------------------------- |
| webhook_id | str  | ✅       | Internal identifier of a webhook |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.incoming_webhooks.activate_glip_webhook_new(webhook_id="webhookId")

print(result)
```

## suspend_glip_webhook_new

Suspends a webhook by ID.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/webhooks/{webhookId}/suspend`

**Parameters**

| Name       | Type | Required | Description                      |
| :--------- | :--- | :------- | :------------------------------- |
| webhook_id | str  | ✅       | Internal identifier of a webhook |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.incoming_webhooks.suspend_glip_webhook_new(webhook_id="webhookId")

print(result)
```

## list_glip_group_webhooks_new

Returns webhooks which are available for the current user by group ID.

- HTTP Method: `GET`
- Endpoint: `/team-messaging/v1/groups/{groupId}/webhooks`

**Parameters**

| Name     | Type | Required | Description                    |
| :------- | :--- | :------- | :----------------------------- |
| group_id | str  | ✅       | Internal identifier of a group |

**Return Type**

`TmWebhookList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.incoming_webhooks.list_glip_group_webhooks_new(group_id="groupId")

print(result)
```

## create_glip_group_webhook_new

Creates a new webhook.

- HTTP Method: `POST`
- Endpoint: `/team-messaging/v1/groups/{groupId}/webhooks`

**Parameters**

| Name     | Type | Required | Description                    |
| :------- | :--- | :------- | :----------------------------- |
| group_id | str  | ✅       | Internal identifier of a group |

**Return Type**

`TmWebhookInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.incoming_webhooks.create_glip_group_webhook_new(group_id="groupId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
