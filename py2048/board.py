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
        self.tileColors = {
            0: (220, 220, 220),
            2: (240, 240, 230),
            4: (225, 225, 200),
            8: (240, 200, 155),
            16: (240, 170, 90),
            32: (240, 160, 130),
            64: (215, 100, 60),
            128: (250, 245, 150),
            256: (230, 230, 100),
            512: (205, 200, 50),
            1024: (185, 180, 30),
            2048: (225, 220, 20)
            }
        self.initializeTiles()

    def initializeTiles(self):
        self.tiles = []
        for i in range(0, self.tileCount):
            self.tiles.append(0)
        return

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
        return

    def tileInBound(self, tileIndex):
        if (tileIndex >= 0 and tileIndex < self.tileCount):
            return True
        return False
    
    def tileRow(self, tileIndex):
        if (self.tileInBound(tileIndex)):
            return math.trunc(tileIndex/self.size)
        return None

    def adjacentTile(self, tileIndex, direction):
        horizontal = False
        vertical = False
        adjacent = None
        if (direction == 'right'):
            adjacent = tileIndex + 1
            horizontal = True
        if (direction == 'left'):
            adjacent = tileIndex - 1
            horizontal = True
        if (direction == 'up'):
            adjacent = tileIndex + self.size
            vertical = True
        if (direction == 'down'):
            adjacent = tileIndex - self.size
            vertical = True
        if (horizontal and self.tileRow(tileIndex) != self.tileRow(adjacent)):
            return None
        if (vertical and (not self.tileInBound(tileIndex) or not self.tileInBound(adjacent))):
            return None
        return adjacent

    def moveTile(self, tileIndex, direction):
        adjacent = self.adjacentTile(tileIndex, direction)
        if(not self.tileInBound(tileIndex)):
            return
        if(self.tiles[tileIndex] == 0):
            return
        if(adjacent is None):
            return
        if(self.tiles[tileIndex] == self.tiles[adjacent]):
            self.tiles[adjacent] *= 2
            self.tiles[tileIndex] = 0
        elif (self.tiles[adjacent] == 0):
            self.tiles[adjacent] = self.tiles[tileIndex]
            self.tiles[tileIndex] = 0
            self.moveTile(adjacent, direction)
        return

    def moveTiles(self, direction):
        previousTiles = self.tiles.copy()
        normal = False
        reverse = False
        if(direction == 'right' or direction == 'up'):
            reverse = True
        if(direction == 'left' or direction == 'down'):
            normal = True
        for i in range(0, self.tileCount):
            j = self.tileCount - i - 1
            if(normal):
                self.moveTile(i, direction)
            if(reverse):
                self.moveTile(j, direction)
        if previousTiles != self.tiles:
            self.spawnTile()
        return

    def tileColor(self, tileValue):
        color = self.tileColors.get(tileValue, (0,0,0))
        return color

    def minimax(self):
        pass

    def draw(self):
        self.window.clear()
        for i in range(0, self.tileCount):
            y = self.tileRow(i)
            x = i - y * self.size
            y *= self.tileHeight
            x *= self.tileWidth
            color = self.tileColor(self.tiles[i])
            pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, 
                                 ('v2i', (x, y,
                                          x, y+self.tileHeight,
                                          x+self.tileWidth, y+self.tileHeight,
                                          x+self.tileWidth, y)),
                                 ('c3B', (color[0], color[1], color[2],
                                          color[0], color[1], color[2],
                                          color[0], color[1], color[2],
                                          color[0], color[1], color[2]))
                             )
        return
