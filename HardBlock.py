  import pygame, sys, math

from Block import Block

class HardBlock(Block):
    def __init__(self, image, pos):
        Block.__init__(self, image, pos)
