import PIL
from tkinter import *
import numpy as np
import os
import time
import random
# from PIL import ImageGrab #For windows
# import tensorflow as tf
import pyscreenshot as ImageGrab
import pyautogui

# Globals
# You will need to make these suitable with your screen
# ------------------
x_pad = 564
y_pad = 280

def areSame(A, B):
    n = len(A)
    for i in range(n):
        for j in range(n):
            for k in range(0, 3):
                if A[i][j][k] != B[i][j][k]:
                    return False
    return True


def makeLeftClick(i, j):
    pyautogui.click(x_pad + 10 + i * 22, 280 + 10 + j * 22, 1, 0, button='left')


def makeRightClick(i, j):
    pyautogui.click(x_pad + 10 + i * 22, 280 + 10 + j * 22, 1, 0, button='right')

def readTiles():
    imgs_pixels = []
    """
        0: unclicked/plain
        1 -> 8: 1 to 8
        9: clicked
        10: Flag
        11: mine
        12: wrong tile
    """
    for l in range(13):
        imgs_pixels.append(np.asanyarray(PIL.Image.open("images/original/tile_" + str(l) + ".png")))

    return imgs_pixels


TilesAsArrayOfPixels = readTiles()
noOfPossibleTiles = len(TilesAsArrayOfPixels)


def screenGrab():
    # End : 833, 498
    box = (x_pad + 2 + 0 * 22, y_pad + 2 + 0 * 22, x_pad + 2 + 16 + 0 * 22, y_pad + 2 + 16 + 0 * 22)
    im = ImageGrab.grab(box)
    # path = os.getcwd() + '/t__' + str(int(time.time())) + '.png'
    # im.save(path)
    im2 = np.asanyarray(im)
    # Board: tile0: start(2, 1) - end(18, 17)
    # Between the tiles (6, 6)
    board = []
    # Read the all board tiles one by one to know what is it contain
    for i in range(0, 10):
        ls = []
        for j in range(0, 10):
            tile = -1
            bx = (x_pad + 2 + j * 22, y_pad + 2 + i * 22, x_pad + 2 + 16 + j * 22, y_pad + 2 + 16 + i * 22)
            im = ImageGrab.grab(bx)
            im2 = np.asanyarray(im)
            # Go ahead and get the value of each tile, comparing it with all possible tiles
            for l in range(noOfPossibleTiles):
                if (areSame(im2, TilesAsArrayOfPixels[l])):
                    tile = l
                    break
            ls.append(tile)
        board.append(ls)

    print(board)
    return board

def find(searchList, elem):
    for i in range(0, len(searchList)):
        if elem in searchList[i]:
            return True
    return False


"""START POINT"""
while True:
    board = screenGrab()
    ## End of the game!
    if find(board, -1):
        print("End of the game :/")
        break

    x = random.randint(0, 9)
    y = random.randint(0, 9)

    while board[x][y] != 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    makeLeftClick(y, x)
