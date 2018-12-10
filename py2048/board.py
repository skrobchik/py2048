import random
import pyglet
import math

class Board(object):
    def __init__(self, size=4, name='board'):
        self.size = size
        self.tiles = []
        self.name = name
        self.window = pyglet.window.Window(width = 400,
                                           height = 400,
                                           caption = self.name)
        self.tileWidth = math.trunc(self.window.width/4)
        self.tileHeight = math.trunc(self.window.height/4)
        self.tileCount = self.size * self.size

    def initializeTiles(self):
        self.tiles = []
        for i in range(0, self.tileCount):
            self.tiles.append(0)

    def spawnTile(self):
        zeroIndexes = []
        for i in range(0, self.tileCount):
            if self.tiles[i] == 0:
                zeroIndexes.append(i)

        if len(zeroIndexes) == 0:
            return

        tilePlace = random.randint(0, len(zeroIndexes)-1)
        tileType = random.randint(1,2)

        self.tiles[zeroIndexes[tilePlace]] = tileType * 2

    def tileRow(self, tileIndex):
        return math.trunc(tileIndex/self.size)

    def moveHorizontally(self, org, adj):
        if(self.tileRow(org) == self.tileRow(adj)):
            if(self.tiles[org] == self.tiles[adj]):
                self.tiles[adj] *= 2
                self.tiles[org] = 0
            elif (self.tiles[adj] == 0):
                self.tiles[adj] = self.tiles[org]
                self.tiles[org] = 0

    def moveRight(self):
        for j in range(0, self.tileCount):
            i = self.tileCount - j - 1
            self.moveHorizontally(i, i+1)

    def moveLeft(self):
        for i in range(0, self.tileCount):
            self.moveHorizontally(i, i-1)

    def draw(self):
        self.window.clear()
        for i in range(0, self.tileCount):
            y = self.tileRow(i)
            x = i - y * self.size
            y *= self.tileHeight
            x *= self.tileWidth
            color = math.trunc(255 - self.tiles[i] * 255/8)
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, 
                                 ('v2i', (x, y,
                                          x, y+self.tileHeight,
                                          x+self.tileWidth, y+self.tileHeight,
                                          x+self.tileWidth, y)),
                                 ('c3B', (0, color, color,
                                          color, color, color,
                                          color, color, color,
                                          color, color, color))
                             )

