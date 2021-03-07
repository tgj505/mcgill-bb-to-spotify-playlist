# mcgill-bb-to-spotify-playlist
Generates a Spotify playlist from a csv with columns of track names and artist names. 
Designed to explore and contextualize the [McGill Billboard Corpus]('https://ddmal.music.mcgill.ca/research/The_McGill_Billboard_Project_(Chord_Analysis_Dataset)/').

## Some results
* [**Spotify Playlist**](https://open.spotify.com/playlist/2whWrl00XDSf1omDLkjBDV) of 691 songs from the McGill Corpus.
* **data/mcgill-bb-playlist.html** some basic playlist analysis from Spotify metadata. Download and open this to see plots and summaries of artist genres, track popularity, dates, and "acoustic features."
* **data/mcgill-bb-playlist-metadata.pickle**. Pickled dataframe of Spotify metadata for each track. 

*Spotify Metadata Notes*

The html and pickle files here are prototype results generated from a separate project, hopefully to be uploaded soon.
You can read in the pickle as a dict object using `from config.config import load_playlist_pickle`.
Contains relevant spotify metadata like album, artist, genre, popularity, etc. 
for each track, as well as spotify's ["audio features"](https://spotipy.readthedocs.io/en/2.17.1/#spotipy.client.Spotify.audio_features) metadata.

*N.B.* The dates in the playlist analysis often don't match the original album date since the search function often returns remastered versions, re-releases, and compilations.

## Replicate Playlist Generation
### Requirements
* `pandas`
* `spotipy`
* `pathlib`
* `datetime`
* `os`
* `pickle`

### Set up `config/config.py`
Set this up with your **Spotify API credentials**, your **Spotify Username**, etc. to be able to write playlist.

Check the pathing as necessary; **set root directory** variable. I'm still learning pathing, apologies. 

### Run `playlist-build_mcgill2spotify.py`
This will read in the `data/mcgill_billboard_index.csv`, query the `spotipy` API to get the track and musician URIs, and create a playlist.

It will open a browser tab to ask you to log in to your Spotify account. 
