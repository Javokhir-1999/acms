import socket
import json
from acms.models import Person, Device, Event, Group
from pprint import pprint
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8088))
sock.listen(5)
while True:
    connection,address = sock.accept()  
    data = connection.recv(1024)
    data = data.decode('utf8').replace("'", '"')
    data = json.loads(data[data.index('{'):data.rfind('}')+1])

    print(data, end='\n-------------------------------\n')

    connection.close()
    device = Device.objects.get(address=data['ipAddress'])
    log = Event(source=device.title, address=data['ipAddress'], type=data['eventType'], details=data, time=data['dateTime'])
    log.save()