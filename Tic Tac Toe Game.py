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