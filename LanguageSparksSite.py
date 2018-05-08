import os
from LSSS import create_app, db
from LSSS.models import User, Article
from flask_migrate import Migrate

app = create_app ( os.getenv ('LSSS_CONFIG') or 'default' )
migrate = Migrate (app, db)

@app.shell_context_processor
def make_shell_context():
    return dict (db=db, User=User, Article=Article)

@app.cli.command('test')
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
