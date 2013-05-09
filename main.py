"""
Project ArePeGe
main.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2013 Micmac Creations. All rights reserved.
"""


import pygame
from pygame.locals import *

from game.gui.viewManager import *
from game.utilities import *
from game.constants import *
from game.controlManager import *
from game.characterManager import *
from game.map.gameMap import *

import sys, os

class GameClient(object):
    
    def __init__(self):
        
        self.viewManager = ViewManager()
        self.controlManager = ControlManager()
        self.clock = pygame.time.Clock()
                        
        self.mode = GAME
        self.rect = pygame.rect.Rect(0, 0, self.viewManager.getWidth(), self.viewManager.getHeight())
        
        self.running = False        
        
    def run(self):
        self.gameMap = GameMap(self, 40, 40)
        self.running = True
        self.characterManager = CharacterManager(self)

    def getSize(self):
        '''
        The size of the pygame screen
        '''
        return (self.viewManager.getWidth(), self.viewManager.getHeight())
    
    def getCaption(self):
        '''
        The caption on the pygame screen
        '''
        return self.viewManager.getCaption()
    
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.controlManager.processKeys(self, event)
		
    def tick(self, deltaT):
        if not self.running:
            self.run()
        self.controlManager.run(self)
        self.clock.tick()
    
    def draw(self, screen):
        if self.running:
            self.gameMap.updateMapSurface()
            screen.blit(self.gameMap.mapSurface, self.rect)
            #self.gameMap.clearTileLayers()
            #self.characterManager.blitPlayer(self)
            #self.gameMap.blitTileLayers(self, screen)
            #self.gameMap.blitSpriteLayer(self, screen)

if __name__ == '__main__':
    gameClient = GameClient()
    run_pygame_loop(gameClient)