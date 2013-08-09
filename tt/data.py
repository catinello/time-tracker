#!/bin/usr/env python

#modules
import bsddb

#classes
class File(object):
	'''handle dataobject i/o'''

	def __init__(self, project):
		self.project = project
		self.idfix = 1000000

	def dump(self):
		db = bsddb.btopen(self.project, 'c')
		list = db
		db.sync()
		return list

	def get(self, id):
		return float(self.dump()[str(id)])

	def set(self, timestamp):
		db = bsddb.btopen(self.project, 'c')
		db[str(len(db) + self.idfix)] = str(timestamp)
		db.sync()

	def lastid(self):
		db = bsddb.btopen(self.project, 'c')
		try:
			id = db.keys()[len(db)-1]
		except IndexError:
			id = 1 #uneven
		db.sync()
		return int(id)

