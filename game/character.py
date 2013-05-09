"""
Character.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""
import pygame

from game.constants import *

class Character(object):
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
    
        self.speed = 1
        self.lookingDirection = DOWN
        self.characterClass = DEFAULT
        self.health = 100
    
        self.sprite = None
        self.rect = None
    
    def getSprite(self):
        return self.sprite
    
    def doRect(self, xPos, yPos, width, height):
        rect = pygame.rect.Rect(xPos, yPos, width, height)
        return rect
        
    def getRect(self):
        return self.rect
    
    def move(self, gameClient, direction):
        if direction == RIGHT:
            self.xPos += 3
        elif direction == LEFT:
            self.xPos -= 3
        elif direction == UP:
            self.yPos -= 3
        elif direction == DOWN:
            self.yPos += 3
        if self.xPos < 0:
            self.xPos = 0
        if self.yPos < 0:
            self.yPos = 0
        if self.xPos > gameClient.viewManager.getWidth()-32:
            self.xPos = gameClient.viewManager.getWidth()-32
        if self.yPos > gameClient.viewManager.getHeight()-64:
            self.yPos = gameClient.viewManager.getHeight()-64
        self.rect = Character.doRect(self, self.xPos, self.yPos, 32, 64)
    
class Player(Character):
    def __init__(self, username):
        
        super(Player, self).__init__()
        
        self.username = username
        
        self.xPos = 64
        self.yPos = 64
        
        self.characterClass = PLAYER
        
        self.level = 1
        self.experience = 0
        
        self.spriteFilename = 'data/sprites/char.bmp'
                
        self.sprite = pygame.image.load(self.spriteFilename).convert()
        
        self.rect = Character.doRect(self, self.xPos, self.yPos, 32, 64)
        
        self.weapon = None
    
    def attack(self, type):
        pass
    
    def use(self, item):
        pass
        
class NPC(Character):
    def __init__(self):
        self.characterClass = NPC
        