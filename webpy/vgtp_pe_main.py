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

import web
import redis
import operator
import os
import sys
import re
import log_config

logger = log_config.log_config("./log/vgtp_pe_main_log.txt", "VGTP_PE")
logger.info("VGTP_PE start.")

list_key_prefix = 'PE_STAT_LIST'

other_libs={'redis':redis, 
            'sys':sys, 
            'operator':operator, 
            're':re , 
            'sorted':sorted}

render = web.template.render('templates/', globals=other_libs)

urls = (
    '/', 'index',
    '/refresh_data', 'refresh_data'
)

r = redis.StrictRedis(host='localhost', port=6379, db=0)

class index:
    def GET(self):
        i = web.input(modid='00')
        list_key = list_key_prefix + i.modid

        content = r.lrange(list_key, 0, -1)

        if len(content)==0:
            logger.info("No Data in Redis DB.")
            return "<html><body><h2> No Data in Redis DB. Wait a min.</h2>\
                    </body></html>"
        else:        
            return render.reg_module(list_key , i.modid)

class refresh_data:
    def GET(self):
        i = web.input(modid='00')
        list_key = list_key_prefix + i.modid

        if r.exists(list_key):
            row = r.lpop(list_key)
            if None != row:
                row = re.sub(r"\s+", "", row)
                row = re.sub(r"\|$", "", row)
                logger.info(row)
                return row
            else:
                logger.info("DATA:NULL")
                return "{DATA:NULL}"
        else:
            logger.info("DATA:NULL")
            return "{DATA:NULL}"
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

