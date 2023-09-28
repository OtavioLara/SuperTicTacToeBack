from player_model import PlayerModel


class PlayerController:

    def __init__(self):
        self.model = PlayerModel()

    def signin(self, email: str, password: str, nick_name: str):
        return self.model.signin(email, password, nick_name)

    def login(self, email: str, password: str):
        return self.model.login(email, password)

    def get_all_online_players(self):
        return self.model.get_all_online_players()

    def get_player_from_email(self, email):
        return self.model.get_player_from_email(email)

