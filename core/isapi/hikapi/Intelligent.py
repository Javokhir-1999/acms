from isapi.HikRequest import HikRequest

class Intelligent(HikRequest):
    def __init__(self):
        pass
    
    __API = {
        'FDLib': "/ISAPI/Intelligent/FDLib",
        'FDLibCapabilities': "/ISAPI/Intelligent/FDLib/capabilities",
        'FaceDataRecord': "/ISAPI/Intelligent/FDLib/FaceDataRecord",
    }

    def get_FDLibCapabilities(self, devices):
        self.send_GET_request(self.__API['FDLibCapabilities'], devices)

    def get_FDLib(self, devices):
        self.send_GET_request(self.__API['FDLib'], devices)

    def create_FDLib(self, devices):
        ''' Query Data: JSON_CreateFPLibCond ''' 
        json = {
            'faceLibType': "blackFD",
            # required, string type, face picture library type: "infraredFD"-infrared face picture library, "blackFD"-list library, "staticFD"-static library, the maximum size is 32 bytes
            'name': "imgb",
            # required, string type, face picture library name, it cannot be duplicated, the maximum size is 48 bytes
        }
        
        self.send_POST_request(self.__API['FDLib'], devices, param="?format=json", json=json)

    def add_FaceDataRecord(self, devices, user=False):
        ''' Query Data: JSON_AddFaceRecordCond '''
        if user:
            data = {'FaceDataRecord': '{"faceLibType":"blackFD","FDID":"1","FPID": "'+str(user.id)+'", "name": "'+user.name+'","gender":"male","bornTime":"2004-05-03"}'}
            files = [
                ('FaceImage',('face.jpg', open('media/'+user.photo.name,'rb'),'image/jpeg'))
            ]
        else:
            data = {'FaceDataRecord': '{"faceLibType":"blackFD","FDID":"1","FPID":"1","name":"Java","gender":"male","bornTime":"2004-05-03"}'}
            files = [
                ('FaceImage',('face.jpg', open('face.jpg','rb'),'image/jpeg'))
            ]

        self.send_POST_request(self.__API['FaceDataRecord'], devices, param="?format=json", data=data, files=files)



