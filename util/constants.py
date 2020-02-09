'''
	@file constants
	@author sb
	@brief module component containing all the constants to be used in the
	program
'''

# standard lib imports
from os import (getcwd, sep)

# file location - hidden
RES_FILE = getcwd() + sep + ".config.json"

# file types
FILE_FTYPE = 'f'
DIR_FTYPE = 'd'

# application dictionary key names
CUR = 'cur'
EXCL = 'excl_chars'
LENP = 'len'
