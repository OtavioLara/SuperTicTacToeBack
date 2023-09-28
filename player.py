from datetime import  datetime, timedelta


class Player:
    def __init__(self, nick_name, email, password):
        super().__init__()
        self.nick_name = nick_name
        self.email = email
        self.password = password
        self.is_online = False
        self.last_update = datetime.now()

    def maintain_online(self):
        self.is_online = True
        self.last_update = datetime.now()

    def update_status(self):
        self.is_online = self.last_update > (datetime.now() - timedelta(minutes=10))

    def logout(self):
        self.is_online = False
        self.last_update = datetime.now()

    def to_dict(self) -> dict:
        return {'nick_name': self.nick_name, 'email': self.email}

