#!/usr/bin/env python

'''
	@file main.py
	@author sb
	@brief program to generate hard to guess passwords
'''

# standard lib imports
from json import (load, JSONDecodeError, dumps)
from datetime import datetime

# third party lib imports

# custom lib imports
from util.util import (file_exists, gen_passwd)
from util.constants import (RES_FILE, FILE_FTYPE, CUR, EXCL, LENP)

def main():
	'''
		@function main
		@brief main function calling other functions
	'''

	json_d = dict()
	if not file_exists(RES_FILE, FILE_FTYPE):
		with open(RES_FILE, 'w') as f:
			print("Configuration file not found, creating it")
			f.write("{}")
	else:
		print("Configuration file exists, reading the contents")
		with open(RES_FILE) as f:
			json_d = load(f)

	#print("Configuration information loaded : {}".format(json_d))

	while True:
		choice = input(
		"Do you wish this program to manage this password? [y/n/q/s] ")

		if choice.lower() == 'y':
			app_name = input("Application name : ")
			print("Password to be managed for : {}".format(app_name))

			# check for the application name in the JSON file - if the
			# application is not present - say adding application to the list
			if app_name in set(json_d.keys()):
				print("found the application in the configuration file")
				# if the application name is found, show the current password
				# before asking for the changing of the password
				print("Archiving current password for date : {}".format(
					datetime.strftime(datetime.now(), "%Y-%m-%d")))

				# get the value of the application name
				print("Current object value of app_name : {}".format(
					json_d.get(app_name)))
				print("Last password that was set : {}".format(
					json_d.get(app_name).get(CUR)))
				print("Last set of excluded characters : {}".format(
					json_d.get(app_name).get(EXCL)))
				print("Last length of the password : {}".format(
					json_d.get(app_name).get(LENP)))

				# ask for the details now
				napp_d = json_d.get(app_name)

				len_passwd = int(input("Required length [>8] : "))
				excl_chars = input("Characters to exclude : ")
				gen_pwd = gen_passwd(len_passwd, excl_chars)

				# Adding the older password in the date section
				archive_date = datetime.strftime(datetime.now(), "%Y-%m-%d")
				napp_d[archive_date] = json_d.get(app_name).get(CUR)
				napp_d[CUR] = gen_pwd
				if excl_chars.lower() == 'null':
					napp_d[EXCL] = ''
				else:
					napp_d[EXCL] += excl_chars
				napp_d[LENP] = len_passwd

				json_d[app_name] = napp_d

				with open(RES_FILE, 'w') as f:
					f.write(dumps(json_d, indent = 3))
					f.write("\n")
			else:
				print("application name not found in the configuration file")
				napp_d = dict()

				len_passwd = int(input("Required length [>8] : "))
				excl_chars = input("Characters to exclude : ")
				gen_pwd = gen_passwd(len_passwd, excl_chars)
				print("Generated password : {}".format(gen_pwd))

				napp_d[CUR] = gen_pwd
				napp_d[EXCL] = excl_chars
				napp_d[LENP] = len_passwd

				json_d[app_name] = napp_d

				with open(RES_FILE, 'w') as f:
					f.write(dumps(json_d, indent = 3))
					f.write("\n")
		elif choice.lower() == 'n':
			print("Choice is No")

			len_passwd = int(input("Required length [>8] : "))
			excl_chars = input("Characters to exclude : ")
			print("Generated password : {}".format(
				gen_passwd(len_passwd, excl_chars)))
		elif choice.lower() == 'q':
			break
		elif choice.lower() == 's':
			app_name = input('Application name : ')
			print("Showing password for : {}".format(app_name))

			print("Applications managed : {}".format(json_d.keys()))

			if app_name in set(json_d.keys()):
				print("Application is managed by this program")
				print("Details of {} : {}".format(app_name,
					json_d.get(app_name).get(CUR)))

				# now copy this immediately in the clipboard

				print("\nCurrent password has been copied in the clipboard\n")
			else:
				print("Applications being managed by this program : {}".format(
					{i for i in json_d.keys()}))

	print("Exiting the application")
	return 0

if __name__ == '__main__':
	'''
		main execution starts here
	'''
	try:
		main()
	except JSONDecodeError as jsderr:
		print("Error : {}".format(jsderr))
	except Exception as exc:
		print("Exception : {}".format(exc))
