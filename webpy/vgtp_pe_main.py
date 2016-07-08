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

other_libs={'redis':redis, 'sys':sys, 'operator':operator, 're':re , 'sorted':sorted}
render = web.template.render('templates/', globals=other_libs)

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.reg_module("reg_module" , "TESTING")
       
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

