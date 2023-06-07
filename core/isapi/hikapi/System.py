from isapi.HikRequest import HikRequest

class System(HikRequest):
    def __init__(self):
        pass
    
    __API = {
        'reboot': "/ISAPI/System/reboot",
        'updateFirmware': "/ISAPI/System/updateFirmware",
        'configurationData': "/ISAPI/System/configurationData",
        'deviceInfo': "/ISAPI/System/deviceInfo",
    }

    def reboot(self, devices):
        ''' Query Data: None '''
        self.send_PUT_request(self.__API['reboot'], devices)

    def updateFirmware(self, devices):
        ''' Query Data: None '''
        self.send_PUT_request(self.__API['updateFirmware'], devices)

    def get_configurationData(self, devices):
        ''' Query Data: None '''
        ''' Response Data: binary or any other format'''

        self.format = None
        self.send_GET_request(self.__API['configurationData'], devices)
    
    def put_configurationData(self, devices):
        ''' Query Data: None '''
        ''' Response Data: binary or any other format'''

        self.send_PUT_request(self.__API['configurationData'], devices)

    def get_deviceInfo(self, devices):
        ''' Query Data: None '''
        self.send_GET_request(self.__API['deviceInfo'], devices)

    def put_deviceInfo(self, devices):
        ''' Query Data: None '''
        self.send_PUT_request(self.__API['deviceInfo'], devices)




