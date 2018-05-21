import sys, time
import BlynkLib
import time
from bledevice import scanble, BLEDevice

if len(sys.argv) != 2:
    print "Usage: python blecomm.py <ble address>"
    print "Scan devices are as follows:"
    print scanble(timeout=3)
    sys.exit(1)

BLYNK_AUTH = 'b1d9aa0b91ee40769c0ade8b3519f8b1'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

hm10 = BLEDevice(sys.argv[1])

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
        #while True:
        vh = hm10.getvaluehandle("ffe1")
        hm10.writecmd(vh, ("%s" % value).encode('hex'))
        #data = hm10.notify()
        #if data is not None:
        #print "Received: ", data
        time.sleep(1)
@blynk.VIRTUAL_READ(2)
def my_read_handler():
# this widget will show some time in seconds..
    blynk.virtual_write(2, time.ticks_ms() // 1000)

# Start Blynk (this call should never return)
blynk.run()
