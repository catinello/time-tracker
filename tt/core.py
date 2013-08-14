#!/bin/usr/env python

#modules
import getopt
import os
import sys
import syslog
import tt.data
import time
import datetime

#functions
def usage():
	'''usage output'''
	print "Usage: tt {--start|--stop|--list} [PROJECT]"
	sys.exit(1) #return value 1 -> error in usage

def main():
	'''arguments calling'''

	#variables
	datastore = os.environ['HOME'] + os.sep + ".tt"
	retval = 0 #default return value -> success

	#constant
	IDFIX = 1000000

	#every call has 3 arguments
	if len(sys.argv) != 3:
		usage()

	#work with all arguments and options
	try:
		options, remainder = getopt.getopt(sys.argv[1:], '', ['start=', 'stop=', 'list='])
	except getopt.GetoptError:
		usage()

	#create datastore in home
	if not os.path.exists(datastore):
                os.makedirs(datastore)

	#open syslog
	syslog.openlog(sys.argv[0], syslog.LOG_PID, syslog.LOG_DAEMON)

	#main loop
	for opt, arg in options:
		if opt in ('--start'):
			syslog.syslog(opt + " -> " + str(arg))
			db = tt.data.File(datastore + os.sep + str(arg), IDFIX)

			if db.lastid() % 2 != 0:
				if db.lastid() == 1:
					print "Project " + arg + " was created."
				db.set(time.time())
			else:
				print "A session is already running for " + arg + "."
				retval = 3 #return value 3 -> session already used
		elif opt in ('--stop'):
			if os.path.exists(datastore + os.sep + str(arg)):
				syslog.syslog(opt + " -> " + str(arg))
				db = tt.data.File(datastore + os.sep + str(arg), IDFIX)

				if db.lastid() % 2 == 0:
					start = db.get(db.lastid())
					db.set(time.time())
					end = db.get(db.lastid())
					diff = datetime.datetime.fromtimestamp(end) - datetime.datetime.fromtimestamp(start)
					print "Session: " + str(diff.total_seconds()/60)[0:6] + " minutes"
				else:
					print "No session running for " + arg + "."
					retval = 3 #return value 3 -> session already used
			else:
				print "Project " + arg + " does not exist."
				retval = 2 #return value 2 -> project does not exist
		elif opt in ('--list'):
			if os.path.exists(datastore + os.sep + str(arg)):
				db = tt.data.File(datastore + os.sep + str(arg), IDFIX)
				list = db.dump()
				total = 0

				for i in range(IDFIX, len(list)+IDFIX-1, 2):
					session = datetime.datetime.fromtimestamp(float(list[str(i+1)])) - datetime.datetime.fromtimestamp(float(list[str(i)]))
					total += session.total_seconds()

					print "Session: " + str(datetime.datetime.fromtimestamp(float(list[str(i)])).strftime("%a %d. %B %Y %H:%M")) + " -> " + \
						str(datetime.datetime.fromtimestamp(float(list[str(i+1)])).strftime("%a %d. %B %Y %H:%M")) + " -> " + \
						str(session.total_seconds()/60)[0:5] + " min"

				print "Total: " + str(total/60/60)[0:6] + " hours"
			else:
				print "Project " + arg + " does not exist."
				retval = 2 #return value 2 -> project does not exist

	#close syslog
	syslog.closelog()
	sys.exit(retval)

if __name__ == "__main__":
	main()
