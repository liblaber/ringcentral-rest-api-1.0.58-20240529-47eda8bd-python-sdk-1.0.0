# GetLocationListResponse

**Properties**

| Name       | Type                  | Required | Description                                    |
| :--------- | :-------------------- | :------- | :--------------------------------------------- |
| navigation | PageNavigationModel   | ✅       | Links to other pages of the current result set |
| paging     | EnumeratedPagingModel | ✅       |                                                |
| uri        | str                   | ❌       | Link to the location list resource             |
| records    | List[LocationInfo]    | ❌       | List of locations                              |

<!-- This file was generated by liblab | https://liblab.com/ -->
