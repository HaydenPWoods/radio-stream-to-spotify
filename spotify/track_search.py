from spotify import spotify, exclusions, blacklisted_artists


def track_search(track_title, artist_name, include_remixes):
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
        good_track = -1
        if tracks.total > 0:
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
                if include_remixes == "0":
                    if "REMIX" in curr_track.name.upper():
                        continue
                if not bad_track:
                    good_track = curr_track
                    break
            if good_track != -1:
                return good_track
    except Exception as e:
        print("Some exception occured... (track_search)")
        print(e)


def track_search_legacy(track_title, include_remixes):
    """
    Takes a track title as a string, searches for the song on Spotify, and then returns the URI of the song if found.
    Attempts to exclude karaoke and 'cover tracks' from spam artists.
    :param track_title: String
    :param include_remixes: Boolean - specifies whether remix tracks are acceptable.
    :return: Spotify URI as a String, or NoneType if no suitable track found.
    """
    try:
        tracks, = spotify.search(track_title, types=('track',), limit=5)
        good_track = -1
        if tracks.total > 0:
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
        print("Some exception occurred... (track_search_legacy")
        print(e)
