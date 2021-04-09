from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    login = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"