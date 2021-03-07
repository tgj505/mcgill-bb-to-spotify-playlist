import pandas as pd
from src.functions_mcgill2spotify import get_spotify_uris, make_playlist_from_track_list
from config.config import MCGILL_CSV_PATH

# read in csv to df, keep only relevant columns/rows with artist/song title info
df = pd.read_csv(MCGILL_CSV_PATH)[['title', 'artist']].dropna().reset_index().drop('index',axis=1)

# make a dict of track and artist URIs if they're found in the spotify API query
# dict might be handy for future work
i=0
uri_dict = {}
while i < len(df['title'].tolist()):
    try:
        track_uri, artist_uri = get_spotify_uris(song_name=df['title'].tolist()[i],
                                                 artist_name=df['artist'].tolist()[i])
        uri_dict[track_uri] = artist_uri
    except TypeError:
        pass
    i+=1

    # To keep track of how many left to go
    # print('Songs left to search:', len(df['title'].tolist())-i)

# create the playlist
make_playlist_from_track_list([*(uri_dict.keys())])
