import PIL

# import cv2 as cv
from tkinter import *
import numpy as np
import os
import time
import random
# from PIL import ImageGrab #For windows
# import tensorflow as tf
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


def areSame(A, B):
    n = len(A)
    for i in range(n):
        for j in range(n):
            for k in range(0, 3):
                # print(A[i][j][k])
                # print(B[i][j][k])
                if A[i][j][k] != B[i][j][k]:
                    return False
    return True


def makeLeftClick(i, j):
    pyautogui.click(x_pad + 10 + i * 22, 280 + 10 + j * 22, 1, 0, button='left')


def makeRightClick(i, j):
    pyautogui.click(x_pad + 10 + i * 22, 280 + 10 + j * 22, 1, 0, button='right')


'''
from tkinter import *

root = Tk()
label1 = Label(root, text="Name: ")
label1.grid(row=0, column=0)
name = Entry(root)
name.grid(row=0, column=1)
label2 = Label(root, text="Email: ")
label2.grid(row=1, column=0)
Email = Entry(root)
Email.grid(row=1, column=1)
option = Checkbutton(root, text="Remember me")
option.grid(columnspan=2)
root.mainloop()

'''


def all_neighbours_are_1_or_more(board, i, j):
    unchicked = 0
    list = []
    if board[i + 1][j] in range(1, 9):  # right
        unchicked += board[i + 1][j]
    if board[i - 1][j] in range(1, 9):  # left
        unchicked += board[i - 1][j]
    if board[i][j + 1] in range(1, 9):  # up
        unchicked += board[i][j + 1]
    if board[i][j - 1] in range(1, 9):  # down
        unchicked += board[i][j - 1]
    if board[i + 1][j + 1] in range(1, 9):
        unchicked += board[i + 1][j + 1]
    if board[i - 1][j - 1] in range(1, 9):
        unchicked += board[i - 1][j - 1]
    if board[i + 1][j - 1] in range(1, 9):
        unchicked += board[i + 1][j - 1]
    if board[i - 1][j + 1] in range(1, 9):
        unchicked += board[i - 1][j + 1]
    if unchicked >= 8:
        board[i][j] = -1
    list.append(i)
    list.append(j)
    return list


def with_specific_number(board, i, j):
    count = 0
    list_of_cordinates = []
    if board[i + 1][j] in range(1, 9) or board[i + 1][j] == 12:  # right
        count += 1
    else:
        list_of_cordinates.append([i + 1, j])
    if board[i - 1][j] in range(1, 9) or board[i - 1][j] == 12:  # left
        count += 1
    else:
        list_of_cordinates.append([i - 1, j])
    if board[i][j + 1] in range(1, 9) or board[i][j + 1] == 12:  # up
        count += 1
    else:
        list_of_cordinates.append([i, j + 1])
    if board[i][j - 1] in range(1, 9) or board[i][j - 1] == 12:  # down
        count += 1
    else:
        list_of_cordinates.append([i, j - 1])
    if board[i + 1][j + 1] in range(1, 9) or board[i + 1][j + 1] == 12:  # up right
        count += 1
    else:
        list_of_cordinates.append([i + 1, j + 1])
    if board[i - 1][j - 1] in range(1, 9) or board[i - 1][j - 1] == 12:  # down left
        count += 1
    else:
        list_of_cordinates.append([i - 1, j - 1])
    if board[i + 1][j - 1] in range(1, 9) or board[i + 1][j - 1] == 12:  # up left
        count += 1
    else:
        list_of_cordinates.append([i + 1, j - 1])
    if board[i - 1][j + 1] in range(1, 9) or board[i - 1][j + 1] == 12:  # down right
        count += 1
    elif board[i - 1][j + 1] == 0:
        list_of_cordinates.append([i - 1, j + 1])
    print(i, "-", "-", j, "-", count)
    if count == 7:
        return list_of_cordinates


