# SubscriptionsService

A list of all methods in the `SubscriptionsService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_subscriptions](#list_subscriptions)   | Returns a list of subscriptions created by the user for the current authorized client application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [create_subscription](#create_subscription) | This API allows client applications to register a new subscription so that it can be notified of events when they occur on the platform. A subscription relates to a set of events that a client application would like to be informed of and the delivery channel by which they will be notified of those events. How subscriptions are established depends upon the notification channel the client application would like to use to receive the event notification. For example, to create a webhook a developer would create a subscription via a REST API call, while specifying a list of events or "event filters" to be notified of, a transport type of `WebHook`, and the address or URL to which they would like the webhook delivered. However, developers wishing to subscribe to a set of events via a WebSocket channel, would first connect to the WebSocket gateway, and then issue their subscription request over the WebSocket itself, as opposed to making a REST API call to this endpoint. While the protocol for establishing a subscription may vary depending upon the delivery channel for that subscription, the schemas used for representing a subscription are the same across all delivery modes. Subscriptions are currently limited to 20 subscriptions per user/extension (for particular application). RingCentral currently supports the following delivery modes for event subscriptions: _ [WebHook](https://developers.ringcentral.com/guide/notifications/webhooks/quick-start) - to receive event notifications as an HTTP POST to a given URL _ [WebSocket](https://developers.ringcentral.com/guide/notifications/websockets/quick-start) - to receive real-time events over a persistent WebSocket connection \* [PubNub](https://developers.ringcentral.com/guide/notifications/push-notifications/quick-start) (deprecated) - to receive a push notification sent directly to a client application Developers should be aware that the PubNub delivery mode is currently deprecated and will be removed in 2024. Developers are encouraged to [migrate their client applications to use WebSockets](https://developers.ringcentral.com/guide/notifications/websockets/migration/) instead. |
| [read_subscription](#read_subscription)     | Returns the existing subscription by ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [update_subscription](#update_subscription) | Updates the existing subscription. The client application can extend or narrow the list of events for which it receives notifications within the current subscription. If event filters are specified, calling this method modifies them for the existing subscription. The method also allows one to set an expiration time for the subscription itself. If parameters other than `events` and `expiresIn` are specified in the request they will be ignored. If the request body is empty then the specified subscription will be renewed without any event filter modifications and using the default expiration time. If the request is sent with empty body, it just renews a subscription (so it is an equivalent of the `POST /restapi/v1.0/subscription/{subscriptionId}/renew`). Please note that `WebSocket` subscriptions cannot be updated via HTTP interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [delete_subscription](#delete_subscription) | Cancels the existing subscription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [renew_subscription](#renew_subscription)   | Renews the existing subscription (this request comes with empty body). Please note that `WebSocket` subscriptions are renewed automatically while websocket session is alive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## list_subscriptions

Returns a list of subscriptions created by the user for the current authorized client application.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/subscription`

**Return Type**

`SubscriptionListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.subscriptions.list_subscriptions()

print(result)
```

## create_subscription

