import spotipy
from datetime import date
import os
from pathlib import Path
import pickle

"""environment variables"""
spotify_username = os.environ["SPOT_USERNAME"]
CLIENT_ID = os.environ["SPOT_ID"]
CLIENT_SECRET = os.environ["SPOT_SECRET"]

"""set mcgill index path"""
ROOT_PATH = Path(os.environ["PATH_mcgill-bb-to-spotify-playlist"])
DATA_PATH = ROOT_PATH / 'data'
MCGILL_CSV_PATH = DATA_PATH / 'mcgill_billboard_index.csv'
MCGILL_PICKLE_PATH = DATA_PATH / 'mcgill-bb-playlist-metadata.pickle'

"""spotipy authentication"""
scope = "playlist-modify-public"
auth_manager = spotipy.SpotifyOAuth(username=spotify_username,
                          scope=scope,
                          client_id=CLIENT_ID,
                          client_secret=CLIENT_SECRET,
                          redirect_uri='http://localhost:8888/callback')
sp = spotipy.Spotify(auth_manager=auth_manager)


"""output playlist variables"""
playlist_name = "McGill Dataset Corpus Playlist"
playlist_description = f"Built on {date.today()}. (github: tgj505)"

def load_playlist_pickle():
    with open(MCGILL_PICKLE_PATH, 'rb') as handle:
        dict = pickle.load(handle)

    return dict