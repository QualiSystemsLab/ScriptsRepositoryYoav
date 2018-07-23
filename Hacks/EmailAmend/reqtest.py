import json
import requests

some_session = requests.session()
headers = {
    'Accept': '*/*',
    'Referer': 'http://qs.cisco.com/Account/Login?ReturnUrl=%2f',
    'Origin': 'http://qs.cisco.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

data = 'username=FPf4d2vJpXOosoQKtHDp028PdOEuDp0BIYCwFNUKTPPD3%2FI0FcVQPl%2F60wbIYm2xCckOEXcdXbcWAOfu0uD70lEwIj436kU7MBy9y70q198fd6pbYp0kiKbhzoQ0HvGDHU5VlGWnX1wGOega%2FmVBvrmJ%2F4PddDu9lUwSwWn1SIc%3D&password=FC9MLgq93fDMLvCR09zPMGHtg2K0CaK8UvwRohqAJKxz8W60Y000s%2BoHNwJpmrt9CK64ERq1yvSMN%2FVUtYh6JVWIU0cs1nd7zJS%2BVIyihKDSRS8J5WSFFNaSRFO91DOtRWwJLYcZ5UIJks%2FUGeu8OYUyV%2FtN0OnzU%2B5PQo9tNQ4%3D&ReturnUrl=%2F&TimezoneOffset=-120&Timezone=Israel+Standard+Time'

r = some_session.post('http://qs.cisco.com/Account/Login', headers=headers, data=data)

# data = json.loads('{"DiagramId":"bea7b7e2-eaf3-42f6-be12-c8c32ba64bd7","FilterList":[{"Id":-1,"Name":"All"},{"Id":0,"Name":"Command"},{"Id":1,"Name":"Reservation"},{"Id":2,"Name":"Resource"},{"Id":3,"Name":"Service"}],"SelectedEventGroupId":-1,"SelectedEventGroupName":"All","Area":"RM","Action":"ListIndex","Controller":"ActivityFeed","ActionUrl":"/RM/ActivityFeed/ListIndex","MainViewName":"ListItems","PartialContainerViewName":"_ListItemContainer","SingleItemDataContainer":"_FullActivityFeedLogItem","ListContainerId":"searchResult","ElementScrollingEventId":null,"IsPagingEnabled":true,"IsSelectingDisabled":false,"Multiselection":false,"PageIndex":2,"NumberOfItems":50,"NumberOfItemsToShow":0,"TotalItems":100,"SearchQuery":null,"OwnerFilterOptions":null,"SelectedOwnerGuid":null,"FiltersPartialViews":["_EventGroupFilter"],"ExcludedItems":null,"GenericListFilter":null,"AllResourcesInDiagram":null}')
data = json.loads('{"DiagramId":"bea7b7e2-eaf3-42f6-be12-c8c32ba64bd7","FilterList":[{"Id":-1,"Name":"All"},{"Id":0,"Name":"Command"},{"Id":1,"Name":"Reservation"},{"Id":2,"Name":"Resource"},{"Id":3,"Name":"Service"}],"SelectedEventGroupId":-1,"SelectedEventGroupName":"All","Area":"RM","Action":"ListIndex","Controller":"ActivityFeed","ActionUrl":"/RM/ActivityFeed/ListIndex","MainViewName":"ListItems","PartialContainerViewName":"_ListItemContainer","SingleItemDataContainer":"_FullActivityFeedLogItem","ListContainerId":"searchResult","ElementScrollingEventId":null,"IsPagingEnabled":true,"IsSelectingDisabled":false,"Multiselection":false,"PageIndex":0,"NumberOfItems":50,"NumberOfItemsToShow":0,"TotalItems":0,"SearchQuery":null,"OwnerFilterOptions":null,"SelectedOwnerGuid":null,"FiltersPartialViews":["_EventGroupFilter"],"ExcludedItems":null,"GenericListFilter":null,"AllResourcesInDiagram":null}')
v = some_session.get('http://qs.cisco.com/RM/ActivityFeed/FullActivityLog/bea7b7e2-eaf3-42f6-be12-c8c32ba64bd7')
f = some_session.post('http://qs.cisco.com/RM/ActivityFeed/ListIndex', data=data)
pass