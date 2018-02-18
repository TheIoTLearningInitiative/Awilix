#!/usr/bin/python

import psutil
import signal
import sys
import time

import paho.mqtt.client as paho

from threading import Thread

CommunicationProtocolsMqttBroker = "iot.eclipse.org"
CommunicationProtocolsMqttPublishTopic = "internetofthings101/sensors"
CommunicationProtocolsMqttSubscribeTopic = "internetofthings101/actuators"

def ThingDataSensors():
    netdata = psutil.net_io_counters()
    return netdata.packets_sent + netdata.packets_recv

def CommunicationProtocolsMqttPublish():
    client = paho.Client()
    client.connect(CommunicationProtocolsMqttBroker, 1883, 60)
    while True:
        topic = CommunicationProtocolsMqttPublishTopic
        status = ThingDataSensors()
        client.publish(topic, status)
        time.sleep(5)

def ThingDataActuators(mosq, obj, msg):
    print "Thing Data Actuators: %s" % msg.payload

def CommunicationProtocolsMqttSubscribe():
    client = paho.Client()
    client.on_message = ThingDataActuators
    client.connect(CommunicationProtocolsMqttBroker, 1883, 60)
    client.subscribe(CommunicationProtocolsMqttSubscribeTopic, 0)
    while client.loop() == 0:
        pass

def SignalHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':

    signal.signal(signal.SIGINT, SignalHandler)

    publish = Thread(target=CommunicationProtocolsMqttPublish)
    publish.start()

    subscribe = Thread(target=CommunicationProtocolsMqttSubscribe)
    subscribe.start()

    while True:
        time.sleep(5)

# End of File
