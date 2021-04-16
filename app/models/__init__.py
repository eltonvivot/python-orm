from mongoengine import connect
import os

def init_app(app):
    # database config
    # app.config['MONGODB_SETTINGS'] = {
    # 'db': os.environ.get('MONGODB_DATABASE'),
    # 'host': os.environ.get('MONGODB_HOST'),
    # 'port': os.environ.get('MONGODB_PORT')
    # }

    connect(
        db='orm-db',
        host='mongodb://orm:orm@orm-mdb:27017/?authSource=admin'
    )
