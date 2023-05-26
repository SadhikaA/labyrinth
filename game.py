from tile import Tile

class Game:

    def __init__(self, board, mover, players, cards):
        self.board = []
        self.mover = None
        self.players = []
        self.cards = []

    def start():
        # first make an empty board
        for i in range(1, 8):
            self.board.append([])
            for j in range(1, 8):
                self.board[i].append(Tile(True, "Tile", None, None, None, None, (i, j)))

        # place fixed non-moveable tiles
        # corner player tiles 
        self.board[1][1] = Tile(False, "Start", None, None, None, None, (1, 1))
        self.board[1][7] = Tile(False, "Goal", None, None, None, None, (1, 7))
        self.board[7][1] = Tile(False, "Goal", None, None, None, None, (7, 1))
        self.board[7][7] = Tile(False, "Goal", None, None, None, None, (7, 7))

        # generate set of moveable tiles

        # randomly place them on the board 


        # assign mover tile to last remaining moveable tile 