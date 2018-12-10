from board import Board
import pyglet
import math

board = Board()
board.initializeTiles()

clock = pyglet.clock.get_default()

def callback(dt):
    board.spawnTile()
    board.moveRight()

clock.schedule_interval(callback, 1)

@board.window.event
def on_draw():
    board.draw()

pyglet.app.run()