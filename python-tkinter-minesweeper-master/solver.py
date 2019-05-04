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
    if board[i+1][j] in range(1, 9):  # right
        unchicked += board[i+1][j]
    if board[i-1][j] in range(1, 9):  # left
        unchicked += board[i-1][j]
    if board[i][j+1] in range(1, 9):  # up
        unchicked += board[i][j+1]
    if board[i][j-1] in range(1, 9):  # down
        unchicked += board[i][j-1]
    if board[i+1][j+1] in range(1, 9):
        unchicked += board[i+1][j+1]
    if board[i-1][j-1] in range(1, 9):
        unchicked += board[i-1][j-1]
    if board[i+1][j-1] in range(1, 9):
        unchicked += board[i+1][j-1]
    if board[i-1][j+1] in range(1, 9):
        unchicked += board[i-1][j+1]
    if unchicked >= 8:
        board[i][j] = -1


def with_specific_number(board, i, j):
    count = 0
    list_of_cordinates = []
    if board[i+1][j] in range(1, 9) or board[i+1][j] == 12:  # right
        count += 1
    else:
        list_of_cordinates.append([i+1, j])
    if board[i-1][j] in range(1, 9) or board[i-1][j] == 12:  # left
        count += 1
    else:
        list_of_cordinates.append([i-1, j])
    if board[i][j+1] in range(1, 9) or board[i][j+1] == 12:  # up
        count += 1
    else:
        list_of_cordinates.append([i, j+1])
    if board[i][j-1] in range(1, 9) or board[i][j-1] == 12:  # down
        count += 1
    else:
        list_of_cordinates.append([i, j-1])
    if board[i+1][j+1] in range(1, 9) or board[i+1][j+1] == 12:  # up right
        count += 1
    else:
        list_of_cordinates.append([i+1, j+1])
    if board[i-1][j-1] in range(1, 9) or board[i-1][j-1] == 12:  # down left
        count += 1
    else:
        list_of_cordinates.append([i-1, j-1])
    if board[i+1][j-1] in range(1, 9) or board[i+1][j-1] == 12:  # up left
        count += 1
    else:
        list_of_cordinates.append([i+1, j-1])
    if board[i-1][j+1] in range(1, 9) or board[i-1][j+1] == 12:  # down right
        count += 1
    elif board[i-1][j+1] == 0:
        list_of_cordinates.append([i-1, j+1])
    if count == 8 - board[i][j]:
        for i in range(len(list_of_cordinates)):
            board[list_of_cordinates[i][0]][list_of_cordinates[i][1]] = -1


def open_last_1s(board, i, j):
    flags = 0
    tiles = 0
    list = [12,1,2,3,4,5,6,7,8]
    list_of_rem = []
    if board[i+1][j] in list:  # right
        tiles += board[i+1][j]
    elif board[i+1][j] == -1:  # right
        flags += 1
    elif board[i + 1][j] == 0:
        list_of_rem.append([i, j])
    if board[i-1][j] in list:  # left
        tiles += board[i-1][j]
    elif board[i-1][j] == -1:  # left
        flags += 1
    elif board[i - 1][j] == 0:
        list_of_rem.append([i, j])
    if board[i][j+1] in list:
        tiles += board[i][j+1]
    elif board[i][j+1] == -1:
        flags += 1
    elif board[i][j+1] == 0:
        list_of_rem.append([i, j])
    if board[i][j-1] in list:
        tiles += board[i][j-1]
    elif board[i][j-1] == -1:
        flags += 1
    elif board[i][j-1] == 0:
        list_of_rem.append([i, j])
    if board[i+1][j+1] in list:
        tiles += board[i+1][j+1]
    elif board[i+1][j+1] == -1:
        flags += 1
    elif board[i + 1][j+1] == 0:
        list_of_rem.append([i, j])
    if board[i-1][j-1] in list:
        tiles += board[i-1][j-1]
    elif board[i-1][j-1] == -1:
        flags += 1
    elif board[i - 1][j-1] == 0:
        list_of_rem.append([i, j])
    if board[i+1][j-1] in list:
        tiles += board[i+1][j-1]
    elif board[i+1][j-1] == -1:
        flags += 1
    elif board[i + 1][j-1] == 0:
        list_of_rem.append([i, j])
    if board[i-1][j+1] in list:
        tiles += board[i-1][j+1]
    elif board[i-1][j+1] == -1:
        flags += 1
    elif board[i - 1][j+1] == 0:
        list_of_rem.append([i, j])
    # if flags == board[i][j] and flags + tiles <= 7:
        # for i in range(len(list_of_rem)):
            # click board[list_of_rem[i][0]][list_of_rem[i][1]]




def make_flags(board):
    for i in range(0, 10):
        for j in range(0, 10):
            if i in range(1, 9) and j in range(1, 9) and board[i][j] > 0:
                with_specific_number(board, i, j)
            elif i in range(1, 9) and j in range(1, 9) and board[i][j] == 0:
                all_neighbours_are_1_or_more(board, i, j)


def printt(board):
    for i in range(10):
        print(board[i])


x = [    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 3, 1, 0, 0, 0, 0, 0, 0, 0],
         [12, 12, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
make_flags(x)
printt(x)
