#/!/usr/bin/env python

import edge as E
import random as R
import colorsys as C
from element import Element

class Moving(object):
	def __init__(self):
		self.ticks = 0
		self.tickCount = 100
		self.sleepTime = 10
		self.maxSpeed = 5
		self.firstMove = True
		self.hueOffset = 10.0/360.0
		self.hue = R.random()
		self.color = self.colorFromHue(self.hue)

	def colorFromHue(self, hue):
		r, g, b = C.hsv_to_rgb(hue, 1, 1)
		rgb = (0xFF * r, 0xFF * g, 0xFF * b)
		return "#" + "".join('{:02X}'.format(int(c)) for c in rgb)

	def createEdge(self):
		return E.Edge(
			R.random() * self.width,
			R.random() * self.height,
			R.random() * self.maxSpeed,
			R.random() * self.maxSpeed)

	def reflect(self, edge, reflectX, reflectY):
		if reflectX >= 0:
			edge.x = reflectX - (edge.x - reflectX)
			edge.dx = - edge.dx
		if reflectY >= 0:
			edge.y = reflectY - (edge.y - reflectY)
			edge.dy = - edge.dy

	def moveEdge(self, edge):
		edge.x = edge.x + edge.dx
		edge.y = edge.y + edge.dy
		reflectX = -1
		reflectY = -1
		if edge.x < 0:
			reflectX = 0
		if edge.x > self.width:
			reflectX = self.width
		if edge.y < 0:
			reflectY = 0
		if edge.y > self.height:
			reflectY = self.height
		self.reflect(edge, reflectX, reflectY)

	def changeColor(self):
		self.hue += self.hueOffset
		if self.hue >= 1:
			self.hue -= 1
		self.color = self.colorFromHue(self.hue)
		
	def reset(self):
		self.changeColor()

	def tick(self):
		self.ticks += 1
		if self.ticks >= self.tickCount:
			self.ticks = 0
			self.reset()

	def beginMove(self):
		pass

	def move(self):
		if self.firstMove:
			self.firstMove = False
			self.beginMove()
		self.tick()
	
	def insertElement(self, e):
		e.insertTo(self.canvas)
		
	def deleteElement(self, e):
		e.deleteFrom(self.canvas)
