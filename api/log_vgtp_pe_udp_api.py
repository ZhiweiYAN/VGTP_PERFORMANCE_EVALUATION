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
import re

UDP_IP = "172.16.187.250"
UDP_PORT = 17012
buff_len = 4096
list_len = 512
list_key_prefix = 'PE_STAT_LIST'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print "Server IP:Port", UDP_IP, UDP_PORT

r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    data, addr = sock.recvfrom(buff_len)
    print "raw data: %r" %(data)

    try:
        id_str = data.split('|')[0].strip(' ').split(':')[1]
    except:
        id_str = ''
    if id_str:
        list_key = list_key_prefix + id_str
        r.rpush(list_key, data)

        # keep list length short.
        if list_len <= r.llen(list_key):
            r.lpop(list_key)
