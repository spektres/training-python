class TicTacToeBoard():
    def __init__(self):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.movi_x = True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_movi = True

    def new_game(self):
        self.field = []
        for row in range(3):
            r = []
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.movi_x = True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_movi = True

    def get_field(self):
        return self.field

    def check_field(self):
        if self.win == 'X':
            return 'X'
        elif self.win == '0':
            return 0
        else:
            return None

    def make_move(self, row, col):
        if self.end_of_game and not self.first_movi:
            return 'Игра завершена'
        else:
            if self.field[row - 1][col - 1] != '-':
                return f'Клктка {row}, {col} уже занята'
            else:
                if self.movi_x:
                    self.field[row - 1][col - 1] = 'X'
                    self.movi_x = False
                    self.first_movi = False
                else:
                    self.field[row - 1][col - 1] = '0'
                    self.movi_x = True
                    self.first_movi = False
            if self.field[0].count(self.field[0][0]) == 3 and self.field[0][0] != '-':
                self.end_of_game = True
                self.win = self.field[0][0]
                return f'Победил игрок {self.field[0][0]}'
            elif self.field[1].count(self.field[1][0]) == 3 and self.field[1][0] != '-':
                self.end_of_game = True
                self.win = self.field[1][0]
                return f'Победил игрок {self.field[1][0]}' 
            elif self.field[2].count(self.field[2][0]) == 3 and self.field[2][0] != '-':
                self.end_of_game = True
                self.win = self.field[2][0]
                return f'Победил игрок {self.field[2][0]}'
            elif self.field[0][0] == self.field[1][0] == self.field[2][0] and self.field[0][0] != '-':
                self.end_of_game = True
                self.win = self.field[0][0]
                return f'Победил игрок {self.field[0][0]}'
            elif self.field[0][1] == self.field[1][1] == self.field[2][1] and self.field[0][1] != '-':
                self.end_of_game = True
                self.win = self.field[0][1]
                return f'Победил игрок {self.field[0][1]}'
            elif self.field[0][2] == self.field[1][2] == self.field[2][2] and self.field[0][2] != '-':
                self.end_of_game = True
                self.win = self.field[0][2]
                return f'Победил игрок {self.field[0][2]}'
            elif self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != '-':
                self.end_of_game = True
                self.win = self.field[0][0]
                return f'Победил игрок {self.field[0][0]}'
            elif self.field[2][0] == self.field[1][1] == self.field[0][2] and self.field[2][0] != '-':
                self.end_of_game = True
                self.win = self.field[2][0]
                return f'Победил игрок {self.field[2][0]}'
            elif self.field[0].count('-') == 3 and self.field[1].count('-') == 3 and self.field[2].count('-') == 3:
                self.end_of_game = True
                self.win = 'ничья'
                return 'Ничья'
            else:
                return 'Продолжаем играть'


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")