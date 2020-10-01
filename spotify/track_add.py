from spotify import spotify


def track_add(spotify_track, playlist_id):
    """
    Takes a valid Spotify FullTrack object (Tekore) and adds the track to the specified playlist.
    :param spotify_track: FullTrack
    :param playlist_id: String
    """
    print(spotify_track)
    tries = 0
    while tries <= 5:
        try:
            max_tracks = 100  # Maximum number of tracks in the playlist
            spotify.playlist_remove(playlist_id, [spotify_track.uri])
            spotify.playlist_add(playlist_id, [spotify_track.uri], 0)  # Adding the track to the playlist
            spotify_playlist = spotify.playlist(playlist_id)
            if spotify_playlist.tracks.total > max_tracks:
                # Number of tracks in playlist has reached the threshold, so remove oldest.
                spotify.playlist_remove_indices(playlist_id, [spotify_playlist.tracks.total - 1],
                                                spotify_playlist.snapshot_id)
            break
        except Exception as e:
            print("Something went wrong, but retrying... (track_add)")
            print(e)
            tries += 1
