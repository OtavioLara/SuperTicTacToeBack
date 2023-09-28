from lobby_model import LobbyModel
from game_match_controller import GameMatchController
from player_controller import PlayerController


class LobbyController:
    def __init__(self, player_controller: PlayerController, game_match_controller: GameMatchController):
        self.model = LobbyModel()
        self.player_controller = player_controller
        self.game_match_controller = game_match_controller

    def create_lobby(self, email):
        return self.model.create_lobby(self.player_controller.get_player_from_email(email))

    def add_player_to_lobby(self, email, lobby_id):
        return self.model.add_player_to_lobby(self.player_controller.get_player_from_email(email), lobby_id)

    def start_game(self, lobby_id):
        return self.game_match_controller.create_match(
            self.model.start_game(lobby_id)
        )

    def get_all_lobbies(self):
        return self.model.get_all_lobbies()