import json
from io import StringIO

import json_stream

from json_stream_to_standard_types import to_standard_types


def test_to_standard_types():
    json_str = '{ "a": [1, 2, 3], "b": { "d": [3, 4, 5] }, "c": 678, "d": [9] }'
    js = json_stream.load(StringIO(json_str))
    converted = to_standard_types(js)
    comparison = json.load(StringIO(json_str))
    assert converted == comparison
    assert isinstance(converted["a"], list)
    assert isinstance(converted["b"], dict)
    assert isinstance(converted["b"]["d"], list)
