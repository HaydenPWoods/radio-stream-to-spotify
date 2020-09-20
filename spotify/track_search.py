from spotify import spotify


def track_search(track_title):
    """
    Takes a track title as a string, searches for the song on Spotify, and then returns the URI of the song if found.
    :param track_title: String
    :return: Spotify URI as a String
    """
    tracks, = spotify.search(track_title, types=('track',), limit=1)
    exclusions = ['karaoke', 'the style of', 'tribute', 'originally performed by', 'includes hidden track',
                  'bluegrass rendition']
    blacklisted_artists = ['karaoke', "Pickin' On Series", 'Midifine Systems', 'Studio Allstars',
                           'Grandes Canciones - Versiones Acústicas', 'Lucky Voice Karaoke', 'The Karaoke Channel',
                           'Ameritz', 'Poptastik Karaoke', "Singer's Edge Karaoke", 'Brazillian Bossa Nova',
                           'Nursery Rhymes 123']
    # Likely filter search here to remove obvious / unlikely tracks.
    if tracks.total > 0:
        return tracks.items[0].uri
