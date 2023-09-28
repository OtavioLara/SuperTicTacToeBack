class TicTacToe:
    def __init__(self):
        self.turn = None
        self.winner = None
        self.matrix = None
        self.start_tic_tac()

    def start_tic_tac(self):
        self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.winner = 0
        self.turn = 1

    def play(self, x, y, turn):
        if self.matrix[x][y] == 0:
            if self.winner == 0:
                self.matrix[x][y] = turn
                self.winner = self.verify_win()
            else:
                print(('x' if self.winner == 1 else 'o'), 'already is the winner, game is over')
        else:
            print('This place was already marked')
        return self.winner

    def str_matrix(self):
        result = ''
        for i in range(3):
            result += '|'.join(
                ['x' if self.matrix[i][j] == 1 else 'o' if self.matrix[i][j] == 2 else ' ' for j in range(3)]) + '\n'
            if i < 2:
                result += '-----\n'
        return result

    def verify_win(self):
        # Verify Row
        for i in range(3):
            if self.matrix[i][0] != 0 and all([self.matrix[i][j] == self.matrix[i][j + 1] for j in range(2)]):
                return self.matrix[i][0]
        # Verify Column
        for i in range(3):
            if self.matrix[0][i] != 0 and all([self.matrix[j][i] == self.matrix[j + 1][i] for j in range(2)]):
                return self.matrix[0][i]
        # Verify main Diagonal
        if self.matrix[0][0] != 0 and all([self.matrix[i][i] == self.matrix[i + 1][i + 1] for i in range(2)]):
            return self.matrix[0][0]
        # Verify other Diagonal
        if (self.matrix[0][(len(self.matrix) - 1)] != 0 and
                all([self.matrix[i][(len(self.matrix) - 1) - i] == self.matrix[i + 1][(len(self.matrix) - 1) - i - 1]
                     for i in range(2)])):
            return self.matrix[0][(len(self.matrix) - 1)]
        return 0


class TicTacToe2(TicTacToe):

    def __init__(self):
        super().__init__()
        self.cur_y = None
        self.cur_x = None
        self.tictactoe_matrix = None
        self.start_tic_tac_2()

    def start_tic_tac_2(self):
        self.tictactoe_matrix = [
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()],
            [TicTacToe(), TicTacToe(), TicTacToe()]
        ]
        self.cur_x = -1
        self.cur_y = -1

    def print_matrix(self):
        for i in range(3):
            print(
                '\n-------------\n'.join(['x' if self.matrix[i][j] == 1 else 'o' if self.matrix[i][j] == 2 else
                self.tictactoe_matrix[i][j].str_matrix() for j in range(3)]))
            if i < 2:
                print('-------------------------------------------------------')

    def get_full_matrix(self):
        full_matrix = []
        for i in range(3):
            full_matrix.append([game.matrix for game in self.tictactoe_matrix[i]])
        return full_matrix

    def get_full_blocked_matrix(self):
        full_matrix = []
        if self.matrix[self.cur_x][self.cur_y] != 0:
            for i in range(3):
                full_matrix.append(
                    [self.cur_x == i and self.cur_y == j for j in range(len(self.tictactoe_matrix[i]))])
            self.cur_x = -1
            self.cur_y = -1
        else:
            for i in range(3):
                full_matrix.append(
                    [not (self.cur_x == i and self.cur_y == j) for j in range(len(self.tictactoe_matrix[i]))])
        return full_matrix

    def play(self, x, y, in_x, in_y):
        if self.cur_x < 0:
            self.cur_x = in_x
            self.cur_y = in_y
        else:
            x = self.cur_x
            y = self.cur_y
            self.cur_x = in_x
            self.cur_y = in_y
        if self.matrix[x][y] == 0:
            if self.winner == 0:
                in_winner = self.tictactoe_matrix[x][y].play(in_x, in_y, self.turn)
                if in_winner != 0:
                    self.matrix[x][y] = in_winner
                self.turn = 1 if self.turn == 2 else 2
                self.winner = self.verify_win()
            else:
                print(('x' if self.winner == 1 else 'o'), 'already is the winner, game is over')
            if self.winner != 0:
                print(('x' if self.winner == 1 else 'o'), 'WIN THE GAME')
                return self.winner
        else:
            print('This place was already marked')

    def restart(self):
        self.start_tic_tac()
        self.start_tic_tac_2()

    def to_dict(self):
        return {'main_matrix': self.matrix,
                'game_matrix': self.get_full_matrix(),
                'cur_matrix_x': self.cur_x,
                'cur_matrix_y': self.cur_y,
                'player': self.turn,
                'blocked_matrix': self.get_full_blocked_matrix(),
                'winner': self.winner}