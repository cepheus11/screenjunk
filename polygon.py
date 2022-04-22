#!/usr/bin/env python

from element import Element

class Polygon(Element):
	def insertTo(self, c):
		c.insertPolygon(self)

	def deleteFrom(self, c):
		c.deletePolygon(self)
