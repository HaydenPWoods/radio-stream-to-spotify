from spotify import spotify


def track_search(track_title, include_remixes):
    """
    Takes a track title as a string, searches for the song on Spotify, and then returns the URI of the song if found.
    Attempts to exclude karaoke and 'cover tracks' from spam artists.
    :param track_title: String
    :param include_remixes: Boolean - specifies whether remix tracks are acceptable.
    :return: Spotify URI as a String, or NoneType if no suitable track found.
    """
    try:
        tracks, = spotify.search(track_title, types=('track',), limit=5)
        exclusions = ['karaoke', 'the style of', 'tribute', 'originally performed by', 'includes hidden track',
                      'bluegrass rendition', 'Live From The Royal Albert Hall', 'Ghostface UK Version', 'Spotify',
                      'Djlilruben', 'djlilruben', 'Made Famous by', 'Bimbo Jones Radio Mix', 'Live Lounge']
        blacklisted_artists = ['Karaoke', "Pickin' On Series", 'Midifine Systems', 'Studio Allstars',
                               'Grandes Canciones - Versiones Acústicas', 'Lucky Voice Karaoke', 'The Karaoke Channel',
                               'Ameritz', 'Poptastik Karaoke', "Singer's Edge Karaoke", 'Brazillian Bossa Nova',
                               'Nursery Rhymes 123', 'DJ Top Gun', 'Dj lil Ruben', 'Extreme DJs & Remixers']
        good_track = -1
        # Likely filter search here to remove obvious / unlikely tracks.
        if tracks.total > 0:
            print(tracks.total)
            if tracks.total < 5:
                tracks_search_num = tracks.total
            else:
                tracks_search_num = 5
            for i in range(tracks_search_num):
                curr_track = tracks.items[i]
                bad_track = False
                for entry in exclusions:
                    if entry.upper() in curr_track.name.upper():
                        bad_track = True
                        break
                if bad_track:
                    continue
                else:
                    for bad_artist in blacklisted_artists:
                        for artist in curr_track.artists:
                            if bad_artist.upper() in artist.name.upper():
                                bad_track = True
                                break
                        if bad_track:
                            break
                    if bad_track:
                        continue
                    else:
                        if not include_remixes:
                            if "REMIX" in curr_track.name.upper():
                                bad_track = True
                            if bad_track:
                                break
                        else:
                            good_track = curr_track
                            break
            if good_track != -1:
                return good_track
    except Exception as e:
        print("Some exception occurred...")
        print(e)


def track_search_alt(track_title, artist_name, include_remixes):
    """
    Takes a track title and artist name as strings, searches for the song on Spotify, and then returns the URI of the
    song if found. Attempts to exclude karaoke and 'cover tracks' from spam artists.
    :param track_title: String
    :param artist_name: String (ideally the first word only - checks against the first artist listed for a track by
                        Spotify
    :param include_remixes: Boolean - specifies whether remix tracks are acceptable.
    :return: Spotify URI as a String, or NoneType if no suitable track found.
    """
    try:
        tracks, = spotify.search(track_title, types=('track',), limit=5)
        exclusions = ['karaoke', 'the style of', 'tribute', 'originally performed by', 'includes hidden track',
                      'bluegrass rendition', 'Live From The Royal Albert Hall', 'Ghostface UK Version', 'Spotify',
                      'Djlilruben', 'djlilruben', 'Made Famous by', 'Bimbo Jones Radio Mix', 'Live Lounge']
        blacklisted_artists = ['Karaoke', "Pickin' On Series", 'Midifine Systems', 'Studio Allstars',
                               'Grandes Canciones - Versiones Acústicas', 'Lucky Voice Karaoke', 'The Karaoke Channel',
                               'Ameritz', 'Poptastik Karaoke', "Singer's Edge Karaoke", 'Brazillian Bossa Nova',
                               'Nursery Rhymes 123', 'DJ Top Gun', 'Dj lil Ruben', 'Extreme DJs & Remixers']
        good_track = -1
        if tracks.total > 0:
            print(tracks.total)
            if tracks.total < 5:
                tracks_search_num = tracks.total
            else:
                tracks_search_num = 5
            for i in range(tracks_search_num):
                curr_track = tracks.items[i]
                bad_track = False
                for entry in exclusions:
                    if entry.upper() in curr_track.name.upper():
                        bad_track = True
                        break
                if bad_track:
                    continue
                if artist_name.upper() not in curr_track.artists[0].name.upper():
                    bad_track = True
                    continue
                for bad_artist in blacklisted_artists:
                    for artist in curr_track.artists:
                        if bad_artist.upper() in artist.name.upper():
                            bad_track = True
                            break
                    if bad_track:
                        break
                if bad_track:
                    continue
                if not include_remixes:
                    if "REMIX" in curr_track.name.upper():
                        bad_track = True
                        continue
                if not bad_track:
                    good_track = curr_track
                    break
            if good_track != -1:
                return good_track
    except Exception as e:
        print("Some exception occured...")
        print(e)