def open_last_1s(board, i, j):
    flags = 0
    tiles = 0
    list = [12, 1, 2, 3, 4, 5, 6, 7, 8]
    list_of_rem = []
    if board[i + 1][j] in list:  # right
        tiles += board[i + 1][j]
    elif board[i + 1][j] == -1:  # right
        flags += 1
    elif board[i + 1][j] == 0:
        list_of_rem.append([i, j])
    if board[i - 1][j] in list:  # left
        tiles += board[i - 1][j]
    elif board[i - 1][j] == -1:  # left
        flags += 1
    elif board[i - 1][j] == 0:
        list_of_rem.append([i, j])
    if board[i][j + 1] in list:
        tiles += board[i][j + 1]
    elif board[i][j + 1] == -1:
        flags += 1
    elif board[i][j + 1] == 0:
        list_of_rem.append([i, j])
    if board[i][j - 1] in list:
        tiles += board[i][j - 1]
    elif board[i][j - 1] == -1:
        flags += 1
    elif board[i][j - 1] == 0:
        list_of_rem.append([i, j])
    if board[i + 1][j + 1] in list:
        tiles += board[i + 1][j + 1]
    elif board[i + 1][j + 1] == -1:
        flags += 1
    elif board[i + 1][j + 1] == 0:
        list_of_rem.append([i, j])
    if board[i - 1][j - 1] in list:
        tiles += board[i - 1][j - 1]
    elif board[i - 1][j - 1] == -1:
        flags += 1
    elif board[i - 1][j - 1] == 0:
        list_of_rem.append([i, j])
    if board[i + 1][j - 1] in list:
        tiles += board[i + 1][j - 1]
    elif board[i + 1][j - 1] == -1:
        flags += 1
    elif board[i + 1][j - 1] == 0:
        list_of_rem.append([i, j])
    if board[i - 1][j + 1] in list:
        tiles += board[i - 1][j + 1]
    elif board[i - 1][j + 1] == -1:
        flags += 1
    elif board[i - 1][j + 1] == 0:
        list_of_rem.append([i, j])
    # if flags == board[i][j] and flags + tiles <= 7:
    # for i in range(len(list_of_rem)):
    # click board[list_of_rem[i][0]][list_of_rem[i][1]]


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
    # list = []
    im = ImageGrab.grab(box)
    # path = os.getcwd() + '/full_snap__' + str(int(time.time())) + '.png'
    # im.save(path)
    im2 = np.asanyarray(im)
    # Board: tile0: start(2, 1) - end(18, 17)
    # Between the tiles (6, 6)
    # img = PIL.Image.open("images/original/tile_plain.png")
    # arr = np.asanyarray(img)
    # if areSame(arr, im2):
    #     print(True)

    ###############################################################################################################
    """
        0: unclicked/plain
        1 -> 8: 1 to 8
        9: clicked
        10: Flag
        11: mine
        12: wrong tile
    """
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
    # for i in range(0, 10):
    #     ls = []
    #     for j in range(0, 10):
    #         bx = (x_pad + 2 + j * 22, y_pad + 2 + i * 22, x_pad + 2 + 16 + j * 22, y_pad + 2 + 16 + i * 22)
    #         im = ImageGrab.grab(bx)
    #         im2 = np.asanyarray(im)
    #         tile = -10
    #         for l in range(1, 9):
    #             img = PIL.Image.open("images/original/tile_" + str(l) + ".png")
    #             arr = np.asanyarray(img)
    #             if areSame(arr, im2):
    #                 tile = l
    #                 ls.append(tile)
    #                 break
    #         if tile == -10:
    #             img = PIL.Image.open("images/original/tile_flag.png")
    #             arr = np.asanyarray(img)
    #             if areSame(arr, im2):
    #                 tile = 11
    #             img = PIL.Image.open("images/original/tile_clicked.png")
    #             arr = np.asanyarray(img)
    #             if areSame(arr, im2):
    #                 tile = 12
    #             img = PIL.Image.open("images/original/tile_plain.png")
    #             arr = np.asanyarray(img)
    #             if areSame(arr, im2):
    #                 tile = 0
    #             img = PIL.Image.open("images/original/tile_mine.png")
    #             arr = np.asanyarray(img)
    #             if areSame(arr, im2):
    #                 tile = 9
    #             img = PIL.Image.open("images/original/tile_wrong.png")
    #             arr = np.asanyarray(img)
    #             if areSame(arr, im2):
    #                 tile = 10
    #             ls.append(tile)
    #     board.append(ls)
    # print(board)
    # return board


################################################################################################

# ls.append((arr == im2).all(axis=1))
# r = np.array(ls)
# print(areSame(im2, arr))
# c = ls.count('False')
# print(c)
# print((arr == im2).all(axis=1))
# print(j)
# break
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
# img = PIL.Image.open("images/original/tile_" + str(1) + ".png")


#     im = ImageGrab.Image
# arr = np.asanyarray(img)
# for i in range(0, len(arr)):
# print(arr)
# print()
# print(len(im2))
# for i in range(0,100):
#     # list = []
#     for j in range(0, 21):
#         for k in range(0, 21):
#             list.append(im2[i])
#         print(list[i])
#     print(i)


# for i in range(0, 216):
#     for j in range(0, 216):
#         print(im2[i][j])
#         if j == 21:
#             print()
#     print()


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

# for m in range(0, 10):
#     x = random.randint(0, 9)
#     y = random.randint(0, 9)
#     if m == 0:
#         makeLeftClick(y, x)
#     for i in range(0, 10):
#         for j in range(0, 10):
#             board = screenGrab()
#             if i in range(1, 9) and j in range(1, 9) and board[i][j] > 0:
#                list = with_specific_number(board, i, j)
#                for k in range(len(list)):
#                    makeRightClick(list[k][1], list[k][0])
#             elif i in range(1, 9) and j in range(1, 9) and board[i][j] == 0:
#                list = all_neighbours_are_1_or_more(board, i, j)
#                makeRightClick(int(list[1]),int(list[0]))
#             else:
#                 x = random.randint(0, 9)
#                 y = random.randint(0, 9)
#                 makeLeftClick(y, x)
