"""
gameMap.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

from game.constants import *
from game.tileEngine.map.tileLayer import *
from game.tileEngine.map.spriteLayer import *

from pygame import Surface

class GameMap(object):
    
    def __init__(self, gameClient, mapWidth, mapHeight):
        
        self.mapWidth = mapWidth 
        self.mapHeight = mapHeight
        self.gameClient = gameClient
        
        self.updated = True
        
        self.tilesize = TILESIZE

        self.widthInPixels = self.mapWidth*self.tilesize
        self.heightInPixels = self.mapHeight*self.tilesize
        
        self.backgroundLayer = TileLayer(gameClient, self.mapWidth, self.mapHeight, "01")
        self.foregroundLayer = TileLayer(gameClient, self.mapWidth, self.mapHeight, "02")
        self.spriteLayer = SpriteLayer(gameClient, self.mapWidth, self.mapHeight)
        
        self.mapSurface = Surface((self.mapWidth * self.tilesize, self.mapHeight * self.tilesize))
            
        self.updateMapSurface()
        
    def clearTileLayers(self):
        self.backgroundLayer.clearSurface()
        self.foregroundLayer.clearSurface()

    def updateMapSurface(self):
        if self.updated:
            self.backgroundLayer.blitTiles(self.gameClient)
            self.foregroundLayer.blitTiles(self.gameClient)
            self.updated = False

            self.mapSurface.blit(self.backgroundLayer.getSurface(), self.backgroundLayer.getSurface().get_rect())
            #self.mapSurface.blit(self.foregroundLayer.getSurface(), self.foregroundLayer.getSurface().get_rect())
            self.mapSurface.convert()

    def getWidthInPixels(self):
        return self.widthInPixels

    def getHeightInPixels(self):
        return self.heightInPixels

    def getSizeInPixels(self):
        return (gameClient.gameMap.getWidthInPixels(), gameClient.gameMap.getHeightInPixels)