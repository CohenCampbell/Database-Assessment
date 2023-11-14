from flask import Flask, redirect, render_template

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)


app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



@app.route("/create_db")
def create():
    db.create_all()
    return redirect("/")

@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.get_by_id(playlist_id)
    songs = playlist.songs
    return render_template("playlist.html", playlist=playlist, songs=songs)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.playlist_name.data
        description = form.description.data
        newList = Playlist(name=name, description=description)
        db.session.add(newList)
        db.session.commit()
        return redirect("/playlists")
    
    return render_template("new_playlist.html", form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    song = Song.get_by_id(song_id)
    playlists = song.playlists

    return render_template("song.html", song=song, playlists=playlists)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    form = SongForm()

    if form.validate_on_submit():
        name = form.song_name.data
        artist = form.artist.data
        newSong = Song(title=name, artist=artist)
        db.session.add(newSong)
        db.session.commit()
        return redirect("/songs")
    return render_template("new_song.html", form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist
    
    curr_on_playlist = [s.song_id for s in playlist.songs]
    
    form.song.choices = [id for (id,) in (Song.query.with_entities(Song.song_id)
                      .filter(Song.song_id.notin_(curr_on_playlist))
                      .all())]
    
    
    if form.validate_on_submit():
          playlist_song = PlaylistSong(song_id=form.song.data,
                                  playlist_id=playlist_id)
          
          db.session.add(playlist_song)
          db.session.commit()  
          return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
