#!/usr/bin/env python

from moving import Moving
import random as R

class Circles(Moving):
	def __init__(self):
		Moving.__init__(self)
		self.maxRadius = 100
		self.circleCount = 300
		self.circles = list()

	def move(self):
		Moving.move(self)
		if len(self.circles) > self.circleCount:
			self.canvas.delete(self.circles[0])
			del self.circles[0]
		r = R.random() * self.maxRadius
		x = R.random() * self.width
		y = R.random() * self.height
		circle = self.canvas.create_oval(
			x-r,
			y-r,
			x+r,
			y+r,
			outline=self.color,
			fill="")
		self.circles.append(circle)
