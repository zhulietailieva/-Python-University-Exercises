class TicTacToe:
    def __init__(self):
        self.board=[]
    def create_board(self):
        for i in range(3):
            row =[]
            for j in range(3):
                row.append('-')
            self.board.append(row)
    def show_board(self):
        for row in self.board:
            for positin in row:
                print(positin,end=" ")
    def play(self,row,col,player):
        self.board[row][col]=player
    def winner(self,player):
        winner=None
        #cols
        for i in range(3):
            win=True
            for j in range(3):
                if self.board[i][j]!=player:
                    win=False
                    break
                if win:
                    return win
        #rows
        for j in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != player:
                    win = False
                    break
                if win:
                    return win
        #diagonals
            #first diagonal
        for i in range(3):
            if self.board[i][i]!=player:
                win=False
                break
            if win:
                return win
            #second diagonal
        for i in range(3):
            if self.board[i][2-i] !=player:
                win=False
                break
            if win:
                return win
    def is_board_filled(self):
        for row in self.board:
            for position in row:
                if(position=="-"):
                    return False
        return True

    def player_turn(self,player):
        if(player=='X'):
            return 'O'
        else:
            return 'X'

    def start_game(self):
