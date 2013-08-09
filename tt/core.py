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
			db = data.File(datastore + os.sep + str(arg))

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
				db = data.File(datastore + os.sep + str(arg))

				if db.lastid() % 2 == 0:
					start = db.get(db.lastid())
					db.set(time.time())
					end = db.get(db.lastid())
					diff = datetime.datetime.fromtimestamp(end) - datetime.datetime.fromtimestamp(start)
					print "Session: " + str(diff.total_seconds()) + " seconds"
				else:
					print "No session running for " + arg + "."
					retval = 3 #return value 3 -> session already used
			else:
				print "Project " + arg + " does not exist."
				retval = 2 #return value 2 -> project does not exist
		elif opt in ('--list'):
			if os.path.exists(datastore + os.sep + str(arg)):
				db = data.File(datastore + os.sep + str(arg))
				list = db.dump()
				#print list
				#print list.keys()
				total = 0
				for i in range(1000000, len(list)+1000000-1, 2):
					#print i, list[str(i)]
					#print i + 1, list[str(i+1)]
					session = datetime.datetime.fromtimestamp(float(list[str(i+1)])) - datetime.datetime.fromtimestamp(float(list[str(i)]))
					total += session.total_seconds()
					print "Session: " + str(datetime.datetime.fromtimestamp(float(list[str(i)])).strftime("%a %d. %B %Y %H:%M")) + " -> " + \
						str(datetime.datetime.fromtimestamp(float(list[str(i+1)])).strftime("%a %d. %B %Y %H:%M")) + " -> " + \
						str(session.total_seconds()/60)[0:5] + " min"
				print "Total: " + str(total/60) + " minutes"
			else:
				print "Project " + arg + " does not exist."
				retval = 2 #return value 2 -> project does not exist

	#close syslog
	syslog.closelog()
	sys.exit(retval)

if __name__ == "__main__":
	main()
