from isapi.HikRequest import HikRequest

class AccessControl(HikRequest):
    def __init__(self):
        pass
    
    __API = {
        'UserInfoCapabilities': "/ISAPI/AccessControl/UserInfo/capabilities",
        'UserInfoRecord': "/ISAPI/AccessControl/UserInfo/Record",
        'UserInfoSetUp': "/ISAPI/AccessControl/UserInfo/SetUp",
        'UserInfoModify': "/ISAPI/AccessControl/UserInfo/Modify",
        'UserInfoDelete': "/ISAPI/AccessControl/UserInfo/Delete",
        'UserInfoDetailDelete': "/ISAPI/AccessControl/UserInfoDetail/Delete",
    }

    def get_UserInfo(self, devices):
        self.send_GET_request(self.__API['UserInfoCapabilities'], devices)
    
    def add_UserInfoRecord(self, devices, user=False):
        ''' Query Data: JSON_UserInfo '''
        if user:
            data = {
            "UserInfo": {
                "employeeNo": str(user.id),
                "userType": "normal",
                "name": user.name,
                "Valid": {
                    "enable": False,
                    "beginTime": str(user.time),
                    "endTime": "2026-06-01",
                    "timeType":"local",
                },
                "doorRight":"1",
                # "belongGroup":"1",
                "RightPlan":[{
                # /*optional, door permission schedule (lock permission schedule)*/
                    "doorNo": "1",
                # /*optional, integer, door No. (lock ID)*/
                    "planTemplateNo":"1"
                # /*optional, string, schedule template No.*/
                }],
            }
        }
        else:
            data = {
            "UserInfo": {
                "employeeNo": "1",
                "userType": "normal",
                "name": "Java",
                "Valid": {
                    "enable": False,
                    "beginTime": "2020-01-01",
                    "endTime": "2023-06-01",
                    "timeType":"local",
                },
                "doorRight":"1",
                # "belongGroup":"1",
                "RightPlan":[{
                # /*optional, door permission schedule (lock permission schedule)*/
                    "doorNo": "1",
                # /*optional, integer, door No. (lock ID)*/
                    "planTemplateNo":"1"
                # /*optional, string, schedule template No.*/
                }],
            }
        }
        
        self.send_POST_request(self.__API['UserInfoRecord'], devices, param="?format=json", json=data)
    
    def del_UserInfoDetailDelete(self, devices, user=False):
        ''' Query Data: UserInfoDetail '''
        if user:
             data = {
                "UserInfoDetail":{
                    "mode":"byEmployeeNo",
                    "EmployeeNoList":[{
                        "employeeNo":str(user.id)
                    }]
                }
            }
        else:
            data = {
                "UserInfoDetail":{
                    "mode":"byEmployeeNo",
                # /*required, string type, deleting mode: "all"-delete all, "byEmployeeNo"-delete by employee No. (person ID)*/
                    "EmployeeNoList":[{
                # /*optional, person ID list, if this node does not exist or is null, it indicates deleting all person information (including linked cards and fingerprints) and permissions*/
                        "employeeNo":"1"
                # /*optional, string type, employee No. (person ID), it is valid when mode is "byEmployeeNo"*/
                    }]
                }
            }
        self.send_PUT_request(self.__API['UserInfoDetailDelete'], devices, param="?format=json", json=data)

    def set_UserInfoSetUp(self, devices):
        ''' Query Data: JSON_UserInfo '''
        pass
    
    def put_UserInfoModify(self, devices, user=False):
        ''' Query Data: JSON_UserInfo '''
        if user:
            data = {
            "UserInfo": {
                "employeeNo": str(user.id),
                "userType": "normal",
                "name": user.name,
                "Valid": {
                    "enable": False,
                    "beginTime": str(user.time),
                    "endTime": "2026-06-01",
                    "timeType":"local",
                },
                "doorRight":"1",
            }
        }
        else:
            data = {
            "UserInfo": {
                "employeeNo": "1",
                "userType": "normal",
                "name": "Java2",
                "Valid": {
                    "enable": False,
                    "beginTime": "2020-01-01",
                    "endTime": "2023-06-01",
                    "timeType":"local",
                },
                "doorRight":"1",
                # "belongGroup":"1",
                "RightPlan":[{
                # /*optional, door permission schedule (lock permission schedule)*/
                    "doorNo": "1",
                # /*optional, integer, door No. (lock ID)*/
                    "planTemplateNo":"1"
                # /*optional, string, schedule template No.*/
                }],
            }
        }

        self.send_PUT_request(self.__API['UserInfoModify'], devices, param="?format=json", json=data)