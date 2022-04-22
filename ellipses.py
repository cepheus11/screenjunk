#!/usr/bin/env python

from moving import Moving
from canvas import Canvas
from ellipsis import Ellipsis

class Ellipses(Moving):
	def __init__(self, ovalCount=25):
		Moving.__init__(self)
		self.maxSpeed = 10
		self.ovalCount = ovalCount
		self.elements = list()
	
	def createEdges(self):
		self.topleft = self.createEdge()
		self.bottomright = self.createEdge()
	
	def beginMove(self):
		Moving.beginMove(self)
		self.createEdges()
	
	def move(self):
		Moving.move(self)
		if len(self.elements) >= self.ovalCount:
			e = self.elements[0]
			self.deleteElement(e)
			del self.elements[0]
		self.moveEdge(self.topleft)
		self.moveEdge(self.bottomright)
		
		e = Ellipsis()
		e.topleft = self.topleft
		e.bottomright = self.bottomright
		e.color = self.color
		self.insertElement(e)
		self.elements.append(e)

