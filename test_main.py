#!/usr/bin/env python

'''
	@file test_main
	@author sb
	@brief script to test the working of the password generator function
'''

# standard lib imports
from util.util import gen_passwd
from traceback import print_exc
from sys import stdout
from random import randint

def test_gen_passwd():
	'''
		@function test_gen_passwd
		@brief function to test the password generation function
	'''

	# randomly choose the length of the password,
	# randomly choose exclusion characters and then
	# cross check if exclusion characters are present in the generated password
	# or not

	num_tests = randint(1, 1000)
	print("Random number of tests : {}".format(num_tests))

	excl_chars = input("Please provide the characters to be excluded : ")

	print("\nNumber of tests to be done : {}".format(num_tests))

	npass = 0
	nfail = 0

	# now start the looop
	for tindex in range(num_tests):
		# call the function and provide the length randomly
		cpasswd = gen_passwd(randint(9, 100), excl_chars)
		#print("Test ID : {} ".format(tindex + 1), end='')

		set_cpasswd = set(cpasswd)
		set_excl_chars = set(excl_chars)

		# for each of these passwords, the test needs to check if the generated
		# password has any of the characters present which falls in the
		# excluded list - intersection should be empty
		if len(set_cpasswd.intersection(set_excl_chars)) == 0:
			npass += 1
			#print("... " + u'\u2713')
		else:
			nfail += 1
			#print("... " + u'\u2717')

	print("Pass : {}%".format(npass / num_tests * 100))
	print("Fail : {}%".format(nfail / num_tests * 100))

	return 0

if __name__ == '__main__':
	try:
		test_gen_passwd()
	except Exception as exc:
		print_exc(file = stdout)
