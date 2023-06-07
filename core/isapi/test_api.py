from isapi.hikapi.AccessControl import AccessControl
from isapi.hikapi.Intelligent import Intelligent
from isapi.hikapi.System import System
from isapi.hikapi.Event import Event
from  .setup import devices

obj1 = AccessControl()
obj2 = Intelligent()
obj3 = Event()
obj4 = System()

# obj1.get_UserInfo(devices)
obj1.add_UserInfoRecord(devices)
# obj1.put_UserInfoModify(devices)
# obj2.get_FDLibCapabilities(devices)
obj2.add_FaceDataRecord(devices)

# obj1.del_UserInfoDetailDelete(devices)


# obj4.get_configurationData(devices)
# obj3.get_httpHosts(devices)
# obj3.get_httpHostsCapabilities(devices)
# obj4.get_deviceInfo(devices)

