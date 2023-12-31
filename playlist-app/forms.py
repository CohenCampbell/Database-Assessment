"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea


class PlaylistForm(FlaskForm):
    """Form for adding playlists.""" 

    playlist_name = StringField("Playlist Name")

    description = StringField("Playlist Description", widget=TextArea())

class SongForm(FlaskForm):
    """Form for adding songs."""

    song_name = StringField("Song Name")

    artist = StringField("Song Artist")

# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
