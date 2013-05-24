"""
gameLayer.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""
import pygame

from game.constants import *

class SpriteLayer(object):
    def __init__(self, gameClient, mapWidth, mapHeight):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        
        self.surface = pygame.Surface((self.mapWidth*TILESIZE, self.mapHeight*TILESIZE)).convert()
        self.surface.fill(TRANSPARENT)
        self.surface.set_colorkey(TRANSPARENT)
        
    def blitSprite(self, sprite):
        self.surface.blit(sprite.getSprite(), sprite.getRect())
        
    def getSurface(self):
        return self.surface
        
    def clearSurface(self):
        self.getSurface().fill(TRANSPARENT)
        