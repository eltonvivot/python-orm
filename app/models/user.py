from mongoengine_goodjson import Document
from mongoengine import StringField

class User(Document):

    name = StringField()
    login = StringField()
    password = StringField()

    def serialize(self, data):
        self.name = data["name"]
        self.login = data["login"]
        self.password = data["password"]

    # def to_json(self):
    #     return {"name": self.name,
    #             "login": self.login,
    #             "password": self.password}