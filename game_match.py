from tictactoe_2 import TicTacToe2
from player import Player


class GameMatch:
    def __init__(self, game_id: int, player1: Player, player2: Player):
        self.game = TicTacToe2()
        self.player1 = player1
        self.player2 = player2
        self.id = game_id

    def play(self, x, y, in_x, in_y):
        self.game.play(x, y, in_x, in_y)
        return self.to_dict()

    def to_dict(self):
        return{
            'id': self.id,
            'player1': self.player1.to_dict() if self.player1 is not None else None,
            'player2': self.player2.to_dict() if self.player2 is not None else None,
            'game_data': self.game.to_dict()
        }

