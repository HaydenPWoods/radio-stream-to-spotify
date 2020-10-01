import stream_handling
from station import Station
from spotify.track_search import track_search
from spotify.track_add import track_add
import time


def main():
    stream_catalogue = []
    streams_txt_location = "streams.txt"
    streams_txt_separator = "@@@"
    streams_txt = open(streams_txt_location, "r")
    for line in streams_txt:
        line_values = line.strip().split(streams_txt_separator)
        print(line_values)
        station_obj = Station.build_from_list(line_values)
        stream_catalogue.append(station_obj)

    while True:
        for stream in stream_catalogue:
            try:
                stream_track = stream_handling.get_track_title(stream.url, stream.encoding, stream.regex)
                print(stream_track)
                if (stream_track != "No title found") & ("ADBREAK" not in stream_track):
                    stream_track_split = stream_track.strip().split(stream.separator)
                    if int(stream.order) == 1:
                        spotify_track = track_search(stream_track_split[0].strip(), stream_track_split[1].split()[0],
                                                     stream.include_remixes)
                    else:
                        spotify_track = track_search(stream_track_split[1].strip(), stream_track_split[0].split()[0],
                                                     stream.include_remixes)
                    if spotify_track is not None:
                        track_add(spotify_track, stream.playlist_id)
            except Exception as e:
                print("Some exception occured...")
                print(e)
        time.sleep(60)


if __name__ == '__main__':
    main()
