import PIL

import minesweeper
#import cv2 as cv
from tkinter import *
import numpy as np
import os
import time
#from PIL import ImageGrab #For windows
#import tensorflow as tf
import pyscreenshot as ImageGrab
import pyautogui

# A simple Python3 program to find
# maximum score that
# maximizing player can get
"""
import math


def minimax(curDepth, nodeIndex,
            maxTurn, scores,
            targetDepth):
    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                           False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                           True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           True, scores, targetDepth))

    # Driver code


scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end="")
print(minimax(0, 0, True, scores, treeDepth))
"""

# Globals
# ------------------
x_pad = 564
y_pad = 280

def screenGrab():
    # End : 833, 498
    box = (x_pad, y_pad, x_pad + 218, y_pad + 218)
    # list = []
    im = ImageGrab.grab(box)
    path = os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png'
    im.save(path)
    im2 = np.asanyarray(im)
    #Board: tile0: start(2, 1) - end(18, 17)
    #Between the tiles (6, 6)
    for i in range(0, 10):
        for j in range(0, 10):
            bx = (x_pad + 2 + i * 22, y_pad + 2 + j * 22, x_pad + 2 + 16 + i * 22, y_pad + 2 + 16 + j * 22)
            im = ImageGrab.grab(bx)
            # time.sleep(.01)
            # path = os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png'
            # im.save(path)
    # ll =[]
    # for m in range(0, 16):
    #     for n in range(0, 16):
    #         ll.append()
    # 100 2D arr, each 21 * 21
    # arrayImageSize: 216, No. of tiles : 100
    # 216 / 100 = 2.16 ~= 2 for each tile
    # for x in range(1, 9):
    img = PIL.Image.open("images/original/tile_" + str(1) + ".png")
#     im = ImageGrab.Image
    #arr = np.asanyarray(img)
    # for i in range(0, len(arr)):
    #print(arr)
    # print()
    # print(len(im2))
    # for i in range(0,100):
    #     # list = []
    #     for j in range(0, 21):
    #         for k in range(0, 21):
    #             list.append(im2[i])
    #         print(list[i])
    #     print(i)


    for i in range(0, 216):
        for j in range(0, 218):
            print(im2[i][j])
            if j == 21:
                print()
        print()

# for i in range(0, 10):
screenGrab()
# pyautogui.click(570 + i * 22, 290 + i * 22, 1, 0, button='right')
# time.sleep(.2)