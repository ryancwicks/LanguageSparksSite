import unittest
from flask import current_app
from LSSS import create_app, db

class BasicsTestCast ( unittest.TestCase ):
    def setUp(self):
        self.app = create_app ('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown (self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists (self):
        self.assertFalse ( current_app is None )

    def test_app_is_testing (self):
        self.assertTrue (current_app.config['TESTING'])

    def test_empty_db(self):
        rv = self.app.get('/news')
        assert b'No entries here so far' in rv.data 
