class Tic_Tac_Toe:
    def __init__(self):
        self.board=[]

    def create_board(self):
        for i in range(3):
            row=[]
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def show_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j],end=' ')
            print()

    def play(self,row,col,player):
        is_move_valid=True
        if(row>=0 and row<=2 and col>=0 and col<=2 and self.board[row][col]=='-'):
            self.board[row][col] = player
        else:
            print('Invlaid!')
            is_move_valid=False
        return is_move_valid

    def switch_player(self,player):
        if(player=='X'):
            return '0'
        return 'X'

    def is_winner(self,player):
        #check rows
        if ((self.board[0][0]==player and self.board[0][1]==player and self.board[0][2]==player)\
        or (self.board[1][0]==player and self.board[1][1]==player and self.board[1][2]==player)\
        or (self.board[2][0]==player and self.board[2][1]==player and self.board[2][2]==player)):
            return True
        #check cols
        if ((self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player) \
        or (self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player) \
        or (self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player)):
            return True
        #check main diagonal
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player):
            return True
        #check second diagonal
        if (self.board[2][2] == player and self.board[1][1] == player and self.board[0][0] == player):
            return True
        return False

    def is_filled(self):
        for i in range (3):
            for j in range(3):
                if(self.board[i][j]=='-'):
                    return False
        return True

    def start(self):
        print('Player X starts')
        self.create_board()
        player='X'
        print('Initial board state: ')
        while True:

            self.show_board()

            print(f'Player {player} turn:')

            row=int(input("row: "))
            col = int(input("col: "))
            while not(self.play(row-1,col-1,player)):
                row = int(input("row: "))
                col = int(input("col: "))

            if(self.is_winner(player)):
                print()
                print(f'Player {player} wins the game!')
                self.show_board()
                return
            print()

            if(self.is_filled()):
                print()
                print('Draw!')
                self.show_board()
                return

            player=self.switch_player(player)

game=Tic_Tac_Toe()
game.start()