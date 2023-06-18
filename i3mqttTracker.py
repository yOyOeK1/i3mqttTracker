#!/usr/bin/env python3


from ot_my_libs.myLoger import myLoger
from ot_my_libs.FileActions import FileActions
from ot_my_libs.myMqttClient import myMqttClient
import traceback

MY_NAME = "i3mqttTracker"
mqtt_conf = {
    "host": "192.168.43.1",
    "port": 10883
}
SEPARATOR = " "
TARGET_FILE = "/run/user/1000/i3mqtt.line"


l = myLoger( MY_NAME, {
    #'info': True, 'debug': True, 'error': True,'critical': True
    'info': False, 'debug': False, 'error': False,'critical': False
    } )
fa = FileActions()

def on_mqErrors( client, userdata, level, buff):
    print("ERROR")
    print(buff)

def onMessage( client, userdata, msg):
    print("onMessage topic:[{}]    msg:[{}]".format(
            msg.topic,
            msg.payload
            ),end="")
    #print("tMap")
    #print(tMap)
    mkFunk = tMap.get( str(msg.topic), None )
    if mkFunk != None:
        try:
            mkFunk( msg.topic, msg.payload.decode('utf-8') )
            updateOutput()
        
        except:
            print("ERROR")
            traceback.print_exc()

    print("OK")

def on_huBAT( topic, payload ):
    #print(f"on_huBAT topic:[{topic}] -> {payload}")
    tDisplay["📱"] = (f"{payload}%")

def on_homeBAT( topic, payload ):
    tr = float( payload ) * 0.02771809
    cell = tr / 4.00
    tDisplay["⛵"] = ("{:.2f} ({:.2f})".format( 
        tr, cell
     ))

cmdC = 0
cStatus = -1
def on_i3cmd( topic, payload ):
    global cmdC
    global cStatus
    cmdC+= 1
    tr = "{} len({}) :: {}".format( cmdC, len( payload ), payload )
    
    if cStatus == -1 and payload == "Hello":
        cStatus = 0
        tr = "yes? 🥊"

    if cStatus == -1 and payload == "c1":
        cStatus = 0
        tr = ":: cmd1 slot ::"

    elif cStatus == 0:
        cStatus = -1
        tr = "zz Z"
        

    tDisplay['🧅'] = tr

    
def updateOutput():
    tr = []
    for key in tDisplay.keys():
        tr.append( f"{key}:{tDisplay[key]}" )
    fa.writeFile( 
        TARGET_FILE,
        SEPARATOR.join(tr) 
        )

tList = [
    {
        "name": "huBAT",
        "topic": [ "hu/bat/percent" ],
        "func": on_huBAT
    },
    {
        "name": "house",
        "topic": [ "e01Mux/adc0" ],
        "func": on_homeBAT
    },
    {
        "name": "cmd",
        "topic": [ "and/i3cmd" ],
        "func": on_i3cmd
    }
]
tMap = {}
tDisplay = {}


if __name__ == "__main__":
    l.i("* start ...")

    subList = []
    for si in tList:
        for t in si["topic"]:
            subList.append( t )
            tMap[ t ] =  si["func"]

    mq = myMqttClient( MY_NAME , mqtt_conf['host'], mqtt_conf['port'],
        subscribe=subList,
        on_message=onMessage
        )
    mq.connect(  )
    #mq.cli.on_log = on_mqErrors
    l.i("* start loop ...")
    mq.cli.loop_forever()
    l.i("* exit loop ... bye!")


