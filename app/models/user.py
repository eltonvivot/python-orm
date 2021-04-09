from . import db

class User(db.Document):

    name = db.StringField()
    login = db.StringField()
    password = db.StringField()

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def to_json(self):
        return {"name": self.name,
                "login": self.email,
                "password": self.password}