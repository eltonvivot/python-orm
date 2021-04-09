from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_app(app):
    # database config
    # pgUser = os.environ.get('POSTGRESQL_USER')
    # pgPwd = os.environ.get('POSTGRESQL_PASSWORD')
    # pgHost = os.environ.get('POSTGRESQL_HOST')
    # pgPort = os.environ.get('POSTGRESQL_PORT')
    # pgDb = os.environ.get('POSTGRESQL_DATABASE')
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{pgUser}:{pgPwd}@{pgHost}:{pgPort}/{pgDb}"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://orm:orm@orm-pdb:5432/orm-db"

    # init
    db.init_app(app)
    migrate = Migrate(app, db)
