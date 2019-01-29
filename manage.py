from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from timeless import create_app, DB

APP = create_app("config.DevelopmentConfig")

MIGRATE = Migrate(APP, DB)
MANAGER = Manager(APP)

MANAGER.add_command("db", MigrateCommand)

if __name__ == "__main__":
    MANAGER.run()
