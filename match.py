class Piece:
    def __init__(self, color):
        self.color = color

    def get_possible_moves(self, board, x, y):
        return []

class King(Piece):
    def __str__(self):
        return 'K' if self.color == 'white' else 'k'

class Queen(Piece):
    def __str__(self):
        return 'Q' if self.color == 'white' else 'q'

class Rook(Piece):
    def __str__(self):
        return 'R' if self.color == 'white' else 'r'

class Bishop(Piece):
    def __str__(self):
        return 'B' if self.color == 'white' else 'b'

class Knight(Piece):
    def __str__(self):
        return 'N' if self.color == 'white' else 'n'

class Pawn(Piece):
    def __str__(self):
        return 'P' if self.color == 'white' else 'p'

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Place white pieces
        board[0][0] = Rook('white')
        board[0][1] = Knight('white')
        board[0][2] = Bishop('white')
        board[0][3] = Queen('white')
        board[0][4] = King('white')
        board[0][5] = Bishop('white')
        board[0][6] = Knight('white')
        board[0][7] = Rook('white')
        for i in range(8):
            board[1][i] = Pawn('white')

        # Place black pieces
        board[7][0] = Rook('black')
        board[7][1] = Knight('black')
        board[7][2] = Bishop('black')
        board[7][3] = Queen('black')
        board[7][4] = King('black')
        board[7][5] = Bishop('black')
        board[7][6] = Knight('black')
        board[7][7] = Rook('black')
        for i in range(8):
            board[6][i] = Pawn('black')

        return board

    def print_board(self):
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))

    def move_piece(self, start_x, start_y, end_x, end_y):
        piece = self.board[start_x][start_y]
        if piece:
            self.board[end_x][end_y] = piece
            self.board[start_x][start_y] = None
        else:
            print("No piece at the starting position.")

if __name__ == "__main__":
    board = Board()
    board.print_board()

    while True:
        move = input("Enter your move (e.g., 'e2 e4'): ")
        if move == 'quit':
            break
        try:
            start, end = move.split()
            start_x = 8 - int(start[1])
            start_y = ord(start[0]) - ord('a')
            end_x = 8 - int(end[1])
            end_y = ord(end[0]) - ord('a')
            board.move_piece(start_x, start_y, end_x, end_y)
            board.print_board()
        except Exception as e:
            print(f"Invalid move: {e}")
