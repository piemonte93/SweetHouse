#!/usr/bin/env python

import sys, time
import BlynkLib
import time
import subprocess
from bledevice import scanble, BLEDevice
import Adafruit_DHT
from time import sleep

"""
if len(sys.argv) != 2:
    print "Usage: python blecomm.py <ble address>"
    print "Scan devices are as follows:"
    print scanble(timeout = 3)
    sys.exit(1)
"""
BLYNK_AUTH = 'Your Auth Token'
"""
macadr = "MAC Adr"
swfir = BLEDevice(macadr)
macadr =  "MAC Adr"   
swsec = BLEDevice(macadr)
"""
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

sensor = Adafruit_DHT.DHT22
pin = 4


# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    # while True:
    vh = swfir.getvaluehandle("ffe1")
    swfir.writecmd(vh, ("%s" % value).encode('hex'))
    # data = hm10.notify()
    # if data is not None:
    # print "Received: ", data
    time.sleep(1)


@blynk.VIRTUAL_WRITE(2)
def my_write_handler(value):
    vh = swsec.getvaluehandle("ffe1")
    swsec.writecmd(vh, ("%s" % value).encode('hex'))
    time.sleep(1)


@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
    if value == '1':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "on"])
    elif value == '0':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "off"])


@blynk.VIRTUAL_WRITE(4)
def my_write_handler(value):
    if value == '18':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t18"])
    elif value == '19':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t19"])
    elif value == '20':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t20"])
    elif value == '21':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t21"])
    elif value == '22':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t22"])
    elif value == '23':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t23"])
    elif value == '24':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t24"])
    elif value == '25':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t25"])
    elif value == '26':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t26"])
    elif value == '27':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t27"])
    elif value == '28':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t28"])
    elif value == '29':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t29"])
    elif value == '30':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "t30"])


@blynk.VIRTUAL_WRITE(5)
def my_write_handler(value):
    if value == '0':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "wind_1"])
    elif value == '1':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "wind_2"])
    elif value == '2':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "wind_3"])


@blynk.VIRTUAL_WRITE(6)
def my_write_handler(value):
    if value == '0':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "swing_start"])
    elif value == '1':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "swing_stop"])


@blynk.VIRTUAL_WRITE(7)
def my_write_handler(value):
    if value == '1':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "mode_auto"])
    elif value == '2':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "mode_cool"])
    elif value == '3':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "mode_dry"])
    elif value == '4':
        ac = subprocess.call(["irsend", "SEND_ONCE", "samsung", "mode_blow"])


@blynk.VIRTUAL_READ(8)
def my_read_handler():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    t = ' {0:0.1f}'.format(temperature)
    blynk.virtual_write(8, t)


@blynk.VIRTUAL_READ(9)
def my_read_handler():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    h = ' {0:0.1f}'.format(humidity)
    blynk.virtual_write(9, h)


# Start Blynk (this call should never return)
blynk.run()


