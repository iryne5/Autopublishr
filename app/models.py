from app import db

class Script(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    word_count = db.Column(db.Integer)
    recommendations = db.relationship('Recommendation', backref='script', lazy=True)

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    script_id = db.Column(db.Integer, db.ForeignKey('script.id'), nullable=False)

# More models for User, VersionHistory, SongSuggestion, etc.

