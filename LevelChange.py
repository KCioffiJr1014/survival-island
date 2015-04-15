import pygame, math, sys
from Block import Block

class LevelChangeBlock(Block):
    def __init__(self,img, pos, size, newlev):
        Block.__init__(self, img, pos, size)
        self.img = img
        print newlev
        self.newlev = newlev
        self.kind = kind


    def playerCollide(self, other):
        print "I'm going to ", self.newlev
            return True
        return False
    
