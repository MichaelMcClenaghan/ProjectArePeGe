"""
gameLayer.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""
import pygame

from game.constants import *
from game.map.mapTile import *
from game.graphics.tileset import *
from game.map.tileArray import *

class TileLayer(object):
    def __init__(self, gameClient, mapWidth, mapHeight, tilesetNumber):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.gameClient = gameClient
        
        self.surface = pygame.Surface(gameClient.viewManager.getResolution()).convert()
        self.surface.fill(RED)
        self.surface.set_colorkey(TRANSPARENT)
        
        self.tileArray = TileArray(gameClient, mapWidth, mapHeight, tilesetNumber)
        
    def blitTiles(self, gameClient):
        for row in self.tileArray.getTileArray():
            for tile in row:
                self.surface.blit(tile.image, tile.rect)
        
    def getSurface(self):
        return self.surface
                
    def getTile(self, xPos, yPos):
        return self.tileArray.getTileArray()[xPos][yPos]
        
    def clearSurface(self):
        self.getSurface().fill(TRANSPARENT)