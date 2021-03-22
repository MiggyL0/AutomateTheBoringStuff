# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:19:51 2020

@author: Miguel
"""

import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

logging.debug('start of program')

def factorial(n):
    logging.debug('start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i,total))
    
    logging.debug('return value is %s' % (total))
    return total

print(factorial(9))

logging.debug('end of program')