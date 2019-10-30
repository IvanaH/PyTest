#! usr/bin/env python
# -*- coding: utf-8 -*-
'''
create 2019/10/30
@author Ivana
'''

import logging
from sys import exc_info

''' using logging '''
# logging.basicConfig(level=logging.WARNING,format='%(asctime)s - %(message)s') #by default, StreamHandler
# logging.basicConfig(level=logging.WARNING,filename='loggingDemo.txt', format='%(asctime)s - %(message)s', datefmt = '%Y-%m-%d %H:%M:%S') #FileHandler
# logging.basicConfig(level=logging.ERROR,format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')  # not work, since the logger has been configed and force is default False
# # logging.basicConfig(level=logging.ERROR,format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S',force=True)  #force added since 3.8
# logging.warning("This is a warning message.\n")
# logging.error("This is an error msg. \n")
# logging.debug("This is an debug msg. \n")  # won't output, 'cause debug is lower than warning


''' custom logger'''
#create a logger
loggerDemo = logging.getLogger('example_log') 
#create handler
e_handler = logging.StreamHandler()
i_handler = logging.FileHandler('loggingDemo.txt',mode='w')  #default mode is a
e_handler.setLevel(logging.ERROR)
i_handler.setLevel(logging.INFO)
#set a formatter and add it to handler
testFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt = '%Y-%m-%d %H:%M:%S')
e_handler.setFormatter(testFormatter)
i_handler.setFormatter(testFormatter)
#add handlers to logger
loggerDemo.addHandler(e_handler)
loggerDemo.addHandler(i_handler)

# loggerDemo.warning("This is a warning message\n")
# loggerDemo.error("This is an error message for custom logger.\n",exc_info = True)
# loggerDemo.exception("This is an exception.\n",exc_info=True)  # log message with ERROR level

def invaildDivision():
    try:
        2/0
    except Exception as e:
        loggerDemo.exception('%s raise an exception:' % invaildDivision.__name__,exc_info=True)
        

if __name__ == '__main__':
   invaildDivision()