from config.config import sp, spotify_username, playlist_name, playlist_description

def get_spotify_uris(song_name, artist_name):
    """
    #mcgill corpus has some multi-artist songs separated by a comma. if that's the case, just take the first artist
    :param song_name: track name to search
    :param artist_name: artist name to search
    :return: track_uri, artist_uri: Spotify URIs for track and artist, if found by search query
    """

    if ',' in artist_name:
        artist_name = artist_name.split(',')[0]

    # search for the track
    result = sp.search(q=f"artist:{artist_name} track:{song_name}", type='track', limit=1)

    # if there's a 1-to-1 match, get those URIs
    try:
        track_uri = result['tracks']['items'][0]['uri']
        artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
        # print(song_name, artist_name, track_uri,artist_uri)
        return track_uri,artist_uri

    # otherwise, search for song name and filter for the first artist listed
    except IndexError:
        result = sp.search(q=f"track:{song_name}", type='track', limit=50)


        # print('IndexError:', artist_name, song_name, result)

        # If the song name was found:
        if len(result['tracks']['items']) > 0:
            for track in result['tracks']:
                for artist in track['artists']:
                    if artist_name in artist['name']: # get first one in the list
                        print(track['uri'],artist['uri'])
                        return track['uri'], artist['uri']
                    else:
                        return None

        # if song name search returned no results
        else:
            return None


def make_playlist_from_track_list(track_list):

    # create an empty playlist
    new_playlist = sp.user_playlist_create(spotify_username,
                                           name=playlist_name,
                                           public=True,
                                           description=playlist_description,
                                           )

    # Spotify API allows you to add max=100 tracks at a time, so if playlist is longer than 100, add iteratively.
    if len(track_list) > 100:
        offset = 100
        while offset-len(track_list) < 0:
            add_list = track_list[offset-100:offset]
            sp.playlist_add_items(playlist_id=new_playlist['id'], items=add_list)
            offset+=100
        # add remainder tracks
        sp.playlist_add_items(playlist_id=new_playlist['id'], items=track_list[offset-100:])

    # if the track list is < 100, add all tracks in one go
    else:
        sp.playlist_add_items(playlist_id=new_playlist['id'], items=track_list)

