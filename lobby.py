from player import Player
from game_match import GameMatch
from enum import Enum


class EnumStatus(Enum):
    WAITING = 1
    READY = 2
    IN_MATCH = 3


class Lobby:

    def __init__(self, lobby_id: int, player: Player):
        self.players: list[Player] = [player]
        self.lobby_status: EnumStatus = EnumStatus.WAITING
        self.id = lobby_id

    def start_game(self):
        self.lobby_status = EnumStatus.IN_MATCH

    def add_player(self, player: Player):
        if len(self.players) < 2:
            self.players.append(player)
            return True
        return False

    def remove_player(self, email):
        if len(self.players) > 0:
            player_to_remove = list(filter(lambda player: player.email == email, self.players))
            if len(player_to_remove) > 0:
                self.players.pop(player_to_remove[0])
                self.lobby_status = EnumStatus.WAITING

    def to_dict(self):
        return {
            'id': self.id,
            'players': [player.to_dict() for player in self.players],
            'status': str(self.lobby_status)
        }
