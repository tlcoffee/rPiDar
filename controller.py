#!/usr/bin/env python3


import openpylivox as opl
import socket
import netifaces as ni


def lidar_sensor():
    sensor = opl.openpylivox(True)

    sensor.showMessages = True
    connected = sensor.auto_connect()


def get_ip_address(ifname):
        ni.ifaddresses(ifname)
        ip = ni.ifaddresses(ifname)[ni.AF_INET][0]['addr']
        print(ip)


def get_ip_broadcast(ifname):
        ni.ifaddresses(ifname)
        broadcast = ni.ifaddresses(ifname)[ni.AF_INET][0]['broadcast']
        print(broadcast)


def start_lidar_sensor():
    return 0

