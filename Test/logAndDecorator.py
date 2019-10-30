#! usr/bin/env python
# -*- coding: utf-8 -*-
'''
create 2019/10/30
@author Ivana
'''

import logging
import functools

def sampleLogger(filepath = None):
    #Create a logger
    logger = logging.getLogger('errorAndWarning')
    
    #Create handlers and set the level
    e_handler = logging.StreamHandler()
    e_handler.setLevel(logging.ERROR)
    if filepath == None:
        w_handler = logging.FileHandler('sample.log')
    else:
        w_handler = logging.FileHandler(filepath)
    w_handler.setLevel(logging.WARNING)
    
    fmter = '%(asctime)s - %(levelname)s - %(msg)s'
    e_handler.setFormatter(fmter)
    w_handler.setFormatter(fmter)

    #add handlers to logger
    logger.addHandler(e_handler)
    logger.addHandler(w_handler)
    
    return logger


def basiclogDecor(func):
    def wrapper(*args, **kw):
        try:        
            return func(*args,**kw)
        except Exception as err:
            err = 'An exception raise by' + functools.__name__
            logging.exception(err,exc_info = True)
        raise
    return wrapper

@basiclogDecor
def invaildDivision():
    2/0


if __name__ == '__main__':
    invaildDivision()