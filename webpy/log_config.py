#!/usr/bin/python
# encoding=utf-8
'''
#example
#import log_config
#logger = log_config.log_config("./test_log.txt", "tester")
#logger.info("start")

#!/usr/bin/env python
# -*- coding:utf-8 -*
'''
""" Setup a Logger which creates a new log file when it
reach up to it limits, such as one hour and file size 10 MB.
"""

__author__ = "Zhiwei Yan"
__copyright__ = "Copyright 2016, The Common tools Project"
__credits__ = ["Zhiwei Yan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Zhiwei YAN"
__email__ = "jerod.yan@gmail.com"
__status__ = "Production"

import os, sys
import logging
import logging.handlers as handlers
import time, datetime
class SizedTimedRotatingFileHandler(handlers.TimedRotatingFileHandler):
    """
    Handler for logging to a set of files, which switches from one file
    to the next when the current file reaches a certain size, or at certain
    timed intervals
    """
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None,
                 delay=0, when='h', interval=1, utc=False):
        # If rotation/rollover is wanted, it doesn't make sense to use another
        # mode. If for example 'w' were specified, then if there were multiple
        # runs of the calling application, the logs from previous runs would be
        # lost if the 'w' is respected, because the log file would be truncated
        # on each run.
        if maxBytes > 0:
            mode = 'a'
        handlers.TimedRotatingFileHandler.__init__(
            self, filename, when, interval, backupCount, encoding, delay, utc)
        self.maxBytes = maxBytes

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.
        """
        if self.stream is None:                 # delay was set...
            self.stream = self._open()
        if self.maxBytes > 0:                   # are we rolling over?
            msg = "%s\n" % self.format(record)
            self.stream.seek(0, 2)  #due to non-posix-compliant Windows feature
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0



def log_config(log_filename, logger_str):

    print '\n'
    print '-' * 80
    ret = os.access(log_filename, os.F_OK)
    if False==ret:
        log_dir = log_filename.split("/")
        if 2!=len(log_dir):
            log_dir = '/'.join(log_dir[0:len(log_dir)-1])
            print "Make log_dir: ", log_dir
            ret = os.access(log_dir, os.F_OK)
            print ret
            if False==ret:
                os.makedirs(log_dir)
    
    logging.basicConfig(format = '%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s:|%(message)s| \n',
                       datefmt = '%Y-%m-%D %H:%M:%S')

    logger=logging.getLogger(logger_str)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)

    handler=SizedTimedRotatingFileHandler(
            log_filename, 
            maxBytes=10*1024*1024, backupCount=24*30,
            when='h',interval=1,
            # encoding='bz2',  # uncomment for bz2 compression
            )

    logformatter = logging.Formatter('%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s:|%(message)s| \n')
    handler.setFormatter(logformatter)
    logger.addHandler(handler)

    
    # logging information will print in the screen, too.
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logformatter)
    logger.addHandler(console)

    return logger
