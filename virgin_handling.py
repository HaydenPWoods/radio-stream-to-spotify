import json

import requests


def get_track_title(url):
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
