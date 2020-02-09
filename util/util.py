'''
	@file util
	@author sb
	@brief module containing all the basic code
'''

# standard lib imports
from pathlib import Path
from string import (ascii_letters, punctuation, digits)
from random import choice

def file_exists(path, ftype):
	'''
		@function file_exists
		@brief function checking existence of directory or file
		@params
			1. path - path to the directory or file
			2. ftype - filetype, f for file and d for directory
		@return boolean value - true for existing, false otherwise
	'''
	if not isinstance(path, str):
		raise TypeError("Path should be of type string")
	if path is None or len(path) == 0:
		raise ValueError("Path should be something legible")

	if not isinstance(ftype, str):
		raise TypeError("Filetype should be of type string")
	if ftype is None or len(ftype) == 0:
		raise ValueError("Filetype should be something legible")

	return Path(path).exists()

def gen_passwd(len_passwd, excl_chars):
	'''
		@function gen_passwd
		@brief function to generate the password
		@params
			1. len_passwd - length of the password
			2. excl_chars - excluded characters
		@return generated password in string type
	'''
	passwd = str()

	if not isinstance(len_passwd, int):
		raise TypeError("Length of the password must be an integer")
	if len_passwd < 8:
		raise ValueError("Minimum length of the password should be 8")

	if not isinstance(excl_chars, str):
		raise TypeError("Excluded characters should be a string")

	chars = ascii_letters + punctuation + digits

	# remove '%' from the punctuation part
	lc = list(chars)
	lc.pop(lc.index('%'))
	chars = ''.join(lc)

	set_excl_chars = set(ord(i) for i in list(excl_chars))
	passwd = "".join(choice(chars) for i in range(len_passwd) if i not in
			set_excl_chars)

	return passwd
