#!/usr/bin/env python

from moving import Moving
from polygon import Polygon

class Mystify(Moving):
	def __init__(self, cornerCount=4, polygonCount=4):
		Moving.__init__(self)
		self.cornerCount = cornerCount
		self.polygonCount = polygonCount
		self.polygons = list()

	def createCorners(self):
		self.corners = list()
		for i in range(0, self.cornerCount):
			self.corners.append(self.createEdge())

	def createPolygon(self, canvas, color):
		p = Polygon()
		p.corners = self.corners
		p.color = self.color
		self.insertElement(p)
		return p

	def beginMove(self):
		Moving.beginMove(self)
		self.createCorners()

	def move(self):
		Moving.move(self)
		if len(self.polygons) >= self.polygonCount:
			p = self.polygons[0]
			self.deleteElement(p)
			del self.polygons[0]
		for edge in self.corners:
			self.moveEdge(edge)
		p = self.createPolygon(self.canvas, self.color)
		self.polygons.append(p)
