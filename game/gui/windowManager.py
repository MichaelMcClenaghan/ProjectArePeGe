"""
interface.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

import pygame

class WindowManager(object):
    def __init__(self):

        self.width = 1920
        self.height = 1080
        self.caption = "Project ArePeGe"
        
    def setCaption(self, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
        
    def getCaption(self):
        return self.caption
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def getResolution(self):
        return (self.width, self.height)

    def fullscreen(self):
        fullSize = pygame.display.list_modes()[0]
        self.width = fullSize[0]
        self.height = fullSize[1]
        pygame.display.set_mode(fullSize, pygame.FULLSCREEN)