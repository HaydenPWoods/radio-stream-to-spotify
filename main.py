import concurrent.futures
import logging
import time

import stream_handling
from spotify.track_add import track_add
from spotify.track_search import track_search
from station import Station


def stream_run(stream):
    """
    Runs all the functions necessary for polling a stream, searching its' current track on Spotify, and adding it to
    the respective playlist.
    :param stream: Station object
    """
    try:
        stream_track = stream_handling.get_track_title(stream.url, stream.encoding, stream.regex)
        logging.info(f'{stream.name} current track: {stream_track}')
        if (stream_track != "No title found") & ("ADBREAK" not in stream_track) & (stream.separator in
                                                                                   stream_track):
            stream_track_split = stream_track.strip().split(stream.separator)
            if int(stream.order) == 1:
                if stream_track_split[1].split()[0].upper() == "THE":
                    artist_first_word = stream_track_split[1].split()[1]
                else:
                    artist_first_word = stream_track_split[1].split()[0]
                spotify_track = track_search(stream_track_split[0].strip(), artist_first_word,
                                             stream.include_remixes)
            else:
                if stream_track_split[0].split()[0].upper() == "THE":
                    artist_first_word = stream_track_split[0].split()[1]
                else:
                    artist_first_word = stream_track_split[0].split()[0]
                spotify_track = track_search(stream_track_split[1].strip(), artist_first_word,
                                             stream.include_remixes)
            if spotify_track is not None:
                track_add(spotify_track, stream.playlist_id)
    except Exception as e:
        print("Some exception occured... (main)")
        print(e)


def main():
    stream_catalogue = []
    streams_txt_location = "streams.txt"
    streams_txt_separator = "@@@"
    streams_txt = open(streams_txt_location, "r")
    for line in streams_txt:
        line_values = line.strip().split(streams_txt_separator)
        station_obj = Station.build_from_list(line_values)
        stream_catalogue.append(station_obj)

    while True:
        log_format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(stream_run, stream_catalogue)
        logging.info("One cycle complete - sleeping for 60 seconds...")
        time.sleep(60)


if __name__ == '__main__':
    main()
