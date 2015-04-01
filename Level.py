import pygame, sys, math

from Block import Block


class Level():
	def __init__(self, screenSize, blockSize):
		self.screenSize = screenSize
		self.blockSize = blockSize
		self.level = ""
		
	def loadLevel(self, level):
		self.level = level
		levelFile = "maps/" + level + ".lvl"
		
		f = open(levelFile, "r")
		lines = f.readlines()
		f.close()
		
		newlines = []
		
		for line in lines:
			newline = ""
			for c in line:
				if c != "\n":
					newline += c
			newlines += [newline]
			
		lines = newlines
		
		for y, line in enumerate(lines):
			for x, c in enumerate(line):
				if c == "#":
					Block("images/Block.png", [x*self.blockSize,y*self.blockSize])
			





\


