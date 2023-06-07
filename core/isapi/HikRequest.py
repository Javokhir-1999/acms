import requests
from requests.auth import HTTPDigestAuth
# from requests.auth import HTTPBasicAuth

class HikRequest:
    ''' Base class that all HikAPI implementations derive from '''

    def __init__(self, protocol):
        self.protocol = protocol

    protocol = "http"

    def __form_address(self, url, ip, param=None)->str:
        address = self.protocol + "://" + ip + url
        if param:
            address += param
            
        print(address)
        return address

    def __validate_optional_attrs(self, kwargs)->dict:
        try:
            headers = kwargs['headers']
        except (KeyError, TypeError):
            headers = None 
        try:
            json = kwargs['json']
        except (KeyError, TypeError):
            json = None 
        try:
            data = kwargs['data']
        except (KeyError, TypeError):
            data = None
        try:
            files = kwargs['files']
        except (KeyError, TypeError):
            files = None
        try:
            params = kwargs['params']
        except (KeyError, TypeError):
            params = None  
        
        return {'headers':headers, 'json':json, 'data':data, 'files':files, 'params':params}

    def __print_req(self, r, method):
        from json import JSONDecodeError
        try:
            print(r.headers, r.json(), end="\n\n ^ send_"+method+"_request  \n\n")
        except JSONDecodeError:
            print(r.headers, r.text, end="\n\n ^ send_"+method+"_request  \n\n")

    def put_ID(self, url, id)->str:
        import re
        return re.sub("<ID>", str(id), url)
    
    def send_GET_request(self, url, devices, param=None, **kwargs):
        attrs = self.__validate_optional_attrs(kwargs)

        for d in devices:
            r = requests.get(
                url=self.__form_address(url, d.address, param),
                auth=HTTPDigestAuth(d.login, d.password),
                json=attrs['json'],
                data=attrs['data'],
                files=attrs['files'],
                params=attrs['params'],
                headers=attrs['headers'],
            )
            self.__print_req(r, "GET")

    def send_POST_request(self, url, devices, param=None, **kwargs):
        attrs = self.__validate_optional_attrs(kwargs)

        for d in devices:
            r = requests.post(
                url=self.__form_address(url, d.address, param),
                auth=HTTPDigestAuth(d.login, d.password),
                json=attrs['json'],
                data=attrs['data'],
                files=attrs['files'],
                params=attrs['params'],
                headers=attrs['headers'],
            )
            self.__print_req(r, "POST")
    
    def send_PUT_request(self, url, devices, param=None, **kwargs):
        attrs = self.__validate_optional_attrs(kwargs)

        for d in devices:
            r = requests.put(
                url=self.__form_address(url, d.address, param),
                auth=HTTPDigestAuth(d.login, d.password),
                json=attrs['json'],
                data=attrs['data'],
                files=attrs['files'],
                params=attrs['params'],
                headers=attrs['headers'],
            )
            self.__print_req(r, "PUT")


