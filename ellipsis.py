#!/usr/bin/env python

from element import Element

class Ellipsis(Element):
	def insertTo(self, c):
		c.insertEllipsis(self)

	def deleteFrom(self, c):
		c.deleteEllipsis(self)
