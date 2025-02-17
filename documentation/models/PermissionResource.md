# PermissionResource

**Properties**

| Name                 | Type                             | Required | Description                                |
| :------------------- | :------------------------------- | :------- | :----------------------------------------- |
| uri                  | str                              | ❌       |                                            |
| id\_                 | str                              | ❌       |                                            |
| display_name         | str                              | ❌       |                                            |
| description          | str                              | ❌       |                                            |
| assignable           | bool                             | ❌       |                                            |
| read_only            | bool                             | ❌       |                                            |
| site_compatible      | PermissionResourceSiteCompatible | ❌       | Site compatibility flag set for permission |
| category             | PermissionCategoryIdResource     | ❌       |                                            |
| included_permissions | List[PermissionIdResource]       | ❌       |                                            |

# PermissionResourceSiteCompatible

Site compatibility flag set for permission

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| INCOMPATIBLE | str  | ✅       | "Incompatible" |
| COMPATIBLE   | str  | ✅       | "Compatible"   |
| INDEPENDENT  | str  | ✅       | "Independent"  |

<!-- This file was generated by liblab | https://liblab.com/ -->
