#!/usr/bin/env python

import sys as S
if S.version_info[0]<3:
	import Tkinter as T
else:
	import tkinter as T
from canvas import Canvas

class TkCanvas(Canvas):
	def __init__(self, pattern):
		Canvas.__init__(self, pattern)
		self.root = T.Tk()
		self.root.title("ScreenJunk")
		self.canvas = T.Canvas(
			self.root,
			width=pattern.width,
			height=pattern.height,
			background="black")
		self.canvas.pack()
		self.root.after(pattern.sleepTime, self.idle)
		self.root.mainloop()
		
	def idle(self):
		self.move()
		self.root.after(self.pattern.sleepTime, self.idle)

	def move(self):
		self.pattern.move()
		
	def deleteElement(self, element):
		self.canvas.delete(element.backendLink)

	def insertEllipsis(self, element):
		element.backendLink = self.canvas.create_oval(
			element.topleft.x, element.topleft.y,
			element.bottomright.x, element.bottomright.y,
			outline=element.color,
			fill="",
			width=2)

	def deleteEllipsis(self, element):
		self.deleteElement(element)
		
	def insertPolygon(self, element):
		element.backendLink = self.canvas.create_polygon(
			0,
			0,
			outline=element.color,
			fill="")
		coords = list()
		for edge in element.corners:
			coords.append(edge.x)
			coords.append(edge.y)
		self.canvas.coords(element.backendLink, *coords)
		
	def deletePolygon(self, element):
		self.deleteElement(element)
		
	def insertLine(self, element):
		element.backendLink = self.canvas.create_line(
			element.a.x,
			element.a.y,
			element.b.x,
			element.b.y,
			fill=element.color,
			width=2)

	def deleteLine(self, element):
		self.deleteElement(element)
