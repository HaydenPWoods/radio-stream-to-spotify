from spotify import spotify


def track_add(spotify_track, playlist_id):
    """
    Takes a valid Spotify FullTrack object (Tekore) and adds the track to the specified playlist.
    :param spotify_track: FullTrack
    :param playlist_id: String
    """
    spotify.playlist_add(playlist_id, [spotify_track.uri], 0)  # Adding the track to the playlist
