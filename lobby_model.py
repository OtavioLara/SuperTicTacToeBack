from lobby import Lobby
from player import Player


class LobbyModel:

    def __init__(self):
        self.lobbies: list[Lobby] = []
        self.count = 1

    def create_lobby(self, player: Player):
        lobby = Lobby(self.count, player)
        self.lobbies.append(lobby)
        self.count += 1
        return lobby.to_dict()

    def get_all_lobbies(self):
        return [lobby.to_dict() for lobby in self.lobbies]

    def find_lobby_by_id(self, lobby_id: int) -> Lobby:
        found_lobby = list(filter(lambda lobby: lobby.id == lobby_id, self.lobbies))
        return found_lobby[0] if len(found_lobby) > 0 else None

    def start_game(self, lobby_id: int):
        lobby = self.find_lobby_by_id(lobby_id)
        if lobby is not None:
            lobby.start_game()
            return lobby

    def add_player_to_lobby(self, player: Player, lobby_id):
        lobby = self.find_lobby_by_id(lobby_id)
        if lobby is not None:
            if lobby.add_player(player):
                return lobby.to_dict()
            else:
                return False
        else:
            return False
