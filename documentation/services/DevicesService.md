# DevicesService

A list of all methods in the `DevicesService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [add_device_to_inventory](#add_device_to_inventory)           | Adds an existing phone (customer provided device - BYOD) as an unassigned device to the account inventory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [delete_device_from_inventory](#delete_device_from_inventory) | Deletes an existing unassigned (without digital line or phone number) device or multiple devices from the account inventory. It is possible to delete up to 10 devices per request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [remove_line_jws_public](#remove_line_jws_public)             | Disassociates a phone line (DL & Device) from an extension: - if the value of `keepAssetsInInventory` is `true`, the given device is moved to unassigned devices and the number is moved to the number inventory; - if the value of `keepAssetsInInventory` is `false`, the given device and number is removed from the account; - if the parameter `keepAssetsInInventory` is not set (empty body), default value `true` is set.                                                                                                                                                                                                                                                                                                            |
| [bulk_add_devices_v2](#bulk_add_devices_v2)                   | Adds multiple BYOD (customer provided) devices to an account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [replace_devices_jws_public](#replace_devices_jws_public)     | Replaces the user device with another device, which is assigned to an extension or is stored in the inventory of the same account. Currently, the following device types can be swapped - `HardPhone` and `OtherPhone`. Please note: - This method allows replacing a device itself, while a phone number, a digital Line and an emergency address associated with this device remain unchanged and will still work together in a chain with the replacement device. - If a target device is from the inventory, then a source device will be moved to the inventory, and a target device will be assigned to the current extension. - If a target device is currently assigned to another extension, then the devices will be just swapped. |
| [read_device](#read_device)                                   | Returns account device(s) by their ID(s).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [update_device](#update_device)                               | Updates account device(s) by their ID(s).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [read_device_sip_info](#read_device_sip_info)                 | Returns device SIP information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [update_device_emergency](#update_device_emergency)           | Updates account device emergency information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [list_extension_devices](#list_extension_devices)             | Returns devices of an extension or multiple extensions by their ID(s). Batch request is supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## add_device_to_inventory

Adds an existing phone (customer provided device - BYOD) as an unassigned device to the account inventory.

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/device-inventory`

**Parameters**

