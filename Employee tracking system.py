import wiotp.sdk.device
import datetime
import time
import random
myConfig = { 
    "identity": {
        "orgId": "3zj2w8",
        "typeId": "vitdevice",
        "deviceId":"8335"
    },
    "auth": {
        "token": "8335920874"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
        
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

now=datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
n=4


for k in range(0, n):
    names =input("enter employee name :" )
    id=input("enter employee id :")
    latitude=22.5555
    longitude= 88.3654
    myData = { "names": names, "id": id,'lat':latitude,'lon':longitude, 'Date_Time':date_time}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
                        
client.commandCallback = myCommandCallback
time.sleep(200)
client.disconnect()
{"mode":"full","isActive":false}





