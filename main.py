import stream_handling


def main():
    print(stream_handling.get_track_title("http://live-absolute.sharp-stream.com/absoluteradio.mp3", "latin1",
                                          "StreamTitle='(.*)';S"))


if __name__ == '__main__':
    main()
