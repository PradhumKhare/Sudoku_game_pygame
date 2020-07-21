 # Sudoko Solver
from random import randint
import time
class game_main :
    def __init__(self):
        print("Welcome to the sudoko Solver")
        self.Check = [
            [0,0,0,4,0,0,0,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]
        self.generated =     [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
        self.newBoard = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
        import numpy as np
        self.board = np.asarray(self.generated)
        self.Board = np.asarray(self.generated)
        self.shed = np.asarray(self.generated)
        self.newBoard = np.asarray(self.newBoard)
        self.generated = np.asarray(self.generated)
        self.create_mat()
        self.board[:, :] = self.generated[:, :]
        self.start = time.time()



    def solve(self , i = 0,j = 0):

        if i == 9 and j == 0 :
            return 1
        end = time.time()
        # print(start - end)
        if(end - self.start) > 2 :
            return 0
        if self.board[i,j] == 0:
            for k in range (1,10):
                if (
                        k not in self.board[:,j] and
                        k not in self.board[i,:] and
                        k not in self.board[i//3 *3 :i//3 * 3 +3,j//3 * 3:j//3 * 3 +3]
                ):
                    self.board[i,j] = k

                    if j < 8 :
                       c =  self.solve(i,j+1)
                       if c == 1:
                           return 1
                       else:
                           self.board[i,j] = 0
                    else :
                       c = self.solve(i+1,0)
                       if c == 1:
                           return 1
                       else:
                           self.board[i,j] = 0


        else:
            if j < 8:
                c = self.solve(i, j + 1)
                if c == 1:
                    return 1
            else :
                c = self.solve(i + 1, 0)
                if c == 1:
                    return 1

        if self.board[i,j] == 0 :
            return 0

        return 0

    def create_mat(self):
            for p  in range(32):
                (i,j) = (randint(0,8),randint(0,8))
                if self.generated[i,j] == 0 :
                    for k in range(1,9):
                        if(
                                k not in self.generated[:, j] and
                                k not in self.generated[i, :] and
                                k not in self.generated[i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3]
                        ):
                            self.generated[i,j] = k


    def gen(self):
        c = self.solve()
        while c == 0 :
            # print("\n",board)
            self.generated[:,:] = self.newBoard[:,:]
            self.create_mat()
            self.board[:, :] = self.generated[:, :]
            self.start = time.time()
            c = self.solve()
            # print(c)
        else :
            self.Board[:,:] = self.generated[:,:]
            self.shed[:,:] =  self.generated[:,:]
            return [self.board,self.Board,self.shed]

# game = game_main()
# [board,Board,shed] = game.gen()
# print(board)
# print(Board)
# print(shed)