This API allows client applications to register a new subscription so that it can be notified of events when they occur on the platform. A subscription relates to a set of events that a client application would like to be informed of and the delivery channel by which they will be notified of those events. How subscriptions are established depends upon the notification channel the client application would like to use to receive the event notification. For example, to create a webhook a developer would create a subscription via a REST API call, while specifying a list of events or "event filters" to be notified of, a transport type of `WebHook`, and the address or URL to which they would like the webhook delivered. However, developers wishing to subscribe to a set of events via a WebSocket channel, would first connect to the WebSocket gateway, and then issue their subscription request over the WebSocket itself, as opposed to making a REST API call to this endpoint. While the protocol for establishing a subscription may vary depending upon the delivery channel for that subscription, the schemas used for representing a subscription are the same across all delivery modes. Subscriptions are currently limited to 20 subscriptions per user/extension (for particular application). RingCentral currently supports the following delivery modes for event subscriptions: _ [WebHook](https://developers.ringcentral.com/guide/notifications/webhooks/quick-start) - to receive event notifications as an HTTP POST to a given URL _ [WebSocket](https://developers.ringcentral.com/guide/notifications/websockets/quick-start) - to receive real-time events over a persistent WebSocket connection \* [PubNub](https://developers.ringcentral.com/guide/notifications/push-notifications/quick-start) (deprecated) - to receive a push notification sent directly to a client application Developers should be aware that the PubNub delivery mode is currently deprecated and will be removed in 2024. Developers are encouraged to [migrate their client applications to use WebSockets](https://developers.ringcentral.com/guide/notifications/websockets/migration/) instead.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/subscription`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [CreateSubscriptionRequest](../models/CreateSubscriptionRequest.md) | ✅       | The request body. |

**Return Type**

`SubscriptionInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateSubscriptionRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateSubscriptionRequest(
    event_filters=[
        "anim "
    ],
    expires_in=1200,
    delivery_mode={
        "transport_type": "WebHook",
        "address": "https://acme.com/myservice/webhook",
        "verification_token": "verificationToken"
    }
)

result = sdk.subscriptions.create_subscription(request_body=request_body)

print(result)
```

## read_subscription

Returns the existing subscription by ID.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/subscription/{subscriptionId}`

**Parameters**

| Name            | Type | Required | Description                           |
| :-------------- | :--- | :------- | :------------------------------------ |
| subscription_id | str  | ✅       | Internal identifier of a subscription |

**Return Type**

`SubscriptionInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.subscriptions.read_subscription(subscription_id="reprehende")

print(result)
```

## update_subscription

Updates the existing subscription. The client application can extend or narrow the list of events for which it receives notifications within the current subscription. If event filters are specified, calling this method modifies them for the existing subscription. The method also allows one to set an expiration time for the subscription itself. If parameters other than `events` and `expiresIn` are specified in the request they will be ignored. If the request body is empty then the specified subscription will be renewed without any event filter modifications and using the default expiration time. If the request is sent with empty body, it just renews a subscription (so it is an equivalent of the `POST /restapi/v1.0/subscription/{subscriptionId}/renew`). Please note that `WebSocket` subscriptions cannot be updated via HTTP interface.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/subscription/{subscriptionId}`

**Parameters**

| Name            | Type                                                                | Required | Description                           |
| :-------------- | :------------------------------------------------------------------ | :------- | :------------------------------------ |
| request_body    | [UpdateSubscriptionRequest](../models/UpdateSubscriptionRequest.md) | ❌       | The request body.                     |
| subscription_id | str                                                                 | ✅       | Internal identifier of a subscription |

**Return Type**

`SubscriptionInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import UpdateSubscriptionRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateSubscriptionRequest(
    event_filters=[
        "sit veniam"
    ],
    expires_in=1200
)

result = sdk.subscriptions.update_subscription(
    request_body=request_body,
    subscription_id="ut in magna Lorem "
)

print(result)
```

## delete_subscription

Cancels the existing subscription.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v1.0/subscription/{subscriptionId}`

**Parameters**

| Name            | Type | Required | Description                           |
| :-------------- | :--- | :------- | :------------------------------------ |
| subscription_id | str  | ✅       | Internal identifier of a subscription |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.subscriptions.delete_subscription(subscription_id="non i")

print(result)
```

## renew_subscription

Renews the existing subscription (this request comes with empty body). Please note that `WebSocket` subscriptions are renewed automatically while websocket session is alive.

- HTTP Method: `POST`
- Endpoint: `/restapi/v1.0/subscription/{subscriptionId}/renew`

**Parameters**

| Name            | Type | Required | Description                           |
| :-------------- | :--- | :------- | :------------------------------------ |
| subscription_id | str  | ✅       | Internal identifier of a subscription |

**Return Type**

`SubscriptionInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.subscriptions.renew_subscription(subscription_id="ullamco v")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
