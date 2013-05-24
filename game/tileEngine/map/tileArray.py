from game.constants import *
from game.tileEngine.tileset import *
from game.tileEngine.map.mapTile import *

class TileArray(object):
    def __init__(self, gameClient, mapWidth, mapHeight, tilesetNumber):
        
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.gameClient = gameClient
        
        self.tilesize = TILESIZE
        self.tilesetFile = 'game/data/tilesets/' + tilesetNumber + '/' + tilesetNumber + '.bmp'
        self.tileset = Tileset(gameClient, self.tilesetFile)
        self.tileArray = self.doTileArray(gameClient, self.mapWidth, self.mapHeight)
        
    def doTileArray(self, gameClient, mapWidth, mapHeight):
        tileArray = []

        for col in range(mapWidth):
            tileArray.append([])
            for row in range(mapHeight):
                tileArray[col].append(MapTile(self, TILESIZE*col, TILESIZE*row))
                if row == 5:
                    #tileArray[col][row].setType('gravel')
                    pass

        return tileArray
        
    def getTileArray(self):
        return self.tileArray
