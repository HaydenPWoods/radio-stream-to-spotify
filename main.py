import stream_handling
import station
from spotify.track_search import track_search


def main():
    stream_track = stream_handling.get_track_title("http://live-absolute.sharp-stream.com/absoluteradio.mp3", "latin1",
                                                   "StreamTitle='(.*)';S")
    print(stream_track)
    print(track_search(stream_track))
    stream_catalogue = []
    streams_txt_location = "streams.txt"
    streams_txt_separator = "@@@"
    streams_txt = open(streams_txt_location, "r")
    streams_count = 0
    for line in streams_txt:
        # print(line)
        line_values = line.strip().split(streams_txt_separator)
        # print(line_values)
        station_obj = station.Station.build_from_list(line_values)
        stream_catalogue.append(station_obj)

    for stream in stream_catalogue:
        print(stream.name)


if __name__ == '__main__':
    main()
