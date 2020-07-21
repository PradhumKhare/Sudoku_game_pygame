class NewBoard :
    def __init__(self):
        newBoard = [
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
        self.newBoard = np.asarray(newBoard)
        self.Board = np.asarray(newBoard)
        self.shed = np.asarray(newBoard)
        self.board = np.asarray(newBoard)

    def plain_board(self):
        return [self.newBoard,self.Board,self.shed,self.board]