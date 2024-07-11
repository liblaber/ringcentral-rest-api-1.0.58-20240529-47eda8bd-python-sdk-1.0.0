# WebinarSubscriptionsService

A list of all methods in the `WebinarSubscriptionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rcw_n11s_list_subscriptions](#rcw_n11s_list_subscriptions)   | Returns a list of webinar subscriptions created by the user for the current authorized client application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [rcw_n11s_create_subscription](#rcw_n11s_create_subscription) | Creates a new webinar subscription for the current authorized user / client application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [rcw_n11s_get_subscription](#rcw_n11s_get_subscription)       | Returns the webinar subscription by ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [rcw_n11s_update_subscription](#rcw_n11s_update_subscription) | Updates the existing subscription. The client application can extend/narrow the list of events for which it receives notifications within this subscription. If event filters are specified, calling this method modifies them for the existing subscription. The method also allows setting the subscription expiration time. If other than `events` and `expiresIn` parameters are passed in the request they will be ignored. If the request body is empty then the specified subscription will be just renewed without any event filter modifications and with default expiration time. |
| [rcw_n11s_delete_subscription](#rcw_n11s_delete_subscription) | Cancels the existing webinar subscription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [rcw_n11s_renew_subscription](#rcw_n11s_renew_subscription)   | Renews the existing webinar subscription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## rcw_n11s_list_subscriptions

Returns a list of webinar subscriptions created by the user for the current authorized client application.

- HTTP Method: `GET`
- Endpoint: `/webinar/notifications/v1/subscriptions`

**Return Type**

`SubscriptionListResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.webinar_subscriptions.rcw_n11s_list_subscriptions()

print(result)
```

## rcw_n11s_create_subscription

Creates a new webinar subscription for the current authorized user / client application.

- HTTP Method: `POST`
- Endpoint: `/webinar/notifications/v1/subscriptions`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateWebhookSubscriptionRequest](../models/CreateWebhookSubscriptionRequest.md) | ✅       | The request body. |

**Return Type**

`SubscriptionInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import CreateWebhookSubscriptionRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateWebhookSubscriptionRequest(
    event_filters=[
        "sint in eu te"
    ],
    expires_in=1200,
    delivery_mode={
        "transport_type": "WebHook",
        "address": "https://acme.com/myservice/webhook",
        "verification_token": "verificationToken"
    }
)

result = sdk.webinar_subscriptions.rcw_n11s_create_subscription(request_body=request_body)

print(result)
```

## rcw_n11s_get_subscription

Returns the webinar subscription by ID

- HTTP Method: `GET`
- Endpoint: `/webinar/notifications/v1/subscriptions/{subscriptionId}`

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

result = sdk.webinar_subscriptions.rcw_n11s_get_subscription(subscription_id="aliqua ad dolor")

print(result)
```

## rcw_n11s_update_subscription

Updates the existing subscription. The client application can extend/narrow the list of events for which it receives notifications within this subscription. If event filters are specified, calling this method modifies them for the existing subscription. The method also allows setting the subscription expiration time. If other than `events` and `expiresIn` parameters are passed in the request they will be ignored. If the request body is empty then the specified subscription will be just renewed without any event filter modifications and with default expiration time.

- HTTP Method: `PUT`
- Endpoint: `/webinar/notifications/v1/subscriptions/{subscriptionId}`

**Parameters**

| Name            | Type                                                                | Required | Description                           |
| :-------------- | :------------------------------------------------------------------ | :------- | :------------------------------------ |
| request_body    | [UpdateSubscriptionRequest](../models/UpdateSubscriptionRequest.md) | ✅       | The request body.                     |
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

result = sdk.webinar_subscriptions.rcw_n11s_update_subscription(
    request_body=request_body,
    subscription_id="ipsum esse"
)

print(result)
```

## rcw_n11s_delete_subscription

Cancels the existing webinar subscription.

- HTTP Method: `DELETE`
- Endpoint: `/webinar/notifications/v1/subscriptions/{subscriptionId}`

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

result = sdk.webinar_subscriptions.rcw_n11s_delete_subscription(subscription_id="in id ex aliqua")

print(result)
```

## rcw_n11s_renew_subscription

Renews the existing webinar subscription.

- HTTP Method: `POST`
- Endpoint: `/webinar/notifications/v1/subscriptions/{subscriptionId}/renew`

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

result = sdk.webinar_subscriptions.rcw_n11s_renew_subscription(subscription_id="ullamco labore vol")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
