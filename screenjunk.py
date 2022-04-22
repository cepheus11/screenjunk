#!/usr/bin/env python

from tkcanvas import TkCanvas

class ScreenJunk(object):
	def __init__(self, pattern):
		pattern.width = 800
		pattern.height = 600
		TkCanvas(pattern)


