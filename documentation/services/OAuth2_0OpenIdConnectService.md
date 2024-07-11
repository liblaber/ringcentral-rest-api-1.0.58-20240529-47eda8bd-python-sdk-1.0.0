# OAuth2_0OpenIdConnectService

A list of all methods in the `OAuth2_0OpenIdConnectService` service. Click on the method name to view detailed information about that method.

| Methods                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_token](#get_token)       | Returns access (and potentially refresh) tokens for making API requests. For confidential client application types this endpoint requires client authentication using one of the supported methods (`client_secret_basic`, `client_secret_jwt` or `private_key_jwt`) For non-confidential client application types the client identifier must be provided via `client_id` request attribute.                                                                                                                               |
| [authorize](#authorize)       | Performs Authentication of the End-User by sending the User Agent to the Authorization Server's Authorization Endpoint for Authentication and Authorization, using request parameters defined by OAuth 2.0 [RFC-6749](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1) and additional parameters and parameter values defined by [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint). This is the version that uses HTTP `GET` method.                        |
| [authorize2](#authorize2)     | Performs Authentication of the End-User by sending the User Agent to the Authorization Server's Authorization Endpoint for Authentication and Authorization, using request parameters defined by OAuth 2.0 [RFC-6749](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1) and additional parameters and parameter values defined by [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint). This is the version that uses HTTP `POST` method.                       |
| [revoke_token](#revoke_token) | Revokes all active access/refresh tokens and invalidates the OAuth session basing on token provided. The `token` parameter may be passed in query string or body and may represent access or refresh token. This endpoint is defined by [RFC-7009 "OAuth 2.0 Token Revocation"](https://datatracker.ietf.org/doc/html/rfc7009) For confidential client application types this endpoint requires client authentication using one of the supported methods (`client_secret_basic`, `client_secret_jwt` or `private_key_jwt`) |

## get_token

Returns access (and potentially refresh) tokens for making API requests. For confidential client application types this endpoint requires client authentication using one of the supported methods (`client_secret_basic`, `client_secret_jwt` or `private_key_jwt`) For non-confidential client application types the client identifier must be provided via `client_id` request attribute.

- HTTP Method: `POST`
- Endpoint: `/restapi/oauth/token`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [GetTokenRequest](../models/GetTokenRequest.md) | ✅       | The request body. |

**Return Type**

`TokenInfo`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models.get_token_request import GetTokenRequest1

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = GetTokenRequest1(
    grant_type="authorization_code",
    code="code",
    redirect_uri="redirect_uri",
    code_verifier="code_verifier",
    client_assertion_type="urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    client_assertion="client_assertion",
    scope="scope",
    client_id="AZwEVwGEcfGet2PCouA7K6",
    endpoint_id="endpoint_id",
    access_token_ttl=3600,
    refresh_token_ttl=604800
)

result = sdk.o_auth_2_0_open_id_connect.get_token(request_body=request_body)

print(result)
```

## authorize

Performs Authentication of the End-User by sending the User Agent to the Authorization Server's Authorization Endpoint for Authentication and Authorization, using request parameters defined by OAuth 2.0 [RFC-6749](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1) and additional parameters and parameter values defined by [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint). This is the version that uses HTTP `GET` method.

- HTTP Method: `GET`
- Endpoint: `/restapi/oauth/authorize`

**Parameters**

| Name                  | Type                                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :-------------------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| client_id             | str                                                             | ✅       | The registered identifier of a client application                                                                                                                                                                                                                                                                                                                                                                                             |
| response_type         | [AuthorizeResponseType](../models/AuthorizeResponseType.md)     | ✅       | Determines authorization flow type. The only supported value is `code` which corresponds to OAuth 2.0 "Authorization Code Flow"                                                                                                                                                                                                                                                                                                               |
| redirect_uri          | str                                                             | ❌       | This is the URI where the Authorization Server redirects the User Agent to at the end of the authorization flow. The value of this parameter must exactly match one of the URIs registered for this client application. This parameter is required if there are more than one redirect URIs registered for the app.                                                                                                                           |
| state                 | str                                                             | ❌       | An opaque value used by the client to maintain state between the request and callback. The authorization server includes this value when redirecting the User Agent back to the client. The parameter SHOULD be used for preventing cross-site request forgery attacks.                                                                                                                                                                       |
| scope                 | str                                                             | ❌       | The list of space separated application permissions (OAuth scopes)                                                                                                                                                                                                                                                                                                                                                                            |
| display               | [DisplayModesEnum](../models/DisplayModesEnum.md)               | ❌       | Specifies how the Authorization Server displays the authentication and consent user interface pages to the End-User.                                                                                                                                                                                                                                                                                                                          |
| prompt                | str                                                             | ❌       | Space-delimited, case-sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent. The defined values are: - `login` - RingCentral native login form, - `sso` - Single Sign-On login form, - `consent` - form to show the requested scope and prompt user for consent. Either `login` or `sso` (or both) must be specified. The default value is `login sso` |
| ui_locales            | str                                                             | ❌       | End-User's preferred languages and scripts for the user interface, represented as a space-separated list of [RFC-5646](https://datatracker.ietf.org/doc/html/rfc5646) language tag values, ordered by preference. If this parameter is provided, its value overrides 'Accept-Language' header value and 'localeId' parameter value (if any)                                                                                                   |
| locale_id             | str                                                             | ❌       | DEPRECATED: `ui_locales` parameter should be used instead                                                                                                                                                                                                                                                                                                                                                                                     |
| code_challenge        | str                                                             | ❌       | The code challenge value as defined by the PKCE specification - [RFC-7636 "Proof Key for Code Exchange by OAuth Public Clients"](https://datatracker.ietf.org/doc/html/rfc7636)                                                                                                                                                                                                                                                               |
| code_challenge_method | [CodeChallengeMethodEnum](../models/CodeChallengeMethodEnum.md) | ❌       | The code challenge method as defined by by the PKCE specification - [RFC-7636 "Proof Key for Code Exchange by OAuth Public Clients"](https://datatracker.ietf.org/doc/html/rfc7636)                                                                                                                                                                                                                                                           |
| nonce                 | str                                                             | ❌       | String value used to associate a Client session with an ID Token, and to mitigate replay attacks. The value is passed through unmodified from the Authentication Request to the ID Token.                                                                                                                                                                                                                                                     |
| ui_options            | str                                                             | ❌       | Login form user interface options (space-separated). By default, the UI options that are registered for this client application will be used                                                                                                                                                                                                                                                                                                  |
| login_hint            | str                                                             | ❌       | Hint to the Authorization Server about the login identifier the End-User might use to log in.                                                                                                                                                                                                                                                                                                                                                 |
| brand_id              | str                                                             | ❌       | RingCentral Brand identifier. If it is not provided in the request, server will try to determine brand from the client application profile.                                                                                                                                                                                                                                                                                                   |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AuthorizeResponseType, DisplayModesEnum, CodeChallengeMethodEnum

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.o_auth_2_0_open_id_connect.authorize(
    client_id="AZwEVwGEcfGet2PCouA7K6",
    response_type="code",
    redirect_uri="redirect_uri",
    state="state",
    scope="scope",
    display="page",
    prompt="login sso",
    ui_locales="en-US",
    code_challenge="code_challenge",
    code_challenge_method="plain",
    nonce="nonce",
    ui_options="ui_options",
    login_hint="login_hint",
    brand_id="1210"
)

print(result)
```

## authorize2

Performs Authentication of the End-User by sending the User Agent to the Authorization Server's Authorization Endpoint for Authentication and Authorization, using request parameters defined by OAuth 2.0 [RFC-6749](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1) and additional parameters and parameter values defined by [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint). This is the version that uses HTTP `POST` method.

- HTTP Method: `POST`
- Endpoint: `/restapi/oauth/authorize`

**Parameters**

| Name         | Type                                              | Required | Description       |
| :----------- | :------------------------------------------------ | :------- | :---------------- |
| request_body | [AuthorizeRequest](../models/AuthorizeRequest.md) | ✅       | The request body. |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AuthorizeRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AuthorizeRequest(
    response_type="code",
    redirect_uri="redirect_uri",
    client_id="AZwEVwGEcfGet2PCouA7K6",
    state="state",
    scope="scope",
    display="page",
    prompt="login sso",
    ui_locales="en-US",
    code_challenge="code_challenge",
    code_challenge_method="plain",
    nonce="nonce",
    ui_options="ui_options",
    login_hint="login_hint",
    brand_id="1210"
)

result = sdk.o_auth_2_0_open_id_connect.authorize2(request_body=request_body)

print(result)
```

## revoke_token

Revokes all active access/refresh tokens and invalidates the OAuth session basing on token provided. The `token` parameter may be passed in query string or body and may represent access or refresh token. This endpoint is defined by [RFC-7009 "OAuth 2.0 Token Revocation"](https://datatracker.ietf.org/doc/html/rfc7009) For confidential client application types this endpoint requires client authentication using one of the supported methods (`client_secret_basic`, `client_secret_jwt` or `private_key_jwt`)

- HTTP Method: `POST`
- Endpoint: `/restapi/oauth/revoke`

**Parameters**

| Name         | Type                                                  | Required | Description                                                                 |
| :----------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------- |
| request_body | [RevokeTokenRequest](../models/RevokeTokenRequest.md) | ❌       | The request body.                                                           |
| token        | str                                                   | ❌       | Access or refresh token to be revoked (along with the entire OAuth session) |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import RevokeTokenRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RevokeTokenRequest(
    token="token",
    client_assertion_type="urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    client_assertion="client_assertion"
)

result = sdk.o_auth_2_0_open_id_connect.revoke_token(
    request_body=request_body,
    token="token"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
