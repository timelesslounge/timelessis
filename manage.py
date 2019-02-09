from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import main
from timeless.db import DB


MIGRATE = Migrate(main.app, DB)
MANAGER = Manager(main.app)

MANAGER.add_command("db", MigrateCommand)


if __name__ == "__main__":
    MANAGER.run()
