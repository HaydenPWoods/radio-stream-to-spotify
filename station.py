class Station:
    def __init__(self, name, url, encoding, regex, separator, order, playlist_id, include_remixes):
        self.name = name
        self.url = url
        self.encoding = encoding
        self.regex = regex
        self.separator = separator
        self.order = order
        self.playlist_id = playlist_id
        self.include_remixes = include_remixes
