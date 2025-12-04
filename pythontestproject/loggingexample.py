'''
Created on Dec 3, 2025

@author: rharidas
'''
import logging
import traceback
from logging.handlers import RotatingFileHandler # we use this when log files are huge for exampl abouve 2 kb then we need to kep may be 5 backups and detele otheres
from logging.handlers import TimedRotatingFileHandler#after wht time should it start rotating
logging.basicConfig(level=logging.DEBUG)
logging.info("info")
logging.debug("debug")
logging.warn("warn")
logging.critical("critical")
logging.error("error")


try:
    a=[1,2,3]
    print(a[4])
except IndexError as e:
    #logging.error(e) ERROR:root:list index out of range
    logging.error(e,exc_info=True)#for displaying the stack trace
    
#if we dont know what kind of  error
try:
    a=[1,2,3]
    print(a[4])
except:
    logging.error("the errir is %s",traceback.format_exc()) #same output as befre 