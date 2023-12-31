from game_match_model import GameMatchModel
from player_controller import PlayerController


class GameMatchController:
    def __init__(self, player_controller: PlayerController):
        self.model = GameMatchModel()
        self.player_controller = player_controller

    def create_match_from_lobby(self, lobby):
        return self.model.create_match_from_lobby(lobby)

    def play(self, game_id, x, y, in_x, in_y):
        return self.model.play(game_id, x, y, in_x, in_y)
