import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4
    assert inc_dec.increment(3) == 4
    assert inc_dec.increment(65535) == 65536
    assert inc_dec.increment(4294967295) == 4294967296
    assert inc_dec.increment(0xFFFFFFFFFFFFFFFE) == 0xFFFFFFFFFFFFFFFF
    assert inc_dec.increment(0xFFFFFFFFFFFFFFFF) == 18446744073709551616

def test_decrement():
    assert inc_dec.decrement(3) == 2
    assert inc_dec.decrement(-3) == -4