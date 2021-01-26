from json import dumps


def to_json(obj):
    assert obj is not None
    return dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)
