from board import Board
import pyglet
from pyglet.window import key
import math

board = Board()
board.tiles = [0, 0, 0, 16,
               0, 0, 0, 4,
               0, 0, 0, 2,
               0, 0, 0, 2]

clock = pyglet.clock.get_default()

@board.window.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        board.moveTiles('right')
    if symbol == key.LEFT:
        board.moveTiles('left')
    if symbol == key.UP:
        board.moveTiles('up')
    if symbol == key.DOWN:
        board.moveTiles('down')
    return

@board.window.event
def on_draw():
    board.draw()

pyglet.app.run()