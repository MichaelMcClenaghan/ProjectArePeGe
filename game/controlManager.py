"""
controlManager.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

from game.constants import *
from game.character import *
from game.characterManager import *
from game.tileEngine.map.gameMap import *


class ControlManager(object):
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        
    def run(self, gameClient):
        if self.left:
            gameClient.characterManager.player.move(gameClient, LEFT)
        if self.right:
            gameClient.characterManager.player.move(gameClient, RIGHT)
        if self.up:
            gameClient.characterManager.player.move(gameClient, UP)
        if self.down:
            gameClient.characterManager.player.move(gameClient, DOWN)
            
    def processKeys(self, gameClient, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                gameClient.gameMap.foregroundLayer.getTile(5,6).setType
                
            elif event.key == pygame.K_o:
                print gameClient.clock.get_fps()

            elif event.key == pygame.K_p:
                print gameClient.camera.centerOnPoint(0,0)
                
            elif event.key == pygame.K_w:
                gameClient.controlManager.up = True
            elif event.key == pygame.K_a:
                gameClient.controlManager.left = True
            elif event.key == pygame.K_s:
                gameClient.controlManager.down = True
            elif event.key == pygame.K_d:
                gameClient.controlManager.right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                gameClient.controlManager.up = False
            elif event.key == pygame.K_a:
                gameClient.controlManager.left = False
            elif event.key == pygame.K_s:
                gameClient.controlManager.down = False
            elif event.key == pygame.K_d:
                gameClient.controlManager.right = False