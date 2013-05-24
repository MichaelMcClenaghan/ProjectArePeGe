"""
Project ArePeGe
main.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2013 Micmac Creations. All rights reserved.
"""


import pygame
from pygame.locals import *

from game.gui.windowManager import *
from game.utilities import *
from game.constants import *
from game.camera import *
from game.controlManager import *
from game.characterManager import *
from game.tileEngine.map.gameMap import *
from game.fpsClock import *

import sys, os

class GameClient(object):
    
    def __init__(self):
        
        self.windowManager = WindowManager()
        self.controlManager = ControlManager()
        self.timer = FpsClock()
        self.clock = pygame.time.Clock()
                        
        self.mode = GAME
        self.rect = pygame.rect.Rect(0, 0, self.windowManager.getWidth(), self.windowManager.getHeight())
        
        self.running = False        
        
    def run(self):
        self.camera = Camera(self)

        self.gameMap = GameMap(self, 200, 200)
        self.running = True
        self.characterManager = CharacterManager(self)

    def getSize(self):
        return (self.windowManager.getWidth(), self.windowManager.getHeight())
    
    def getCaption(self):
        return self.windowManager.getCaption()
    
    def processEvent(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.controlManager.processKeys(self, event)

    def tick(self, deltaT):
        if not self.running:
            self.run()

        self.camera.centerOnPoint(self.characterManager.player.xPos, self.characterManager.player.yPos)        
        self.controlManager.run(self)
        self.clock.tick()
        self.timer.tick()
    
    def draw(self, screen):
        if self.running:
            self.gameMap.spriteLayer.clearSurface()
            self.gameMap.updateMapSurface()

            screen.fill(BLACK)
            self.characterManager.blitPlayer(self)
            screen.blit(self.gameMap.mapSurface, self.gameMap.mapSurface.get_rect(), self.camera.view)
            screen.blit(self.gameMap.spriteLayer.surface, self.gameMap.spriteLayer.surface.get_rect(), self.camera.view)

if __name__ == '__main__':
    gameClient = GameClient()
    run_pygame_loop(gameClient)