 #Autor: Jesús Sánchez Sänchez (gokuhs)
 #Based on veproza proyect: https://gist.github.com/veproza/55ec6eaa612781ac29e7
import requests
import serial

#Edit me!!
token = "<< Your tokken >>" #Token getted from u-blox
comPort = "<< Your GPS Module COM port >>" #GPS Com port

print "Connecting to u-blox"
r = requests.get("http://online-live1.services.u-blox.com/GetOnlineData.ashx?token=" + token + ";gnss=gps;datatype=eph,alm,aux,pos;filteronpos;format=aid", stream=True)
print "Downloading A-GPS data"

ser = serial.Serial(comPort, 9600)
print "Waiting to GPS be free"
drainer = True
while drainer:
    drainer = ser.inWaiting()
    ser.read(drainer)

print "Writing AGPS data"
ser.write(r.content)
print "Done"

buffer = True
message = ""
try:
    while buffer:
        buffer = ser.read()
        if buffer == "$":
            if message.startswith("$GPGGA"):
                print message.strip()
            message = ""
        message = message + buffer
except KeyboardInterrupt:
    ser.close()
