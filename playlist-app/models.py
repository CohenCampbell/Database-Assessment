"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.playlist_id==id).first()

    playlist_id = db.Column(db.Integer,
              primary_key=True,
              autoincrement=True)
    
    name = db.Column(db.String,
                     nullable=False)
    
    description = db.Column(db.String,
                            nullable=False)

    songs = db.relationship('Song', secondary='playlist_songs', backref='playlists')

class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.song_id==id).first()

    song_id = db.Column(db.Integer,
              primary_key=True,
              autoincrement=True)
    
    title = db.Column(db.String,
                      nullable=False)
    
    artist = db.Column(db.String,
                       nullable=False)


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer,
              primary_key=True,
              autoincrement=True)
    
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey('playlists'))

    song_id = db.Column(db.Integer,
                            db.ForeignKey('songs'))

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
