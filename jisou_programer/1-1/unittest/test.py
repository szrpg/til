from main import calc_md5


def test_calc_md5():
    actual = calc_md5(' This is Content ')
    assert actual == b'<ハッシュ値>'