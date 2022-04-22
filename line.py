#!/usr/bin/env python

from element import Element

class Line(Element):
	def insertTo(self, c):
		c.insertLine(self)
		
	def deleteFrom(self, c):
		c.deleteLine(self)
