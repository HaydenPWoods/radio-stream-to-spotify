import stream_handling
from station import Station
from spotify.track_search import track_search
from spotify.track_add import track_add
import time


def main():
    # stream_track = stream_handling.get_track_title("http://live-absolute.sharp-stream.com/absoluteradio.mp3", "latin1",
    #                                               "StreamTitle='(.*)';S")
    # print(stream_track)
    # spotify_track = track_search(stream_track)
    # track_add(spotify_track, "1viwaS9PU13aFMTqH1KB64")
    stream_catalogue = []
    streams_txt_location = "streams.txt"
    streams_txt_separator = "@@@"
    streams_txt = open(streams_txt_location, "r")
    for line in streams_txt:
        print(line)
        line_values = line.strip().split(streams_txt_separator)
        print(line_values)
        station_obj = Station.build_from_list(line_values)
        stream_catalogue.append(station_obj)

    while True:
        for stream in stream_catalogue:
            stream_track = stream_handling.get_track_title(stream.url, stream.encoding, stream.regex)
            print(stream_track)
            if (stream_track != "No title found") & ("STOP ADBREAK" not in stream_track):
                spotify_track = track_search(stream_track)
                if spotify_track is not None:
                    track_add(spotify_track, stream.playlist_id)
        time.sleep(60)


if __name__ == '__main__':
    main()