| Name         | Type                                                                    | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AddDeviceToInventoryRequest](../models/AddDeviceToInventoryRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`AddDeviceToInventoryResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AddDeviceToInventoryRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AddDeviceToInventoryRequest(
    type_="OtherPhone",
    quantity=22,
    site={
        "id_": "id"
    }
)

result = sdk.devices.add_device_to_inventory(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## delete_device_from_inventory

Deletes an existing unassigned (without digital line or phone number) device or multiple devices from the account inventory. It is possible to delete up to 10 devices per request.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v2/accounts/{accountId}/device-inventory`

**Parameters**

| Name         | Type                                                                              | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [DeleteDeviceFromInventoryRequest](../models/DeleteDeviceFromInventoryRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`DeleteDeviceFromInventoryResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import DeleteDeviceFromInventoryRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = DeleteDeviceFromInventoryRequest(
    records=[
        {
            "device_id": "deviceId"
        }
    ]
)

result = sdk.devices.delete_device_from_inventory(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## remove_line_jws_public

Disassociates a phone line (DL & Device) from an extension: - if the value of `keepAssetsInInventory` is `true`, the given device is moved to unassigned devices and the number is moved to the number inventory; - if the value of `keepAssetsInInventory` is `false`, the given device and number is removed from the account; - if the parameter `keepAssetsInInventory` is not set (empty body), default value `true` is set.

- HTTP Method: `DELETE`
- Endpoint: `/restapi/v2/accounts/{accountId}/devices/{deviceId}`

**Parameters**

| Name         | Type                                                | Required | Description                                                                                                                                                  |
| :----------- | :-------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [RemoveLineRequest](../models/RemoveLineRequest.md) | ❌       | The request body.                                                                                                                                            |
| account_id   | str                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| device_id    | str                                                 | ✅       | Internal identifier of a source device                                                                                                                       |

**Return Type**

`RemoveLineResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import RemoveLineRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RemoveLineRequest(
    keep_assets_in_inventory=True
)

result = sdk.devices.remove_line_jws_public(
    request_body=request_body,
    account_id="~",
    device_id="deviceId"
)

print(result)
```

## bulk_add_devices_v2

Adds multiple BYOD (customer provided) devices to an account.

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/devices/bulk-add`

**Parameters**

| Name         | Type                                                        | Required | Description                                                                                                                                                  |
| :----------- | :---------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [BulkAddDevicesRequest](../models/BulkAddDevicesRequest.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                         | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |

**Return Type**

`BulkAddDevicesResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import BulkAddDevicesRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BulkAddDevicesRequest(
    records=[
        {
            "cost_center_id": "224149",
            "extension": {
                "id_": "12345"
            },
            "type_": "OtherPhone",
            "emergency": {
                "address": {
                    "street": "20 Davis Dr",
                    "street2": "nostrud",
                    "city": "Belmont",
                    "state": "CA",
                    "zip": "94002",
                    "country": "US"
                }
            },
            "phone_info": {
                "toll_type": "Toll"
            }
        }
    ]
)

result = sdk.devices.bulk_add_devices_v2(
    request_body=request_body,
    account_id="~"
)

print(result)
```

## replace_devices_jws_public

Replaces the user device with another device, which is assigned to an extension or is stored in the inventory of the same account. Currently, the following device types can be swapped - `HardPhone` and `OtherPhone`. Please note: - This method allows replacing a device itself, while a phone number, a digital Line and an emergency address associated with this device remain unchanged and will still work together in a chain with the replacement device. - If a target device is from the inventory, then a source device will be moved to the inventory, and a target device will be assigned to the current extension. - If a target device is currently assigned to another extension, then the devices will be just swapped.

- HTTP Method: `POST`
- Endpoint: `/restapi/v2/accounts/{accountId}/extensions/{extensionId}/devices/{deviceId}/replace`

**Parameters**

| Name         | Type                                                | Required | Description                                                                                                                                                           |
| :----------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [SwapDeviceRequest](../models/SwapDeviceRequest.md) | ✅       | The request body.                                                                                                                                                     |
| account_id   | str                                                 | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)          |
| extension_id | str                                                 | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used) |
| device_id    | str                                                 | ✅       | Internal identifier of a source device that is currently assigned to the given extension                                                                              |

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import SwapDeviceRequest

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SwapDeviceRequest(
    target_device_id="8459879873"
)

result = sdk.devices.replace_devices_jws_public(
    request_body=request_body,
    account_id="~",
    extension_id="~",
    device_id="deviceId"
)

print(result)
```

## read_device

Returns account device(s) by their ID(s).

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/device/{deviceId}`

**Parameters**

| Name                   | Type | Required | Description                                                                                                                                                  |
| :--------------------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id             | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| device_id              | str  | ✅       | Internal identifier of a device                                                                                                                              |
| sync_emergency_address | bool | ❌       | Specifies if an emergency address should be synchronized or not                                                                                              |

**Return Type**

`DeviceResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.devices.read_device(
    account_id="~",
    device_id="deviceId",
    sync_emergency_address=True
)

print(result)
```

## update_device

Updates account device(s) by their ID(s).

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/device/{deviceId}`

**Parameters**

| Name         | Type                                                    | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AccountDeviceUpdate](../models/AccountDeviceUpdate.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| device_id    | str                                                     | ✅       | Internal identifier of a device                                                                                                                              |
| prestatement | bool                                                    | ❌       |                                                                                                                                                              |

**Return Type**

`DeviceResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AccountDeviceUpdate

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AccountDeviceUpdate(
    emergency_service_address={
        "street": "street",
        "street2": "street2",
        "city": "city",
        "zip": "zip",
        "customer_name": "customerName",
        "state": "state",
        "state_id": "stateId",
        "country": "country",
        "country_id": "countryId"
    },
    emergency={
        "address": {
            "country": "country",
            "country_id": "countryId",
            "country_iso_code": "countryIsoCode",
            "country_name": "countryName",
            "state": "state",
            "state_id": "stateId",
            "state_iso_code": "stateIsoCode",
            "state_name": "stateName",
            "city": "city",
            "street": "street",
            "street2": "street2",
            "zip": "zip",
            "customer_name": "customerName"
        },
        "location": {
            "id_": "id",
            "name": "name",
            "address_format_id": "addressFormatId"
        },
        "out_of_country": False,
        "address_status": "Valid",
        "visibility": "Private",
        "sync_status": "Verified",
        "address_editable_status": "MainDevice"
    },
    extension={
        "id_": "id"
    },
    phone_lines={
        "phone_lines": [
            {
                "id_": "id"
            }
        ]
    },
    use_as_common_phone=True,
    name="name"
)

result = sdk.devices.update_device(
    request_body=request_body,
    account_id="~",
    device_id="deviceId",
    prestatement=True
)

print(result)
```

## read_device_sip_info

Returns device SIP information.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/device/{deviceId}/sip-info`

**Parameters**

| Name       | Type | Required | Description                                                                                                                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| account_id | str  | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| device_id  | str  | ✅       | Internal identifier of a device                                                                                                                              |

**Return Type**

`SipInfoResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.devices.read_device_sip_info(
    account_id="~",
    device_id="deviceId"
)

print(result)
```

## update_device_emergency

Updates account device emergency information.

- HTTP Method: `PUT`
- Endpoint: `/restapi/v1.0/account/{accountId}/device/{deviceId}/emergency`

**Parameters**

| Name         | Type                                                    | Required | Description                                                                                                                                                  |
| :----------- | :------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [AccountDeviceUpdate](../models/AccountDeviceUpdate.md) | ✅       | The request body.                                                                                                                                            |
| account_id   | str                                                     | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used) |
| device_id    | str                                                     | ✅       | Internal identifier of a device                                                                                                                              |

