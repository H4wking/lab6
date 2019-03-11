class ChessBoard:
    def __init__(self, width, height, num_players):
        self.width = width
        self.height = height
        self.num_players = num_players
        self.board = self.create_board()
        # self.all_figures = [ChessFigure("W", "B", "Tour", [0, 0]), ChessFigure("B", "B", "Hourse", [0, 1]), ChessFigure("W", "B", "Elephant", [0, 2]), ChessFigure("B", "B", "Queen", [0, 3]), ChessFigure("W", "B", "King", [0, 4]), ChessFigure("B", "B", "Elephant", [0, 5]), ChessFigure("W", "B", "Hourse", [0, 6]), ChessFigure("B", "B", "Tour", [0, 7])]
        # for i in range(self.size):
        #     if i % 2 == 0:
        #         self.all_figures.append(ChessFigure("B", "B", "Peshka", [1, i]))
        #     else:
        #         self.all_figures.append(ChessFigure("W", "B", "Peska", [1, i]))

    def create_board(self):
        board = [[0 for j in range(self.width)] for i in range(self.height)]
        for k in range(self.height):
            for l in range(self.width):
                if (k + l) % 2 == 0:
                    board[k][l] = '⬜️'
                else:
                    board[k][l] = '⬛️'
        return board

    # def put_figure(self, figure):
    #     # self.board[figure.figure_coordinates[0]][figure.figure_coordinates[1]] = figure !!!!! треба так)
    #     self.board[figure.figure_coordinates[0]][figure.figure_coordinates[1]] = figure.show_figure()
    #
    # def put_all_figures(self):
    #     for figs in self.all_figures:
    #         self.put_figure(figs)


class ChessFigure:
    def __init__(self, square_color, figure_color, figure_type, figure_coordinates):
        self.square_color = square_color
        self.figure_color = figure_color
        self.figure_type = figure_type
        self.figure_coordinates = figure_coordinates

    def show_figure(self):
        return self.figure_color + " " + self.figure_type[0]


class Chess:
    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.chess_figures = [ChessFigure("W", "B", "Tour", [0, 0]), ChessFigure("B", "B", "Hourse", [0, 1]),
                            ChessFigure("W", "B", "Elephant", [0, 2]), ChessFigure("B", "B", "Queen", [0, 3]),
                            ChessFigure("W", "B", "King", [0, 4]), ChessFigure("B", "B", "Elephant", [0, 5]),
                            ChessFigure("W", "B", "Hourse", [0, 6]), ChessFigure("B", "B", "Tour", [0, 7])]
        for i in range(self.chess_board.width):
            if i % 2 == 0:
                self.chess_figures.append(ChessFigure("B", "B", "Peshka", [1, i]))
            else:
                self.chess_figures.append(ChessFigure("W", "B", "Peska", [1, i]))

    def put_figure(self, figure):
        # self.board[figure.figure_coordinates[0]][figure.figure_coordinates[1]] = figure !!!!! треба так)
        self.chess_board.board[figure.figure_coordinates[0]][figure.figure_coordinates[1]] = figure.show_figure()

    def put_all_figures(self):
        for figs in self.chess_figures:
            self.put_figure(figs)


class Chess_x2(Chess):
    pass


board = ChessBoard(8, 8, 2)
chess = Chess(board)

chess.put_all_figures()

boardx2 = ChessBoard(16, 12, 2)

for i in range(8):
    print(board.board[i])

for i in range(boardx2.height):
    print(boardx2.board[i])
