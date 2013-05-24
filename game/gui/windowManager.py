"""
interface.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

import pygame

class WindowManager(object):
    def __init__(self):
        self.width = 640
        self.height = 640
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