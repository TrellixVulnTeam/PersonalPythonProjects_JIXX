import numpy as np

rows = 6
columns = 7
default = " "
symbol = "O"
turn = 0

board_array = np.array(
    [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]])


def insert(column, board=board_array):
    if column >= columns:
        print("The board isn't that big.")
        return
    if column < 0:
        print("Negative columns don't exist.")
        return
    if board[0, column] != default:
        print("Column full you idiot. Do you have eyes?")
        return
    for row in range(rows - 1):
        if board[rows - 1, column] == default:
            board[5, column] = symbol
            return
        if board[row + 1, column] != default:
            board[row, column] = symbol
            return


def scanForWin(symbolToLookFor, board = board_array):
    for column in range(columns):
        count = 0
        for row in range(rows):
            if board[row, column] == symbolToLookFor:
                count = count + 1
                if count == 4:
                    #print("\n\n\n\n\n WINNER \n\n\n\n\n")
                    return True
            if board[row, column] != symbolToLookFor:
                count = 0

    for row in range(rows):
        count = 0
        for column in range(columns):
            if board[row, column] == symbolToLookFor:
                count = count + 1
                if count == 4:
                    #print("\n\n\n\n\n WINNER \n\n\n\n\n")
                    return True
            if board[row, column] != symbolToLookFor:
                count = 0

    for row in range(rows):
        count = 0
        for column in range(columns):
            if board[row, column] == symbolToLookFor:
                count = 1
                if row >= 3 and column <= columns - 4:
                    for x in range(3):
                        x = x + 1
                        if board[row - x, column + x] == symbolToLookFor:
                            count = count + 1
                            if count == 4:
                                #print("\n\n\n\n\n WINNER \n\n\n\n\n")
                                return True
                        else:
                            count = 1
                            break
                if row <= rows - 4 and column <= columns - 4:
                    for x in range(3):
                        x = x + 1
                        if board_[row + x, column + x] == symbolToLookFor:
                            count = count + 1
                            if count == 4:
                                #print("\n\n\n\n\n WINNER \n\n\n\n\n")
                                return True
                        else:
                            count = 1
                            break
                if row >= 3 and column >= 3:
                    for x in range(3):
                        x = x + 1
                        if board[row - x, column - x] == symbolToLookFor:
                            count = count + 1
                            if count == 4:
                                #print("\n\n\n\n\n WINNER \n\n\n\n\n")
                                return True
                        else:
                            count = 1
                            break
                if row <= rows - 4 and column >= 3:
                    for x in range(3):
                        x = x + 1
                        if board[row + x, column - x] == symbolToLookFor:
                            count = count + 1
                            if count == 4:
                                #print("\n\n\n\n\n WINNER \n\n\n\n\n")
                                return True
                        else:
                            count = 1
                            break

while True:
    turn = turn + 1
    if (turn % 2) == 0:
        symbol = "O"
    else:
        symbol = "X"
    print(board_array)
    column = int(input("Select a column to insert an " + symbol + ". (1-7)"))
    column = column - 1
    insert(column)
    if scanForWin(symbol):
        break

print("\n\n\n\n\n THE WINNER IS " + symbol + "! \n\n\n")
print(board_array)


def AI():
    test_board = board_array
    for column in range(columns):
        insert(column, test_board)
        if




