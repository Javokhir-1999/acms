from isapi.HikRequest import HikRequest

class Event(HikRequest):
    def __init__(self):
        pass
    
    __API = {
        'httpHostsCapabilities': "/ISAPI/Event/notification/httpHosts/capabilities",
        'httpHosts': "/ISAPI/Event/notification/httpHosts",
        'httpHostsIDtest': "/ISAPI/Event/notification/httpHosts/<ID>/test"
    }

    def get_httpHostsCapabilities(self, devices):
        self.send_GET_request(self.__API['httpHostsCapabilities'], devices, param="?format=json")

    def get_httpHosts(self, devices):
        self.send_GET_request(self.__API['httpHosts'], devices)
    
    def set_httpHosts(self, devices):
        ''' Query Data: XML_HttpHostNotificationList '''      
        test_xml = '''<HttpHostNotification>
                            <id>1</id>
                            <url></url>
                            <protocolType>HTTP</protocolType>
                            <parameterFormatType>XML</parameterFormatType>
                            <addressingFormatType>ipaddress</addressingFormatType>
                            <ipAddress>192.168.0.168</ipAddress>
                            <portNo>8000</portNo>
                            <userName></userName>
                            <httpAuthenticationMethod>none</httpAuthenticationMethod>
                        </HttpHostNotification>'''

        self.send_PUT_request(self.__API['httpHosts'], devices, data=test_xml)
    
    def set_httpHostsIDtest(self, devices):
        ''' Query Data: XML_HttpHostNotification '''
        test_xml = '''<HttpHostNotification>
                        <id>1</id>
                        <url>http://<ipAddress>:<portNo>/<uri>--></url>
                        <protocolType><!--required, xs:string, "HTTP,HTTPS,EHome"--></protocolType>
                        <parameterFormatType><!--required, xs:string, alarm/event information format, "XML,JSON"--></parameterFormatType>
                        <addressingFormatType><!--required, xs:string, "ipaddress,hostname"--></addressingFormatType>
                        <hostName><!--dependent, xs:string--></hostName>
                        <ipAddress><!--dependent, xs:string--></ipAddress>
                        <ipv6Address><!--dependent, xs:string--></ipv6Address>
                        <portNo><!--optional, xs:integer--></portNo>
                        <userName><!--dependent, xs:string--></userName>
                        <password><!--dependent, xs:string--></password>
                        <httpAuthenticationMethod><!--required, xs:string, "MD5digest,none"--></httpAuthenticationMethod>
                        <ANPR><!--optional-->
                            <detectionUpLoadPicturesType>
                            <!--optional, xs:string, types of alarm picture to be uploaded: "all, licensePlatePicture, detectionPicture"-->
                            </detectionUpLoadPicturesType>
                        </ANPR>
                        <eventType optional="AID,TFS,TPS"><!--required, xs:string--></eventType>
                        <uploadImagesDataType>
                            <!--optional, xs:string, "URL", "binary" (default), for cloud storage, only "URL" is supported-->
                        </uploadImagesDataType>
                        <eventMode><!--optional, xs:string, "all,list"--></eventMode>
                        <EventList><!--dependent, it is valid only when eventMode is "list"-->
                            <Event><!--required-->
                            <type><!--required, xs:string--></type>
                            </Event>
                        </EventList>
                        <channels><!--optional, xs:string, "1,2,3,4…"--></channels>
                        <SubscribeEvent/><!--optional, event subscription parameters, see details in the message of XML_SubscribeEvent-->
                        </HttpHostNotification>'''
        test_id = 1 

        self.send_PUT_request(self.put_ID(self.__API['httpHostsIDtest'], test_id), devices, data=test_xml)