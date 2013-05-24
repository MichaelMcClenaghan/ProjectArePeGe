"""
Character.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""
import pygame

from game.constants import *

class Camera(object):

    def __init__(self, gameClient): 
        self.originX = 0
        self.originY = 0

        self.mode = 1

        self.gameClient = gameClient

        self.view = pygame.Rect(0, 0, gameClient.windowManager.getWidth(), gameClient.windowManager.getHeight())

        self.zoomLevel = 1

    def updateView(self):
        if self.mode == 0:
            if pygame.mouse.get_pos()[0] < 50:
                self.moveRelative(-5,0)
                #movement = pygame.mouse.get_rel()
                #self.moveRelative(-movement[0], -movement[1])
            if pygame.mouse.get_pos()[1] < 50:
                self.moveRelative(0,-5)
            if pygame.mouse.get_pos()[0] > self.gameClient.windowManager.getWidth() - 50:
                self.moveRelative(5,0)
            if pygame.mouse.get_pos()[1] > self.gameClient.windowManager.getHeight() - 50:
                self.moveRelative(0,5)
        elif self.mode == 1:
            self.centerOnPoint(self.gameClient.characterManager.player.xPos, self.gameClient.characterManager.player.yPos)

        self.originX = self.view.left
        self.originY = self.view.top 

    def centerOnPoint(self, xPos, yPos):
        self.view.center = (xPos, yPos)

    
    def moveRelative(self, xAmount, yAmount):
        self.view.move_ip(xAmount, yAmount)