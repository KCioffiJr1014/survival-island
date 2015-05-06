import pygame, sys, math

from Block import Block

class HardBlock(Block):
    def __init__(self, image, pos = (0,0), blocksize = [50,50]):
        Block.__init__(self, image, pos, blocksize)
