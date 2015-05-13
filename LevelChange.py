import pygame, math, sys
from Block import Block

class LevelChangeBlock(Block):
    def __init__(self,img, pos, size):
        Block.__init__(self, img, pos, size)
        self.img = img
        self.kind = kind


    def playerCollide(self, other):
        return True
        return False
    
