# GetTokenRequest

# GetTokenRequest_1

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest1GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| code                  | str                                 | ❌       | For `authorization_code` grant type only. User's authorization code                                                                                                                                                                                                                                                          |
| redirect_uri          | str                                 | ❌       | For `authorization_code` grant type only. This is a callback URI which determines where the response is sent. The value of this parameter must exactly match one of the URIs you have provided for your app upon registration                                                                                                |
| code_verifier         | str                                 | ❌       | For `authorization_code` grant type only. The code verifier as defined by the PKCE specification - [RFC-7636 "Proof Key for Code Exchange by OAuth Public Clients"](https://datatracker.ietf.org/doc/html/rfc7636)                                                                                                           |
| client_assertion_type | GetTokenRequest1ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_1GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_1ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_2

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest2GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| username              | str                                 | ❌       | For `password` grant type only. User login name: email or phone number in E.164 format                                                                                                                                                                                                                                       |
| password              | str                                 | ❌       | For `password` grant type only. User's password                                                                                                                                                                                                                                                                              |
| extension             | str                                 | ❌       | For `password` grant type only. Optional. Extension short number. If a company number is specified as a username, and extension is not specified, the server will attempt to authenticate client as main company administrator DEPRECATED: use extension number embedded into username string like `+16501234567*101`        |
| pin                   | str                                 | ❌       | IVR pin for pin-based authentication. DEPRECATED: use a dedicated `ivr_pin` grant type instead                                                                                                                                                                                                                               |
| client_assertion_type | GetTokenRequest2ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_2GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_2ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_3

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest3GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| assertion             | str                                 | ❌       | For `urn:ietf:params:oauth:grant-type:jwt-bearer` or `partner_jwt` grant types only. Authorization grant assertion (JWT) as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.1).                                                                                                                |
| client_assertion_type | GetTokenRequest3ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_3GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_3ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_4

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest4GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| refresh_token         | str                                 | ❌       | For `refresh_token` grant type only. Previously issued refresh token.                                                                                                                                                                                                                                                        |
| client_assertion_type | GetTokenRequest4ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_4GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_4ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_5

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest5GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| ivr_pin               | str                                 | ❌       | For `ivr_pin` grant type only. User's IVR pin.                                                                                                                                                                                                                                                                               |
| client_assertion_type | GetTokenRequest5ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_5GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_5ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_6

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest6GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| device_code           | str                                 | ❌       | For `urn:ietf:params:oauth:grant-type:device_code` grant type only. The device verification code as defined by [RFC-8628](https://datatracker.ietf.org/doc/html/rfc8628#section-3.4)                                                                                                                                         |
| client_assertion_type | GetTokenRequest6ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_6GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_6ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_7

# GetTokenRequest_7_1

**Properties**

| Name                  | Type                                  | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :------------------------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id            | str                                   | ✅       | RingCentral internal account ID                                                                                                                                                                                                                                                                                              |
| grant_type            | GetTokenRequest7_1GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| client_assertion_type | GetTokenRequest7_1ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                   | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                   | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                   | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                   | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                   | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                   | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_7_1GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_7_1ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_7_2

**Properties**

| Name                  | Type                                  | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :------------------------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| brand_id              | str                                   | ✅       | RingCentral Brand identifier.                                                                                                                                                                                                                                                                                                |
| grant_type            | GetTokenRequest7_2GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| partner_account_id    | str                                   | ❌       | The ID of the account on RingCentral partner's side                                                                                                                                                                                                                                                                          |
| client_assertion_type | GetTokenRequest7_2ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                   | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                   | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                   | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                   | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                   | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                   | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_7_2GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_7_2ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_8

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest8GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| code                  | str                                 | ❌       | For `otp` grant type only. One-time password code                                                                                                                                                                                                                                                                            |
| client_assertion_type | GetTokenRequest8ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_8GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_8ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

# GetTokenRequest_9

**Properties**

| Name                  | Type                                | Required | Description                                                                                                                                                                                                                                                                                                                  |
| :-------------------- | :---------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type            | GetTokenRequest9GrantType           | ✅       | Grant type                                                                                                                                                                                                                                                                                                                   |
| brand_id              | str                                 | ❌       | RingCentral Brand identifier.                                                                                                                                                                                                                                                                                                |
| resource_type         | str                                 | ❌       | Resource type for the guest access.                                                                                                                                                                                                                                                                                          |
| resource              | str                                 | ❌       | Resource URL for the guest access.                                                                                                                                                                                                                                                                                           |
| client_assertion_type | GetTokenRequest9ClientAssertionType | ❌       | Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types  |
| client_assertion      | str                                 | ❌       | Client assertion (JWT) for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types |
| scope                 | str                                 | ❌       | The list of application permissions (OAuth scopes) requested. By default, it includes all permissions configured on the client application registration                                                                                                                                                                      |
| client_id             | str                                 | ❌       | The registered identifier of a client application. Used to identify a client ONLY if the client authentication is not required and corresponding credentials are not provided with this request                                                                                                                              |
| endpoint_id           | str                                 | ❌       | The unique identifier of a client application instance. If not specified, the derived or auto-generated value will be used                                                                                                                                                                                                   |
| access_token_ttl      | int                                 | ❌       | Access token lifetime in seconds                                                                                                                                                                                                                                                                                             |
| refresh_token_ttl     | int                                 | ❌       | Refresh token lifetime in seconds                                                                                                                                                                                                                                                                                            |

# GetTokenRequest_9GrantType

Grant type

**Properties**

| Name                                         | Type | Required | Description                                    |
| :------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| AUTHORIZATION_CODE                           | str  | ✅       | "authorization_code"                           |
| PASSWORD                                     | str  | ✅       | "password"                                     |
| REFRESH_TOKEN                                | str  | ✅       | "refresh_token"                                |
| CLIENT_CREDENTIALS                           | str  | ✅       | "client_credentials"                           |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_JWT_BEARER  | str  | ✅       | "urn:ietf:params:oauth:grant-type:jwt-bearer"  |
| URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE | str  | ✅       | "urn:ietf:params:oauth:grant-type:device_code" |
| DEVICE_CERTIFICATE                           | str  | ✅       | "device_certificate"                           |
| PARTNER_JWT                                  | str  | ✅       | "partner_jwt"                                  |
| GUEST                                        | str  | ✅       | "guest"                                        |
| PERSONAL_JWT                                 | str  | ✅       | "personal_jwt"                                 |
| OTP                                          | str  | ✅       | "otp"                                          |
| IVR_PIN                                      | str  | ✅       | "ivr_pin"                                      |

# GetTokenRequest_9ClientAssertionType

Client assertion type for the `client_secret_jwt` or `private_key_jwt` client authentication types, as defined by [RFC-7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2). This parameter is mandatory if the client authentication is required and a client decided to use one of these authentication types

**Properties**

| Name                                                   | Type | Required | Description                                              |
| :----------------------------------------------------- | :--- | :------- | :------------------------------------------------------- |
| URN_IETF_PARAMS_OAUTH_CLIENT_ASSERTION_TYPE_JWT_BEARER | str  | ✅       | "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" |

<!-- This file was generated by liblab | https://liblab.com/ -->
