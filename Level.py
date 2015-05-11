import pygame, sys, math
from Block import Block
from HardBlock import HardBlock
from LevelChange import LevelChangeBlock


class Level():
    def __init__(self, screenSize, blockSize, hardblockSize):
        self.screenSize = screenSize
        self.blockSize = blockSize
        self.hardblockSize = hardblockSize
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
                    Block("maps/sand.png", [x*self.blockSize,y*self.blockSize])
                elif c =="!":
                    Block("maps/grass.png", [x*self.blockSize,y*self.blockSize])
                elif c =="+":
                    Block("maps/grasssand.png", [x*self.blockSize,y*self.blockSize])
                elif c =="-":
                    HardBlock("maps/rock.png", [x*self.hardblockSize,y*self.hardblockSize])
                elif c =="c":
                    HardBlock("maps/sand.png", [x*self.hardblockSize,y*self.hardblockSize])
                elif c =="s":
                    HardBlock("maps/grasssand.png", [x*self.hardblockSize,y*self.hardblockSize])
                elif c =="r":
                    HardBlock("maps/grass.png", [x*self.hardblockSize,y*self.hardblockSize])
                '''elif c =="n":
                    LevelChangeBlock("maps/grass.png", [x*self.blockSize,y*self.blockSize, newlev, c])'''








