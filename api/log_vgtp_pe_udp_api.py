#!/usr/bin/python
# encoding=utf-8

"""
The Web Server that displays and log the performance parameters
of VGTP (Vaxum Graphic/Image Transfer Protocol)

"""
__author__ = "Zhiwei Yan"
__copyright__ = "Copyright 2016, The VGTP Project"
__credits__ = ["Zhiwei Yan"]
__license__ = "Private License"
__version__ = "1.0"
__maintainer__ = "Zhiwei YAN"
__email__ = "jerod.yan@gmail.com"
__status__ = "Production"

import socket
import redis

UDP_IP = "172.16.187.231"
UDP_PORT = 17012
data_len = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print "Server IP:Port", UDP_IP, UDP_PORT

r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    data, addr = sock.recvfrom(data_len)
    print "received msg:", data
    r.rpush('PE_STAT_LIST', data)
    
