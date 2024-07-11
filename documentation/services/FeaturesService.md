# FeaturesService

A list of all methods in the `FeaturesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :-------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [read_extension_features](#read_extension_features) | Returns a list of supported features and the information on their availability for the current extension. Particular feature(s) can be checked by providing `featureId` query parameter. Multiple values are supported in the format: `?featureId=Feature1&featureId=Feature2`. To get only available features in order to decrease response size, `availableOnly=true` query param can be specified. If a feature is available for the current user, `"available": true` is returned in response for the record with the corresponding feature ID. Otherwise, the additional attribute `reason` is returned with the appropriate code: - `ServicePlanLimitation` - a feature is not included in account service plan; - `AccountLimitation` - a feature is turned off for account; - `ExtensionTypeLimitation` - a feature is not applicable for extension type; - `ExtensionLimitation` - a feature is not available for extension, e.g., additional license required; - `InsufficientPermissions` - required permission is not granted to the current user (not the one, who is specified in the URL, but the one who is calling this API); - `ConfigurationLimitation` - a feature is turned off for extension, e.g., by account administrator. Also, some features may have additional parameters, e.g. limits, which are returned in `params` attribute as a name-value collection: `    {       "id": "HUD",       "available": true,       "params": [         {           "name": "limitMax",           "value": "100"         }       ]     }` |

## read_extension_features

Returns a list of supported features and the information on their availability for the current extension. Particular feature(s) can be checked by providing `featureId` query parameter. Multiple values are supported in the format: `?featureId=Feature1&featureId=Feature2`. To get only available features in order to decrease response size, `availableOnly=true` query param can be specified. If a feature is available for the current user, `"available": true` is returned in response for the record with the corresponding feature ID. Otherwise, the additional attribute `reason` is returned with the appropriate code: - `ServicePlanLimitation` - a feature is not included in account service plan; - `AccountLimitation` - a feature is turned off for account; - `ExtensionTypeLimitation` - a feature is not applicable for extension type; - `ExtensionLimitation` - a feature is not available for extension, e.g., additional license required; - `InsufficientPermissions` - required permission is not granted to the current user (not the one, who is specified in the URL, but the one who is calling this API); - `ConfigurationLimitation` - a feature is turned off for extension, e.g., by account administrator. Also, some features may have additional parameters, e.g. limits, which are returned in `params` attribute as a name-value collection: `    {       "id": "HUD",       "available": true,       "params": [         {           "name": "limitMax",           "value": "100"         }       ]     }`

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/features`

**Parameters**

| Name           | Type      | Required | Description                                                                                                                                                           |
| :------------- | :-------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id     | str       | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id   | str       | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| available_only | bool      | ❌       | Allows to filter features by availability for an extension                                                                                                            |
| feature_id     | List[str] | ❌       | Internal identifier(s) of the feature(s)                                                                                                                              |

**Return Type**

`FeatureList`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
feature_id=[
    "featureId"
]

result = sdk.features.read_extension_features(
    account_id="~",
    extension_id="~",
    available_only=True,
    feature_id=feature_id
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
