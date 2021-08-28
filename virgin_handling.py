import json

import requests


def get_track_title(url):
    """
    Given a Virgin Radio UK API URL, gets the latest played song for the given station and formats this into a "Artist -
    Title" string.

    :param url: The API request link. The parameters "station", "withSongs", "hasPrograms", and "numberOfSongs" are all
                required.
    :return: The most recently played song, if available, formatted as an "artist - title" string.
    """
    try:
        virgin_json = json.loads(requests.get(url).text)
        return virgin_json["recentlyPlayed"][0]["artist"] + " - " + virgin_json["recentlyPlayed"][0]["title"]
    except Exception as e:
        print("Some exception occurred... (virgin_handling)")
        print(e)
        return "No title found"


def get_track_title_legacy(url):
    try:
        virgin_json = json.loads(requests.get(url).text
                                 .replace("jsonCallback_virgin(", "")
                                 .replace("jsonCallback_anthems(", "")
                                 .replace("jsonCallback_chilled(", "")
                                 .replace("jsonCallback_groove(", "")
                                 .replace(");", ""))
        return virgin_json["nowplaying"][0]["artist"] + " - " + virgin_json["nowplaying"][0]["title"]
    except Exception as e:
        print("Some exception occurred... (virgin_handling)")
        print(e)
        return "No title found"
