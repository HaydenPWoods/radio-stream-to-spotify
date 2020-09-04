import re
import struct

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


def get_track_title(url, encoding, regex):
    """
    Checks a stream url and returns the currently reported playing song,
    if one is found. Based heavily on https://stackoverflow.com/a/35104372.

    :param url: the URL string of the stream to check (mp3, ogg)
    :param encoding: latin1, iso-8859-1 for mp3, utf-8 for ogg
    :param regex: Regular expression string to search for title
    :return: the reported track title as a string, or "No title found" string
    """
    request = urllib2.Request(url, headers={'Icy-MetaData': "1"})  # Requesting metadata
    try:
        response = urllib2.urlopen(request)
    except Exception as e:
        print(e)
        return "No title found"
    metaint = int(response.headers['icy-metaint'])
    for _ in range(5):
        response.read(metaint)  # Skipping past garbage data
        metadata_length = struct.unpack('B', response.read(1))[0] * 16
        metadata = response.read(metadata_length).rstrip(b'\0').decode(encoding, errors='replace')
        regex_find = re.search(regex, metadata)  # Finding title
        if regex_find:
            title = regex_find.group(1)
            if title:
                break
    else:
        return "No title found"
    return title
