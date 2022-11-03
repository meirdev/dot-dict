from dot_dict import DotDict


def test_dot_dict():
    obj = DotDict({"a": 1, "b": {"c": 2}, "d": [3, 4, {"e": 5}]})
    assert obj.a == 1
    assert obj.b.c == 2
    assert obj.d[2].e == 5
    assert obj.b() == {"c": 2}
