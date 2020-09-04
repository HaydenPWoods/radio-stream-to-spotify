import re
import struct

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


def get_track_title(url, encoding):
    """
    Checks a stream url and returns the currently reported playing song,
    if one is found. Based heavily on https://stackoverflow.com/a/35104372.

    :param url: the URL of the stream to check (mp3, ogg)
    :param encoding: latin1, iso-8859-1 for mp3, utf-8 for ogg
    :return: the reported track title, or "No title found"
    """
    request = urllib2.Request(url, headers={'Icy-MetaData': 1})  # Requesting metadata
    response = urllib2.urlopen(request)
    metaint = int(response.headers['icy-metaint'])
    for _ in range(5):
        response.read(metaint)  # Skipping past garbage data
        metadata_length = struct.unpack('B', response.read(1))[0] * 16
        metadata = response.read(metadata_length).rstrip(b'\0')
        # print(metadata)
        regex_find = re.search(br"StreamTitle='(.*)';S", metadata)  # Finding title
        if regex_find:
            title = regex_find.group(1)
            if title:
                break
    else:
        return "No title found"
    return title.decode(encoding, errors='replace')
