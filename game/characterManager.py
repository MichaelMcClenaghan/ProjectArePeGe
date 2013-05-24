"""
characterManager.py

Created by Michael McClenaghan on 2012-05-29.
Copyright (c) 2012 Micmac Creations. All rights reserved.
"""

from game.constants import *
from game.character import *

class CharacterManager(object):
    def __init__(self, gameClient):
        self.player = Player("Player")
        self.gameClient = gameClient
        
    def blitPlayer(self, gameClient):
        self.gameClient.gameMap.spriteLayer.blitSprite(self.player)