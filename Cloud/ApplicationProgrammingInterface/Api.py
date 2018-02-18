#!/usr/bin/python

import psutil
import signal
import sys
import time

from flask import Flask, jsonify

app = Flask(__name__)

def ThingDataSensors():
    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

@app.route('/api/sensors', methods=['GET'])
def ThingDataSensorsGet():
    return str(ThingDataSensors()) + "\n"

def ThingDataActuators():
    return "Thing Data Actuators"

@app.route('/api/actuators', methods=['GET'])
def ThingDataActuatorsGet():
    return ThingDataActuators() + "\n"

def SignalHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, SignalHandler)
    app.run(debug=True)

# End of File
