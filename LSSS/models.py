from . import db

class Article ( db.Model ):
    __tablename__ = "articles"
    id = db.Column (db.Integer, primary_key=True)
    text = db.Column (db.Text)
    creation_date = db.Column (db.Date)
    user_id = db.Column (db.Integer, db.ForeignKey('users.id'))

    def __repr__ (self):
        return "<Article %r>" % self.title
    
    def to_json(self):
        json_post = {
            'url': url_for('main.news', id=self.id),
            'text': self.text,
            'creation_date': self.creation_date,
        }
        return json_post

class User ( db.Model ):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column (db.String(64), unique=True, index=True)
    email = db.Column (db.String (64))
    articles = db.relationship ('Article', backref='user', lazy='dynamic')

    def __repr__(self):
        return "<User %r>" % self.username
