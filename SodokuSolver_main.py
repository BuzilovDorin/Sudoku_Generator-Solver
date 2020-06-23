import random, time

grid2 = [5, 3, 0, 0, 7, 0, 0, 0, 0], \
       [6, 0, 0, 1, 9, 5, 0, 0, 0], \
       [0, 9, 8, 0, 0, 0, 0, 6, 0], \
       [8, 0, 0, 0, 6, 0, 0, 0, 3], \
       [4, 0, 0, 8, 0, 3, 0, 0, 1], \
       [7, 0, 0, 0, 2, 0, 0, 0, 6], \
       [0, 6, 0, 0, 0, 0, 2, 8, 0], \
       [0, 0, 0, 4, 1, 9, 0, 0, 5], \
       [0, 0, 0, 0, 8, 0, 0, 0, 0]
# Settings
solutionNo = 0

#Print a gui for SUDOKU board in terminal ---------------------
def printBoard(board):
       print("\n             SUDOKU                     \n")
       for i in range(len(board)):
              if i % 3 == 0 and i != 0:
                     print("----------------------------------")

              for j in range(len(board[0])):
                     if j % 3 == 0 and j != 0:
                            print (" | ", end=" ")

                     if j == 8:
                            print(board[i][j])
                     else:
                            print(str(board[i][j]) + " ", end=" ")

#Puzzle Generator ------------------------------------
def generateSudokuBoard():
       grid = [[0 for x in range(9)] for y in range(9)]
       seedRandomSudoku(grid)

def seedRandomSudoku(board):
       x, y = 0, 0
       for i in range(9):
              xSq , ySq = 3*(x//3), 3*(y//3)
              randSquare9 = random.sample(list(range(1,10)), 9)
              index = 0
              for xrow in range(xSq, xSq +3):
                     for ycol in range(ySq, ySq +3):
                            board[xrow][ycol] = randSquare9[index]
                            index += 1
              if y < 6:
                     y += 3
              else:
                     y = 0
                     x += 3
              printBoard(board)
       shrinkingBoxAlgo(board)

def boxAdjacentCellSwap(board, x, y, registerednumbers):
       xSq, ySq = 3 * (x // 3), 3 * (y // 3)
       for xrow in range(xSq, xSq + 3):
              for ycol in range(ySq, ySq + 3):
                     count = 0
                     count += 1
                     if xrow <= x and ycol <= y:
                            pass
                     elif xrow > x:
                            if board[xrow][ycol] not in registerednumbers:
                                   board[x][y], board[xrow][ycol] = board[xrow][ycol], board[x][y]
                                   return board[x][y]



def shrinkingBoxAlgo(board):
       registeredNumbs = [[0 for x in range(9)] for y in range(9)]
       diag = -1
       for sqCheck in range(9):
              diag += 1
              for ycol in range(9):
                     if board[diag][ycol] not in registeredNumbs[diag]:
                            registeredNumbs[diag][ycol] = board[diag][ycol]
                            print(registeredNumbs[diag])
                            print("No. Registered-- Num:{} ,Cell:[{}][{}]".format(board[diag][ycol], diag, ycol))
                     else:
                            print("\n            Negative found ---- Num:{} ,Cell:[{}][{}]\n".format(board[diag][ycol], diag, ycol))
                            registeredNumbs[diag][ycol] = boxAdjacentCellSwap(board, diag, ycol, registeredNumbs[diag])
                            print(registeredNumbs[diag])
              printBoard(board)
              input("next?")

#Rules --------------------------
def checkRow(board, y, n):
       for i in range(0, 9):
              if board[y][i] == n:
                     return False
       return True

def checkColumn(board, x, n):
       for i in range(0, 9):
              if board[i][x] == n:
                     return False
       return True

def checkSquare(board, y, x, n):
       squareX = (x // 3) * 3
       squareY = (y // 3) * 3
       for iy in range(3):
              for ix in range(3):
                     if board[squareY + iy][squareX + ix] == n:
                            return False
       return True

def checkPossibleNum(board, y, x, n):
       if checkRow(board, y, n):
              if checkColumn(board, x, n):
                     if checkSquare(board, y, x, n):
                            return True


#Recursive & Backtracking AutoSolver ------------------------------------
def autoSolveBacktrack(board):
       for y in range(9):
              for x in range(9):
                     if board[y][x] == 0:
                            for n in range(1, 10):
                                   if checkPossibleNum(board, y, x, n):
                                          board[y][x] = n
                                          #time.sleep(0.6)
                                          autoSolveBacktrack(board)
                                          board[y][x] = 0
                            return
       printBoard(board)
       #input ("Solution:" + str(solutionNo) + "\n more solutions?")

#autoSolveBacktrack(grid2)
generateSudokuBoard()