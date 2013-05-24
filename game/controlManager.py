"""
controlManager.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

from game.constants import *
from game.character import *
from game.characterManager import *
from game.tileEngine.map.gameMap import *
import random
from math import *


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
        print gameClient.clock.get_fps()

        if event.type == pygame.KEYDOWN:
                
            if event.key == pygame.K_o:
                print gameClient.clock.get_fps()

            elif event.key == pygame.K_SPACE:
                gameClient.camera.mode = abs(gameClient.camera.mode-1)

            elif event.key == pygame.K_p:
                gameClient.gameMap.backgroundLayer.getTile(random.randint(0,20),random.randint(0,20)).setType('gravel')
                
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