**Return Type**

`DeviceResource`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import AccountDeviceUpdate

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AccountDeviceUpdate(
    emergency_service_address={
        "street": "street",
        "street2": "street2",
        "city": "city",
        "zip": "zip",
        "customer_name": "customerName",
        "state": "state",
        "state_id": "stateId",
        "country": "country",
        "country_id": "countryId"
    },
    emergency={
        "address": {
            "country": "country",
            "country_id": "countryId",
            "country_iso_code": "countryIsoCode",
            "country_name": "countryName",
            "state": "state",
            "state_id": "stateId",
            "state_iso_code": "stateIsoCode",
            "state_name": "stateName",
            "city": "city",
            "street": "street",
            "street2": "street2",
            "zip": "zip",
            "customer_name": "customerName"
        },
        "location": {
            "id_": "id",
            "name": "name",
            "address_format_id": "addressFormatId"
        },
        "out_of_country": False,
        "address_status": "Valid",
        "visibility": "Private",
        "sync_status": "Verified",
        "address_editable_status": "MainDevice"
    },
    extension={
        "id_": "id"
    },
    phone_lines={
        "phone_lines": [
            {
                "id_": "id"
            }
        ]
    },
    use_as_common_phone=True,
    name="name"
)

result = sdk.devices.update_device_emergency(
    request_body=request_body,
    account_id="~",
    device_id="deviceId"
)

print(result)
```

## list_extension_devices

Returns devices of an extension or multiple extensions by their ID(s). Batch request is supported.

- HTTP Method: `GET`
- Endpoint: `/restapi/v1.0/account/{accountId}/extension/{extensionId}/device`

**Parameters**

| Name         | Type                                                              | Required | Description                                                                                                                                                                                                                                       |
| :----------- | :---------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| account_id   | str                                                               | ✅       | Internal identifier of the RingCentral account (can be set to "~" to indicate that the account associated with current authorization session should be used)                                                                                      |
| extension_id | str                                                               | ✅       | Internal identifier of the RingCentral extension/user (can be set to "~" to indicate that the extension associated with current authorization session should be used)                                                                             |
| page         | int                                                               | ❌       | The result set page number (1-indexed) to return                                                                                                                                                                                                  |
| per_page     | int                                                               | ❌       | The number of items per page. If provided value in the request is greater than a maximum, the maximum value is applied                                                                                                                            |
| line_pooling | [LinePooling](../models/LinePooling.md)                           | ❌       | Pooling type of device - Host - a device with standalone paid phone line which can be linked to a soft client instance - Guest - a device with a linked phone line - None - a device without a phone line or with specific line (free, BLA, etc.) |
| feature      | [DeviceFeatureEnum](../models/DeviceFeatureEnum.md)               | ❌       | Device feature or multiple features supported                                                                                                                                                                                                     |
| type\_       | [ListExtensionDevicesType](../models/ListExtensionDevicesType.md) | ❌       | Device type                                                                                                                                                                                                                                       |
| line_type    | [PhoneLineTypeEnum](../models/PhoneLineTypeEnum.md)               | ❌       | Phone line type                                                                                                                                                                                                                                   |

**Return Type**

`GetExtensionDevicesResponse`

**Example Usage Code Snippet**

```python
from ring_central import RingCentral, Environment
from ring_central.models import LinePooling, DeviceFeatureEnum, ListExtensionDevicesType, PhoneLineTypeEnum

sdk = RingCentral(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.devices.list_extension_devices(
    account_id="~",
    extension_id="~",
    page=1,
    per_page=100,
    line_pooling="Host",
    feature="BLA",
    type_="HardPhone",
    line_type="Unknown"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
