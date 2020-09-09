from spotify import spotify


def track_search(track_title):
    """
    Takes a track title as a string, searches for the song on Spotify, and then returns the URI of the song if found.
    :param track_title: String
    :return: Spotify URI as a String
    """
    tracks, = spotify.search(track_title, types=('track',), limit=1)
    # Likely filter search here to remove obvious / unlikely tracks.
    if tracks.total > 0:
        return tracks.items[0].uri
