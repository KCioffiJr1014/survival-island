import pygame, math
from Lvel import Level

class BlockCollide(pygame.sprite.Sprite):
    
for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    Block("maps/sand.png", [x*self.blockSize,y*self.blockSize])
                elif c =="!":
                    Block("maps/grass.png", [x*self.blockSize,y*self.blockSize])
                elif c =="+":
                    Block("maps/grasssand.png", [x*self.blockSize,y*self.blockSize])
                elif c =="-":
                    Block("maps/rock.png", [x*self.blockSize,y*self.blockSize])
                    
