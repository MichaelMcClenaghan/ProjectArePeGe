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

        self.view = pygame.Rect(0, 0, gameClient.windowManager.getWidth(), gameClient.windowManager.getHeight())

        self.zoomLevel = 1

    def updateView(self):
        pass
        #self.view.move_ip(1, 1)

    def centerOnPoint(self, xPos, yPos):
        self.view.center = (xPos, yPos)
        self.originX = self.view.left
        self.originY = self.view.top