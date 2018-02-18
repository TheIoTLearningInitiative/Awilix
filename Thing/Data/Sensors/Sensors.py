#!/usr/bin/python

import psutil
import signal
import sys
import time

def ThingDataSensors():
    netdata = psutil.net_io_counters()
    data = netdata.packets_sent + netdata.packets_recv
    return data

def SignalHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, SignalHandler)

    while True:
        print "Thing Data Sensors: %s " % ThingDataSensors()
        time.sleep(5)

# End of File
