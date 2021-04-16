from mongoengine import connect
import os

def init_app(app):
    # database config
    connect(
        db='orm-db',
        host='mongodb://orm:orm@orm-mdb:27017/?authSource=admin'
    )
