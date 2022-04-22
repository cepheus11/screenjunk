#!/usr/bin/env python

from moving import Moving
from line import Line

class JumpingLines(Moving):
	def __init__(self):
		Moving.__init__(self)
		self.sleepTime = 3
		self.tickCount = 360
		self.maxSpeed = 10
		self.hueOffset = self.hueOffset / 10.0

	def createEdges(self):
		self.a = self.createEdge()
		self.b = self.createEdge()

	def beginMove(self):
		Moving.beginMove(self)
		self.lines = list()
		self.createEdges()

	def reset(self):
		for line in self.lines:
			self.deleteElement(line)
		self.lines = list()
		self.createEdges()

	def move(self):
		Moving.move(self)
		self.moveEdge(self.a)
		self.moveEdge(self.b)
		line = Line()
		line.a = self.a
		line.b = self.b
		line.color = self.color
		self.insertElement(line)
		self.lines.append(line)
		self.changeColor()
