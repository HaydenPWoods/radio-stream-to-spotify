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

    @classmethod
    def build_from_list(cls, v_v):
        obj = cls(v_v[0], v_v[1], v_v[2], v_v[3], v_v[4], v_v[5], v_v[6], v_v[7])
        return obj
