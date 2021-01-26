import json


class WiFiInfo:
    def __init__(self, ssid: str, password: str, first: str=None, last: str=None):
        self.ssid = ssid
        self.password = password
        if first is not None:
            self.first_connected_time = first
        if last is not None:
            self.last_connected_time = last

    def __repr__(self):
        return json.dumps(self.__dict__)