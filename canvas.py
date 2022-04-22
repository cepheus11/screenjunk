#!/usr/bin/env python

class Canvas:
	def __init__(self, pattern):
		self.pattern = pattern
		pattern.canvas = self
		
	def insertEllipsis(self, element):
		pass

	def deleteEllipsis(self, element):
		pass
		
	def insertPolygon(self, element):
		pass
		
	def deletePolygon(self, element):
		pass
		
	def insertLine(self, element):
		pass
	
	def deleteLine(self, element):
		pass
