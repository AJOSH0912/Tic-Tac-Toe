class TicTacToe:
    def __init__(self):
        # Initialize an empty board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
    
    def make_move(self, row, col):
        # Place the current player's mark on the board if the spot is empty
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return True
            elif self.check_draw():
                self.print_board()
                print("The game is a draw!")
                return True
            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("This spot is already taken. Choose another one.")
        return False

    def check_win(self):
        # Check all rows, columns, and diagonals for a win
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        
        return False
    
    def check_draw(self):
        # Check if all cells are filled and there's no winner
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def play(self):
        # Main game loop
        while True:
            self.print_board()
            row = int(input(f"Player {self.current_player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {self.current_player}, enter the column (0, 1, 2): "))
            if self.make_move(row, col):
                break

game = TicTacToe()
game.play()