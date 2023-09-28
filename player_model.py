import time

from player import Player
from threading import Thread


class PlayerModel(Thread):

    def __init__(self):
        super().__init__()
        self.players: dict[str: Player] = {}

    def signin(self, email: str, password: str, nick_name: str):
        if email not in self.players.keys():
            player = Player(nick_name, email, password)
            self.players.update({email: player})
            return player
        else:
            return 'User already exists'

    def login(self, email: str, password: str):
        if email in self.players.keys():
            player = self.players[email]
            if player.password == password:
                player.is_online = True
                self.players[email].is_online = True
                return player
            else:
                return 'Wrong password'
        else:
            return 'User does not exists'

    def update_players_status(self):
        for player in self.players:
            player.update_status()

    def get_all_online_players(self):
        return [player.to_dict() for player in self.players.values() if player.is_online]

    def get_player_from_email(self, email):
        return self.players[email]

    def run(self):
        while True:
            self.update_players_status()
            time.sleep(30)
