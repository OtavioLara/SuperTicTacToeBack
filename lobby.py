from player import Player
from game_match import GameMatch


class Lobby:

    def __init__(self, lobby_id: int, player: Player):
        self.players: list[Player] = [player]
        self.game_match = None
        self.id = lobby_id

    def start_game(self):
        if len(self.players) == 2:
            self.game_match = GameMatch(self.players[0], self.players[1])
        return self.game_match

    def add_player(self, player: Player):
        if len(self.players) < 2:
            self.players.append(player)
            return player.nick_name
        else:
            return 'There is no space in this lobby'

    def remove_player(self, email):
        if len(self.players) > 0:
            player_to_remove = list(filter(lambda player: player.email == email, self.players))
            if len(player_to_remove) > 0:
                self.players.pop(player_to_remove[0])

    def to_dict(self):
        return {
            'id': self.id,
            'players': [player.to_dict() for player in self.players],
            'game_match': self.game_match.to_dict() if self.game_match is not None else None
        }
