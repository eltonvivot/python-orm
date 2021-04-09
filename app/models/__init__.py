from flask_mongoengine import MongoEngine
import os

db = MongoEngine()

def init_app(app):
    # database config
    # app.config['MONGODB_SETTINGS'] = {
    # 'db': os.environ.get('MONGODB_DATABASE'),
    # 'host': os.environ.get('MONGODB_HOST'),
    # 'port': os.environ.get('MONGODB_PORT')
    # }

    app.config['MONGODB_SETTINGS'] = {
    'db': "orm-db",
    'host': "orm-mdb",
    'port': 5432
    }

    # init
    db.init_app(app)
