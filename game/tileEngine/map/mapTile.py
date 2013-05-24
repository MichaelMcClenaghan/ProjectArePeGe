"""
mapTile.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

import pygame

import random

from game.constants import *

class MapTile(object):
    def __init__(self, tileArray, xPos, yPos):
        
        self.tileArray = tileArray
        self.gameClient = tileArray.gameClient

        self.xPos = xPos
        self.yPos = yPos
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.tiletype = None
        
        self.image = self.tileArray.tileset.getTileImage(TILEIMAGE['grass'])
        
        self.isHovered = False
        self.passable = True
        
        self.rect = self.doRect(xPos, yPos, self.width, self.height)
        
    def doRect(self, xPos, yPos, width, height):
        rect = pygame.rect.Rect(xPos, yPos, width, height)
        return rect
        
    def setType(self, tiletype):
        print "Setting tile at:", self.xPos, self.yPos, "to type: ", tiletype
        self.tiletype = tiletype
        self.image = self.tileArray.tileset.getTileImage(TILEIMAGE[tiletype])   
        self.gameClient.gameMap.updated = True
     