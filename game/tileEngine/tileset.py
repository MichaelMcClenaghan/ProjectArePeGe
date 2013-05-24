"""
tileset.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

import pygame

from game.constants import *

class Tileset(object):
    def __init__(self, gameClient, filename):
        self.tileWidth = TILESIZE
        self.tileHeight = TILESIZE
        
        self.tilesetImage = pygame.image.load(filename).convert()
        self.imageWidth, self.imageHeight = self.tilesetImage.get_size()
        
        self.tileImageArray = self.doTileImageArray()
        
    def doTileImageArray(self):
        tilesetImageArray = []
        
        for tile_x in range(0, self.imageWidth/self.tileWidth):
            self.row = []
            tilesetImageArray.append(self.row)
            for tile_y in range(0, self.imageHeight/self.tileHeight):
                self.rect = (tile_x * self.tileWidth, tile_y * self.tileHeight,
                             self.tileWidth, self.tileHeight)
                self.row.append(self.tilesetImage.subsurface(self.rect))
                
        return tilesetImageArray
        
    def getTileImage(self, (xPos, yPos)):
        return self.tileImageArray[xPos][yPos]