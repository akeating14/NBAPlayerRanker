from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from project import app, db
import os

app.config.from_object(os.getenv('APP_SETTINGS', 'config.ProductionConfig'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
