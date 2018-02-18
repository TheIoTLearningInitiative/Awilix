#!/usr/bin/python

import dweepy
import psutil
import signal
import sys
import time

from flask import Flask, jsonify

app = Flask(__name__)

def ThingDataSensors():
    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def ThingDataActuators():
    return "Thing Data Actuators"

def SignalHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, SignalHandler)

    while True:

         dweepy.dweet_for('InternetOfThings101Sensors', {'Sensors': ThingDataSensors()})
         dweepy.dweet_for('InternetOfThings101Actuators', {'Actuators': ThingDataActuators()})
         time.sleep(5)

# End of File
