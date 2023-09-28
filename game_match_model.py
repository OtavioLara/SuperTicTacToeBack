from game_match import GameMatch
from lobby import Lobby


class GameMatchModel:

    def __init__(self):
        self.games_matches: list[GameMatch] = []
        self.count = 1

    def create_match_from_lobby(self, lobby: Lobby):
        game_match = GameMatch(
                self.count,
                lobby.players[0],
                lobby.players[1],
            )
        self.games_matches.append(game_match)
        self.count += 1
        return game_match.to_dict()

    def play(self, game_id, x, y, in_x, in_y):
        game_match = list(filter(lambda game: game.id == game_id, self.games_matches))
        if len(game_match) > 0:
            return game_match[0].play(x, y, in_x, in_y)
